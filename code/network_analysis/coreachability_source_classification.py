import numpy as np
import networkx as nx
import network_analysis_functions as net
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

#%%

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    # Construct a network with networkx
    G = nx.DiGraph({'U':['V'],'V':['zA','zB'],'zZ':[]})
    '''mermaid vis from networkx
    https://blog.mdb977.de/rendering-networkx-graphs-or-graphml-files-via-mermaid/
    https://github.com/mermaid-js/mermaid/issues/1791'''
    # nx.draw(G, with_labels=True)
    
    # View the adjacency and reachability matrices
    A = nx.adjacency_matrix(G, nodelist=sorted(G.nodes())).todense()
    print(A)
    R = net.reachability(A).astype(int)
    print(R)
    
    iA = 2
    jB = 3
    def _idx_to_shape(i,iA=iA,jB=jB):
        if (i==iA):
            return 600
        if (i==jB):
            return 600
        else:
            return 300
    
    S = partition_sources_ab(R,iA,jB)
    print(S)
    print(validate_sources(S))
    S_labels = condense_source_type_labels(S)
    label_colors = {'S+':'lightgreen','S-':'lightcoral','S0':'lightgrey'}
    C = {'node_color':[label_colors[s] for s in S_labels]}
    Sh = {'node_size':[_idx_to_shape(i) for i in range(len(S_labels))]}
    C.update(Sh)
    
    fig,ax = plt.subplots(2,1,figsize=(4,8))
    ax
    # net.draw_np_adj(A, ax[0])
    # net.draw_np_adj(R, ax[1])
    
    net.draw_np_adj(A, ax[0], more_options=C)
    net.draw_np_adj(R, ax[1], more_options=C)
    
    ax[0].set_title('big nodes are source, target\n green nodes are S+\nred nodes are S-')
    ax[0].set_ylabel('adjacency')
    ax[1].set_ylabel('reachability')
    fig
    


