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
#%%

if __name__ == '__main__':
    # TEST script for categorizing whether sources increase or 
    # decrease correlation between two nodes
    import matplotlib.pyplot as plt
    import pandas as pd
    # Construct a network with networkx
    # G = nx.DiGraph({'U':['V'],'V':['zA','zB'],'zZ':['zB'],'zA':['zB']})
    # G = nx.DiGraph({'A':['B'],'B':['A','C']})
    G = nx.DiGraph({'A':['B','C']})


    '''mermaid vis from networkx
    https://blog.mdb977.de/rendering-networkx-graphs-or-graphml-files-via-mermaid/
    https://github.com/mermaid-js/mermaid/issues/1791'''
    # nx.draw(G, with_labels=True)
    
    # View the adjacency and reachability matrices
    A = nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()
    print(A)
    R = net.reachability(A).astype(int)
    print(R)
    
    iA = 0
    jB = 1
    
    S = partition_sources_ab(R,iA,jB)
    print(S)
    print(validate_sources(S))
    S_labels = condense_source_type_labels(S)
    
    def _idx_to_node_size(i,iA=iA,jB=jB):
        if (i==iA):
            return 800
        if (i==jB):
            return 800
        else:
            return 300
    label_colors = {'S+':'lightgreen','S-':'lightcoral','S0':'lightgrey'}
    node_opts = {'node_color':[label_colors[s] for s in S_labels]}
    node_sizes = {'node_size':[_idx_to_node_size(i) for i in range(len(S_labels))]}
    node_opts.update(node_sizes)
    
    fig,ax = plt.subplots(2,1,figsize=(4,8))
    ax
    
    net.draw_np_adj(A, ax[0], more_options=node_opts)
    net.draw_np_adj(R, ax[1], more_options=node_opts)
    
    ax[0].set_title('big nodes are source, target\n green nodes are S+\nred nodes are S-')
    ax[0].set_ylabel('adjacency')
    ax[1].set_ylabel('reachability')
    fig
        
    print(S_labels)

    #%%
    n = A.shape[0];
    
    def compute_coreachability_tensor(R):
        n = R.shape[0]
        df = pd.DataFrame(columns=['iA','jB','kS','type'])
        for i in range(n):
            for j in range(i,n):
                _s_labels = partition_and_label_sources(R,i,j)
                for k in range(n):
                    df = df.append({'iA':i,'jB':j,'kS':k,'type':_s_labels[k]},ignore_index=True)
        return df
        
    df = compute_coreachability_tensor(R)
    df['node_color'] = df.apply(lambda row: label_colors[row['type']],axis=1)
    df['node_size'] = df.apply(lambda row: _idx_to_node_size(row['kS'],row['iA'],row['jB']),axis=1)
    print(R)
    # sub_df = df[ (df['iA']==0) & (df['jB']==1)]
    # print( sub_df )
    #%%
    #TODO: Highlight false connections by taking forkreachability - adjacency
    
    #%%
    fig,ax = plt.subplots(n,n,figsize=(n*2.5,n*2.5))

    #manage axes
    myplot.label_and_clear_axes_grid(ax)
    
    #TODO: highlight true and illusory edges in background of plot!

    for i in range(n):
        for j in range(i,n):
            df_rows = df[ (df['iA']==i) & (df['jB']==j)]
            node_opts = {'node_color':[c for c in df_rows['node_color']]}
            node_sizes = {'node_size':[s for s in df_rows['node_size']]}
            # print(node_opts)
            # print(node_sizes)
            node_opts.update(node_sizes)
            node_opts.update({'edge_color':'lightgrey'})
            net.draw_np_adj(A, ax[i][j], more_options=node_opts)
            # highlight queried edge
            edge_A = 0*A;
            edge_A[i,j]=1
            node_opts.update({'edge_color':'black','style':':','arrowstyle':'-'})
            net.draw_np_adj(edge_A, ax[i][j], more_options=node_opts)
            
    [myplot.expand_bounds(__ax) for _ax in ax for __ax in _ax ]
    fig.suptitle('To node j\n(target)',fontsize=20)
    myplot.super_ylabel(fig, 'From node i\n(source)',fontsize=20)
    fig

        

