import re
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt

def mermaid_str_to_networkx(merm_graph, verbose=False):
    '''
    Parses mermaid-js strings into networkx diagrams 
    NOTE: currently only handles simple one-way arrow (-->) syntax 
    
    TODO:
    - parse node style, edge labels
    - take LR / TD to inform networkx layout
    - parse additional arrows 
    '''
    node_labels = {}
    G = nx.DiGraph()
    for L in merm_graph.splitlines():
        # source → target
        if '-->' in L:
            src,targ = L.split('-->')
            # parse ( or [ which usually denotes style and label of node
            if '(' in targ or '[' in targ:
                split_res = re.split('([\(\[])',targ,maxsplit=1)

                targ = split_res[0].strip()
                targ_label = ''.join(split_res[1:]).strip()
            else:
                targ_label = targ
                
            G.add_edge(src.strip(),targ.strip())
            node_labels[targ] = targ_label
            if verbose: print(f'{src} → {targ}')
    return G
    
def nx_to_np_adj(G,min_nodes=None):
    '''
    Converts a NetworkX graph to a dense adjacency matrix (via numpy)
    '''
    
    if min_nodes is not None:
        nodelist = np.arange(min_nodes)
    else:
        nodelist = sorted(G.nodes())
    adj =  nx.adjacency_matrix(G, nodelist=nodelist).todense()
    n = adj.shape[0]
    return adj
    
#%%

if __name__ == "__main__":
    mg='''mermaid
    graph LR
      S1-->A((A))
      A-->m( )
      m-->B((B))
      click A callback "Tooltip"
      linkStyle 0 stroke:#0f0
      linkStyle 3 stroke:#f00
    '''
    G = mermaid_str_to_networkx(mg)
    print(G.edges)
    gs = str(G.edges)
    print(nx.to_pandas_edgelist(G))
    
    
    #%% 
    nx.draw_networkx(G)
    #%%
    