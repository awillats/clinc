# reachability of adjacency matrix ...
import numpy as np 
import networkx as nx 
import scipy.linalg as splinalg

import matplotlib.pyplot as plt
import plotting_functions as myplot
DYNAMIC = 0
# %load_ext autoreload
# %autoreload 2
#%%

#%%
def correlation_from_reachability(i,j, Rw , s, verbose=False):
    '''
    i -- index of first node
    j -- index of second node
    Rw -- weighted reachability matrix, also denoted with W~  
        - uses indexing convention Rw(from, to) 
    s -- vector of source variances
    
    reminder, python operations on numpy vectors/matrices are elementwise by default
    correlation should be symmetric with respect to i,j (but not Rw, s)
    '''
    Ri = Rw[:,i]
    Rj = Rw[:,j]
    # clip negative values of s
    s = np.array(s)
    eps = 1e-15
    

    if verbose and any(s<eps):
        print('WARNING: regularizing s')
    s[s<eps] = eps
    
    if any(np.less(s,0)):
        raise ValueError('ERROR: s cannot be negative, it represents a variance')
    
    return sum(Ri*Rj*s) / np.sqrt(sum(Ri**2 * s) * sum(Rj**2 * s))




#%%
'''
MOVE THIS INTO IF NAME MAIN
'''

#%%
#%%  

def reachability_weight( adj ):
    # intended to capture the total scaling a unit input at node i 
    # experiences by the time it ends up at node j
    n = adj.shape[0]
    reach = 0.0*adj;
    curr = np.eye(adj.shape[0]);

    '''
    NOTE!!
    - [ ] this needs to be replaced with the matrix exponential to handle reciprocally connected circuits
    '''
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
def indirect( adj ):
    return reachability(adj)-adj #could be xor?


def undirect( adj ):
    return np.logical_or( adj.T, adj)
    
def correlations( adj ):
    '''
    [UNTESTED], binary
    fork reachabile OR direct reachable
    '''    
    return undirect( np.logical_or(fork_reachability(adj), reachability(adj)) )
    
def illusory_correlations( adj , corr=None):
    if corr is None:
        corr = correlations(adj)
    return corr.astype(int)-undirect(adj) #could be xor?

#TODO: partial correlations
'''
def partial_correlations( adj, i_condition ):
    return adj
''' 
#%%  network plotting  
def draw_np_adj(adj, ax=None, more_options={}):
    nx_adj = nx.from_numpy_matrix(adj, create_using=nx.DiGraph) 
    pos = nx.circular_layout(nx_adj)
    
    options = {
        'node_color': 'lightgrey',
        'node_size': 1000,
        'width': 5,
        'arrowstyle': '-|>',
        'arrowsize':25,
        'ax':ax,
        'pos':pos,
        'connectionstyle':"arc3,rad=0.1"
    }
    
    myplot.unbox(ax)
    # myplot.expand_bounds(ax)
    options.update(more_options)
    nx.draw_networkx(nx_adj, arrows=True, **options)
    return pos
def straight_edge_style(color):
    return {'edge_color':color,'connectionstyle':'arc3,rad=0','arrowstyle':'-'}
    
def draw_reachability(A,R=None,ax=None):
    if R is None:
        R = reachability(A)
    draw_np_adj(R, ax=ax, more_options={'edge_color':'lightgrey'})
    draw_np_adj(A, ax=ax)
    
def draw_correlations(A,Corr=None,ax=None,grey_correlations=False):
    if Corr is None:
        Corr = correlations(A)
    #NOTE: does it make sense to have "yellow" correlations which are in the reachability but NOT the adj 
    # then "red" correlations which aren't in the reachability ?
    
    good_corr_style = straight_edge_style('lightgreen') if not grey_correlations else straight_edge_style('lightgrey')
    bad_corr_style = straight_edge_style('lightcoral') if not grey_correlations else straight_edge_style('lightgrey')
    
    draw_np_adj(Corr, ax=ax, more_options=good_corr_style)
    draw_np_adj(illusory_correlations(A,Corr), ax=ax, more_options=bad_corr_style)

def draw_adj_reach_corr(A,axs,add_titles=True,grey_correlations=False):
    pos = draw_np_adj(A, ax=axs[0])
    draw_reachability(A, None, axs[1])
    draw_correlations(A, None, axs[2], grey_correlations=grey_correlations)
    if add_titles:
        axs[0].set_title('adj')
        axs[1].set_title('reach')
        axs[2].set_title('correlations')
    return pos
#%%

if __name__ == "__main__":
    A = np.array([[1,0,1],
                  [0,1,1],
                  [0,0,1]])
    
    rA = reachability(A);
    rwA = reachability_weight(A);
    corrA = correlations(A)
    
    fig, ax = plt.subplots(1,3,figsize=(12,4))
    
    draw_adj_reach_corr(A, ax)
    
    fig
    