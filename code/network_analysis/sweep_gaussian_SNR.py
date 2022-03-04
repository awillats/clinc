import numpy as np

# rng = default_rng(seed=123)

%load_ext autoreload
%autoreload 2

np.set_printoptions(precision=3,suppress=True)
import matplotlib.pyplot as plt
import plotting_functions as myplot
plt.rcParams.update({'font.size': 15})


import network_analysis_functions as net
import example_circuits as egcirc
import sys #for debug only
import scipy
import network_plotting_functions as netplot
import network_data_functions as net_data

import sim_simple_network_functions as sim
#%%
def lerp(a,b,p):
    return (1-p)*a + p*b
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
CTRL['target_fn'] = lambda nt: sim.gen_gauss(nt,123)*10




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

def ctrl_spec_to_varS(varS,CTRL):
    varS_ctrl = varS.copy()    
    test_targ = CTRL['target_fn'](nt)
    varS_ctrl[CTRL['location']] = np.var(CTRL['target_fn'](nt))
    return varS_ctrl

'''
Prepare for simulation
'''
N = W.shape[0]
# E = np.random.randn(nt,N)

B = -rowmat(np.array([1.,2.,3.]))*0 # input sensitivity
u = colmat(sim.flat_fn(nt)) # bias inputs

'''
Sweep-specific variables
'''

sweep_vars = np.logspace(-5,3,80)
pasv_corrs = []
ctrl_corrs = [] 
#%%
for i,v in enumerate(sweep_vars):

    this_stdv = np.sqrt(v)

    this_CTRL = CTRL.copy()
    this_CTRL['target_fn'] = lambda nt: this_stdv*CTRL['target_fn'](nt)
    u_OL = colmat(this_CTRL['target_fn'](nt))
    B = np.array([0.0, 0.0, 0.0])

    B[this_CTRL['location']] = 1.0
    B = rowmat(B)
    
    
    this_S = np.array([1.0, 1.0, 1.0]) # source standard deviations
    this_varS = this_S**2    
    this_varS_ctrl = ctrl_spec_to_varS(this_varS, this_CTRL)
    total_ctrl_effect = this_CTRL['effectiveness']
    this_varS_ctrl_lerp = lerp(this_varS,this_varS_ctrl, total_ctrl_effect)

    #% %
    '''
    Simulate both scenarios
    '''
    X     = sim.sim_dg(nt, W, this_S, B, u_OL, ctrl=no_CTRL)
    Xctrl = sim.sim_dg(nt, W, this_S, B, u, ctrl=this_CTRL)

    # % %
    '''
    Predict and measure correlations
    '''
    corr_pasv = net.predict_and_quantify_correlations(Rw_pasv, this_varS, X)
    corr_ctrl = net.predict_and_quantify_correlations(Rw_ctrl, this_varS_ctrl_lerp, Xctrl)

    # node, only saving one correlation of interest. 
    # TODO: generalize this into saving a dataframe of results
    pasv_corrs.append(corr_pasv['r2_empr'][1,2])
    ctrl_corrs.append(corr_ctrl['r2_empr'][1,2])

#%%
plt.rcParams.update({'font.size': 15})

CTRL_node = ['A','B','C'][CTRL['location']]
pasv_corrs
f,a = plt.subplots(figsize=(7,4))
a.plot(sweep_vars, pasv_corrs[0]*np.ones(sweep_vars.shape),':',color='grey')
mid = len(sweep_vars)//2
a.text(sweep_vars[mid], pasv_corrs[0]-.05, 'passive', color='grey')
a.plot(sweep_vars, pasv_corrs,color='dodgerblue')
a.text(sweep_vars[0], pasv_corrs[0]+.05, 'open-loop', color='dodgerblue')
cl_linestyle = '|' if CTRL["effectiveness"] >= 0.999 else ':'
a.plot(sweep_vars, ctrl_corrs,cl_linestyle,color='orange')
a.text(sweep_vars[0]+1e-4, ctrl_corrs[0]-.3, f'closed-loop\n {CTRL["effectiveness"]*100:.0f}%', color='orange')
a.set_xscale('log')
a.set_ylim([-.1,1.1])
a.set_xlabel('$\sigma_{intervention}$')
a.set_ylabel('$r^2$\n B→C',rotation='horizontal',ha='right')
a.set_title(f'A→B→C \n impact of intervention at {CTRL_node}')
f.savefig(f'bidirectional_var_control_demo_{CTRL["effectiveness"]*100:.0f}pc_at_{CTRL_node}.png',bbox_inches="tight",facecolor='w')
f

#%%

# # #%%
# 'Plot correlations from uncontrolled network'
# fig,axs = netplot.plot_empirical_corrs(W, Rw_pasv, X, corr_pasv['r2_pred'], corr_pasv['r2_empr'],n_plot)
# print(corrs_pasv['r2_empr'])
# axs[3][1].text(-.4,0,f'pred err:\n {corrs_pasv["max_diff"]:.1e}',color='grey',fontsize=15)
# fig
# # #%%
# # 
# # #%%
# 'Plot correlations from controlled network'
# Rw_ctrl
# fig,axs = netplot.plot_empirical_corrs(W_ctrl, Rw_ctrl, Xctrl, corr_ctrl['r2_pred'], corr_ctrl['r2_empr'],n_plot)
# axs[1][CTRL["location"]].set_title(f'CTRL @ {CTRL["location"]}')
# axs[3][1].text(-.4,0,f'pred err:\n {corrs_ctrl["max_diff"]:.1e}',color='grey',fontsize=15)
# fig
