import numpy as np
# from numpy.random import default_rng
# rng = default_rng()

%load_ext autoreload
%autoreload 2


np.set_printoptions(precision=3,suppress=True)
import matplotlib.pyplot as plt
import plotting_functions as myplot

import network_analysis_functions as net
import example_circuits as egcirc
import sys #for debug only
import scipy
import network_plotting_functions as netplot
import network_data_functions as net_data

import sim_simple_network_functions as sim
#%%
# matrix manipulation
def colmat(v):
    return v[:,np.newaxis]
def rowmat(v):
    return v[np.newaxis,:]
def censor_diag(A, censor_val=0):
    C = A.copy()
    n = C.shape[0]
    C[np.diag_indices(n)] = censor_val
    return C
# censor_diag = lambda x: x

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

CTRL = sim.DEFAULT_CTRL

nt = int(5e6)
# W = 1.5*egcirc.get_curto_overrepresented_3node()[0]
W = 1*np.array(
[[.1,1,0],
[0,0,.5],
[0,0,0]])

#%%

N = W.shape[0]
E = np.random.randn(nt,N)
S = np.array([1,1,1])
B = -rowmat(np.array([1,2,3]))*0
u = colmat(sim.flat_fn(nt))
#%%
X = sim.sim_dg(nt, W, S, B,u, ctrl=CTRL)

'''
- [ ] draw S 
- [ ] draw Ctrl!
'''
Xts = X.copy()
# Xts[:,1] = np.roll(Xts[:,1],-1)
if CTRL is None:
    Rw = net.reachability_weight(W)
else:
    Rw = net.reachability_weight(net.sever_inputs(W,CTRL['location']))

corr_pred = net.correlation_matrix_from_reachability(Rw, S**2)
r2_pred  = corr_pred**2
print(r2_pred,'\n')
corr = np.corrcoef(Xts,rowvar=False) # this this computes r2
r2_empr = corr**2 
print(r2_empr)

#%%



#%%

# print(np.round(corr,4))
print(np.round(r2_empr,4))
print()
print(np.round(r2_pred,4))
wid_ratios = [1,4,1,1,1]
fig,axs = plt.subplots(2,len(wid_ratios),figsize=(sum(wid_ratios)*3,2*3),gridspec_kw={'width_ratios': wid_ratios})

ax = axs[0,:]
ax[0].imshow(W)
ax[0].set_title('adj')

ax[1].plot(X,linewidth=3)
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
netplot.draw_weighted_corr(r2_empr,ax[3])
netplot.draw_weighted_corr(r2_pred,ax[4])

fig
#%% markdown

$$
X = E S\\
X \mathrel{+}= X(\widetilde{W}-I)
$$ 
#%%
# 1-lag correlation-plot
# if nt<1e5:
#     fig,ax = plt.subplots(3,3,figsize=(5,5),subplot_kw=dict(box_aspect=1))
#     for i in range(3):
#         for j in range(3):
#             # ax[i,j].plot(X[:-2,j],X[2:,i],'k.',markersize=.005)
#             ax[i,j].plot(X[:-1,i],X[1:,j],'k.',markersize=500/nt)
# 
#     fig

#%%
# Archived XCORR plots
'''
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
'''














#%%