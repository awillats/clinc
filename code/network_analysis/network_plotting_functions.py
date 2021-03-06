import numpy as np 
import networkx as nx 
# import scipy.linalg as linalg
import coreachability_source_classification as coreach
import network_analysis_functions as net
import network_data_functions as netdata

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

import plotting_functions as myplot
from aenum import Flag,auto
import string
#%%
'''
TODO:
- [ ] clean up: def __draw() functions
- [ ] debug styling dotted arrows 
    see:
    https://stackoverflow.com/questions/51413834/networkx-arrows-ploting
    https://stackoverflow.com/questions/66889224/networkx-not-drawing-arrows-in-directed-graph
    https://stackoverflow.com/questions/47894931/increase-thickness-in-a-matplotlib-annotation-double-sided-arrow
- [ ] list commonly editted networkx / matplotlib style options
----
looking into alternate network visualization libraries:
- comparison of 3 libs: https://towardsdatascience.com/visualizing-networks-in-python-d70f4cbeb259
## python:
    - pyviz - https://pyvis.readthedocs.io/en/latest/tutorial.html
        - nice, includes interactivity, but writes to html
        - see also pygraphviz: https://pygraphviz.github.io/documentation/stable/auto_examples/index.html
        
    - igraph - https://igraph.org/python/tutorial/latest/tutorial.html    
    - ? scikit-network viz? https://scikit-network.readthedocs.io/en/latest/reference/visualization.html#graphs

## python via plotly / Dash:
    - ploty + networkx: https://plotly.com/python/network-graphs/
        - cumbersome, but interactive
    - dash cytoscape: https://www.linuxtut.com/en/4b187020daff72667208/
    - vis-dash (visj): 
        
## not python:
- SVG: 
    - see svg_draw.py
    
- cytoscape (standalone)
- gephi (standalone)
- PGF/TIKZ


'''

#%%
'''
Style settings 
'''
DEFAULT_NET_PLOT_OPTIONS = {
        'node_color': 'lightgrey',
        'node_size': 500, #1000
        'width': 4,
        'arrowstyle': '-|>',
        'arrowsize':25,
        'connectionstyle':"arc3,rad=0.1", 
    }
#NOTE: consider using negative radius if connections are mostly clockwise
    
# dusty_orange = '#b4a390'    
DARK_CTRL_COLOR = 'darkorange'
CTRL_COLOR = 'orange'
LIGHT_CTRL_COLOR = 'moccasin'

OPEN_LOOP_COLOR = 'dodgerblue'
# mpl::lightgrey == #D3D3D3
LIGHTER_GREY = '#e6e6e6'
GREY = '#D3D3D3'
DARKER_GREY = '#adadad'

def get_edge_style(type, do_grey_out=False,base_options={}):
    if 'pos' in type or 'incr' in type:
        edge_style = straight_edge_style(DARKER_GREY) #was 'peachpuff'
        edge_style.update({'width':10})
    if 'neg' in type or 'decr' in type:
        edge_style = straight_edge_style(LIGHTER_GREY) # was 'lightblue'
        edge_style.update({'width':2})
    if 'neut' in type or 'same' in type:
        edge_style = straight_edge_style(GREY) #lightgrey')
        edge_style.update({'width':5})
    
    if 'good' in type:
        edge_style = straight_edge_style('lightgreen')
    if 'bad' in type:
        edge_style = straight_edge_style('lightcoral')
    
    if type is None:
        edge_style = straight_edge_style(GREY)
        
    if do_grey_out:
        edge_style['edge_color'] = GREY
    edge_style.update(base_options)
    return edge_style
    
    
#%%
# _ABC_DICT = {number:chr(letter) for (number,letter) in zip(range(26),range(ord('A'),ord('Z')+1))}
# Network plotting  
def draw_weighted_corr(W, ax=None, min_w=0,max_w=10, more_options={},pos_override=None):
    G = nx.from_numpy_matrix(W, create_using=nx.Graph) 
    weights = np.array(list(nx.get_edge_attributes(G,'weight').values()))
    weights = rescale(weights, min_w,max_w, 0,1)
    
    if pos_override is None:
        pos = clockwise_circular_layout(G)
    else:
        pos = pos_override
    
    options = DEFAULT_NET_PLOT_OPTIONS.copy()
    options.update({'ax':ax,'pos':pos})
    options.update({'width':weights,'node_size':150})
    options.update(more_options)
    
    nx.draw(G, **options)
    ax.set_aspect('equal')
    # nx.draw_networkx_edge_labels(G, pos=pos)
    # myplot.expand_bounds(ax)
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
def clockwise_circular_layout(G=None, initial_rot=0, do_relabel_abc=False):
    if G is None:
        G = nx.DiGraph()
        G.add_nodes_from([0,1,2])
    pos = nx.circular_layout(G)
    pos = rotate_layout(pos, np.pi/3 + initial_rot, True)
    if do_relabel_abc:
        pos = relabel_pos_abc(pos)
    return pos
#%%    
def _gen_layout_from_adj(adj):
    nx_adj = nx.from_numpy_matrix(adj, create_using=nx.DiGraph) 
    pos = clockwise_circular_layout(nx_adj)
    return pos
def relabel_nodes_abc(G,do_uppercase=True):
    abc = string.ascii_uppercase if do_uppercase else string.ascii_lowercase
    return nx.relabel_nodes(G, dict(zip(G,abc)))
def relabel_pos_abc(pos_dict, do_uppercase=True):
    abc = string.ascii_uppercase if do_uppercase else string.ascii_lowercase
    return {abc[k]:v for k,v in pos_dict.items()}
def draw_np_adj(adj, ax=None, more_options={}, do_rename_abc=True, node_labels=None):
    '''
    core plotting function that renders an adjacency_matrix 
    - gets used is several other higher-level plotting functions
    - TODO: still node using node labels properly!!
    '''
    
    # DROP non-finite edges (like None, np.NaN etc.)
    adj = adj.copy()
    adj[~np.isfinite(adj)] = 0
    
    nx_adj = nx.from_numpy_matrix(adj, create_using=nx.DiGraph) 
    
    if do_rename_abc:
        nx_adj = relabel_nodes_abc(nx_adj)
    if node_labels:
        nx_adj = nx.relabel_nodes(nx_adj, node_labels)
    
    pos = clockwise_circular_layout(nx_adj)
    
    options = DEFAULT_NET_PLOT_OPTIONS.copy()
    options.update({'ax':ax,'pos':pos})
    options.update(more_options)
    # options.update({'with_labels':True})
    
    nx.draw_networkx(nx_adj, arrows=True, **options)
    
    #DEBUG: DRAW arrowheads on again, because matplotlib doesn't like dotted arrows
    if options.get('style') == ':' or options.get('style') == '--':
        options.update({'width':0,'arrowsize':40,'style':'-','arrowstyle':'-|>'})
        nx.draw_networkx(nx_adj, arrows=True, **options)

    if ax is not None:
        myplot.unbox(ax)
    # myplot.expand_bounds(ax)
    return pos
def draw_nx(G, ax=None, do_rename_abc=True,node_labels=None, more_options={}):
    return draw_np_adj(netdata.nx_to_np_adj(G),ax=ax,do_rename_abc=do_rename_abc, more_options=more_options)
#%%
from matplotlib import patches
straight_arrow_style = patches.ArrowStyle.Curve()
def straight_edge_style(color):
    return {'edge_color':color,'connectionstyle':'arc3,rad=0','arrowstyle':'-'}
    # return {'edge_color':color,'connectionstyle':'arc3,rad=0','style':'--','arrowstyle':straight_arrow_style}


def indicate_ctrl(ax, pos_i, markersize=20, color=DARK_CTRL_COLOR):
    # ms of 30 corresponds to a node size of 1000
    ax.plot(pos_i[0],pos_i[1],'o',color=color,markersize=markersize,markeredgewidth=4,fillstyle='none')

def indicate_intervention(ax, pos_i, type='open-loop'):
    '''
    see also indicate_ctrl
    '''
    arrow_mag = 0.4
    arrow_c = OPEN_LOOP_COLOR if type=='open-loop' else CTRL_COLOR
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
        connectionstyle='arc3',
        lw=5)
        
    ax.annotate("", xy=(x0+dx,y0+dy), xycoords='data',
                    xytext=(x0,y0), textcoords='data',
                    arrowprops=arrow_spec,
                        zorder=100
                    )    

def indicate_intervention_from_plot_type_loc(ax, pos, ptl):
    i = ptl['intervention_location']
    if ptl['plot_type'] & NetPlotType.OPEN:
        indicate_intervention(ax,pos[i])
    if ptl['plot_type'] & NetPlotType.CTRL:
        indicate_ctrl(ax,pos[i])

# %%    
def draw_reachability(A,R=None,ax=None, reach_edge_style=None):
    if R is None:
        R = net.reachability(A)
    if reach_edge_style is None:
        reach_edge_style = {'edge_color':'lightgrey'}
    draw_np_adj(R, ax=ax, more_options=reach_edge_style)
    draw_np_adj(A, ax=ax)
    
def draw_correlations(A,Corr=None,ax=None,grey_correlations=False,base_options={}):
    '''
    grey_correlations - if False, direct correlations are colored green, indirect correlations are colored red
    '''
    if Corr is None:
        Corr = net.binary_correlations(A)
    #NOTE: does it make sense to have "yellow" correlations which are in the reachability but NOT the adj 
    # then "red" correlations which aren't in the reachability ?
    
    # bad_corr_style.update(base_options)
    good_corr_style = get_edge_style('good', do_grey_out = grey_correlations, base_options = base_options)
    bad_corr_style  = get_edge_style('bad', do_grey_out = grey_correlations, base_options = base_options)

    draw_np_adj(Corr, ax=ax, more_options=good_corr_style)
    pos = draw_np_adj(net.illusory_correlations(A,Corr), ax=ax, more_options=bad_corr_style)
    return pos

def draw_adj_reach_corr(A, axs=None, add_titles=True, grey_correlations=True, expand_bounds=None):
    if axs is None:
        fig,axs = myplot.subplots(1,3)
    pos = draw_np_adj(A, ax=axs[0])
    draw_reachability(A, None, axs[1])
    draw_correlations(A, None, axs[2], grey_correlations=grey_correlations)
    if add_titles:
        axs[0].set_title('adj')
        axs[1].set_title('reach')
        axs[2].set_title('correlations')
    if expand_bounds:
        myplot.expand_bounds(axs[0],expand_bounds)
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
    ctrl_marker_color = DARK_CTRL_COLOR
    severed_edge_style = {'edge_color':LIGHT_CTRL_COLOR,'style':':'}
    
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
                
def draw_controlled_correlations(ax, adj,  adj_ctrls=None,corr_ctrls=None, add_titles=True, ctrl_color=None):
    '''
    expects ax to be 1 x (N) subplot axes
    '''
    if adj_ctrls is None or corr_ctrls is None:
        adj_ctrls = net.each_closed_loop_adj(adj)
        corr_ctrls = net.each_closed_loop_correlations(adj) #pass through is_binary?
    N = len(adj_ctrls)

    if ctrl_color is None:
        ctrl_color = DARK_CTRL_COLOR #dark_orange

    for i in range(N):
        _ax = ax[i]
        pos = draw_correlations(adj_ctrls[i], Corr=corr_ctrls[i],
            ax=_ax, grey_correlations=True)
        indicate_ctrl(_ax, pos[i],color=ctrl_color)
        if add_titles:
            _ax.set_title(f'ctrl$_{i}$')
        # myplot.expand_bounds(_ax)
#%%
def __draw_ctrl_adj_at_source(ax,adj,intv_loc,adj_ctrl=None,
        node_position=None,add_title=True):
    if adj_ctrl is None:
        adj_ctrl = net.sever_inputs(adj,intv_loc)
    if node_position is None:
        node_position = _gen_layout_from_adj(adj)
    
    # light_orange = '#936d4699'
    # dark_orange = '#ece3de99'
    DARK_GREY_TRANS = '#53535366'
    LIGHT_GREY_TRANS = '#b5b5b566'
    severed_direct_style = {'edge_color':DARK_GREY_TRANS,'style':'--'}
    severed_indirect_style = {'edge_color':LIGHT_GREY_TRANS,'style':'--'}

    
    myplot.unbox(ax)
    r = net.reachability(adj)
    draw_np_adj(r,        ax=ax, more_options=severed_indirect_style)
    draw_np_adj(adj,      ax=ax, more_options=severed_direct_style)
    draw_np_adj(adj_ctrl, ax=ax)
    indicate_ctrl(ax, node_position[intv_loc])
    
    if add_title:
        ax.set_title(f'ctrl @ {intv_loc}')

def __draw_ctrl_correlations_at_source(ax,adj, intv_loc, adj_ctrl=None,corr_ctrl=None,
    node_position=None,grey_correlations=False,add_title=True):
    if adj_ctrl is None:
        adj_ctrl = net.sever_inputs(adj,intv_loc)
    if corr_ctrl is None:
        corr_ctrl  = net.closed_loop_correlations(adj, intv_loc, is_binary=True)
    if node_position is None:
        node_position = _gen_layout_from_adj(adj)
    
    #draw background, indirect correlations
    # draw_correlations(adj, ax=ax, grey_correlations=grey_correlations,base_options={'style':':','edge_color':'#dfa3a3'})
    
    draw_correlations(adj_ctrl, Corr=corr_ctrl, ax=ax, grey_correlations=grey_correlations)
    indicate_ctrl(ax, node_position[intv_loc])
    if add_title:
        ax.set_title(f'corr\nw/ctrl @ {intv_loc}')
#%%
def draw_controlled_adj_correlations(ax, adj, adj_ctrls=None, corr_ctrls=None):
    '''
    expects ax to be 2 x (3+N) subplot axes
    '''
    if adj_ctrls is None or corr_ctrls is None:
        adj_ctrls = net.each_closed_loop_adj(adj)
        corr_ctrls = net.each_closed_loop_correlations(adj) #pass through is_binary?
    
    N = len(adj_ctrls)
    ctrl_marker_color = DARK_CTRL_COLOR # unused?
    severed_edge_style = {'edge_color':LIGHT_CTRL_COLOR,'style':':'}

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
def __draw_coreachability_by_source(adj, axs, node_position=None, add_titles=True, grey_correlations=False):
    '''
    NOTE: work in progress
    - refactoring with a more standard interface
    '''
    if node_position is None:
        node_position = _gen_layout_from_adj(adj)
    # if df is None:
    df = coreach.compute_coreachability_tensor(net.reachability(adj))
    draw_coreachability_by_source(df=df, axs=axs, node_position=node_position, 
        add_titles=add_titles, grey_correlations=grey_correlations)

def __draw_coreachability_at_source(adj, ax,intv_loc,df=None, node_position=None, add_titles=True, grey_correlations=False):
    '''
    TODO: DOCS: how do these __draw version differ from others?
        - they're intended as internal-only functions 
        - they're being actively updated and aren't stable for public use
    '''
    if df is None:
        df = coreach.compute_coreachability_tensor(net.reachability(adj))
        
    if node_position is None:
        node_position = _gen_layout_from_adj(adj)
    pos_edge_style = straight_edge_style('darkgrey')#'peachpuff'
    pos_edge_style.update({'width':10})
    neg_edge_style = straight_edge_style('lightgrey') #'lightblue')
    neg_edge_style.update({'width':2})
    neut_edge_style = straight_edge_style('grey')
    neut_edge_style.update({'width':5})
    
    if grey_correlations:
        pos_edge_style['edge_color'] = 'lightgrey'
        neg_edge_style['edge_color'] = 'lightgrey'
        neut_edge_style['edge_color'] = 'lightgrey'
    pos_edges, neut_edges, neg_edges = coreach.get_coreachability_from_source(df, intv_loc)
    
    draw_np_adj(neut_edges, ax, more_options=neut_edge_style)
    draw_np_adj(pos_edges, ax, more_options=pos_edge_style)
    draw_np_adj(neg_edges, ax, more_options=neg_edge_style)
    indicate_intervention(ax, node_position[intv_loc])
    # print(node_position)
    if add_titles:
        ax.set_title(f'corr\nw/open-loop @ $S_{intv_loc}$')
    
def draw_coreachability_by_source(df, axs, node_position, add_titles=True, grey_correlations=False):
    '''
    ! requires dataframe, which can be generated from ...
    indicates increased, decreased and neutral correlations
    - e.g. as a result of open-loop intervention at each node
    
    - [ ] TODO: move default styles elsewhere
    '''
    increase_edge_style = get_edge_style('increase', do_grey_out=grey_correlations)
    decrease_edge_style = get_edge_style('decrease', do_grey_out=grey_correlations)
    neutral_edge_style = get_edge_style('neutral', do_grey_out=grey_correlations)

    #TODO: scale these by IDSNR weighted co-reachability
    n = len(coreach.get_node_names_from_coreach(df))
    
    node_names = list(node_position.keys())
    
    for i in range(n):
        # __draw_coreachability_at_source(adj=None, ax=axs[i], df=df,intv_loc=i,
        #     node_position=node_position,add_titles=add_titles, 
        #     grey_correlations=grey_correlations)
            
        incr_edges, neut_edges, decr_edges = coreach.get_coreachability_from_source(df,i)
        
        draw_np_adj(neut_edges, axs[i], neutral_edge_style)
        draw_np_adj(incr_edges, axs[i], increase_edge_style)
        draw_np_adj(decr_edges, axs[i], decrease_edge_style)
        indicate_intervention(axs[i], node_position[node_names[i]])
        # print(node_position)
        if add_titles:
            axs[i].set_title(f'open-loop $S_{i}$')
            # effect of $S_{i}$
    #        
def draw_adj_reach_corr_coreach(A, df=None, axs=None, add_titles=True, grey_correlations=False):    
    n = A.shape[0]
    n_plot = 3+n;  
    if df is None:
        df = coreach.compute_coreachability_tensor(net.reachability(A))

    if axs is None:
        # fig, axs =  plt.subplots(1,n_plot, figsize=((n_plot)*5, 2*2.5),sharey=True)#, aspect='equal')
        fig, axs = myplot.subplots(1,n_plot)
        print('INFO: creating axes')
    else:
        fig = axs[0].get_figure()

    graph_pos = draw_adj_reach_corr(A, axs[0:3], add_titles, grey_correlations=True)
    draw_coreachability_by_source(df, axs[3:], graph_pos, add_titles, grey_correlations=grey_correlations)
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
    F = M.copy().astype('float')
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
def strip_trailing_int(str,delim='@'):
    if delim in str:
        return int(str.split(delim)[1])
    else:
        return None
# from aenum import Flag, auto

# see https://github.com/awillats/clinc-gen/blob/main/small_circuit_scripts/circuit_functions/run_PID_ctrl.py 
# for another usage of Flag, auto
# some discussion of enum vs aenum here: https://stackoverflow.com/questions/60635855/python-enum-flag-with-one-flag-that-is-used-by-some-others

class NetPlotType(Flag):
    '- NOTE: this is probably useful in analysis also... so maybe these types should live elsewhere'
    ADJ = auto() 
    REACH = auto()
    CORR = auto() 
    COREACH = auto()

    PASV = auto()
    OPEN = auto()
    CTRL = auto()
    
    ADJ_CTRL = ADJ | CTRL
    CORR_CTRL = CORR | CTRL
    REACH_CTRL = REACH | CTRL
    COREACH_CTRL = REACH | COREACH | CTRL
    
    def __init__(self,flag_val):
        # Flag.__init__(self) #replace with super?
        # super(NetPlotType, self).__init__()
        super().__init__()
    #     self.intervention_location=None
    # def set_intervention_location(self, loc):
    #     '''
    #     DANGER: this is acting like a class-level property
    #     '''
    #     self.intervention_location = loc
    def intv_type(self):
        for t in [NetPlotType.PASV,NetPlotType.OPEN,NetPlotType.CTRL]:
            if self & t:
                return t
        return None
        
    def color(self):
        if self & NetPlotType.PASV:
            return 'grey'
        if self & NetPlotType.OPEN:
            return 'dodgerblue'
        if self & NetPlotType.CTRL:
            return 'orange'
        return 'black'
        
    def lightcolor(self):
        if self & NetPlotType.PASV:
            return 'lightgrey'
        if self & NetPlotType.OPEN:
            return '#b0d3f0'
        if self & NetPlotType.CTRL:
            return '#ffd6a8'
        return 'white'

    def __hash__(self):
        #custom has function, hopefully so object can be used as key
        # https://stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key
        return hash(str(self))
    def __eq__(self, other):
        return str(self) == str(other)
    def __repr__(self):
        r = f'{self.name}'
    #     if hasattr(self,'intervention_location') and self.intervention_location is not None:
    #         r +=f'@{string.ascii_uppercase[self.intervention_location]}'
        return r
    def __str__(self):
        return self.__repr__()
        
def parse_plot_type(plot_str):
    plot_str = plot_str.lower()
    intv_loc = strip_trailing_int(plot_str)
    pt = NetPlotType.ADJ & NetPlotType.REACH
    '''
    Note, the resulting plot type can combine ADJ/REACH/CORR with CTRL 
    - this is achieved by using the OR:| operation with flags
    
    '''
    
    if 'adj' in plot_str:
        pt |= NetPlotType.ADJ
    if 'reach' in plot_str:
        pt |= NetPlotType.REACH
    if 'corr' in plot_str:
        pt |= NetPlotType.CORR
    if 'coreach' in plot_str:
        pt |= NetPlotType.COREACH
    if 'ctrl' in plot_str:
        pt |= NetPlotType.CTRL
        # pt.set_intervention_location(strip_trailing_int(plot_str))
    if 'open' in plot_str:
        pt |= NetPlotType.OPEN
        
        # pt.set_intervention_location(strip_trailing_int(plot_str))        
    return {'plot_type':pt,'intervention_location':intv_loc}
def plot_type_loc_to_str(plot_type_loc):
    s = str(plot_type_loc['plot_type'])
    if plot_type_loc['intervention_location'] is not None:
        s += f' @ {string.ascii_uppercase[plot_type_loc["intervention_location"]]}'
    return s

def plot_adj_by_plot_type(ax, A, plot_type_loc, add_titles=True):
    grey=True
    plot_type = plot_type_loc['plot_type']
    intervention_location = plot_type_loc['intervention_location']
    
    # NOTE: this responsibility should belong to NetPlotType !
    plot_funs = {
        NetPlotType(0):         lambda adj,ax,intv_loc: adj*2,
        NetPlotType.ADJ:        lambda adj,ax,intv_loc: draw_np_adj(adj,ax=ax),
        NetPlotType.REACH:      lambda adj,ax,intv_loc: draw_reachability(adj,ax=ax),
        NetPlotType.CORR:       lambda adj,ax,intv_loc: draw_correlations(adj,ax=ax,grey_correlations=grey),
        NetPlotType.ADJ_CTRL:   lambda adj,ax,intv_loc: __draw_ctrl_adj_at_source(adj=adj,ax=ax,intv_loc=intv_loc),
        NetPlotType.CORR_CTRL:  lambda adj,ax,intv_loc: __draw_ctrl_correlations_at_source(adj=adj,ax=ax,intv_loc=intv_loc,grey_correlations=grey),
        # NetPlotType.REACH_CTRL :  lambda adj,ax,intv_loc: netplot.__draw_coreachability_at_source(adj,ax=ax,intv_loc=intv_loc),
        # NetPlotType.CTRL :  lambda adj,ax,intv_loc: netplot.__draw_coreachability_at_source(adj,ax=ax,intv_loc=intv_loc),
        NetPlotType.OPEN:       lambda adj,ax,intv_loc: __draw_coreachability_at_source(adj=adj,ax=ax,intv_loc=intv_loc,grey_correlations=grey),
    }
    this_plot_fun = plot_funs.get(plot_type)
    
    this_plot_fun(A, ax, intervention_location)
    
    # # NOTE: this responsibility should belong to NetPlotType !
    plot_title_fn_by_type = {
        NetPlotType(0):         lambda plot_type_loc: '',
        NetPlotType.ADJ:        lambda plot_type_loc: 'adjacency',
        NetPlotType.REACH:      lambda plot_type_loc: 'reachability',
        NetPlotType.CORR:       lambda plot_type_loc: 'correlations',
        NetPlotType.ADJ_CTRL:   lambda plot_type_loc: 'modified\nadjacency',
        NetPlotType.CORR_CTRL:  lambda plot_type_loc: 'correlations',
        NetPlotType.OPEN:       lambda plot_type_loc: 'correlations',
    }
    
    
    if add_titles:
        # ax.set_title(str(plot_type),color='lightgrey')
        ax.set_title(plot_title_fn_by_type[plot_type](plot_type_loc),color=GREY)
    else:
        ax.set_title('')

def plot_each_adj_by_plot_type(axs, As, plot_types,ax_padding=1.2):
    N_circ = len(As)
    N_plots = len(plot_types)
    if axs is None:
        fig,axs = myplt.subplots(N_circ,N_plots)
    else:
        fig = axs[0][0].get_figure()
    for j,A in enumerate(As):
        for i,plot_type in enumerate(plot_types):
            plot_adj_by_plot_type(axs[j][i],A,plot_type, add_titles=(j==0))
    myplot.expand_bounds(axs[0][0],ax_padding)
    return fig
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