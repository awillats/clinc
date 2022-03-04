import numpy as np
from numpy.random import default_rng
rng = default_rng()

%load_ext autoreload
%autoreload 2



import matplotlib.pyplot as plt
import plotting_functions as myplot

import network_analysis_functions as net
import example_circuits as egcirc
import sys #for debug only
import scipy
import network_plotting_functions as netplot
import network_data_functions as net_data
#%%
nt = 10000
nplot = min(nt,2000)

#standard deviations of "exogenous source noise"
s_x = 1
s_y = 1
s_u = 1

#edge weights
w_ux = 1
w_uy = 1

'''
choose:
- flip-flop
- gaussian 
- saw-tooth
- sine
'''
SHARED_SIGNAL_TYPE = 'flip-flop'

#%%
# HELPER FUNCTIONS
flat = lambda nt: np.ones(nt)
def gen_poisson(nt, lam=1):
    '''
    scaling up Poisson noise post-hoc doesn't work the same way as for gaussian noise ... 
    '''
    return np.random.poisson(lam, nt)

def gen_gauss(nt,seed=None):
    rng = default_rng(seed)    
    return rng.standard_normal(nt)
def sample_gauss(t):
    return gen_gauss(1)
    
def g(nt=nt, noise_type='gaussian'):
    '''
    signal generator for gaussian noise
    '''
    gen_fn = {'gaussian':gen_gauss,'poisson':gen_poisson}[noise_type]
    return gen_fn(nt)
    
def gu(nt=nt, signal_type='gaussian'):
    '''
    signal generator for shared input (u)
    '''
    t_fn = lambda nt: np.arange(0,nt)
    t = t_fn(nt)
    
    period = 100 #parameter used to set period of sine, saw-tooth, flip-flop
    extra_noise = 1/5
    signal_fns = {
        'flip-flop': lambda nt: np.mod(np.cumsum(np.random.rand(nt)<1/period),2),
        'gaussian': lambda nt: gen_gauss(nt),
        'saw-tooth': lambda nt: np.mod(t_fn(nt),period)/period,
        'sine': lambda nt: np.sin(t/period),
    }
    # choose the signal generation type
    signal_fn = signal_fns.get(signal_type, g)
    wave = signal_fn(nt)+g(nt)*extra_noise
    
    #standarize the signal to have mean 0, variance 1
    wave = (wave-np.mean(wave))/np.std(wave)
    return wave.T
#%%
def colmat(v):
    return v[:,np.newaxis]
def rowmat(v):
    return v[np.newaxis,:]
#%%
# simple quantification, analysis
def cov(a,b):
    COV = np.cov(a.T,b.T)
    return COV[0,1]

def corr(a,b):
    CORR = np.corrcoef(a.T,b.T)
    return CORR[0,1]

def pythag(a,b):
    # useful if a,b are standard deviations of independent sources 
    # pythag(a,b) = std.dev of a+b
    return np.sqrt(a**2+b**2)

#%%
CTRL = {'location':0, 'target_fn':sample_gauss,'effectiveness':1.0}

def sim_dg(nt, W, S, B,u, ctrl=None, noise_gen=gen_gauss, input_gen=gen_gauss):
    '''
    Simulate  a directed graph
    S - Nx1 vector of noise standard deviations
    u - 1xnt vector of stimulus intensities (scalar for now)
    TODO: 
    - enforce dimension checks
    '''
    N = W.shape[0] #number of nodes
    Wt = scipy.linalg.expm(W)
    # noise is independent of any input, can be precomputed 
    E = np.random.randn(nt, N)
    X = np.zeros((nt,N))
    # X_prev = X[0,:]
    
    '''
    This strategy side-steps having to simulate a dynamical system, 
    network influence happens within a single timestep
    '''
    X = E @ np.diag(S)
    X += X @ Wt + u @ B
    
    '''
    This strategy treats the system as a discrete-time dynamical system 
    and uses the previous sample's values to compute the current sample 
    - this is slower to compute 
    - to look at the first type of correlation with the second type of data
        - could consider down-sampling/binning
    '''
    
    '''
    for ti in range(nt):
        E_t = E[ti,:]
        # print(S @ E_t, '_')
        u_t = u[ti]
        if ctrl:
            Targ_t = ctrl['target_fn'](ti)
        # 
        # print('__')
        # print((X_prev @ W).shape)
        # print(S * E_t)
        # NOTE: relies on assumption that u_t is scalar
        # X_t = X_prev @ W + B*u_t + S * E_t
        X_t = S*E_t
        X_t += X_t @ W + B*u_t 
        
        """
        Control can override state here:
        """
        
        X[ti,:] = X_t
        X_prev = X_t
    '''
    return X
        
    # return {'u':u,'x':x,'y':y}

def censor_diag(A, censor_val=0):
    C = A.copy()
    n = C.shape[0]
    C[np.diag_indices(n)] = censor_val
    return C
# censor_diag = lambda x: x
nt = int(5e5)
# W = 1.5*egcirc.get_curto_overrepresented_3node()[0]
W = 1*np.array(
[[0,1,0],
[0,0,1],
[0,0,0]])
N = W.shape[0]
E = np.random.randn(nt,N)
S = np.array([1,1,5])*0.05
B = -rowmat(np.array([1,2,3]))*0
u = colmat(flat(nt))

X = sim_dg(nt, W, S, B,u)
#% %
np.set_printoptions(precision=3,suppress=True)

Xts = X.copy()
# Xts[:,1] = np.roll(Xts[:,1],-1)

Rw = net.reachability_weight(W)
corr_pred = net.correlation_matrix_from_reachability(Rw, S**2)
r2_pred  = corr_pred**2
corr = np.corrcoef(Xts,rowvar=False) # this this computes r2
r2_empr = corr**2

# print(np.round(corr,4))
print(np.round(r2_empr,4))
print()
print(np.round(r2_pred,4))
wid_ratios = [1,4,1,1,1]
fig,axs = plt.subplots(2,len(wid_ratios),figsize=(sum(wid_ratios)*3,2*3),gridspec_kw={'width_ratios': wid_ratios})

ax = axs[0,:]
ax[0].imshow(W)
ax[0].set_title('adj')
ax[1].plot(X)
ax[1].set_xlim([1,200])
ax[2].imshow(censor_diag(Rw), vmin=0)
ax[2].set_title('$\widetilde{W}$')
ax[3].imshow(censor_diag(r2_empr), vmin=0,vmax=1)
ax[3].set_title('$r^2$ empr.')
ax[4].imshow(censor_diag(r2_pred), vmin=0,vmax=1)
ax[4].set_title('$r^2$ pred.')
ax = axs[1,:]
netplot.draw_np_adj(W,ax[0])
myplot.unbox(ax[1],clear_labels=True)
netplot.draw_np_adj(Rw, ax[2])
netplot.draw_weighted_corr(r2_pred,ax[3])
netplot.draw_weighted_corr(r2_pred,ax[4])

# netplot.draw_weighted(r2_empr, ax[3])
# netplot.draw_weighted(r2_pred, ax[4])
fig

#%%

# fig,ax = plt.subplots()

# fig,ax = plt.subplots()
# import networkx as nx
# G = nx.from_numpy_matrix(r2_pred, create_using=nx.Graph) 
# weights = np.array(list(nx.get_edge_attributes(G,'weight').values()))
# # weights
# weights = netplot.rescale(weights, 0,1, 0,1)
# 
# pos = nx.circular_layout(G)
# pos = netplot.rotate_layout(pos, np.pi/3, True)
# 
# options = netplot.DEFAULT_NET_PLOT_OPTIONS.copy()
# options.update({'ax':ax[4],'pos':pos,'width':weights,'node_size':0})
# 
# nx.draw(G, **options)
# ax[4].set_aspect('equal')
# # nx.draw_networkx_edge_labels(G, pos=pos)
# myplot.expand_bounds(ax[4])
fig

#%%
# 1-lag co-plot
if nt<1e5:
    fig,ax = plt.subplots(3,3,figsize=(5,5),subplot_kw=dict(box_aspect=1))
    for i in range(3):
        for j in range(3):
            # ax[i,j].plot(X[:-2,j],X[2:,i],'k.',markersize=.005)
            ax[i,j].plot(X[:-1,i],X[1:,j],'k.',markersize=500/nt)

    fig
#%%

sys.exit()

#%%
def sim_dag(w_ux=w_ux, w_uy=w_uy, S=[s_u,s_x,s_y], g=g, gu=gu):
    '''
    Simulate  a (hard-coded) directed graph
        y←u→x
        
    - g() is a "generator" function for random noise 
    - gu() is a "generator" for the shared input term u
        choose:
        - flip-flop 
        - gaussian 
        - saw-tooth 
        - sine
    '''
    [s_u, s_x, s_y]=S
    u = gu(nt, SHARED_SIGNAL_TYPE)*s_u
    # u1 = gu(nt, SHARED_SIGNAL_TYPE)*s_u
    # u2 = gu(nt, SHARED_SIGNAL_TYPE)*s_u
    x = g()*s_x + w_ux*u
    y = g()*s_y + w_uy*u
    return {'u':u,'x':x,'y':y}

#%% 
# RUN SIMULATION
res = sim_dag()
u,x,y=res.values() #unpacks results - NOTE: this is a lazy way to do this, should access by key
#subselect data for plotting
up = u[:nplot]
xp = x[:nplot]
yp = y[:nplot]
#%%
# COMPUTE & PREDICT SUMMARY CORRELATION STATISTICS
'''
prefix 'e' denotes 'empirical' here
prefix 'p' denotes 'predicted' here

-er_xy : empirical correlation coefficient 
-pr_xy : predicted ^^

-pso_x : predicted std.dev of the /output/ of x

'''
er_xy = corr(x,y)
print(er_xy)

pcov_xy = (w_ux*s_u)*(w_uy*s_u)
cov_str = f' cov {cov(x,y):.2f}, pred {pcov_xy:.2f}'

#predicted output assumes variances of independent sources sum
pso_x = pythag(s_x, w_ux*s_u)
pso_y = pythag(s_y, w_uy*s_u)

# https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
pr_xy = pcov_xy / (pso_x * pso_y)
r2_str = f' r^2 {er_xy:.2f}, pred {pr_xy:.2f}'

# This SNR is modeled after Pearson_correlation_coefficient, 
# but using only the "noise" std.dev in the denominator
psnr_xy = pcov_xy / (s_x * s_y)
esnr_xy = cov(x,y)/ (np.std(x-w_ux*u) * np.std(y-w_uy*u))
snr_str = f' SNR* {esnr_xy:.2f}, pred {psnr_xy:.2f}'

# postulate: SNR = r2 / (1-r2) 
print(f'transformed R2 = {er_xy/(1-er_xy):.3f}')
print(f'     empr. SNR = {esnr_xy:.3f}')


#%%
# PAIRS OF SCATTERPLOTS 
fig,ax = plt.subplots(1,3,figsize=(12,5),sharey=True,sharex=False)
ax[0].plot(up, xp,'k.',markersize=1)
ax[1].plot(up, yp,'k.',markersize=1)
ax[2].plot(xp, rng.permutation(yp),'.',color='grey',markersize=3)
ax[2].plot(xp, yp,'r.',markersize=2)

ax[0].set_xlabel('u')
ax[1].set_xlabel('u')
ax[2].set_xlabel('x')

ax[0].set_ylabel('x')
ax[1].set_ylabel('y')
ax[2].set_ylabel('y')
ax[1].set_title('x ← u → y')
ax[2].set_title(f'{cov_str}\n{r2_str}\n{snr_str}')
fig
#%%
# fig,ax=plt.subplots()
# ax.plot(x,(y-np.mean(y))/x,'k.')
# ax.set_ylim([-1,10])

#%% 
# PLOT TIMESERIES
fig,ax = plt.subplots(3,1,figsize=(10,3))
ax[0].plot(up);
ax[0].set_ylabel('u');
ax[1].plot(xp);
ax[1].set_ylabel('x');
ax[2].plot(yp);
ax[2].set_ylabel('y');
fig
#%%
# COMPUTE XCORR
def xcorr(x,y):
    # note, this normalizes by standard deviations... might not be what we want
    xc=np.correlate(x/np.std(x), y/np.std(y), mode='same')
    return xc/len(xc)
    
xx_xcorr = xcorr(x, x)
yy_xcorr = xcorr(y, y)
xy_xcorr = xcorr(x, y)

# naive "shuffle correction" on y to predict "side-lobe variance" of xcorr
_xy_xcorr = xcorr(x, rng.permutation(y))
# the above will underestimate xcorr from auto-correlation
# a more appropriate surrogate would be simulating a counterfactual DAG where
# all common inputs are broken into independent paths
# while this is infeasible without oracle knowledge, this may be an inroad to 
# deriving an expression for the expected std.dev(xcorr(side_band))


mid_lag = len(xx_xcorr)//2
lags = np.arange(0,len(xx_xcorr))-mid_lag

side_std_xy = np.std(xy_xcorr[(nt//2+nplot//2):]) # has to do with autocorr!
side_std_xx = np.std(xx_xcorr[(nt//2+nplot//2):]) # has to do with autocorr!
side_std_yy = np.std(yy_xcorr[(nt//2+nplot//2):]) # has to do with autocorr!
print(side_std_xy)
#%%


#%%

fig,ax= plt.subplots(figsize=(10,4))
ax.plot(lags, xy_xcorr,'k');
# ax.plot(lags, _xy_xcorr,'b',linewidth=.5);
1/pythag(pso_x,pso_y)
1/pythag(np.std(x),np.std(y))

noise_std = np.std(xy_xcorr[nt//2+1:])
# noise_std = np.std(_xy_xcorr)
ax.plot(0, pr_xy,'gx',markersize=10)
ax.plot([-mid_lag, mid_lag], [noise_std,noise_std],'m--')
ax.plot([-mid_lag, mid_lag], [-noise_std,-noise_std],'m--')
ax.set_xlim([-nplot,nplot])
xy_xcorr[nt//2]

esnr_xcorr_xy = xy_xcorr[nt//2]/noise_std
print(f'xcorr(lag=0) = {xy_xcorr[mid_lag]:.2f}, r2 = {er_xy:.2f}\n')
print(f'          emp. 0-lag SNR = {esnr_xy:.3f}') 
print(f'emp. peak/side xcorr SNR = {xy_xcorr[mid_lag] / side_std_xy:.3f}') # what we're measuring for analysis later
ax.set_title('how can we predict the magenta bars? \nif we can, we predict XCORR-SNR');
# peaksnr_xy = 2*xy_xcorr[nt//2] / (xx_xcorr[nt//2]+yy_xcorr[nt//2])
# print(peaksnr_xy)
fig

#%%
# Experimental 3D XCORR visualization - feel free to ignore
'''
fig,ax=plt.subplots()
ax.plot(xp,np.roll(yp,0),'k.')
#%%
fig,_ = plt.subplots(figsize=(12,7))
ax = fig.add_subplot(projection='3d')
for lag in range(-900,900,10):
    c = np.abs(lag)/900 * np.array([1,0,0])
    s = .1*np.abs(xy_xcorr[lag+mid_lag])**2
    
    if lag == 0:
        c = [0,0,1]
        s = 5
    ax.scatter(lag, xp,np.roll(yp,lag),color=c,marker='.',s=s)
ax.view_init(elev=10., azim=70)
fig
#%%
ax.view_init(elev=5., azim=85)
fig

#%%
ax.view_init(elev=0., azim=0)
fig
#%%
'''


















#%%