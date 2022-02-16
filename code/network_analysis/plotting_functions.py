import numpy as np
import matplotlib.pyplot as plt

def unbox(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    return ax
def expand_bounds(ax,expansion_factor=1.1):
    ax.set_xlim([1.1*x for x in ax.get_xlim()])
    ax.set_ylim([1.1*y for y in ax.get_ylim()])
    return ax