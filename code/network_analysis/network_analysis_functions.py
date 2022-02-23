# reachability of adjacency matrix ...
import numpy as np 
import networkx as nx 
import scipy.linalg as linalg

import matplotlib.pyplot as plt
import plotting_functions as myplot
DYNAMIC = 0
# %load_ext autoreload
# %autoreload 2
#%%

def sever_inputs(adj, ctrl_loc):
    '''
    could imagine an "imperfect" control which scales down inputs by a factor 
    instead of setting them to zero
    '''
    new_adj = adj.copy()
    new_adj[:,ctrl_loc] = 0
    return new_adj
    
def closed_loop_binary_reachability(adj, ctrl_loc):
    return reachability(sever_inputs(adj, ctrl_loc))
    
def closed_loop_weighted_reachability(adj, ctrl_loc):
    return reachability_weight(sever_inputs(adj, ctrl_loc))
    
def closed_loop_binary_reachability(adj, ctrl_loc, is_binary=True):
    reach_fn = reachability if is_binary else reachability_weight
    return reach_fn(sever_inputs(adj, ctrl_loc))

    
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
'''
Quantitative properties of correlations
'''
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
    # clip negative values of s - useful to error-proof this function...
    # ... against numerical gradient calculation
    s = np.array(s)
    eps = 1e-15    
    if verbose and any(s<eps):
        print('WARNING: regularizing s')
    s[s<eps] = eps
    
    if any(np.less(s,0)):
        raise ValueError('ERROR: s cannot be negative, it represents a variance')
    
    return sum(Ri*Rj*s) / np.sqrt(sum(Ri**2 * s) * sum(Rj**2 * s))

#%%  
# Network plotting  
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
        Corr = binary_correlations(A)
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
    def draw_ctrl(ax, pos_i):
        ax.plot(pos_i[0],pos_i[1],'o',color='darkorange',markersize=30,markeredgewidth=4,fillstyle='none')
        
    fig, ax = plt.subplots(2,6,figsize=(18,7))
    
    pos = draw_adj_reach_corr(A, ax[1,:3],grey_correlations=True)
    for _ax in ax:
        for __ax in _ax:
            myplot.unbox(__ax, clear_labels=True)
    for i in range(3):
        plot_i = i+3
        _ax0 = ax[0,plot_i]
        _ax1 = ax[1,plot_i]
        
        adj_ctrl_i = sever_inputs(A,i)
        reach_ctrl_i = closed_loop_binary_reachability(A,i)
        corr_ctrl_i = binary_correlations(adj_ctrl_i)
        
        draw_np_adj(A, ax=_ax0, more_options={'edge_color':'moccasin','style':':'})
        draw_np_adj(adj_ctrl_i, ax=_ax0)
        _ax0.set_title(f'ctrl @ {i}')
        draw_correlations(adj_ctrl_i,Corr=corr_ctrl_i,ax=_ax1,grey_correlations=True)
        draw_ctrl(_ax0, pos[i])
        draw_ctrl(_ax1, pos[i])
    ax[0,3].set_ylabel('ctrl adj')
    ax[1,3].set_ylabel('ctrl corr')

    for _ax in ax:
        for __ax in _ax:
            myplot.expand_bounds(__ax)
    plt.savefig('effect_of_control_horiz.png',dpi=100,facecolor='w')


    
    
    #%%
    fig, ax = plt.subplots(4,3,figsize=(11,17))
    
    draw_adj_reach_corr(A, ax[0,:],grey_correlations=True)
    for i in range(3):
        plot_i = i+1
        # draw_correlations(A, None, ax[i,0], grey_corre)
        draw_np_adj(A, ax=ax[plot_i,0], more_options={'edge_color':'moccasin','style':':'})
        draw_np_adj(reachability(A), ax=ax[plot_i,1], more_options={'edge_color':'moccasin','style':':'})


        pos = draw_adj_reach_corr(sever_inputs(A,i), ax[plot_i,:],grey_correlations=True)
        for _ax in ax[plot_i,:]:
            _ax.plot(pos[i][0],pos[i][1],'o',color='darkorange',markersize=30,markeredgewidth=4,fillstyle='none')
        ax[plot_i,0].set_ylabel(f'Ctrl @ {i}')
        # c = plt.Circle((pos[i][0],pos[i][1]),.2,color='r',)
        # ax[i,0].add_patch(c)
        # print(pos[i])
    # plt.savefig('effect_of_control.png',dpi=100,facecolor='w')
    