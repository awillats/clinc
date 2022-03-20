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

    
#%%
#GENERATE hypothesis set 
N_circ = 6
# N = 3
p = 0.2
# As = egcirc.gen_random_circuit_set(N_circ, N, p)
As = egcirc.get_common_3node()
N_circ = len(As)
N = As[0].shape[0]

Rs = [net.reachability(A) for A in As]
A = netdata.nx_to_np_adj(netdata.arrow_str_to_networkx('A→B→C',line_delim=';'))
# A = As[0]
R = net.reachability(A)

df = cor.compute_coreachability_tensor(R)
print(R)

netplot.draw_adj_reach_corr(A,expand_bounds=1.3);

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

# experiments = ['adj','corr']+[f'corr open@{i}' for i in range(N)]+[f'corr ctrl@{i}' for i in range(N)]
ctrl_view = 'coreach'
experiments = ['adj','corr','open@0',f'{ctrl_view} ctrl@0','open@1',f'{ctrl_view} ctrl@1','open@2',f'{ctrl_view} ctrl@2']
print(experiments)
plot_types = [netplot.parse_plot_type(p) for p in experiments]
print(plot_types)

#%%
'''
infrastrcture:
- record results into dataframe


----
- connect compute_view_by_plot_type to plot 
    - [ ] get to plug new corrs into megaplot :)
- unify view output format? 
    - df_edgelist_to_numpy_adj
    - dataframe v.s. numpy adj 
better annotation for correlations 
    https://stackoverflow.com/questions/28372127/add-edge-weights-to-plot-output-in-networkx
'''
A
# coreach.compute_coreachability_from_src(
#%%



#%%
f,ax = myplot.subplots(len(As),len(plot_types),w=5)


def coreach_to_weighted_corr(df, N=N,weight_dict = {'S^':5,'Sv':.1,'S=':.5,'Sx':0}):
    df['weight'] = df['type'].apply(lambda sl: weight_dict[sl])
    wc = np.zeros((N,N))
    I = df['iA'].astype(int)
    J = df['jB'].astype(int)
    wc[I,J] = df['weight']
    return wc

# x
df = pd.DataFrame()

for ai,A in enumerate(As):
    Astr = netdata.graph_components_to_arrow_str(nx.DiGraph(A),line_delim=';')
    for i,p in enumerate(plot_types):
        _ax = ax[ai,i]
        
        x = net.compute_view_by_plot_type(A,p)
        pos = netplot.clockwise_circular_layout(nx.Graph(A))
        if type(x)==type(pd.DataFrame()):
            wc = coreach_to_weighted_corr(x)
            # print(wc)
            
            netplot.draw_weighted_corr(wc,_ax,more_options={'edge_color':'lightgrey'})
            
            #quick annotation of correlation at edges
            G = nx.from_numpy_matrix(wc, create_using=nx.DiGraph)
            
            # df to edge label dictionary
            ij = zip(x.iA,x.jB)
            ijt = zip(ij,x.type)
            el = dict(ijt)
            # print(el)
            # nx.draw_networkx_edge_labels(G, pos=pos,edge_labels=el,ax=ax[i],font_color='#ff0000',font_weight='bold',font_size=20,bbox={'color':'#ffffff00','edgecolor':None})
        else:
            netplot.draw_np_adj(x,_ax)
            
        'draw intervention from plot_type_loc dict'
        netplot.indicate_intervention_from_plot_type_loc(_ax,pos,p)

        if ai==0:
            _ax.set_title(netplot.plot_type_loc_to_str(p),fontsize=15,
                backgroundcolor=p['plot_type'].lightcolor())
        
        df_row = pd.DataFrame()
        df = df.append({'adj':Astr,'view_type':str(p['plot_type']),'intv_loc':p['intervention_location'],'result':x},ignore_index=True)
# myplot.expand_bounds(ax[0][0], .15)
f    
#%%
df