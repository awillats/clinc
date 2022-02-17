import numpy as np
import networkx as nx
import network_analysis_functions as net
import plotting_functions as myplot
import coreachability_source_classification as coreach
#%%
'''
to-do list
- [ ] compute entropy across hypotheses
    - mega df?
    - tokenizer for each circuit?
        - dictionary with tuples of patterns as keys?
    - compute entropy across tokens
    - ( weight by prior )
'''
#%%