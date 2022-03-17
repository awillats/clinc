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

'''
Reconstructs a circuit's reachability from its "CoReachability tensor"
...that is a map of which correlations between pairs of nodes increased or decreased 
as a result of open-loop stimulation at each node 

NOTE: think this assumes all excitatory weights
'''
#%%

# G = nx.DiGraph({'A':['B','E'],'B':['C','D'],'C':['B'],'E':['D']})
# G = nx.DiGraph({'A':['B'], 'B':['C'], 'C':['D'], 'D':['E']})
# N = len(G.nodes())
# Generate random circuit with N nodes, conneciton probability p 
N = 10
G = nx.fast_gnp_random_graph(N,0.8*N/N**2,directed=True)
A = netdata.nx_to_np_adj(G)
R = net.reachability(A).astype(int)
df = cor.compute_coreachability_tensor(R)
# df
#%%
'set up multi-index for co-reachability'
df = df[df['iA']!=df['jB']] # dont care about A→A connections for now
dft = df.set_index(['kS','iA','jB']).sort_values(['kS','iA','jB'])
# dft
#%%
'Only care about connections adjacent to the source node'
c1 = dft.index.get_level_values('kS')==dft.index.get_level_values('iA')
c2 = dft.index.get_level_values('kS')==dft.index.get_level_values('jB')
dft_local = dft.loc[np.logical_or(c1,c2)]
# dft_local
#%%
'''
build reconstruction based on edges with increased correlations
if corr(A,B | OL@A) > corr(A,B), A→→B
'''
ReR = nx.DiGraph()
for i,row in dft_local.iterrows():
    # print(row['type'])
    # print(i)
    nodes = i[1:]
    node_self = i[0]
    
    other_nodes = list(nodes)
    other_nodes.remove(node_self)
    node_other = other_nodes[0]
    
    if row['type'] == 'S+':
        ReR.add_edge(node_self,node_other)
    # adding this back in seems to reconstruct fork-shaped reachability
    # elif row['type'] == 'S-':
        # R.add_edge(node_other,node_self)
        pass
ReR_adj = netdata.nx_to_np_adj(ReR,N)
ReCorr = net.binary_correlations(ReR_adj)
# print(ReR.edges)
#%%
reach_error = R-ReR_adj
# ignore reachability errors along the diagonal
reach_error = netplot.censor_diag(reach_error.astype(float),np.nan) 
reach_error_norm = np.nansum(np.abs(reach_error))
#%%
# plot true and reconstructed circuits
fig,ax=plt.subplots(2,3,figsize=(16,12),sharex=True,sharey=True)
myplot.unbox_each(ax)
netplot.draw_adj_reach_corr(A, ax[0,:],grey_correlations=True)

netplot.draw_adj_reach_corr(ReR_adj, ax[1,:],grey_correlations=True)
ax[1][0].cla()

ax[1,1].set_title(f'reach from open-loop\nrecon. error:{reach_error_norm}',fontsize=20)
myplot.expand_bounds(ax[0][0])
fig





        





