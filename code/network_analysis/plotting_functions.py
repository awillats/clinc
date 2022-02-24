import numpy as np
import matplotlib.pyplot as plt

def unbox(ax, clear_labels=False):
    '''
    removes edges of subplot frame
    '''
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if clear_labels:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_yticklabels([])
        ax.set_xticklabels([])
    return ax

def unbox_each(ax, clear_labels=False):
    for _ax in ax:
        for __ax in _ax:
            unbox(__ax,clear_labels)
            
def expand_bounds(ax,expansion_factor=1.1):
    '''
    sets the boundaries of an axis to be a little larger 
    - useful in conjunction with networkx+matplotlib
    - which sometimes results in axes clipping the edge of nodes
    '''
    ax.set_xlim([1.1*x for x in ax.get_xlim()])
    ax.set_ylim([1.1*y for y in ax.get_ylim()])
    return ax
    
def expand_bounds_each(ax, expansion_factor=None):
    for _ax in ax: 
        for __ax in _ax:
            expand_bounds(__ax, expansion_factor)
            
def label_and_clear_axes_grid(ax):
    '''
    writes index into x and y-labels
    '''
    n = ax.shape[0]
    [_ax.set_title(i) for i,_ax in enumerate(ax[0,:])]
    [_ax.set_xlabel(i) for i,_ax in enumerate(ax[n-1,:])]
    [_ax.set_ylabel(i) for i,_ax in enumerate(ax[:,0])]
    [_ax.set_ylabel(i) for i,_ax in enumerate(ax[:,n-1])]
    [_ax.yaxis.set_label_position('right') for i,_ax in enumerate(ax[:,n-1])]
    [__ax.set_yticks([]) for _ax in ax for __ax in _ax ]
    [__ax.set_xticks([]) for _ax in ax for __ax in _ax ]
    [unbox(__ax)  for _ax in ax for __ax in _ax ]

def super_ylabel(fig,txt,fontsize=20):
    fig.text(0.1,.5,txt,fontsize=fontsize,ha='center',va='center',rotation='vertical')
#%%
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