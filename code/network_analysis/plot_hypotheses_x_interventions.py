import numpy as np
import networkx as nx

%load_ext autoreload
%autoreload 2


import pandas as pd
import example_circuits as egcirc
import network_analysis_functions as net
import network_plotting_functions as netplot
import coreachability_source_classification as cor

import matplotlib.pyplot as plt
import plotting_functions as myplot
#%%
# Load adjacency matrices 
As = egcirc.get_chainlike_3node()
# As = [np.array([[0,1,0],[0,0,1],[0,0,0]])]*3
# As = egcirc.get_recur_dense_3node()

n = As[0].shape[0]
n_circ = len(As)
n_plot = 3+2*n
#%%

'''
plot co-reachability tensor as a function of source location
-requires As, n_circ

controlled correlations don't include open-loop effects....

would be incredible to produce animation / interactive plot of these panels as a function of intervention variance!!
'''


fig, axs =  plt.subplots(1, 1, figsize=(3,3))
pos = netplot.draw_np_adj(As[0],axs)
fig
#%%
# Plot open-loop impact
fig, axs = plt.subplots(n_circ, n_plot-n,figsize=(4.5*(n_plot-n),5*n_circ),sharey=True)
for i,_A in enumerate(As):
    ax_row = axs[i,:]
    ax_ol = ax_row
    _A
    netplot.draw_adj_reach_corr_coreach(_A, axs=ax_ol, add_titles=(i==0))    
    # cor.draw_adj_reach_corr_coreach(_A, axs=axsax_, add_titles=(i==0))
    # netplot.draw_controlled_correlations(ax_cl, _A, add_titles=(i==0)) 

# fig.text((2+n_circ/2)/(n_circ+2),.92,'Interventions',size=35,va='center',ha='center')
# myplot.super_ylabel(fig,'Hypothesized Circuits',35)
# fig
#%%
# Plot open-loop and closed-loop impact (interlaced)
fig, axs = plt.subplots(n_circ, n_plot,
    figsize=(4.5*n_plot,5*n_circ),
    sharex=True, sharey=True)
    
axs[0,[0,1,2,3,5,7]]
ctrl_color = '#ec970c'
for i,_A in enumerate(As):
    ax_row = axs[i,:]
    #interlace open-loop and closed-loop columns
    ax_ol = ax_row[[0,1,2, 3,5,7]]
    ax_cl = ax_row[[4,6,8]]
    netplot.draw_adj_reach_corr_coreach(_A, axs=ax_ol, add_titles=(i==0), grey_correlations=True)  
    # cor.draw_adj_reach_corr_coreach(_A, axs=axsax_, add_titles=(i==0))
    netplot.draw_controlled_correlations(ax_cl, _A, add_titles=(i==0), ctrl_color=ctrl_color) 

'HACK: transfer titles to bottom row'
for i,_ax in enumerate(ax_row):
    _ax.set_xlabel(axs[0,i].get_title(),rotation=90,fontsize=25)
    axs[0,i].set_title('')

myplot.expand_bounds(axs[0][0],1.1)  # will expand all axes, 
#effectively shrinking the graphs / adding more whitespace

intv_text_x = (2+n_circ/2)/(n_circ+2)
intv_text_y = .92
fig.text(intv_text_x, intv_text_y,'Interventions',size=35,va='center',ha='center')
myplot.super_ylabel(fig,'Hypothesized Circuits',35)

# fig.text(intv_text_x, 1-intv_text_y,'Interventions',size=35,va='center',ha='center',rotation=180)

fig.savefig('hypo_x_intv_.png',dpi=100,facecolor='w')
fig
