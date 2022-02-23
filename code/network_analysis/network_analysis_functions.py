# reachability of adjacency matrix ...
import numpy as np 
import networkx as nx 
import scipy.linalg as linalg

import matplotlib.pyplot as plt
import plotting_functions as myplot
DYNAMIC = 0
# %load_ext autoreload
# %autoreload 2
'''
TODO: unify naming convention:
    - control v.s. closed-loop control etc.
TODO: some function(s) add the diagonal into the adjacency matrix 
    - this is likely a clunky result of not deciding whether a node is "adjacent to" itself
'''
#%%



#%%
# control-related functions
def sever_inputs(adj, ctrl_loc):
    '''
    could imagine an "imperfect" control which scales down inputs by a factor 
    instead of setting them to zero
    '''
    new_adj = adj.copy()
    new_adj[:,ctrl_loc] = 0
    return new_adj
    
#%%  

def reachability_weight( adj ):
    # intended to capture the total scaling a unit input at node i 
    # experiences by the time it ends up at node j
    reach = linalg.expm(adj)
    # previous sum-based solution:
    # n = adj.shape[0]
    # reach = 0.0*adj;
    # curr = np.eye(adj.shape[0]);
    # for i in range(n):
    #     curr = np.matmul(adj, curr)
    #     reach += curr
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
    return np.matmul( reachability(adj.T), reachability(adj) )
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
# Network plotting  
def draw_np_adj(adj, ax=None, more_options={}):
    '''
    core plotting function that renders an adjacency_matrix 
    - gets used is several other higher-level plotting functions
    '''
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
    
def draw_reachability(A,R=None,ax=None, reach_edge_style=None):
    if R is None:
        R = reachability(A)
    if reach_edge_style is None:
        reach_edge_style = {'edge_color':'lightgrey'}
    draw_np_adj(R, ax=ax, more_options=reach_edge_style)
    draw_np_adj(A, ax=ax)
    
def draw_correlations(A,Corr=None,ax=None,grey_correlations=False):
    if Corr is None:
        Corr = binary_correlations(A)
    #NOTE: does it make sense to have "yellow" correlations which are in the reachability but NOT the adj 
    # then "red" correlations which aren't in the reachability ?
    
    good_corr_style = straight_edge_style('lightgreen') if not grey_correlations else straight_edge_style('lightgrey')
    bad_corr_style = straight_edge_style('lightcoral') if not grey_correlations else straight_edge_style('lightgrey')
    
    draw_np_adj(Corr, ax=ax, more_options=good_corr_style)
    draw_np_adj(illusory_correlations(A,Corr), ax=ax, more_options=bad_corr_style)

def draw_adj_reach_corr(A, axs, add_titles=True, grey_correlations=False):
    pos = draw_np_adj(A, ax=axs[0])
    draw_reachability(A, None, axs[1])
    draw_correlations(A, None, axs[2], grey_correlations=grey_correlations)
    if add_titles:
        axs[0].set_title('adj')
        axs[1].set_title('reach')
        axs[2].set_title('correlations')
    return pos

def draw_ctrl(ax, pos_i, color='darkorange'):
    ax.plot(pos_i[0],pos_i[1],'o',color=color,markersize=30,markeredgewidth=4,fillstyle='none')

def draw_controlled_representations(ax, adj, adj_ctrls=None, reach_ctrls=None, corr_ctrls=None):
    '''
    expects ax to be (N+1) x 3 subplot axes
    '''
    reach = reachability(adj)
    
    if adj_ctrls is None or corr_ctrls is None or reach_ctrls is None:
        adj_ctrls = each_closed_loop_adj(adj)
        reach_ctrls = each_closed_loop_reachability(adj) #pass through is_binary?
        corr_ctrls = each_closed_loop_correlations(adj) #pass through is_binary?
    N = len(adj_ctrls)
    ctrl_marker_color = 'darkorange'
    severed_edge_style = {'edge_color':'moccasin','style':':'}
    
    pos = draw_adj_reach_corr(A, ax[0,:],grey_correlations=True)
    # loop across control locations
    for i in range(N):
        plot_i = i+1
        ax_row = ax[plot_i,:]
        draw_np_adj(adj,   ax_row[0], more_options=severed_edge_style)
        draw_np_adj(reach, ax_row[1], more_options=severed_edge_style)

        # across a row, draw adj, reach, corr
        draw_adj_reach_corr(adj_ctrls[i], ax_row, grey_correlations=True)
        ax_row[0].set_ylabel(f'ctrl @ {i}')
        for _ax in ax_row:
            draw_ctrl(_ax, pos[i])
            if i>0:
                _ax.set_title('')

def draw_controlled_correlations(ax, adj, adj_ctrls=None, corr_ctrls=None):
    '''
    expects ax to be 2 x (3+N) subplot axes
    '''
    if adj_ctrls is None or corr_ctrls is None:
        adj_ctrls = each_closed_loop_adj(adj)
        corr_ctrls = each_closed_loop_correlations(adj) #pass through is_binary?
    
    N = len(adj_ctrls)
    ctrl_marker_color = 'darkorange'
    severed_edge_style = {'edge_color':'moccasin','style':':'}

    #draw unmodified circuit in lower left 3 panels
    pos = draw_adj_reach_corr(A, ax[1,:3], grey_correlations=True)
    #clear unused axes
    myplot.unbox_each(ax, clear_labels=True)
    
    for i in range(N):
        plot_i = i+3
        _ax0 = ax[0, plot_i]
        _ax1 = ax[1, plot_i]    
        
        #overlay unmodified & modified adj
        draw_np_adj(adj,          ax=_ax0, more_options=severed_edge_style)
        draw_np_adj(adj_ctrls[i], ax=_ax0)
        _ax0.set_title(f'ctrl @ {i}')
        
        draw_correlations(adj_ctrls[i], Corr=corr_ctrls[i],
            ax=_ax1, grey_correlations=True)
        
        #add node indicators of location of control    
        draw_ctrl(_ax0, pos[i])
        draw_ctrl(_ax1, pos[i])
        
    ax[0,3].set_ylabel('ctrl adj')
    ax[1,3].set_ylabel('ctrl corr')

    myplot.expand_bounds_each(ax)
    
    return ax
    
    


#%%

if __name__ == "__main__":
    A = np.array([[1,2,0],
                  [1,1,0],
                  [0,4,1]])
    
    rA = reachability(A);
    rwA = reachability_weight(A);
    corrA = binary_correlations(A)
    
    fig, ax = plt.subplots(1,3,figsize=(12,4))
    
    draw_adj_reach_corr(A, ax)
    
    fig

    #%%    
    fig, ax = plt.subplots(2,6,figsize=(18,7))
    adj_ctrls = each_closed_loop_adj(A) 
    corr_ctrls = each_closed_loop_correlations(A)
    ax = draw_controlled_correlations(ax, A)
    fig
    # plt.savefig('effect_of_control_horiz.png',dpi=100,facecolor='w')


    
    #%%
    fig, ax = plt.subplots(4,3,figsize=(11,17))
    draw_controlled_representations(ax, A)
    # plt.savefig('effect_of_control_grid.png',dpi=100,facecolor='w')
    