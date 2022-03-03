import numpy as np 
import networkx as nx 
# import scipy.linalg as linalg
import coreachability_source_classification as coreach
import network_analysis_functions as net
import network_data_functions as netdata

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import plotting_functions as myplot
#%%
DEFAULT_NET_PLOT_OPTIONS = {
        'node_color': 'lightgrey',
        'node_size': 1000, #1000
        'width': 5,
        'arrowstyle': '-|>',
        'arrowsize':25,
        'connectionstyle':"arc3,rad=0.1",
    }
# Network plotting  
def draw_weighted_corr(W, ax=None, min_w=0,max_w=10, more_options={}):
    G = nx.from_numpy_matrix(W, create_using=nx.Graph) 
    weights = np.array(list(nx.get_edge_attributes(G,'weight').values()))
    weights = rescale(weights, min_w,max_w, 0,1)
    
    pos = clockwise_circular_layout(G)
    
    options = DEFAULT_NET_PLOT_OPTIONS.copy()
    options.update({'ax':ax,'pos':pos})
    options.update({'width':weights,'node_size':100})
    nx.draw(G, **options)
    ax.set_aspect('equal')
    # nx.draw_networkx_edge_labels(G, pos=pos)
    myplot.expand_bounds(ax)
    return pos
    
def rescale(x,out_min=0, out_max=1, in_min=None,in_max=None,clip_min=True,clip_max=True):
    if in_min is None:
        in_min = x.min()
    if in_max is None:
        in_max is x.max()
    vals = np.interp(x, (in_min, in_max), (out_min, out_max))
    
    if clip_min:
        vals = np.clip(vals,out_min,None)
    if clip_max:
        vals = np.clip(vals,None,out_max)
    return vals
#%%
def flipper(is_horizontal=True):
    F = np.eye(2,2)
    if is_horizontal:
        F[0,0] = -1
    else:
        F[1,1] = -1
    return F
    
def rotor(angle):
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle) , np.cos(angle)]])
    return R

def rotate_layout(pos,angle=np.pi/3,flip_h=True):
    '''
    TODO: shift center of rotation
    '''
    transform = flipper(flip_h) @ rotor(angle)
    new_pos = {k:np.dot(transform,v) for k,v in pos.items()}
    return new_pos
def clockwise_circular_layout(G):
    pos = nx.circular_layout(G)
    pos = rotate_layout(pos, np.pi/3, True)
    return pos
#%%    
def draw_np_adj(adj, ax=None, more_options={}):
    '''
    core plotting function that renders an adjacency_matrix 
    - gets used is several other higher-level plotting functions
    '''
    
    # DROP non-finite edges (like None, np.NaN etc.)
    adj = adj.copy()
    adj[~np.isfinite(adj)] = 0
    
    nx_adj = nx.from_numpy_matrix(adj, create_using=nx.DiGraph) 
    pos = clockwise_circular_layout(nx_adj)
    
    options = DEFAULT_NET_PLOT_OPTIONS.copy()
    options.update({'ax':ax,'pos':pos})
    options.update(more_options)
    
    nx.draw_networkx(nx_adj, arrows=True, **options)
    
    myplot.unbox(ax)
    # myplot.expand_bounds(ax)
    return pos
#%%
def straight_edge_style(color):
    return {'edge_color':color,'connectionstyle':'arc3,rad=0','arrowstyle':'-'}
    
def indicate_ctrl(ax, pos_i, markersize=30, color='darkorange'):
    # ms of 30 corresponds to a node size of 1000
    ax.plot(pos_i[0],pos_i[1],'o',color=color,markersize=markersize,markeredgewidth=4,fillstyle='none')

def indicate_intervention(ax, pos_i, type='open-loop'):
    '''
    see also indicate_ctrl
    '''
    arrow_mag = 0.4
    arrow_c = 'k'
    # start from "outside" the node
    x0 = pos_i[0]*(1+arrow_mag)
    y0 = pos_i[1]*(1+arrow_mag)
    # point back towards the node
    dx = -pos_i[0]*arrow_mag*.8
    dy = -pos_i[1]*arrow_mag*.8
    
    # https://stackoverflow.com/questions/37819215/matplotlib-arrowheads-and-aspect-ratio
    # https://stackoverflow.com/questions/27598976/matplotlib-unknown-property-headwidth-and-head-width/27611041
    arrow_spec =  dict(arrowstyle='->, head_width=0.2',
        color=arrow_c,
        connectionstyle='arc3')
        
    ax.annotate("", xy=(x0+dx,y0+dy), xycoords='data',
                    xytext=(x0,y0), textcoords='data',
                    arrowprops=arrow_spec,
                        zorder=100
                    )    

# %%    
def draw_reachability(A,R=None,ax=None, reach_edge_style=None):
    if R is None:
        R = net.reachability(A)
    if reach_edge_style is None:
        reach_edge_style = {'edge_color':'lightgrey'}
    draw_np_adj(R, ax=ax, more_options=reach_edge_style)
    draw_np_adj(A, ax=ax)
    
def draw_correlations(A,Corr=None,ax=None,grey_correlations=False):
    if Corr is None:
        Corr = net.binary_correlations(A)
    #NOTE: does it make sense to have "yellow" correlations which are in the reachability but NOT the adj 
    # then "red" correlations which aren't in the reachability ?
    
    good_corr_style = straight_edge_style('lightgreen') if not grey_correlations else straight_edge_style('lightgrey')
    bad_corr_style = straight_edge_style('lightcoral') if not grey_correlations else straight_edge_style('lightgrey')
    
    draw_np_adj(Corr, ax=ax, more_options=good_corr_style)
    pos = draw_np_adj(net.illusory_correlations(A,Corr), ax=ax, more_options=bad_corr_style)
    return pos

def draw_adj_reach_corr(A, axs, add_titles=True, grey_correlations=False):
    pos = draw_np_adj(A, ax=axs[0])
    draw_reachability(A, None, axs[1])
    draw_correlations(A, None, axs[2], grey_correlations=grey_correlations)
    if add_titles:
        axs[0].set_title('adj')
        axs[1].set_title('reach')
        axs[2].set_title('correlations')
    return pos


def draw_controlled_representations(ax, adj, adj_ctrls=None, reach_ctrls=None, corr_ctrls=None):
    '''
    expects ax to be (N+1) x 3 subplot axes
    '''
    reach = net.reachability(adj)
    
    if adj_ctrls is None or corr_ctrls is None or reach_ctrls is None:
        adj_ctrls = net.each_closed_loop_adj(adj)
        reach_ctrls = net.each_closed_loop_reachability(adj) #pass through is_binary?
        corr_ctrls = net.each_closed_loop_correlations(adj) #pass through is_binary?
    N = len(adj_ctrls)
    ctrl_marker_color = 'darkorange'
    severed_edge_style = {'edge_color':'moccasin','style':':'}
    
    pos = draw_adj_reach_corr(adj, ax[0,:],grey_correlations=True)
    # loop across control locations
    for i in range(N):
        plot_i = i+1
        ax_row = ax[plot_i,:]
        draw_np_adj(adj,   ax_row[0], more_options=severed_edge_style)
        draw_np_adj(reach, ax_row[1], more_options=severed_edge_style)

        # across a row, draw adj, reach, corr
        draw_adj_reach_corr(adj_ctrls[i], ax_row, add_titles=(i==0),grey_correlations=True)
        ax_row[0].set_ylabel(f'ctrl @ {i}')
        for _ax in ax_row:
            indicate_ctrl(_ax, pos[i])
                
def draw_controlled_correlations(ax, adj,  adj_ctrls=None, corr_ctrls=None, add_titles=True):
    '''
    expects ax to be 1 x (N) subplot axes
    '''
    if adj_ctrls is None or corr_ctrls is None:
        adj_ctrls = net.each_closed_loop_adj(adj)
        corr_ctrls = net.each_closed_loop_correlations(adj) #pass through is_binary?
    N = len(adj_ctrls)
    
    for i in range(N):
        _ax = ax[i]
        pos = draw_correlations(adj_ctrls[i], Corr=corr_ctrls[i],
            ax=_ax, grey_correlations=True)
        indicate_ctrl(_ax, pos[i],color='#b4a390')
        if add_titles:
            _ax.set_title(f'ctrl$_{i}$')
        # myplot.expand_bounds(_ax)

    
def draw_controlled_adj_correlations(ax, adj, adj_ctrls=None, corr_ctrls=None):
    '''
    expects ax to be 2 x (3+N) subplot axes
    '''
    if adj_ctrls is None or corr_ctrls is None:
        adj_ctrls = net.each_closed_loop_adj(adj)
        corr_ctrls = net.each_closed_loop_correlations(adj) #pass through is_binary?
    
    N = len(adj_ctrls)
    ctrl_marker_color = 'darkorange'
    severed_edge_style = {'edge_color':'moccasin','style':':'}

    #draw unmodified circuit in lower left 3 panels
    pos = draw_adj_reach_corr(adj, ax[1,:3], grey_correlations=True)
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
        indicate_ctrl(_ax0, pos[i])
        indicate_ctrl(_ax1, pos[i])
        
    ax[0,3].set_ylabel('ctrl adj')
    ax[1,3].set_ylabel('ctrl corr')

    myplot.expand_bounds_each(ax)
    
    return ax
#%%
# Plotting functions
def draw_coreachability_by_source(df, axs, node_position, add_titles=True):
    pos_edge_style = straight_edge_style('peachpuff')
    pos_edge_style.update({'width':10})
    neg_edge_style = straight_edge_style('lightblue')
    neg_edge_style.update({'width':2})
    neut_edge_style = straight_edge_style('lightgrey')
    neut_edge_style.update({'width':5})
    
    #NOTE: temporarily overriding rendering style
    # pos_edge_style['edge_color'] = 'lightgrey'
    # neg_edge_style['edge_color'] = 'lightgrey'

    #TODO: scale these by IDSNR weighted co-reachability
    n = len(df['iA'].unique())
    for i in range(n):
        pos_edges, neut_edges, neg_edges = coreach.get_coreachability_from_source(df,i)
        
        draw_np_adj(neut_edges, axs[i], neut_edge_style)
        draw_np_adj(pos_edges, axs[i], pos_edge_style)
        draw_np_adj(neg_edges, axs[i], neg_edge_style)
        indicate_intervention(axs[i],node_position[i])
        # print(node_position)
        if add_titles:
            axs[i].set_title(f'open-loop $S_{i}$')
            #effect of $S_{i}$
            
def draw_adj_reach_corr_coreach(A, df=None, axs=None, add_titles=True):    
    n = A.shape[0]
    n_plot = 3+n;  
    if df is None:
        df = coreach.compute_coreachability_tensor(net.reachability(A))

    if axs is None:
        fig, axs =  plt.subplots(1,n_plot, figsize=((n_plot)*5, 2*2.5),sharey=True,aspect='equal')
        print('INFO: creating axes')
    else:
        fig = axs[0].get_figure()

    graph_pos = draw_adj_reach_corr(A, axs[0:3], add_titles, grey_correlations=True)
    draw_coreachability_by_source(df, axs[3:], graph_pos, add_titles)
    return fig
    
#%%
def censor_diag(A, censor_val=0):
    '''
    adjacency and reachability matrices often have 1s along the diagonal 
        which can skew colormaps
    this function replaces values along the diagonal with a "censored" value for
    better visualization
    '''
    C = A.copy()
    n = C.shape[0]
    C[np.diag_indices(n)] = censor_val
    return C
def fade_zero(M,censor_val=np.NaN):
    F = M.copy()
    F[F==0]=censor_val
    return F
    
def plot_empirical_corrs(A,Rw,X, r2_pred,r2_empr,n_plot=1000,node_colors=None):
    '''
    Draws matrices as both heatmaps and as graphs, alongside timeseries
    
    A - (weighted) adjacency_matrix
    Rw - weighted reachability
    X - time series [samples x nodes]
    r2_pred - predicted corelation matrix
    r2_empr - emprirical correlation matrix
    
    - [ ] draw S 
    - [ ] draw Ctrl!
    ''' 
    wid_ratios = [1,6,1,1,1]
    ncols = len(wid_ratios)
    N = A.shape[0]
    # fig,axs = plt.subplots(2,len(wid_ratios),figsize=(sum(wid_ratios)*3,2*3),gridspec_kw={'width_ratios': wid_ratios})
    fig = plt.figure(figsize=(3*sum(wid_ratios), 2*N))

    gs = GridSpec(2*N,ncols, figure=fig,width_ratios=wid_ratios)
    fasgs = lambda i,j: fig.add_subplot(gs[i,j])

    # Construct panels of figure
    axs = []
    for i in range(5):
        if i==1: 
            _axs=[]
            for i in range(N):
                ii = 2*i
                _ax = fasgs(slice(ii,(ii+2)),1)
                _axs.append(_ax)
            axs.append(_axs)
        else:
            ax_t = fasgs(slice(0,N),i)
            ax_b = fasgs(slice(N,None),i)
            axs.append([ax_t,ax_b])
    '''
    ----------------------------------------------------------------------------
    |            |                         |           |           |           |
    |            |       1, 0              |           |           |           |
    |   0, 0     |_________________________|    2, 0   |   3, 0    |   4, 0    |
    |            |                         |           |           |           |
    |____________|       1, 1              |___________|___________|___________|
    |            |                         |           |           |           |
    |            |_________________________|           |           |           |
    |   0, 1     |                         |    2, 1   |   3, 1    |   4, 1    |
    |            |       1, 2              |           |           |           |
    |____________|_________________________|___________|___________|___________|
    '''
    
    if node_colors is None:
        from matplotlib.cm import get_cmap
        node_colors = get_cmap("tab10").colors
    

    for i,ax in enumerate(axs[1]):
        ax.plot(X[:n_plot,i],linewidth=1,color=node_colors[i])
        
        plt.setp(ax.get_xticklabels(),visible=(i==N-1))
        
        
    ax = [c[0] for c in axs]
    
    # fade_zero = lambda M:( M[M==0] := None)
    A = fade_zero(A)
    Rw = fade_zero(Rw)
    

    ax[0].imshow(A)
    ax[0].set_title('adj')

    # ax[1].plot(X, linewidth=3)
    # ax[1].set_xlim([1,200])

    ax[2].imshow(fade_zero(censor_diag(Rw)), vmin=0)
    ax[2].set_title('$\widetilde{W}$')

    ax[3].imshow(censor_diag(r2_pred), vmin=0,vmax=1)
    ax[3].set_title('$r^2$ pred.')

    ax[4].imshow(censor_diag(r2_empr), vmin=0,vmax=1)
    ax[4].set_title('$r^2$ empr.')

    ax = [c[1] for c in axs]
    draw_np_adj(A, ax[0])
    # myplot.unbox(ax[1],clear_labels=True)
    draw_np_adj(Rw, ax[2])
    draw_weighted_corr(r2_pred,ax[3])
    draw_weighted_corr(r2_empr,ax[4])
    return fig,axs


#%%



#%%
# 1-lag correlation-plot
# if nt<1e5:
#     fig,ax = plt.subplots(3,3,figsize=(5,5),subplot_kw=dict(box_aspect=1))
#     for i in range(3):
#         for j in range(3):
#             # ax[i,j].plot(X[:-2,j],X[2:,i],'k.',markersize=.005)
#             ax[i,j].plot(X[:-1,i],X[1:,j],'k.',markersize=500/nt)
# 
#     fig

#%%
# Archived XCORR plots
'''
# COMPUTE XCORR
def xcorr(x,y):
    # note, this normalizes by standard deviations... might not be what we want
    xc=np.correlate(x/np.std(x), y/np.std(y), mode='same')
    return xc/len(xc)
    
xx_xcorr = xcorr(x, x)
yy_xcorr = xcorr(y, y)
xy_xcorr = xcorr(x, y)

# naive "shuffle correction" on y to predict "side-lobe variance" of xcorr
_xy_xcorr = xcorr(x, rng.permutation(y))
# the above will underestimate xcorr from auto-correlation
# a more appropriate surrogate would be simulating a counterfactual DAG where
# all common inputs are broken into independent paths
# while this is infeasible without oracle knowledge, this may be an inroad to 
# deriving an expression for the expected std.dev(xcorr(side_band))


mid_lag = len(xx_xcorr)//2
lags = np.arange(0,len(xx_xcorr))-mid_lag

side_std_xy = np.std(xy_xcorr[(nt//2+nplot//2):]) # has to do with autocorr!
side_std_xx = np.std(xx_xcorr[(nt//2+nplot//2):]) # has to do with autocorr!
side_std_yy = np.std(yy_xcorr[(nt//2+nplot//2):]) # has to do with autocorr!
print(side_std_xy)
#%%


#%%

fig,ax= plt.subplots(figsize=(10,4))
ax.plot(lags, xy_xcorr,'k');
# ax.plot(lags, _xy_xcorr,'b',linewidth=.5);
1/pythag(pso_x,pso_y)
1/pythag(np.std(x),np.std(y))

noise_std = np.std(xy_xcorr[nt//2+1:])
# noise_std = np.std(_xy_xcorr)
ax.plot(0, pr_xy,'gx',markersize=10)
ax.plot([-mid_lag, mid_lag], [noise_std,noise_std],'m--')
ax.plot([-mid_lag, mid_lag], [-noise_std,-noise_std],'m--')
ax.set_xlim([-nplot,nplot])
xy_xcorr[nt//2]

esnr_xcorr_xy = xy_xcorr[nt//2]/noise_std
print(f'xcorr(lag=0) = {xy_xcorr[mid_lag]:.2f}, r2 = {er_xy:.2f}\n')
print(f'          emp. 0-lag SNR = {esnr_xy:.3f}') 
print(f'emp. peak/side xcorr SNR = {xy_xcorr[mid_lag] / side_std_xy:.3f}') # what we're measuring for analysis later
ax.set_title('how can we predict the magenta bars? \nif we can, we predict XCORR-SNR');
# peaksnr_xy = 2*xy_xcorr[nt//2] / (xx_xcorr[nt//2]+yy_xcorr[nt//2])
# print(peaksnr_xy)
fig

#%%
'''















#%%