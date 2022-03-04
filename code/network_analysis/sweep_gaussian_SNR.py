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
off_diag = ~np.eye(3,dtype=bool)

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
CTRL['target_fn'] = lambda nt: sim.gen_gauss(nt,123)*1


nt = int(5e6)
# W = 1.5*egcirc.get_curto_overrepresented_3node()[0]
W = .9*np.array(
[[0,1,0],
[0,0,1],
[0,0,0]])

W_ctrl = net.__sever_inputs(W, CTRL)

Rw_pasv = net.reachability_weight(W)
Rw_ctrl = net.reachability_weight(W_ctrl)


CTRL_node = ['A','B','C'][CTRL['location']]

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

sweep_vars = np.logspace(-3, 3, 50)
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

    this_varS_OL = this_S.copy() + (B*np.var(u_OL))[0]
    this_varS_OL
    this_varS
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
    corr_pasv = net.predict_and_quantify_correlations(Rw_pasv, this_varS_OL, X)
    corr_ctrl = net.predict_and_quantify_correlations(Rw_ctrl, this_varS_ctrl_lerp, Xctrl)

    # node, only saving one correlation of interest. 
    # TODO: generalize this into saving a dataframe of results
    # pasv_corrs.append(corr_pasv['r2_empr'][1,2])
    # ctrl_corrs.append(corr_ctrl['r2_empr'][1,2])
    pasv_corrs.append(corr_pasv)
    ctrl_corrs.append(corr_ctrl)

#%%

plt.rcParams.update({'font.size': 20})

from matplotlib.gridspec import GridSpec

'''
Lay out panels like:
|--------------|
|____|____|____|
|____|____|____|
|              |
|______________|

'''
n_cols = 6
height_ratios = [1,1,6]
fig = plt.figure(figsize=(2.5*n_cols,sum(height_ratios)*1.5))
gs = GridSpec(3,n_cols, figure=fig, height_ratios=height_ratios)

axs = []

axs.append( [fig.add_subplot(gs[0,i]) for i in range(n_cols)] )
axs.append( [fig.add_subplot(gs[1,i]) for i in range(n_cols)] )
axs.append(fig.add_subplot(gs[2,:]))

'DRAW line plots for corr'
a = axs[2]

p = lambda M: M[off_diag].flatten()[1:4] #get off diagonal corrs

pasv_r2 = [p(c['r2_empr']) for c in pasv_corrs]
ctrl_r2 = [p(c['r2_empr']) for c in ctrl_corrs]

# a.plot(sweep_vars, [p(c['r2_pred']) for c in pasv_corrs],'o',color='dodgerblue',fillstyle='none')
a.plot(sweep_vars, pasv_r2,'dodgerblue',linewidth=3)

# a.plot(sweep_vars, [p(c['r2_pred']) for c in ctrl_corrs],'o',color='orange',fillstyle='none')
a.plot(sweep_vars, ctrl_r2,'orange',linewidth=3)
dy = 0.01
bluec = 'steelblue'
ol_color = 'dodgerblue'
cl_color = 'orange'
a.text(sweep_vars[0],pasv_r2[0][0]+dy,'A,B',fontsize=15,color=bluec)
a.text(sweep_vars[0],pasv_r2[0][1]+dy,'A,C',fontsize=15,color=bluec)
a.text(sweep_vars[0],pasv_r2[0][2]+dy,'B,C',fontsize=15,color=bluec)

a.text(sweep_vars[-1],ctrl_r2[-1][0]+dy,'A,B',fontsize=15,color=cl_color)
a.text(sweep_vars[-1],ctrl_r2[-1][1]+5*dy,'A,C',fontsize=15,color=cl_color)
a.text(sweep_vars[-1],ctrl_r2[-1][2]-dy,'B,C',fontsize=15,color=cl_color)

a.spines['top'].set_visible(False)
a.spines['right'].set_visible(False)

a.set_xscale('log')
a.set_xlabel('$\sigma_{intervention}$')
a.set_ylabel('$r^2$',rotation='horizontal',ha='right')

'DRAW weighted corr circuits'
chain_pos = {0:[-1,.7],1:[0,.6],2:[.7,0]}
for i in range(0,n_cols):
    si = (len(sweep_vars)*i)//n_cols
    
    ax0= axs[0][i]
    ax1 = axs[1][i]
    pos=netplot.draw_weighted_corr(pasv_corrs[si]['r2_empr'], ax0,pos_override=chain_pos)
    pos_i = pos[CTRL['location']]
    netplot.indicate_intervention(ax0, pos_i)
    netplot.draw_weighted_corr(ctrl_corrs[si]['r2_empr'], ax1,pos_override=chain_pos)
    netplot.indicate_ctrl(ax1, pos_i,markersize=10)
pos
# axs[0].set_title('intervention at B')
fig.suptitle('A→B→C\nintervention at B')
fig.text(.1,.80,'open-\nloop',ha='right',color=ol_color)
fig.text(.1,.70,'closed-\nloop',ha='right',color=cl_color)
fig.savefig(f'bidirectional_corr_circuits_{CTRL["effectiveness"]*100:.0f}pc_at_{CTRL_node}.png',bbox_inches="tight",facecolor='w')
fig

#%%
idx_list = lambda L,i: np.array([x[i] for x in L])

fig,ax = plt.subplots(2,1,figsize=(8,8),sharex=True)
ax[0].plot(sweep_vars, idx_list(pasv_r2,1),ol_color,':',linewidth=1)
ax[0].plot(sweep_vars, ctrl_r2,cl_color,':',linewidth=1)
ax[0].plot(sweep_vars, idx_list(pasv_r2,2),ol_color,linewidth=4)
ax[0].plot(sweep_vars, idx_list(ctrl_r2,2),cl_color,linewidth=4)
ax[0].set_xscale('log')

a = ax[0]
a.text(sweep_vars[0],pasv_r2[0][1]-15*dy,'A,C',fontsize=15,color=bluec)
a.text(sweep_vars[0],pasv_r2[0][2]+5*dy,'B,C',fontsize=15,color=bluec)

a.text(sweep_vars[-1],ctrl_r2[-1][1]+10*dy,'A,C',fontsize=15,color=cl_color)
a.text(sweep_vars[-1],ctrl_r2[-1][2]-dy,'B,C',fontsize=15,color=cl_color)

a.spines['top'].set_visible(False)
a.spines['right'].set_visible(False)

a.set_xscale('log')
a.set_ylabel('$r^2$',rotation='horizontal',ha='right')


pasv_disnr = idx_list(pasv_r2,2)/idx_list(pasv_r2,1)
ctrl_disnr = idx_list(ctrl_r2,2)/idx_list(ctrl_r2,1)
ax[1].plot(sweep_vars, pasv_disnr ,ol_color,linewidth=2)
# ax[1].plot(sweep_vars, idx_list(pasv_r2,2)/idx_list(pasv_r2,0),ol_color,linewidth=1)
ax[1].plot(sweep_vars, ctrl_disnr,cl_color,linewidth=2)
# ax[1].plot(sweep_vars, idx_list(ctrl_r2,2)/idx_list(ctrl_r2,0),cl_color,linewidth=2)

ax[1].set_xlabel('$\sigma_{intervention}$')
ax[1].set_yscale('log')
ax[1].set_ylabel('$SNR:\\frac{direct}{indirect}$ \n=    \n $\\frac{r^2(B,C)}{r^2(A,C)}$',rotation='horizontal',ha='right',va='center')

ax[1].text(sweep_vars[0],pasv_disnr[0]+2,'open-loop',color=ol_color,fontsize=15)
ax[1].text(sweep_vars[0]+3e-3,min(ctrl_disnr[0:10])-100,'closed-loop',color=cl_color,fontsize=15)

fig.savefig(f'directSNR_{CTRL["effectiveness"]*100:.0f}pc_at_{CTRL_node}.png',bbox_inches="tight",facecolor='w')
fig.suptitle('A→B→C\nintervention at B')
fig
#%%
# # '''
# # DEBUG: verify prediction versus empirical
# # '''
# 
# f,a = plt.subplots(figsize=(10,5))
# 
# p = lambda M: M[off_diag].flatten()
# a.plot(sweep_vars, [p(c['r2_pred']) for c in pasv_corrs],'o',color='dodgerblue',fillstyle='none')
# a.plot(sweep_vars, [p(c['r2_empr']) for c in pasv_corrs],'dodgerblue')
# 
# a.plot(sweep_vars, [p(c['r2_pred']) for c in ctrl_corrs],'o',color='orange',fillstyle='none')
# a.plot(sweep_vars, [p(c['r2_empr']) for c in ctrl_corrs],'orange')
# a.set_xscale('log')
# # a.plot([ c['max_diff'] for c in ctrl_corrs],'orange')
# f


#%%






#%%
# sys.exit()

'''
extract B→C correlation
'''
pasv_corrs_BC = [c['r2_empr'][1,2] for c in pasv_corrs]
ctrl_corrs_BC = [c['r2_empr'][1,2] for c in ctrl_corrs]
#%%

_pasv_corrs = pasv_corrs_BC 
_ctrl_corrs = ctrl_corrs_BC
cl_linestyle = '-' if CTRL["effectiveness"] >= 0.999 else ':'


f,a = plt.subplots(figsize=(15,8))
a.plot(sweep_vars, _pasv_corrs[0]*np.ones(sweep_vars.shape),':',color='grey')
mid = 3*len(sweep_vars)//4
a.text(sweep_vars[mid], _pasv_corrs[0]-.08, 'passive', color='grey')

a.plot(sweep_vars, _pasv_corrs, color='dodgerblue')
a.text(sweep_vars[0], _pasv_corrs[0]+0.05, 'open-loop', color='dodgerblue')

a.plot(sweep_vars, _ctrl_corrs,cl_linestyle,color='orange')
a.text(sweep_vars[0], _ctrl_corrs[0]+0.05, f'closed-loop\n {CTRL["effectiveness"]*100:.0f}%', color='orange')

a.set_xscale('log')
a.set_ylim([-.1,1.1])
a.set_xlabel('$\sigma_{intervention}$')
a.set_ylabel('$r^2$\n B→C',rotation='horizontal',ha='right')
a.set_title(f'A→B→C \n impact of intervention at {CTRL_node}')
# f.savefig(f'bidirectional_var_control_demo_{CTRL["effectiveness"]*100:.0f}pc_at_{CTRL_node}.png',bbox_inches="tight",facecolor='w')
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
