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
def add_self_reach(R):
    return np.logical_or(R, np.eye(R.shape[0])) 
def _coreach_logic_from_src(R,i,j,s,logic_fn):
    R = add_self_reach(R)
    #NOTE: adjacency convention dependent
    return logic_fn(R[s,i],R[s,j])
def and_coreach_from_src(R,i,j,s):
    return _coreach_logic_from_src(R,i,j,s,np.logical_and)
def xor_coreach_from_src(R,i,j,s):
    return _coreach_logic_from_src(R,i,j,s,np.logical_xor)
def nor_coreach_from_src(R,i,j,s):
    return _coreach_logic_from_src(R,i,j,s, lambda a,b : np.logical_not(np.logical_or(a,b)))

incr_ij_from_src = and_coreach_from_src
decr_ij_from_src = xor_coreach_from_src
indp_ij_from_src = nor_coreach_from_src

def label_coreach_from_src(R,i,j,s):
    if and_coreach_from_src(R,i,j,s): return 'S^' 
    if xor_coreach_from_src(R,i,j,s): return 'Sv' 
    if nor_coreach_from_src(R,i,j,s): return 'S='
    else:
        return None

def compute_coreachability_from_src(R, src_loc, ignore_self_connections=True, to_multiindex=False):
    n = R.shape[0]
    df = pd.DataFrame(columns=['iA','jB','kS','type'])
    
    j_offset = 1 if ignore_self_connections else 0
    
    for i in range(n):
        for j in range(i+j_offset, n):
            # _s_labels = partition_and_label_sources(R,i,j)
            this_label = label_coreach_from_src(R,i,j,src_loc)
            # for k in range(n):
            df = df.append({'iA':i,'jB':j,'kS':src_loc,'type':this_label},ignore_index=True)
    if to_multiindex:
        df = add_multiindex_to_coreach(df)
    return df
                  
#%%
# set up functions for computing whether a source can reach both A and B
# this section slices across all sources
#NOTE: adjacency convention dependent
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
    R = add_self_reach(R)
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

def add_multiindex_to_coreach(df):
    return df.set_index(['kS','iA','jB']).sort_values(['kS','iA','jB'])
    
def compute_coreachability_tensor(R, ignore_self_connections=True, to_multiindex=False):
    n = R.shape[0] 
    df = pd.DataFrame()
    for k in range(1,n):
        df = df.append(compute_coreachability_from_src(R,k, ignore_self_connections=ignore_self_connections, to_multiindex=to_multiindex))
        
    '''
    df = pd.DataFrame(columns=['iA','jB','kS','type'])
    
    j_offset = 1 if ignore_self_connections else 0
    
    for i in range(n):
        for j in range(i+j_offset, n):
            _s_labels = partition_and_label_sources(R,i,j)
            for k in range(n):
                df = df.append({'iA':i,'jB':j,'kS':k,'type':_s_labels[k]},ignore_index=True)
    
    #set up multi-index        
    if to_multiindex:
        df = add_multiindex_to_coreach(df)
    '''
    return df
#%%
# Data parsing functions
def df_edgelist_to_numpy_adj(df, source_key, target_key, node_list):
    return nx.to_numpy_matrix(nx.from_pandas_edgelist(df, source_key, target_key, create_using=nx.DiGraph), nodelist=node_list)

def get_node_names_from_coreach(df):
    return list(set(df['iA'].unique()) | set(df['jB'].unique()))

def get_coreachability_from_source(df, kS):
    df_rows = df[df['kS']==kS]
    # df_rows = df.xs(kS,level='kS')
    df_pos  = df_rows[df_rows['type']=='S+']
    df_neg  = df_rows[df_rows['type']=='S-']
    df_neut = df_rows[df_rows['type']=='S0']
    
    nodes = get_node_names_from_coreach(df_rows)
    
    # nodes = df.index.unique(level='iA')
    pos_edges = df_edgelist_to_numpy_adj(df_pos,  'iA','jB',nodes)
    neg_edges = df_edgelist_to_numpy_adj(df_neg,  'iA','jB',nodes)
    neut_edges = df_edgelist_to_numpy_adj(df_neut,'iA','jB',nodes)

    return pos_edges, neut_edges, neg_edges

    
#%%
def reconstruct_reach_from_coreach_df(df):
    '''
    Reconstructs a circuit's reachability from its "CoReachability tensor"
        ...that is a map of which correlations between pairs of nodes increased or decreased 
        as a result of open-loop stimulation at each node 
    if corr(A,B | OL@A) > corr(A,B), A→→B
    
    NOTE: think this assumes all excitatory weights
    NOTE: Expects df to have kS,iA,jB as mutliindex
    '''
    
    'Only care about connections adjacent to the source node'
    c1 = df.index.get_level_values('kS')==df.index.get_level_values('iA')
    c2 = df.index.get_level_values('kS')==df.index.get_level_values('jB')
    dft_local = df.loc[np.logical_or(c1,c2)]
    
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
    return ReR

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
    
        

