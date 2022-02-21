import numpy as np
import networkx as nx
import network_analysis_functions as net
import plotting_functions as myplot
import coreachability_source_classification as coreach
#%% markdown

to-do list
- [ ] compute entropy across hypotheses
    - mega df?
        - am converting from adj to df ... instead perhaps should keep circuit as packaged cell 
        - should circuit be "distributed" by index?
        - or fit in a single cell by wrapping []
        - string of [+,+,+,+,+] or [-,-,+,=] or [1v,v,1^,^,-,0v,0]
        - passive [=,=,=,_]
        - to get finger print need to mux S+-0 with baseline corr
        
    - tokenizer for each circuit?
        - correlations should be "undirected"
            ```
            for i in range(n):
                for j in range(i,n):
            ```
            takes care of this 
            but might be nice to have more robust version
        - dictionary with tuples of patterns as keys?
    - compute entropy across tokens
        - simply requires counting occurences
    - ( weight by prior )

#%%