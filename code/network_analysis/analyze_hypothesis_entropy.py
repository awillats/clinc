import numpy as np
import networkx as nx

%load_ext autoreload
%autoreload 2

import pandas as pd
import example_circuits as egcirc
import network_analysis_functions as net
import network_plotting_functions as netplot
import network_data_functions as netdata
import coreachability_source_classification as cor

import matplotlib.pyplot as plt
import plotting_functions as myplot

#%%
#GENERATE hypothesis set 
N_circ = 4
N = 5
p = 0.1
As = egcirc.gen_random_circuit_set(N_circ, N, 0.2)
N_circ = len(As)
N = As[0].shape[0]

Rs = [net.reachability(A) for A in As]
R = Rs[0]

df = cor.compute_coreachability_tensor(R)
# # dfcor.xs(0,level='kS')
print(df)
#%%
dg = df[df['kS']==0]
dg['iA'].unique()
#%%
# 
dcs = cor.get_coreachability_from_source(df,0)
print(dcs)
#%%
'''
COMPUTE reach, corr

adj 
 \ 
  \----------------(intv→new adj)-- CL @ 1 
   \       from S       from S 
    \       \ \ \        \ \ \
   reach 
       \ 
       corr 
'''

experiments = ['adj','corr']+[f'corr open@{i}' for i in range(N)]+[f'corr ctrl@{i}' for i in range(N)]
plot_types = [netplot.parse_plot_type(p) for p in experiments]

    
