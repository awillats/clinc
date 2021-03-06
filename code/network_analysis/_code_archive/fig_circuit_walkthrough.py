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
"""
see also /code/network_analysis/fig_3circuit_walkthrough.py
    - as of May 6 2022, that one is being used to produce the manuscript figure 

NOTE: this version is intended more as a showcase of flexible plotting options provided by 
plot_each_adj_by_plot_type
"""
#%%
'''
- [ ] I'm annoyed at how networkx (via matplotlib) handles arrow styles 
    - can't have dotted arrows without arrowheads 
    - have to redraw 
    - proposed solution: look at draw_np_adj, switch to draw_networkx_edges() 
        - to see if this gives us more control 
    - proposed solution: switch everything to plotly https://plotly.com/python/network-graphs/
    - see also svg_draw !! (installed locally)
    
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
#%%
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
As = [A0,A1]

#%%    
pos = netplot._gen_layout_from_adj(A)

#%%
netplot.draw_adj_reach_corr_coreach(As[0])
#%%
'''
can specify what you want in the columns 
( see network_plotting_functions/parse_plot_type() for )
'''
cols = ['adj','reach','corr','open@0','adj ctrl@1','corr ctrl@0']
plot_types_locs = [netplot.parse_plot_type(p) for p in cols]


fig=netplot.plot_each_adj_by_plot_type(None,As,plot_types_locs)
# # myplot.savefig(f'results/circuit_walkthrough_{len(As)}circuits.png',this_file='/code/fig_circuit_walkthrough.py')        
fig