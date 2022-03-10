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
- [ ] compartmentalize plotting for easier composition
    - single correlation 
        draw_correlations(adj_ctrls[i], Corr=corr_ctrls[i],
            ax=_ax, grey_correlations=True)
        indicate_ctrl(_ax, pos[i],color='#b4a390')
    - severed adj 
        #overlay unmodified & modified adj
        draw_np_adj(adj,          ax=_ax0, more_options=severed_edge_style)
        draw_np_adj(adj_ctrls[i], ax=_ax0)
        indicate_ctrl(_ax0, pos[i])
        indicate_ctrl(_ax1, pos[i])
    - weighted correlation (from open-loop)
    
- ( ) improve size of OL indication 
- [ ] pull circuit from egcirc 


| adj   | reach     | corr    | OL @ mid | CL @ mid |
| ----- | --------- | ------- | -------- | -------- |
| a→b→c | a→b→c,a→c | a↔b↔c↔a | ++-      | ++0      |

'''
A = np.array([[0, .1, 0],
              [1, 0,  0],
              [1, 4,  0]])
A0 = np.array([[0, .1, 0],
              [1, 0,  0],
              [0, 4,  0]])
A1 = np.array([[0, .1, 0],
              [1, 0,  0],
              [1, 4,  0]])                           

# rA = net.reachability(A);
# rwA = net.reachability_weight(A);
# corrA = net.binary_correlations(A)
#%%    
pos = netplot._gen_layout_from_adj(A)
#%%
fig, ax = plt.subplots(2,6,figsize=(18,7))
# adj_ctrls = net.each_closed_loop_adj(A) 
# corr_ctrls = net.each_closed_loop_correlations(A)
ax = netplot.draw_controlled_adj_correlations(ax, A)
# fig
#%%

# adjs = [A0,A1]

from aenum import Flag, auto
# see https://github.com/awillats/clinc-gen/blob/main/small_circuit_scripts/circuit_functions/run_PID_ctrl.py 
# for another usage of Flag, auto
# some discussion of enum vs aenum here: https://stackoverflow.com/questions/60635855/python-enum-flag-with-one-flag-that-is-used-by-some-others
def strip_trailing_int(str,delim='@'):
    return int(str.split(delim)[1])

class NetPlotType(Flag):
    ADJ = auto() 
    REACH = auto()
    CORR = auto() 
    CTRL = auto()
    OPEN = auto()
    ADJ_CTRL = ADJ | CTRL
    CORR_CTRL = CORR | CTRL
    REACH_CTRL = REACH | CTRL
    
    def __init__(self,flag_val):
        # Flag.__init__(self) #replace with super?
        # super(NetPlotType, self).__init__()
        super().__init__()
        self.intervention_location=None
    def set_intervention_location(self, loc):
    
        self.intervention_location = loc
    # 
    def __repr__(self):
        r = f'{self.name}'
        if hasattr(self,'intervention_location') and self.intervention_location is not None:
            r +=f'@{self.intervention_location}'
        return r
    def __str__(self):
        return self.__repr__()

n = NetPlotType(0)

a=NetPlotType.ADJ
r=NetPlotType.REACH
a
r
ar = a|r
print(ar)

print(ar & a)
print(ar & r)

cc=NetPlotType.CORR_CTRL
print(cc)

        #%%
def parse_plot_type(plot_str):
    plot_str = plot_str.lower()
    # pt = NetPlotType.DEFAULT
    pt = NetPlotType(0)
    
    if 'adj' in plot_str:
        pt |= NetPlotType.ADJ
    if 'reach' in plot_str:
        pt |= NetPlotType.REACH
    if 'corr' in plot_str:
        pt |= NetPlotType.CORR
    if 'ctrl' in plot_str:
        pt |= NetPlotType.CTRL
        pt.set_intervention_location(strip_trailing_int(plot_str))
        
    if 'open' in plot_str:
        pt |= NetPlotType.OPEN
        pt.set_intervention_location(strip_trailing_int(plot_str))
        
    return pt
# ---- 

def plot_adj_by_plot_type(ax, A, plot_type):
    add_titles = True
    grey=True
    plot_funs = {
        NetPlotType(0) : lambda adj,ax,intv_loc: adj*2,
        NetPlotType.ADJ :   lambda adj,ax,intv_loc: netplot.draw_np_adj(adj,ax=ax),
        NetPlotType.REACH : lambda adj,ax,intv_loc: netplot.draw_reachability(adj,ax=ax),
        NetPlotType.CORR :  lambda adj,ax,intv_loc: netplot.draw_correlations(adj,ax=ax,grey_correlations=grey),
        NetPlotType.ADJ_CTRL :  lambda adj,ax,intv_loc: netplot.__draw_ctrl_adj_at_source(adj=adj,ax=ax,intv_loc=intv_loc),
        NetPlotType.CORR_CTRL :  lambda adj,ax,intv_loc: netplot.__draw_ctrl_correlations_at_source(adj=adj,ax=ax,intv_loc=intv_loc,grey_correlations=grey),
        # NetPlotType.REACH_CTRL :  lambda adj,ax,intv_loc: netplot.__draw_coreachability_at_source(adj,ax=ax,intv_loc=intv_loc),
        # NetPlotType.CTRL :  lambda adj,ax,intv_loc: netplot.__draw_coreachability_at_source(adj,ax=ax,intv_loc=intv_loc),
        NetPlotType.OPEN :  lambda adj,ax,intv_loc: netplot.__draw_coreachability_at_source(adj,ax=ax,intv_loc=intv_loc,grey_correlations=grey),
    }
    this_plot_fun = plot_funs.get(plot_type)
    
    # print(f'this_plot_fun:{this_plot_fun}\n for {plot_type}')
    
    this_plot_fun(A, ax, plot_type.intervention_location)
    if add_titles:
        ax.set_title(str(plot_type),color='lightgrey')
    myplot.expand_bounds(ax)
    return ax
#-----
cols = ['adj','reach','corr','open@1','adj ctrl@1','corr ctrl@1']
plot_types = [parse_plot_type(p) for p in cols]

fig,ax = plt.subplots(2,len(cols),figsize=(3*len(cols),7))
for j,_A in enumerate([A0,A1]):
    for i,pt in enumerate(plot_types):    
        plot_adj_by_plot_type(ax[j][i],_A,pt)
# fig
#%%
fig,ax = plt.subplots(1,3,figsize=(9,3))
df = coreach.compute_coreachability_tensor(net.reachability(A))
# ax = netplot.draw_coreachability_by_source(df,ax,node_position=pos,grey_correlations=True)
# ax = netplot.__draw_coreachability_by_source(A,ax,grey_correlations=True)
fig