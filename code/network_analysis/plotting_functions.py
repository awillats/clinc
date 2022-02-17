import numpy as np
import matplotlib.pyplot as plt

def unbox(ax):
    '''
    removes edges of subplot frame
    '''
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return ax
    
def expand_bounds(ax,expansion_factor=1.1):
    '''
    sets the boundaries of an axis to be a little larger 
    - useful in conjunction with networkx+matplotlib
    - which sometimes results in axes clipping the edge of nodes
    '''
    ax.set_xlim([1.1*x for x in ax.get_xlim()])
    ax.set_ylim([1.1*y for y in ax.get_ylim()])
    return ax

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
    fig.text(0.05,.5,txt,fontsize=fontsize,ha='center',va='center',rotation='vertical')