import numpy as np 
import networkx as nx 

%load_ext autoreload
%autoreload 2


import matplotlib.pyplot as plt
import plotting_functions as myplot

import network_plotting_functions as netplot
import network_analysis_functions as net
import coreachability_source_classification as coreach
#%%
'''
- [ ] I'm annoyed at how networkx (via matplotlib) handles arrow styles 
    - can't have dotted arrows without arrowheads 
    - have to redraw 
    - proposed solution: look at draw_np_adj, switch to draw_networkx_edges() 
        - to see if this gives us more control 
    - proposed solution: switch everything to plotly https://plotly.com/python/network-graphs/
- [ ] compartmentalize plotting for easier composition
- ( ) ideally this script should expose computing all the derived matrices separately from plotting them 
- [ ] wrap circuits we want in / pull from `example_circuits.py`
    - [ ] find and include frequent circuit (curto + motif)
- [ ] alt method of displaying indirect paths?
  - https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.simple_paths.all_simple_paths.html#networkx.algorithms.simple_paths.all_simple_paths


| adj   | reach     | corr    | OL @ mid | CL @ mid |
| ----- | --------- | ------- | -------- | -------- |
| a→b→c | a→b→c,a→c | a↔b↔c↔a | ++-      | ++0      |

'''
A = np.array([[0, .1, 0],
              [1, 0,  0],
              [1, 4,  0]])
              
A0 = np.array([[0, 1, 0],
              [1, 0,  0],
              [0, 1,  0]])
              
A1 = np.array([[0, 1, 0],
              [1, 0,  0],
              [1, 1,  0]])                    
                     
A2 = np.array([[0, 1, 0],
              [0, 0,  0],
              [1, 1,  0]])

#%%    
pos = netplot._gen_layout_from_adj(A)

#%%
netplot.draw_adj_reach_corr_coreach(As[0])
#%%
'''
can specify what you want in the columns 
( see network_plotting_functions/parse_plot_type() for )
'''
cols = ['adj','reach','corr','open@1','adj ctrl@1','corr ctrl@1']
plot_types = [netplot.parse_plot_type(p) for p in cols]
plot_types
As = [A0,A1]

fig=netplot.plot_each_adj_by_plot_type(None,As,plot_types)
# 
# '''
# get_coreachability_from_source not working 
# '''
# 
# fig,ax = plt.subplots(len(As),len(cols),figsize=(3*len(cols),3.5*len(As)),sharex=True,sharey=True)
# for j,_A in enumerate(As):
#     for i,pt in enumerate(plot_types):    
#         netplot.plot_adj_by_plot_type(ax[j][i],_A, pt, add_titles=(j==0))
# # myplot.expand_bounds(ax[0][0],1.3)
# # 
# # myplot.savefig(f'results/circuit_walkthrough_{len(As)}circuits.png',this_file='/code/fig_circuit_walkthrough.py')        
fig