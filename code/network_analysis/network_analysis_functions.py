# reachability of adjacency matrix ...
import numpy as np 
import networkx as nx 
import scipy.linalg as linalg

import network_data_functions as netdata
import matplotlib.pyplot as plt
import plotting_functions as myplot
DYNAMIC = 0
# %load_ext autoreload
# %autoreload 2
'''
TODO: unify naming convention:
    - control v.s. closed-loop control etc.
    - A v.s. adj
TODO: some function(s) add the diagonal into the adjacency matrix 
    - this is likely a clunky result of not deciding whether a node is "adjacent to" itself
'''

#%%
def multi_lerp(p, N):
    return 1-(1-p)**N
def inv_multi_lerp(P,N):
    return 1-(1-P)**(1/N)
    
def __sever_inputs(adj, CTRL):
    '''
    [UNTESTED]
    partially sever inputs
    '''
    new_adj = adj.copy().astype('float')
    if CTRL is not None and CTRL['location'] is not None:
        new_adj[:,CTRL['location']] *= (1.0-CTRL['effectiveness'])          
    return new_adj
    
    
# control-related functions
def sever_inputs(adj, ctrl_loc, verbose=False):
    '''
    could imagine an "imperfect" control which scales down inputs by a factor 
    instead of setting them to zero
    '''
    
    if ctrl_loc is None:
        return adj
    if verbose:
        print(f'adding control at {ctrl_loc}')    
    new_adj = adj.copy()
    new_adj[:,ctrl_loc] = 0
    return new_adj
    
#%%  
#%% markdown
'''
$ \sum_{n=1}^{\infty} A^{n} = (I-A)^{-1}$  

Let $f(A) :  = (I-A)^{-1}$  

$ f(A^T) = f(A)^T$ (assumed, and tested empirically)  

therefore this should work for either indexing convention of W
'''
#%%
inf_sum_mat = lambda M: np.linalg.inv(np.eye(M.shape[0]) - M )
# print(inf_sum(W))
# print(  )
# print(inf_sum(W.T).T)
# print(  ) 
# np.max(np.abs(inf_sum(W.T).T - inf_sum(W)))
#%%
def reachability_weight( adj ):
    # intended to capture the total scaling a unit input at node i 
    # experiences by the time it ends up at node j
    
    
    reach = inf_sum_mat(adj)
    
    # previous sum-based solution:
    # n = adj.shape[0]
    # reach = 0.0*adj;
    # curr = np.eye(adj.shape[0]);
    # for i in range(n):
    #     curr = adj @ curr
    #     reach += curr
    return reach

def reachability_weight_w_ctrl(adj, CTRL):
    '''
    CTRL - dictionary specifying control
    several other functions would benefit from using this
    '''
    if CTRL is None:
        return reachability_weight(adj)
    reach = reachability_weight(sever_inputs(adj,CTRL['location']))
    # reach = reachability_weight(__sever_inputs(adj,CTRL))

    return reach
    
def net_reach_per_node( adj ):
    '''
    useful in computing the steady state impact of connectivity
    '''
    return np.sum(reachability_weight(adj),axis=0)
    
def reachability( adj ):
    '''
    [BINARY?]
    - convert to networkx
    - calculate reachability
    - convert back to numpy
    '''
    nx_dag = nx.from_numpy_matrix(adj, create_using=nx.DiGraph) 
    nx_reach = nx.dag.transitive_closure( nx_dag ) #TODO: is this binary?
    reach = nx.to_numpy_array( nx_reach )
    return reach
    
def fork_reachability( adj ):
    '''
    [UNTESTED]
    '''
    return reachability(adj.T) @ reachability(adj) 
def indirect( adj ):
    return reachability(adj)-adj #could be xor?

def undirect( adj ):
    '''
    [BINARY]
    '''
    return np.logical_or( adj.T, adj)
    
def binary_correlations( adj ):
    '''
    [UNTESTED][BINARY]
    fork reachabile OR direct reachable
    '''    
    return undirect( np.logical_or(fork_reachability(adj), reachability(adj)) )
    
def illusory_correlations( adj , corr=None):
    '''
    [BINARY]
    '''
    if corr is None:
        corr = binary_correlations(adj)
    return corr.astype(int)-undirect(adj) #could be xor?

#TODO: partial correlations
'''
def partial_correlations( adj, i_condition ):
    return adj
''' 

#%%
# def closed_loop_binary_reachability(adj, ctrl_loc):
#     return reachability(sever_inputs(adj, ctrl_loc))
# 
# def closed_loop_weighted_reachability(adj, ctrl_loc):
#     return reachability_weight(sever_inputs(adj, ctrl_loc))
    

def closed_loop_reachability(adj, ctrl_loc, is_binary=True):
    reach_fn = reachability if is_binary else reachability_weight
    return reach_fn(sever_inputs(adj, ctrl_loc))

def closed_loop_correlations(adj, ctrl_loc, is_binary=True):
    corr_fn = binary_correlations if is_binary else 'ERROR'
    return corr_fn(sever_inputs(adj, ctrl_loc))

def each_closed_loop_adj(adj):
    return [sever_inputs(adj,i) for i in range(adj.shape[0])]

# looping functions
def each_closed_loop_reachability(adj, is_binary=True):
    return [closed_loop_reachability(adj, i, is_binary) for i in range(adj.shape[0])]
    
def each_closed_loop_correlations(adj, is_binary=True):
    return [closed_loop_correlations(adj, i, is_binary) for i in range(adj.shape[0])]

def each_closed_loop_intervention(adj, is_binary=True):
    return {'adj':each_closed_loop_adj(adj),
    'corr':each_closed_loop_correlations(adj,is_binary)}

#%%
'''
Quantitative properties of correlations
'''
def correlation_from_reachability(i,j, Rw , S, verbose=False):
    '''
    NEEDS RENAMING, something like _by_source
    i -- index of first node
    j -- index of second node
    Rw -- weighted reachability matrix, also denoted with W~  
        - uses indexing convention Rw(from, to) 
    S -- vector of source variances
    
    reminder, python operations on numpy vectors/matrices are elementwise by default
    correlation should be symmetric with respect to i,j (but not Rw, s)
    '''
    Ri = Rw[:,i]
    Rj = Rw[:,j]
    # clip negative values of s - useful to error-proof this function...
    # ... against numerical gradient calculation
    S = np.array(S)
    eps = 1e-15    
    if verbose and any(S<eps):
        print('WARNING: regularizing s')
    S[S<eps] = eps
    
    if any(np.less(S,0)):
        raise ValueError('ERROR: s cannot be negative, it represents a variance')
    
    return sum(Ri*Rj*S) / np.sqrt(sum(Ri**2 * S) * sum(Rj**2 * S))

def correlation_matrix_from_reachability(Rw, S, verbose=False):
    '''
    computes correlations across all pairs of edges
    -migy
    '''
    N = Rw.shape[0]
    corr_coeffs = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            corr_coeffs[i,j] = correlation_from_reachability(i,j, Rw, S, verbose)
    return corr_coeffs 
    
def correlation_matix_from_adjacency(A, S, verbose=False):
    Rw = reachability_weight(A)
    return correlation_matrix_from_reachability(Rw, S, verbose)
    
def correlation_matrix_from_controlled_adjacency(A,S, ctrl_loc, verbose=False):
    '''
    note, this represents a combination of closed-loop control (via ctrl_loc)
    AND open-loop control (via S)
    AND endogenous noise sources (via S)
    '''
    return correlation_matix_from_adjacency(sever_inputs(A,ctrl_loc), S, verbose)
    
def correlation_matrix_from_each_control(A, S, verbose=False):
    return [correlation_matix_from_adjacency(sever_inputs(A,ctrl_loc),S,verbose)\
                for ctrl_loc in range(A.shape[0])]

# def corrcoeff_from_reachability_controlled(i,j):
#%%  
'''
Predict and quantify correlations
'''
def predict_and_quantify_correlations(Rw, varS, X, verbose=False):
    '''
    Rw - weighted reachability
    varS - vector of source variances
    X - timerseries [samples x nodes]
    '''
    
    corr_pred = correlation_matrix_from_reachability(Rw, varS)
    r2_pred  = corr_pred**2
    corr_empr = np.corrcoef(X, rowvar=False) 
    r2_empr = corr_empr**2 
    max_diff = np.max(np.abs(r2_empr-r2_pred))
    if verbose:
        print(r2_pred,'\n')
        print(r2_empr)
        print(f'\nmax diff = {max_diff:.1e}')
    
    return {'r2_pred':r2_pred,'r2_empr':r2_empr,'r_pred':corr_pred,'r_empr':corr_empr,'max_diff':max_diff}

#%%

    
    


#%%

if __name__ == "__main__":
    import network_plotting_functions as netplot
    A = np.array([[0,.1,0],
                  [1,0,0],
                  [0,4,0]])
    
    rA = reachability(A);
    rwA = reachability_weight(A);
    corrA = binary_correlations(A)
    
    fig, ax = plt.subplots(1,3,figsize=(12,4))
    
    netplot.draw_adj_reach_corr(A, ax)
    
    fig

    #%%    
    fig, ax = plt.subplots(2,6,figsize=(18,7))
    adj_ctrls = each_closed_loop_adj(A) 
    corr_ctrls = each_closed_loop_correlations(A)
    ax = netplot.draw_controlled_adj_correlations(ax, A)
    fig
    # plt.savefig('effect_of_control_horiz.png',dpi=100,facecolor='w')
    
    #%%
    fig, ax = plt.subplots(4,3,figsize=(6,8))
    netplot.draw_controlled_representations(ax, A)
    # plt.savefig('effect_of_control_grid.png',dpi=100,facecolor='w')
    fig