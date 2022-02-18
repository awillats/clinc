import numpy as np
import networkx as nx
import network_analysis_functions as net
import plotting_functions as myplot
%load_ext autoreload
%autoreload 2


#%%
# set up functions for computing whether a source can reach both A and B
def and_coreach(R,i,j):
    return np.logical_and(R[:,i],R[:,j])
def xor_coreach(R,i,j):
    return np.logical_xor(R[:,i],R[:,j])
def nor_coreach(R,i,j):
    return np.logical_not(np.logical_or(R[:,i],R[:,j]))
    
def partition_sources_ab(R,i,j):
    '''
    assumes IN x OUT convention for reachability R
    '''
    # adds diagonal elements if they don't already exist
    # this represents the assumption that sources can access every node
    R = np.logical_or(R, np.eye(R.shape[0])) 
    return {'S+':and_coreach(R,i,j),
            'S-':xor_coreach(R,i,j),
            'S0':nor_coreach(R,i,j)}

def validate_sources(S):
    '''
    only and exactly 1 category should contain true at each index
    - [ ] could also check length off all categories are equal
    '''
    Smat = np.array([S['S+'], S['S-'], S['S0']]) #3xN
    is_valid = np.all(np.sum(Smat, axis=0) == 1)
    return is_valid
    
def condense_source_type_labels(S):
    S_labels = []
    for i in range(len(S['S+'])):
        if S['S+'][i]:
            this_label = 'S+'
        if S['S-'][i]:
            this_label = 'S-'
        if S['S0'][i]:
            this_label = 'S0'
        S_labels.append(this_label)
    return S_labels

def partition_and_label_sources(R,i,j):
    return condense_source_type_labels(partition_sources_ab(R,i,j))
def compute_coreachability_tensor(R):
    n = R.shape[0]
    df = pd.DataFrame(columns=['iA','jB','kS','type'])
    for i in range(n):
        for j in range(i,n):
            _s_labels = partition_and_label_sources(R,i,j)
            for k in range(n):
                df = df.append({'iA':i,'jB':j,'kS':k,'type':_s_labels[k]},ignore_index=True)
    return df
#%%
def df_edgelist_to_numpy_adj(df, source_key, target_key, node_list):
    return nx.to_numpy_matrix(nx.from_pandas_edgelist(df, source_key, target_key, create_using=nx.DiGraph),nodelist=node_list)

def get_coreachability_from_source(df, kS):
    df_rows = df[df['kS']==kS]
    df_pos  = df_rows[df_rows['type']=='S+']
    df_neg  = df_rows[df_rows['type']=='S-']
    df_neut = df_rows[df_rows['type']=='S0']
    
    nodes = df_rows['iA'].unique()
    pos_edges = df_edgelist_to_numpy_adj(df_pos,  'iA','jB',nodes)
    neg_edges = df_edgelist_to_numpy_adj(df_neg,  'iA','jB',nodes)
    neut_edges = df_edgelist_to_numpy_adj(df_neut,'iA','jB',nodes)

    return pos_edges, neut_edges, neg_edges

def indicate_intervention(intv_idx, pos, ax, type='open-loop'):
    arrow_mag = 0.4
    arrow_c = 'k'
    # start from "outside" the node
    x0 = pos[intv_idx][0]*(1+arrow_mag)
    y0 = pos[intv_idx][1]*(1+arrow_mag)
    # point back towards the node
    dx = -pos[intv_idx][0]*arrow_mag*.8
    dy = -pos[intv_idx][1]*arrow_mag*.8
    
    # https://stackoverflow.com/questions/37819215/matplotlib-arrowheads-and-aspect-ratio
    # https://stackoverflow.com/questions/27598976/matplotlib-unknown-property-headwidth-and-head-width/27611041
    arrow_spec =  dict(arrowstyle='->, head_width=0.2',
        color=arrow_c,
        connectionstyle='arc3')
        
    ax.annotate("", xy=(x0+dx,y0+dy), xycoords='data',
                    xytext=(x0,y0), textcoords='data',
                    arrowprops=arrow_spec,
                        zorder=100
                    )
    

def draw_coreachability_by_source(df, axs, node_position, add_titles=True):
    pos_edge_style = net.straight_edge_style('peachpuff')
    pos_edge_style.update({'width':10})
    neg_edge_style = net.straight_edge_style('lightblue')
    neg_edge_style.update({'width':2})
    neut_edge_style = net.straight_edge_style('lightgrey')
    neut_edge_style.update({'width':5})

    #TODO: scale these by IDSNR weighted co-reachability
    n = len(df['iA'].unique())
    for i in range(n):
        pos_edges, neut_edges, neg_edges = get_coreachability_from_source(df,i)
        
        net.draw_np_adj(neut_edges, axs[i], neut_edge_style)
        net.draw_np_adj(pos_edges, axs[i], pos_edge_style)
        net.draw_np_adj(neg_edges, axs[i], neg_edge_style)
        indicate_intervention(i, node_position, axs[i])
        # print(node_position)
        if add_titles:
            axs[i].set_title(f'effect of $S_{i}$')
            
def draw_adj_reach_corr_coreach(A, df=None, axs=None, add_titles=True):    
    n = A.shape[0]
    n_plot = 3+n;  
    if df is None:
        df = compute_coreachability_tensor(net.reachability(A))

    if axs is None:
        fig, axs =  plt.subplots(1,n_plot, figsize=((n_plot)*5, 2*2.5),sharey=True,aspect='equal')
        print('INFO: creating axes')
    else:
        fig = axs[0].get_figure()

    graph_pos = net.draw_adj_reach_corr(A, axs[0:3], add_titles, grey_correlations=True)
    draw_coreachability_by_source(df, axs[3:], graph_pos, add_titles)
    return fig


#%%

if __name__ == '__main__':
    # TEST script for categorizing whether sources increase or 
    # decrease correlation between two nodes
    import matplotlib.pyplot as plt
    import pandas as pd
    plt.rcParams.update({'font.size': 25})
    import example_circuits as egcirc

    # Construct a network with networkx
    # G = nx.DiGraph({'U':['V'],'V':['zA','zB'],'zZ':['zB'],'zA':['zB']})
    # G = nx.DiGraph({'A':['B'],'B':['A','C']})
    # G = nx.DiGraph({'A':['B','C']})
    G = nx.DiGraph({'A':['B'],'B':['A'],'C':['A']})

    '''mermaid vis from networkx
    https://blog.mdb977.de/rendering-networkx-graphs-or-graphml-files-via-mermaid/
    https://github.com/mermaid-js/mermaid/issues/1791'''
    # nx.draw(G, with_labels=True)
    
    # View the adjacency and reachability matrices
    A = nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()
    print(A)
    R = net.reachability(A).astype(int)
    print(R)
    
    def _idx_to_node_size(i,iA,jB):
        if (i==iA):
            return 800
        if (i==jB):
            return 800
        else:
            return 300
    # label_colors = {'S+':'lightgreen','S-':'lightcoral','S0':'lightgrey'}
    label_colors = {'S+':'peachpuff','S-':'lightblue','S0':'lightgrey'}

    # # Examine co-reachability for a single source-target pair
    # iA = 0
    # jB = 1
    # 
    # S = partition_sources_ab(R,iA,jB)
    # print(S)
    # print(validate_sources(S))
    # S_labels = condense_source_type_labels(S)
    # node_opts = {'node_color':[label_colors[s] for s in S_labels]}
    # node_sizes = {'node_size':[_idx_to_node_size(i) for i in range(len(S_labels))]}
    # node_opts.update(node_sizes)
    # 
    # fig,ax = plt.subplots(2,1,figsize=(4,8))
    # ax
    # 
    # net.draw_np_adj(A, ax[0], more_options=node_opts)
    # net.draw_np_adj(R, ax[1], more_options=node_opts)
    # 
    # ax[0].set_title('big nodes are source, target\n green nodes are S+\nred nodes are S-')
    # ax[0].set_ylabel('adjacency')
    # ax[1].set_ylabel('reachability')
    # fig
    # print(S_labels)

    #%%
    n = A.shape[0];
    
    df = compute_coreachability_tensor(R)
    df['node_color'] = df.apply(lambda row: label_colors[row['type']],axis=1)
    df['node_size'] = df.apply(lambda row: _idx_to_node_size(row['kS'],row['iA'],row['jB']),axis=1)

    #%%
    
    fig, ax = plt.subplots(1,3,figsize=(12,4))
    net.draw_adj_reach_corr(A, ax)
    fig
    #%%
    # print(A)
         
    # As = egcirc.get_all_2node()
    As = egcirc.get_chainlike_3node()

    ncirc = len(As)                    
    npanels = 3    
    fig,ax = plt.subplots(ncirc,npanels,figsize=(10,4*ncirc), sharey=True)
    for i,_A in enumerate(As):
        net.draw_adj_reach_corr(_A,ax[i,:3],add_titles=(i==0))
    myplot.super_ylabel(fig,'hypothesized circuits',30)
    
    #%%
    # #PLOT coreachability sensor by AxB...S embedded in node color
    # fig,ax = plt.subplots(n,n,figsize=(n*2.5,n*2.5))
    # 
    # #manage axes
    # myplot.label_and_clear_axes_grid(ax)
    # 
    # for i in range(n):
    #     for j in range(i,n):
    #         df_rows = df[ (df['iA']==i) & (df['jB']==j)]
    #         node_opts = {'node_color':[c for c in df_rows['node_color']]}
    #         node_sizes = {'node_size':[s for s in df_rows['node_size']]}
    #         # print(node_opts)
    #         # print(node_sizes)
    #         node_opts.update(node_sizes)
    #         node_opts.update({'edge_color':'lightgrey'})
    #         net.draw_np_adj(A, ax[i][j], more_options=node_opts)
    #         # highlight queried edge
    #         edge_A = 0*A;
    #         edge_A[i,j]=1
    #         node_opts.update({'edge_color':'black','style':':','arrowstyle':'-'})
    #         net.draw_np_adj(edge_A, ax[i][j], more_options=node_opts)
    # 
    # [myplot.expand_bounds(__ax) for _ax in ax for __ax in _ax ]
    # fig.suptitle('To node j\n(target)',fontsize=20)
    # myplot.super_ylabel(fig, 'From node i\n(source)',fontsize=20)
    # fig

    #%%
    '''
    plot co-reachability tensor as a function of source location
    '''
    # df['node_color'] = df.apply(lambda row: label_colors[row['type']],axis=1)
    # df['node_size'] = df.apply(lambda row: _idx_to_node_size(row['kS'],row['iA'],row['jB']),axis=1)
    
    n = As[0].shape[0]
    n_plot = 3+n
    # ncirc = 3
    fig, axs =  plt.subplots(ncirc, n_plot, figsize=((n_plot)*5, ncirc*5),sharey=True)
    
    for i,_A in enumerate(As):
        draw_adj_reach_corr_coreach(_A, axs=axs[i,:], add_titles=(i==0))
    
    fig.text((2+ncirc/2)/(ncirc+2),.92,'Interventions',size=35,va='center',ha='center')
    myplot.super_ylabel(fig,'Hypothesized Circuits',35)
    # plt.savefig('hypo_x_intv_2node_openloop.png',dpi=100,facecolor='w')
    # fig
    
    #%%
    

    # fig

            
        

