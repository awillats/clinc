import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})#25

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
