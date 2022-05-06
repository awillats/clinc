import numpy as np 
import networkx as nx 

%load_ext autoreload
%autoreload 2


import matplotlib.pyplot as plt

import example_circuits as egcirc

import plotting_functions as myplot
import network_data_functions as netdata
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

aa = 'C→A,B; A→B'
ab = 'C→B↔A'
ac = 'C→B↔A; C→A'

'''
uses 
{from x to} syntax
'''
# As = egcirc.get_walkthrough_trio()
As = netdata.all_arrow_str_to_np_adj([aa,ab,ac], min_nodes=3)

#%%    
pos = netplot._gen_layout_from_adj(As[0])

#%%

#%%
# df = 
fig,axs = myplot.subplots(1,6)
fig = netplot.draw_adj_reach_corr_coreach(As[0],axs=axs,grey_correlations=False)

fig
#%%
'FOR DEBUG ONLY'

# df = coreach.compute_coreachability_from_src(
df = coreach.compute_coreachability_tensor(net.reachability(As[0]))
print(df[df['kS']==1])
pos_edges, neut_edges, neg_edges = coreach.get_coreachability_from_source(df, 2)

print(pos_edges)
print(neut_edges)
print(neg_edges)
# fig,ax=plt.subplots()


#%%
'''
can specify what you want in the columns 
( see network_plotting_functions/parse_plot_type() for )
'''
cols = ['adj','reach','corr','open@1','adj ctrl@1','corr ctrl@1']
plot_types_locs = [netplot.parse_plot_type(p) for p in cols]
print(plot_types_locs)

fig,axs = myplot.subplots(3,6)
fig=netplot.plot_each_adj_by_plot_type(axs,As,plot_types_locs,ax_padding=1.0)
myplot.savefig(f'results/circuit_walkthrough_{len(As)}circuits.png',
    this_file='/code/network_analysis/fig_3circuit_walkthrough.py',
    save_svg=True)        
fig

# fig