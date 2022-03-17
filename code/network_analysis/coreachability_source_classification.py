import numpy as np
import networkx as nx
import network_analysis_functions as net
import network_data_functions as netdata
import network_plotting_functions as netplot
import plotting_functions as myplot
import pandas as pd

'''
the if __name__ == '__main__' is far too complicated 
- separate this into a minimal example included here 
- and a comprehensive script elsewhere
'''



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
# Data parsing functions
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

    
#%%



#%%

if __name__ == '__main__':
    # %load_ext autoreload
    # %autoreload 2
    # TEST script for categorizing whether sources increase or 
    # decrease correlation between two nodes
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 25})
    import example_circuits as egcirc

    # Construct a network with networkx
    # G = nx.DiGraph({'U':['V'],'V':['zA','zB'],'zZ':['zB'],'zA':['zB']})
    # G = nx.DiGraph({'A':['B'],'B':['A','C']})
    # G = nx.DiGraph({'A':['B','C']})
    G = nx.DiGraph({'A':['B','E'],'B':['C','D'],'C':['B']})
    # G = nx.DiGraph({'A':['B'],'B':['A'],'C':['A','B']})

    '''mermaid vis from networkx
    https://blog.mdb977.de/rendering-networkx-graphs-or-graphml-files-via-mermaid/
    https://github.com/mermaid-js/mermaid/issues/1791'''
    # nx.draw(G, with_labels=True)
    
    # View the adjacency and reachability matrices
    A = netdata.nx_to_np_adj(G)
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


    #%%
    n = A.shape[0];
    df = compute_coreachability_tensor(R)
    df['node_color'] = df.apply(lambda row: label_colors[row['type']],axis=1)
    df['node_size'] = df.apply(lambda row: _idx_to_node_size(row['kS'],row['iA'],row['jB']),axis=1)
    df.to_csv('results/demo_fingerprint.csv')
    
    demo_adj_file = open('results/demo_adj.txt','w')
    demo_adj_file.write(str(G.edges))
    demo_adj_file.close()
    
    
    #%%
    
    fig, ax = plt.subplots(1,3,figsize=(12,4))
    netplot.draw_adj_reach_corr(A, ax)
    fig
    #%%
    # print(A)
         
    # As = egcirc.get_all_2node()
    As = egcirc.get_chainlike_3node()

    ncirc = len(As)                    
    npanels = 3    
    fig,ax = plt.subplots(ncirc,npanels,figsize=(10,4*ncirc), sharey=True)
    for i,_A in enumerate(As):
        netplot.draw_adj_reach_corr(_A,ax[i,:3],add_titles=(i==0))
    myplot.super_ylabel(fig,'hypothesized circuits',30)
    fig
    
        

