import numpy as np
import networkx as nx

import pandas as pd
import example_circuits as egcirc
import network_analysis_functions as net
import coreachability_source_classification as cor

import matplotlib.pyplot as plt
import plotting_functions as myplot
plt.rcParams.update({'font.size': 25})
#%%
# Load adjacency matrices 
As = egcirc.get_chainlike_3node()
# As = egcirc.get_recur_dense_3node()

n = As[0].shape[0]
n_circ = len(As)
n_plot = 3+2*n
#%%

'''
plot co-reachability tensor as a function of source location
-requires As, n_circ
'''


fig, axs =  plt.subplots(1, 1, figsize=(3,3))
pos = net.draw_np_adj(As[0],axs)

#%%
# 
fig, axs = plt.subplots(n_circ, n_plot,figsize=(4.5*n_plot,5*n_circ),sharey=True)
axs[0,[0,1,2,3,5,7]]
for i,_A in enumerate(As):
    ax_row = axs[i,:]
    #interlace open-loop and closed-loop columns
    ax_ol = ax_row[[0,1,2, 3,5,7]]
    ax_cl = ax_row[[4,6,8]]
    cor.draw_adj_reach_corr_coreach(_A, axs=ax_ol, add_titles=(i==0))    
    # cor.draw_adj_reach_corr_coreach(_A, axs=axsax_, add_titles=(i==0))
    net.draw_controlled_correlations(ax_cl, _A, add_titles=(i==0)) 

fig.text((2+n_circ/2)/(n_circ+2),.92,'Interventions',size=35,va='center',ha='center')
myplot.super_ylabel(fig,'Hypothesized Circuits',35)
plt.savefig('hypo_x_intv_dense_weight2.png',dpi=100,facecolor='w')
fig
