import numpy as np
import networkx as nx

%load_ext autoreload
%autoreload 2

import pandas as pd
import example_circuits as egcirc
import network_analysis_functions as net
import network_plotting_functions as netplot
import network_data_functions as netdata
import network_pattern_entropy as neth
import coreachability_source_classification as cor

import matplotlib.pyplot as plt
import plotting_functions as myplot
#%%
# set pandas display width
pd.options.display.max_colwidth=100
#%%
'''
TODO 
- [ ] add passive to table
    - [ ] convert view for passive to dataframe 

- [ ] add summary plot

- [ ] refine example hypothesis set 
    - ideally including walkthrough hypotheses?
        - more powerful if these could be distinct from walkthrough ... 

- [ ] look for key differences 
    - ideal scenario is where closed-loop control is the best for the hypothesis set across ALL intervention locations 
    - also ideal would include many hypotheses

PLOTS:
- [ ] bar plots for distro
- [ ] summary plot by type, by location


CLEANUP:
- PR distinct is based on sampling with replacement ... 
    ... which means that perfect interventions can't hit "perfect" on this metric
    ... should update to sample without replacement
- split sweep and plot into two separate functions 
- file away / relocate 
    - def coreach_to_weighted_corr
FUTURE WORK:
- parallelize sweep across hypothesis, intervention

'''
    
#%%
#GENERATE hypothesis set 
N_circ = 100
N = 5
p = 0.1 # 50ish max

# As = egcirc.gen_random_unique_circuit_set(N_circ, N, p)

N_unique = 0
As = []
n_tries = 0

N_nodes=N
p_connect=p
n_tries_max=100


As = egcirc.gen_random_circuit_set(N_circ, N_nodes, p_connect=p)
As = egcirc.merge_lists_of_circuits(As,min_nodes=N)
print(len(As))
N_circ = len(As)
#%%
# ad = {}
# for i,A in enumerate(As):
#     a = str(A)
#     if a in ad.keys():
#         ad[a] += 1
#         print(netdata.np_adj_to_arrow_str(A))
#     else:
#         ad[a] = 1
# print(list(ad.values()))

#%%
N_circ = len(As)
# As = egcirc.gen_random_unique_circuit_set(N_circ-N_unique, N_nodes, p_connect=p,n_tries_max=1000)
# assert(len(As) == N_circ)
print(f'Done generating {N_circ} circuits!')
#%%
# As = A_fig

#%%
N_circ = len(As)
N = As[0].shape[0]

# # Check some sample circuits
# Rs = [net.reachability(A) for A in As]
# A = netdata.nx_to_np_adj(netdata.arrow_str_to_networkx('A→B→C',line_delim=';'))
# # A = As[0]
# R = net.reachability(A)
# df = cor.compute_coreachability_tensor(R)
# netplot.draw_adj_reach_corr(A, expand_bounds=1.3);

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

ctrl_view = 'coreach'
experiments = ['corr','open@0',f'{ctrl_view} ctrl@0','open@1',f'{ctrl_view} ctrl@1','open@2',f'{ctrl_view} ctrl@2']
# print(experiments)
plot_types = [netplot.parse_plot_type(p) for p in experiments]
print(plot_types)

#%%
'''
infrastructure:
- connect compute_view_by_plot_type to plot 
    - [ ] get to plug new corrs into megaplot :)
- unify view output format? 
    - df_edgelist_to_numpy_adj
    - dataframe v.s. numpy adj 
better annotation for correlations 
    https://stackoverflow.com/questions/28372127/add-edge-weights-to-plot-output-in-networkx
'''
#%%


def coreach_to_weighted_corr(df, N=N,weight_dict = {'S^':5,'Sv':.1,'S=':.5,'Sx':0}):
    '''
    for plotting/viz only
    '''
    df['weight'] = df['type'].apply(lambda sl: weight_dict[sl])
    wc = np.zeros((N,N))
    I = df['iA'].astype(int)
    J = df['jB'].astype(int)
    wc[I,J] = df['weight']
    return wc

#%%
df = pd.DataFrame()

#%%
'''
Perform all interventions across all hypotheses
'''
f,ax = myplot.subplots(len(As),len(plot_types),w=5)

do_plot = False



for ai,A in enumerate(As):
    # bundling to string allows compact representation for visualizing in a table
    Astr = netdata.graph_components_to_arrow_str(nx.DiGraph(A),line_delim=';')
    
    # loop across interventions for a given hypothesis
    for i,p in enumerate(plot_types):
        _ax = ax[ai,i]
        print(A)
        x = net.compute_view_by_plot_type(A, p)
        
        pos = netplot.clockwise_circular_layout(nx.Graph(A))
        if type(x)==type(pd.DataFrame()):
            wc = coreach_to_weighted_corr(x)
            # print(wc)
            G = nx.from_numpy_matrix(wc, create_using=nx.DiGraph)
            
            if do_plot: netplot.draw_weighted_corr(wc,_ax,more_options={'edge_color':'lightgrey'})
            
            #quick annotation of correlation at edges
            # - df to edge label dictionary
            ij = zip(x.iA,x.jB)
            ijt = zip(ij,x.type)
            el = dict(ijt)
            # print(el)
            # nx.draw_networkx_edge_labels(G, pos=pos,edge_labels=el,ax=ax[i],font_color='#ff0000',font_weight='bold',font_size=20,bbox={'color':'#ffffff00','edgecolor':None})
        else:
            if do_plot: netplot.draw_np_adj(x,_ax)
            
        #draw intervention from plot_type_loc dict
        if do_plot: netplot.indicate_intervention_from_plot_type_loc(_ax,pos,p)

        if do_plot and ai==0:
            _ax.set_title(netplot.plot_type_loc_to_str(p),fontsize=15,
                backgroundcolor=p['plot_type'].lightcolor())
        
        # add a single intervention X hypothesis to the dataframe
        df_row = pd.DataFrame()
        df = df.append({'adj':Astr,
                    'view_type':str(p['plot_type']),
                    'intv_loc':p['intervention_location'],
                    'result':x}, 
                    ignore_index=True)
# myplot.expand_bounds(ax[0][0], .15)

if do_plot: f    

#%%
df
#%%
# df['adj'].value_counts()
#check for duplicates!
#%%
# DFC: filtered dataframe of coreachability

dfc = df[(df['view_type']=='COREACH_CTRL') | (df['view_type']=='OPEN')]
dfc = dfc.reset_index()

# # pick out single row for test analysis
# df0 = dfc.loc[0]
# neth.extract_circuit_signature_single_df(df0['result'])['fingerprint_dict']
# 
# print(df0['result'])
# df0['result'].groupby('kS').agg({'type':' '.join})

def get_first_value(d):
    '''
    takes a 1-item list and returns its sole value
    '''
    assert(len(d.values()) == 1)
    return list(d.values())[0]
    
df_to_fingerprint = lambda df: get_first_value(neth.extract_circuit_signature_single_df(df)['fingerprint_dict'])
# df_to_fingerprint = lambda df: df.agg({'type':''.join})
# dfc['fingerprint'] = dfc['result'].apply( lambda d: d.groupby('kS').agg({'type':' '.join}))

#%%
# Transform coreachability entries to "fingerprint" strings
dfc['fingerprint'] = dfc['result'].apply(df_to_fingerprint)
# Cleanup: Subselect columns, arrange hierarchical index and sort
dfcs = dfc[['view_type','intv_loc','adj','fingerprint']]
idx_cols = ['intv_loc','view_type','adj']
dfcs.index = pd.MultiIndex.from_frame(dfcs[idx_cols])
dfcs = dfcs.drop(idx_cols,axis=1)
dfcs = dfcs.sort_values(idx_cols)

#DFCS: Sorted coreachability dataframe
# - is the clearest *tidy* representation of the sweep
dfcs
#%%

#%%
'''
- Pivot DFCS to pivot_table (dfp) for better visualization
    - unstacks by hypothesis (adjacency matrix)
- compute entropy and similar across-hypothesis measures
    
TODO: assert fingerprint_idx are all equal ...

'''
# dfcs
dfp = dfcs.unstack()
# dfp
 
# Compute across-hypothesis summary statistics
dfp['distro'] = dfp.apply( lambda d: neth.count_unique_frequency(list(d.values)), axis=1)
dfp['H'] = dfp['distro'].apply(lambda d: neth.entropy_of_dict(d))
dfp['pr distinct'] = dfp['distro'].apply(lambda d: 100*(1-neth.compute_prob_dupe_from_freq(d)))
dfp['E(# equiv)'] = dfp['distro'].apply(lambda d: neth.compute_expected_equivalence_class_size_from_freq(d))
dfp
#%%
# round off columns for formatting / viz
for c,r in zip(['H','pr distinct','E(# equiv)'],[2,1,1]):
    dfp[c] = dfp[c].apply(lambda x: round(x,r))
#%%
# Print across-hypothesis summary
'''
TODO: produce table with asterisk for max
'''
dfp[['distro','H','pr distinct','E(# equiv)']]
#%%
'''
Print conclusions
- which intervention was the best?
    - highest entropy?
    - highest prob. distinct? (in theory these should be the same)
- print ALL interventions with this 
'''

#Note: this is NOT true of minimums
try:
    assert( dfp['pr distinct'].idxmax() == dfp['H'].idxmax() )
except:
    print('\n---')
    print('NOTE: max entropy at:')
    print(dfp['H'].idxmax())
    print(dfp['distro'][dfp['H'].idxmax()])
    print('\ndoesnt correspond to max prob. distinct pair of samples')
    print(dfp['pr distinct'].idxmax())
    print(dfp['distro'][dfp['pr distinct'].idxmax()])
    print('---\n\n')
    

performance_column_id = 'H'
perf_column = dfp[performance_column_id]

best_H = perf_column.max()
best_intv = perf_column.idxmax()
tied_best_intv = perf_column == best_H

# tuple → str → plot_type → plot_type.intv_type
best_intv_type = netplot.parse_plot_type(str(best_intv))['plot_type'].intv_type()
best_intv_loc = best_intv[0]

if (tied_best_intv.value_counts()[True] > 1):
    print('NOTE: Multiple tied-for-best interventions:')
    print(perf_column[tied_best_intv],'\n')
else:
    print(f'Best intervention is:\n {best_intv_type} at location {best_intv_loc}')
    print(f' ')
print(f'resulting in\n {performance_column_id}: {best_H} / {np.log2(len(As)):.2f}')

#%% 
'''
print per-location, per-intervention, average H

'''
#%%
'''
sequential intervention matrix
'''