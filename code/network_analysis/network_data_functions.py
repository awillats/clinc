import re
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt
import network_plotting_functions as netplot



import enum
import re 
def flatten_list(L):
    return list(np.concatenate(L).flat)
    
def split_each(A,delim):
    return flatten_list([a.split(delim) for a in A])
    
def split_by_any(A,delims, keep_delim=False):
    matches = [A]
    for d in delims:
        if keep_delim:
            # https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators
            matches = [re.split(f'([!{d}])',part) for part in matches]
        else:
            matches = [part.split(d) for part in matches]
        matches = [m.strip() for m in flatten_list(matches)]
    return matches
    
    
def arrow_str_to_networkx(arrow_graph, line_delim='\n',node_delim = ','):
    '''
    Takes a string like A→B→C↔D and converts it to a directed graph
    can connect multiple nodes to multiple nodes:
        A→B,C == A→B, A→C
    can connect right to left 
        A←B == B→A
    can be specified over multiple lines
        A→B,C 
        C↔D
    '''
    right_arrow = '→'
    left_arrow = '←'
    bi_arrow = '↔'
    all_arrows = [right_arrow, left_arrow, bi_arrow]
    
    # line_delim = '\n'
    # https://github.com/awillats/circuit-visualizer-p5/blob/main/sketch.js → parseTextToAdj
    
    G = nx.DiGraph()
    
    class direction(enum.Flag):
        LEFT = enum.auto()
        RIGHT = enum.auto()
        NEITHER = LEFT & RIGHT
        BIDIR = LEFT | RIGHT
    
    def _connect(G,left_node_str, right_node_str, dir=direction.RIGHT,node_delim=node_delim):
        from_nodes = []
        to_nodes = []
        left_nodes = _split_and_strip_nodes(left_node_str,node_delim)
        right_nodes = _split_and_strip_nodes(right_node_str,node_delim)
        
        if dir & direction.LEFT:
            from_nodes.extend(right_nodes)
            to_nodes.extend(left_nodes)
        if dir & direction.RIGHT:
            from_nodes.extend(left_nodes)
            to_nodes.extend(right_nodes)
        
        for L in left_nodes:
            for R in right_nodes:
                if dir & direction.LEFT:
                    G.add_edge(R,L)
                if dir & direction.RIGHT:
                    G.add_edge(L,R)
    def _delim_and_dir_from_str(L):
        this_arrow = '𐂂'
        dir = direction.NEITHER
        
        if left_arrow in L:
            this_arrow = left_arrow
            dir = direction.LEFT
        if right_arrow in L:
            this_arrow = right_arrow
            dir = direction.RIGHT
        if bi_arrow in L:
            this_arrow = bi_arrow 
            dir = direction.BIDIR
        return (this_arrow, dir)
    def _split_and_strip_nodes(node_str,node_delim=node_delim):
        node_names = node_str.split(node_delim)
        node_names = [n.strip() for n in node_names]
        return node_names
        
    for L in arrow_graph.split(line_delim):
        '''
        each line can ONLY contain one type of arrow
        '''
        
        this_arrow, dir = _delim_and_dir_from_str(L)
        pieces = split_by_any(L, all_arrows)
        
        if len(pieces)<2:
            #skip, probably no connection
            continue
            
        elif len(pieces)>2:
            # connect up a chain 
            pieces_and_arrows = split_by_any(L, all_arrows, keep_delim=True)
            for i, arw in enumerate(pieces_and_arrows[1::2]):
                _,dir = _delim_and_dir_from_str(arw)
                left_node_str = pieces_and_arrows[2*i]
                right_node_str = pieces_and_arrows[2*i+2]
                _connect(G, left_node_str, right_node_str, dir)
                
        else:
            _connect(G, pieces[0], pieces[1], dir)

    return G
            
    
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
    # gs = str(G.edges)
    # print(nx.to_pandas_edgelist(G))

    #%% 
    netplot.draw_nx(G)
    #%%
    
    arrg = 'A→B→C←D ; E↔A'
    AG = arrow_str_to_networkx(arrg,line_delim=';')
    #%%
    fig,ax=plt.subplots(figsize=(8,8))
    netplot.draw_nx(AG,ax);
    fig
    #%%
    print(AG.edges())
    