# reachability of adjacency matrix ...
import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt
import plotting_functions as myplot
DYNAMIC = 0
# %load_ext autoreload
# %autoreload 2
#%%
def reachability_weight( adj ):
    # intended to capture the total scaling a unit input at node i 
    # experiences by the time it ends up at node j
    n = adj.shape[0]
    reach = 0.0*adj;
    curr = np.eye(adj.shape[0]);

    for i in range(n):
        curr = np.matmul(adj, curr)
        reach += curr
    return reach

def net_reach_per_node( adj ):
    '''
    useful in computing the steady state impact of connectivity
    '''
    return np.sum(reachability_weight(adj),axis=0)
    
def reachability( adj ):
    '''
    - convert to networkx
    - calculate reachability
    - convert back to numpy
    '''
    nx_dag = nx.from_numpy_matrix(adj, create_using=nx.DiGraph) 
    nx_reach = nx.dag.transitive_closure( nx_dag )
    reach = nx.to_numpy_array( nx_reach )
    return reach
    
def fork_reachability( adj ):
    '''
    [UNTESTED]
    '''
    return np.matmul( reachability(adj.T), reachability(adj) )
def undirect( adj ):
    return np.logical_or( adj.T, adj)
def correlations( adj ):
    '''
    [UNTESTED], binary
    fork reachabile OR direct reachable
    '''    
    return undirect( np.logical_or(fork_reachability(adj), reachability(adj)) )
    
def indirect( adj ):
    return reachability(adj)-adj

def illusory_correlations( adj ):
    return correlations(adj).astype(int)-undirect(adj)
    
def draw_np_adj(adj, ax=None, more_options={}):
    nx_adj = nx.from_numpy_matrix(adj, create_using=nx.DiGraph) 
    pos = nx.circular_layout(nx_adj)
    
    options = {
        'node_color': 'lightgrey',
        'node_size': 1000,
        'width': 2,
        'arrowstyle': '-|>',
        'ax':ax,
        'pos':pos,
        'connectionstyle':"arc3,rad=0.1"
    }
    
    myplot.unbox(ax)
    # myplot.expand_bounds(ax)
    # print(pos)
    options.update(more_options)
    nx.draw_networkx(nx_adj, arrows=True, **options)
    return pos

#%%

if __name__ == "__main__":
    A = np.array([[0,1,0],
                  [1,0,1],
                  [0,0,0]])
    
    rA = reachability(A);
    rwA = reachability_weight(A);
    frA = illusory_correlations(A)
    
    fig,ax = plt.subplots(1,3,figsize=(12,4))
    
    
    draw_np_adj(A, ax=ax[0])
    
    # 'draw reachability light grey under'
    draw_np_adj(rA, ax=ax[1])
    
    # 'draw illusory red, no curvature over'
    draw_np_adj(frA, ax=ax[2])
    ax[0].set_title('adj')
    ax[1].set_title('reach')
    ax[2].set_title('corr - adj')
    # [myplot.expand_bounds(_ax,2) for _ax in ax]# doesn't work?
    print(rwA)
    fig
    