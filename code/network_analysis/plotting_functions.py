import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})#25

def subplots(nrows,ncols, figsize=None,w=3):
    
    
    if figsize is None:
        figsize = (w*ncols,w*nrows)
    fig,ax = plt.subplots(nrows,ncols,figsize=figsize, 
        sharex=True,sharey=True)
    
    for a in ax.flatten():
        a.set_aspect('equal')

    return fig,ax
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
    ax.set_xlim([expansion_factor*x for x in ax.get_xlim()])
    ax.set_ylim([expansion_factor*y for y in ax.get_ylim()])
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
# import inspect
# import sys
# from os import path
# 
# def get_caller_filename():
#     filename = inspect.stack()[0].filename 
#     return filename
'''
see: https://github.com/awillats/clinc-gen/blob/main/data_handling/saving_functions.py
'''
def savefig(img_name,dpi=100,facecolor='w',this_file=None,save_svg=False):
    '''
    just wraps a default into matplotlibs savefig
    '''
    plt.savefig(img_name,dpi=dpi,facecolor=facecolor)
    if save_svg:
        svg_file_name = img_name.rsplit('.png',1)[0]+'.svg'
        plt.savefig(svg_file_name,facecolor=facecolor)
    if this_file:
        print(f'![](code/network_analysis/{img_name} "generated by {this_file}")')
    # print(inspect.stack())

def imshow_png(ax,png,do_unbox=False):
    w,h = png.size
    hw = w/2.
    hh = h/2.
    ax.imshow(png,extent = [-hw,hw,-hh,hh]) 
    if do_unbox:
        unbox(ax,clear_labels=True)