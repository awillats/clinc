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
            - need both correlations + dR2/dS to get at net corr
            - in the quantitative case, absolute R2 should be sufficient
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
'''
    
----
- [ ] construct a set of circuits 
- [ ] construct the coreachability df across circuits 
    - ( ) adjacency key 
- [ ] export corr x dR/dS string
'''

'''
from wikipedia: "entropy is a logarithmic measure of the number of system states with significant probability of being occupied"
alt. implementations: https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
- compute counts            
- normalize counts      
- compute -Sum(p log p) in some base
    - components have a max at p = 1/e
'''

import scipy.stats as stats
#low-level
def normalize_freq_dict(d):
    count_sum = sum(d.values())
    new_vals = [v/count_sum for v in d.values()]
    return dict(zip(d.keys(),new_vals))

def sort_dict_by_value(d,reverse=True):
    '''
    sorts in descending order by defaults
    '''
    ds = dict(sorted(d.items(), key = lambda kv: kv[1], reverse=reverse))
    return ds
            
def count_unique_frequency(data, do_sort=True, do_normalize=False):
    vals, counts = np.unique(data, return_counts=True)
    token_frequencies = dict(zip(vals,counts))
    
    if do_normalize:
        token_frequencies = normalize_freq_dict(token_frequencies)
    if do_sort:
        # consider using collections.OrderedDict for this
        token_frequencies = sort_dict_by_value(token_frequencies)
    
    return token_frequencies
    
#wrappers
#NOTE: seems to work if values are counts OR probabilities
def component_entropy_of_dict(d, base=2):
    '''
    -log(p)
    how many bits does it take to encode each individual outcome
    - q: why is it possible for this to be larger than N_total?
        - if p == 1/N, entropy is maximized
    alt. explanation "a measure of surprise"
        
    '''
    return {k:-np.log(v)/np.log(base) for k,v in d.items()}
    
def entropy_of_dict(d, base=2):
    H = stats.entropy( list(d.values()), base=base )
    return H
    
def max_entropy_of_dict(d,base=2):
    return np.log( len(d.keys()) ) / np.log(base)

def format_dict_fstr(d,f=lambda k,v: f'{k}: {v:.3f}'):
    s = " ".join([f(k,v) for k,v in d.items()])
    return s


#%%
if __name__ == '__main__':
    # data = [*['A']*10, 'B','B','C','D','e','f','g','h']
    # data = [*['A']*4,'B','B','C','D']
    # data = [*['A']*40,*['B']*35,*['C']*20,*['D']*5]
    # data = [*['A']*500,*['B']*250,*['C']*125,*['D']*125]
    data = [*['A']*127,*['B']*64,*['C']*64,*['D']*1]

    # data = [0,1,2,*[3]*100]
    # data = [*[0]*7,1]
    tf = count_unique_frequency(data, do_normalize=True)
    ts = component_entropy_of_dict(tf)
    print(f'token frequencies:')
    print(format_dict_fstr(tf))
    # print(1/(2**len(tf.keys())))

    # print(f'component_entropy_of_dict(tf)')
    print(f'token suprise / encoding costs:')
    print(format_dict_fstr(ts))
    entr_base = 2
    # how many rounds of 20 questions will it take to identify your answer? H < Q < H+1 < #max
    H = entropy_of_dict(tf, entr_base)
    H_max = max_entropy_of_dict(tf, entr_base)
    print(f'  H / H_max = {H:.2f} / {H_max:.2f} = {H/H_max:.2f}% efficiency')
    
    #how many equivalent equal categories are present
    print(f'    #states = {2**H:.1f} / {len(tf.keys())} max')
    p = np.array(list(tf.values()))
    sum(p*np.array([1,2,3,3]))
    import matplotlib.pyplot as plt
    p = np.linspace(1e-3,1-1e-3,200)
    y = (-p*np.log2(p))
    y2 = (-p*np.log2(p)) + (-(1-p)*np.log2(1-p))
    
    plt.plot(p,y,'k')
    plt.plot(p,y2,'b:')
    #%%
    # plt.plot([0,1], [0.5 for _ in range(2)],'r--')
    


