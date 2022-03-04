import numpy as np
from numpy.random import default_rng

# rng = default_rng(seed=123)

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
no_CTRL = sim.NONE_CTRL
CTRL = sim.DEFAULT_CTRL
CTRL['location'] = 1
# CTRL['target_fn'] = lambda nt: 1*np.sin(np.linspace(0,9000*np.pi,nt))
CTRL['effectiveness'] = 1.0
CTRL['target_fn'] = lambda nt: default_rng(seed=123).standard_normal(nt)*1/2
# np.random.randn(nt)*10


nt = int(5e6)
# W = 1.5*egcirc.get_curto_overrepresented_3node()[0]
W = 1*np.array(
[[0,1,0],
[0,0,1],
[0,0,0]])

W_ctrl = net.__sever_inputs(W, CTRL)

Rw_pasv = net.reachability_weight(W)
Rw_ctrl = net.reachability_weight(W_ctrl)

#%%


def lerp(a,b,p):
    return (1-p)*a + p*b
'''
Prepare for simulation
'''
N = W.shape[0]
# E = np.random.randn(nt,N)
S = np.array([1.,1.,1.]) # source standard deviations
varS = S**2
B = -rowmat(np.array([1.,2.,3.]))*0
u = colmat(sim.flat_fn(nt))


varS_ctrl = varS.copy()
test_targ = CTRL['target_fn'](nt)
ci = CTRL['location']
varS_ctrl[ci] = np.var(CTRL['target_fn'](nt))

#%%
'''
Simulate both scenarios
'''
X     = sim.sim_dg(nt, W, S, B, u, ctrl=no_CTRL)
Xctrl = sim.sim_dg(nt, W, S, B, u, ctrl=CTRL)


Xts = X.copy()
'''
If the system is simulated as a discrete-time dynamical system,
    need to do something like this to look for 1-lag correlations 
    ( a more robust alternative is needed )
'''
# Xts[:,1] = np.roll(Xts[:,1],-1)

#%%
'''
Predict and quantify correlations
'''
def predict_and_quantify_correlations(Rw, varS, X, verbose=True):
    '''
    Rw - weighted reachability
    varS - vector of source variances
    X - timerseries [samples x nodes]
    '''
    
    corr_pred = net.correlation_matrix_from_reachability(Rw, varS)
    r2_pred  = corr_pred**2
    corr_empr = np.corrcoef(X, rowvar=False) 
    r2_empr = corr_empr**2 
    max_diff = np.max(np.abs(r2_empr-r2_pred))
    if verbose:
        print(r2_pred,'\n')
        print(r2_empr)
        print(f'\nmax diff = {max_diff:.1e}')
    
    return {'r2_pred':r2_pred,'r2_empr':r2_empr,'r_pred':corr_pred,'r_empr':corr_empr,'max_diff':max_diff}


'''
CURRENTLY A MESS
'''


total_ctrl_effect = CTRL['effectiveness']
varS_ctrl_lerp = lerp(varS,varS_ctrl, total_ctrl_effect)

0.9
corrs_pasv = predict_and_quantify_correlations(Rw_pasv, varS, X)
corrs_ctrl = predict_and_quantify_correlations(Rw_ctrl, varS_ctrl_lerp, Xctrl)

#%%

'''
# Treating control effectiveness as a post-hoc hyperparameter
n_sweep = 100
es = np.linspace(0,1,n_sweep)
ds = []
for e in es:
    _varS_ctrl_lerp = lerp(varS,varS_ctrl, e)
    _corrs_ctrl = predict_and_quantify_correlations(Rw_ctrl, _varS_ctrl_lerp, Xctrl,False)
    ds.append(_corrs_ctrl['max_diff'])
#%%
post_hoc_eff = es[np.argmin(ds)]
post_hoc_err = min(ds)
f,a = plt.subplots()
print()
a.plot([0,1],[0,0],'k--')
a.plot(es,ds);
a.plot(post_hoc_eff,post_hoc_err,'ro')
a.plot(CTRL['effectiveness'],0,'x',color='limegreen',markersize=10)
a.set_title(f'pre:{CTRL["effectiveness"]:.2f}, post:{post_hoc_eff:.3f}, post err = {post_hoc_err:.2e}')
# a.set_ylim([-1e-3,2e-1])
f
'''
#%%
n_plot = int(2e3)

corrs_pasv['r2_empr']
corrs_ctrl['r2_empr']
#%%
'Plot correlations from uncontrolled network'
fig,axs = netplot.plot_empirical_corrs(W, Rw_pasv, X, corrs_pasv['r2_pred'], corrs_pasv['r2_empr'],n_plot)
print(corrs_pasv['r2_empr'])
axs[3][1].text(-.4,0,f'pred err:\n {corrs_pasv["max_diff"]:.1e}',color='grey',fontsize=15)
fig
#%%
W_ctrl
wbar = lambda W: net.inf_sum_mat(W) - np.eye(W.shape[0])
wbar(W)
wbar(W_ctrl)
#%%

net.inv_multi_lerp(.5,3)
#%%
Rw_ctrl
fig,axs = netplot.plot_empirical_corrs(W_ctrl, Rw_ctrl, Xctrl, corrs_ctrl['r2_pred'], corrs_ctrl['r2_empr'],n_plot)
axs[1][CTRL["location"]].set_title(f'CTRL @ {CTRL["location"]}')
fig
#%%
# plt.plot(Xctrl[:,0],Xctrl[:,2],'k.',markersize=0.01)
# #%%
# fig,ax=plt.subplots(figsize=(10,2))
# ax.plot( Xctrl[:,CTRL['location']] ,'k',linewidth=1)
# ax.plot( CTRL['target_fn'](nt) ,'g',linewidth=2) 
# # ax.set_xlim([0,10000])
# # ax.set_ylim([-5,5])
# ax
# fig
# # Xctrl[:,CTRL['location']].sh
#%%