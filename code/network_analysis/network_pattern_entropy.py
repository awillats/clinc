import numpy as np
import networkx as nx
import network_analysis_functions as net
import plotting_functions as myplot
import coreachability_source_classification as coreach

import random
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
        - token to xaxis label
    - compute entropy across tokens
        - simply requires counting occurences
    - ( weight by prior )

#%%
'''
    
----
- [~] construct a set of circuits 
- [ ] !! construct the coreachability df across circuits 
    - ( ) adjacency key 
- [~] export corr x dR/dS string

---
plotting 
- graphs as axis labels:
    - https://stackoverflow.com/questions/44246650/add-image-annotations-to-bar-plots
- highlights via plotly?
    - p( A→B ) = count/total = 0.01
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
#%%    
#wrappers
#NOTE: seems to work if values are counts OR probabilities
def component_entropy_of_dict(d, base=2):
    '''
    -log(p)
    how many bits does it take to encode each individual outcome
    - q: why is it possible for this to be larger than N_total?
        - if p == 1/N, entropy is maximized
    alt. explanation "a measure of surprise"
    - rename to surprise?
        
    '''
    return {k:-np.log(v)/np.log(base) for k,v in d.items()}
    
def entropy_of_dict(d, base=2):
    H = stats.entropy( list(d.values()), base=base )
    return H
    
def max_entropy_of_dict(d,base=2):
    return np.log( len(d.keys()) ) / np.log(base)

def compute_prob_dupe_from_freq(token_freq):
    '''
    assumes replacement
    sum of probabilities squared, i.e p(AA) + p(BB) + p(CC)
    '''
    probs = np.array(list(token_freq.values()))
    probs /= sum(probs)
    return sum(probs**2)
    
def lower_bound_prob_dupe_from_entropy(H, base=2):
    '''
    given the entropy(H) of a pmf , 
    compute the probability that two samples drawn from it are the same
    NOTE: this assumes hypotheses are drawn *with replacement*
    TODO: add version which computes probability without replacement
    
    __N_correction_factor should be the number of tokens...
    without scale correct, prediction is likely to be an lowerbound on prob_dupe
    '''
    p_equiv = (1/(base**H))
    # if __N_correction_factor is None:
    return p_equiv
    # else:
    #     print(f'un adjusted {p_equiv:.2f}')
    #     _n = __N_correction_factor
    #     _scale = (_n)/(_n-1)
    #     p_adjust = 1-_scale*((1-p_equiv)**2)
    #     return p_adjust
#%%

def compute_entropy_stats_of_dict(token_freq,entropy_base=2):
    H = entropy_of_dict(token_freq, entropy_base)
    H_max = max_entropy_of_dict(token_freq, entropy_base)
    p_dupe = compute_prob_dupe_from_freq(token_freq)
    p_dupe_lb = lower_bound_prob_dupe_from_entropy(H)
    p_uni = lower_bound_prob_dupe_from_entropy(H_max)
    summary_str = f'H / H_max = {H:.2f} / {H_max:.2f} \n= {100*H/H_max:.1f}% efficiency\n'
    summary_str+= f'prob. non-dupe = {(1-p_dupe)*100:.1f}% / {(1-p_uni)*100:.1f} %'
    
    return {'H':H, 'H_max':H_max,
            'p_dupe':p_dupe,'p_dupe_lb':p_dupe_lb, 'summary_str':summary_str}
    
def compute_and_plot_count_entropy(data, ax, do_normalize=True, entropy_base=2, keys_to_xlabels=lambda x: x):
    token_freq = count_unique_frequency(data,do_normalize=do_normalize)
    N = len(token_freq)
    token_surprise = component_entropy_of_dict(token_freq)
    entropy_res = compute_entropy_stats_of_dict(token_freq, entropy_base)
    H, H_max, p_dupe,p_dupe_lb, summary_str = entropy_res.values()
    
    ax.bar(keys_to_xlabels(token_freq.keys()), token_freq.values())
    # ax.plot([-.5,N+.5],[1/N,1/N],'g:')
    ax.set_ylabel('p')
    ax.set_xlabel('Symbol')
    ax.set_title(entropy_res['summary_str'])

    return {'token_frequencies':token_freq,'H':H,'H_max':H_max,'base':entropy_base,
        'ax':ax,'_entropy_res':entropy_res}
#%%

def format_dict_fstr(d,f=lambda k,v: f'{k}: {v:.2f}'):
    s = " ".join([f(k,v) for k,v in d.items()])
    return s


def weighted_surprise_plot(token_freq, ax, entropy_res=None, token_surprise=None):
    regularized_probs = np.array(list(token_freq.values()))+.01
    N = len(token_freq)
    
    if token_surprise is None:
        token_surprise = component_entropy_of_dict(token_freq)
    if entropy_res is None:
        entropy_res = compute_entropy_stats_of_dict(token_freq, 2)
    H, H_max, p_dupe,p_dupe_lb, summary_str = entropy_res.values()
    
    bar_h = token_surprise.values()
    ax.bar(token_freq.keys(), bar_h, width=regularized_probs)
    ax.plot([-.5, N-0.5],[H,H],'k:')
    ax.plot([-.5, N-0.5],[H_max,H_max],'g--',linewidth=1)
    ax.set_title(summary_str)
    ax.set_ylabel('surprise [bits]')
    return ax

def component_efficiency_plot(token_freq, ax, entropy_res=None):
    '''
    verify this does what we expect
    '''
    N = len(token_freq)
    regularized_probs = np.array(list(token_freq.values()))+.01

    if entropy_res is None:
        entropy_res = compute_entropy_stats_of_dict(token_freq, 2)
    H, H_max, p_dupe,p_dupe_lb, summary_str = entropy_res.values()

    _entropy_ = lambda p: -p*np.log2(p)
    # bar_h = [_entropy_(v)*len(token_freq.values()) for v in token_freq.values()]
    N = len(token_freq.values())
    g = np.log2(N) 
    bar_h = [_entropy_(v)*g  for v in token_freq.values()]

    ax.bar(token_freq.keys(), bar_h)
    ax.plot([-.5, len(token_freq)-0.5],[g*H/N,g*H/N],'k:')
    ax.plot([-.5, len(token_freq)-0.5],[g*H_max/N,g*H_max/N],'g--',linewidth=1)
    # ax.set_title(summary_str
    # ax.set_title('Entropy$_i$ = $p_i$log$(p_i)$ [bits / symbol]')
    ax.set_title('efficiency$_i \propto$ $p_i$log$(p_i)$')
    return ax

    
#%%
# Data parsing functions 
# TODO: separate to their own file
def extract_circuit_signature_single_df(df):
    sort_order = ['kS','iA','jB']
    iAs = df.sort_values(sort_order).groupby('kS').agg({'iA':list})
    jBs = df.sort_values(sort_order).groupby('kS').agg({'jB':list})
    #tuples of (i,j) associated with each link
    ij_fingerprint = list(zip(iAs.loc[0].item(),jBs.loc[0].item()))
    #TODO: check this ordering is consistent across kS
    
    fingerprint_str = df.sort_values(sort_order).groupby('kS').agg({'type':' '.join})
    # Convert df to dictionary
    # - keys are kS 
    # - values are strings representing 
    fingerprint_dict = fingerprint_str.T.to_dict('index')['type']
    
    return {'fingerprint_dict':fingerprint_dict,'fingerprint_idx':ij_fingerprint}
        
#%%
# DEMO SCRIPT
if __name__ == '__main__':
    import pandas as pd
    import matplotlib.pyplot as plt
    # data = [*['A']*10, 'B','B','C','D','e','f','g','h']
    # data = [*['A']*8,'B','B','C','D']
    # data = [*['A']*2,'B','B','C','D']
    
    data = [*['A']*80,*['B']*5,*['C']*5,*['D']*5,*['E']*5]
    # data = [*['A']*40,*['B']*35,*['C']*20,*['D']*5]
    # data = [*['A']*500,*['B']*250,*['C']*125,*['D']*125]
    # data = [*['A']*127,*['B']*64,*['C']*64,*['D']*1]
    # data = [*['A→B']*127,*['A←B']*64,*['A↔B']*64,*['A.B']*1]
    # data = [0,0,1,2]
    # data = [*['A']*13,'B','C','D']
    
    # pA = 32
    # _n = (158-pA)//3
    # data = [*['A']*pA,*['B']*_n,*['C']*_n,*['D']*_n] #has 1bit of info
    
    # data = [*['A']*80,*['B']*10,*['C']*10] 

    # T = 256
    # na = 100
    # data = [*['A']*na,*['B']*(T-na)]
    len(data)
# data = [*[0]*7,1]
    
    tf = count_unique_frequency(data, do_normalize=True)
    ts = component_entropy_of_dict(tf)
    print(f'token frequencies:')
    print(format_dict_fstr(tf))

    # print(f'token suprise / encoding costs:')
    # print(format_dict_fstr(ts))
    entr_base = 2
    # how many rounds of 20 questions will it take to identify your answer? H < Q < H+1 < #max
    H = entropy_of_dict(tf, entr_base)
    H_max = max_entropy_of_dict(tf, entr_base)
    print(f'  H / H_max = {H:.4f} / {H_max:.2f} = {100*H/H_max:.2f}% efficiency')
    
    #how many equivalent equal categories are present
    print(f'    #states = {2**H:.1f} / {len(tf.keys())} max')

    #%%

    #%%
    # Basic summary plot
    fig,ax = plt.subplots(figsize=(5,6))
    res = compute_and_plot_count_entropy(data, ax)
    fig 
    
    #%%
    import time
    
    # emprirically draw pairs and check how many are equal
    
    n_samp = int(1e5)
    tic = time.perf_counter()
    A = random.choices(data,k=n_samp)
    B = random.choices(data,k=n_samp)
    n_dupe = sum(1 for a,b in zip(A,B) if a==b)
    toc = time.perf_counter()
    t1 = toc-tic
    
    # # # sample WITHOUT replacement...
    # tic = time.perf_counter()
    # AB = [random.sample(data,2) for i in range(n_samp)] 
    # n_dupe_no = sum(1 for a,b in AB if a==b)
    # toc = time.perf_counter()
    # t2 = toc-tic
    # #% %
    
    print(f't: {t1:.3f} sec')
    # print(t2)
    empr_p_dupe = n_dupe/n_samp
    
    #%%
    print(f"lowr bnd: {100*res['_entropy_res']['p_dupe_lb']:.1f}%")
    print(f"analytic: {100*compute_prob_dupe_from_freq(tf):.1f}%")
    print(f"    empr: {100*empr_p_dupe:.1f}%")
    # print(f"empr. w/o rep: {n_dupe_no/n_samp:.3f}")
    assert(res['_entropy_res']['p_dupe_lb'] <= compute_prob_dupe_from_freq(tf))
    
    #%% 
    # Additional, debug / extra-insight plots
    fig,ax = plt.subplots(1,2, figsize=(9,6))
    weighted_surprise_plot(res['token_frequencies'], ax[0])
    component_efficiency_plot(res['token_frequencies'], ax[1])
    #%%
    
    '''
    TEST: extract the circuit signature under a given open-loop intervention (kS)
    - while this snippet is a good test run
        - need to be able to aggregate across multiple hypotheses
        - so likely will need to construct a large multi-circuit df first, then extract
    - alt. could use some method which appends dictionary values
    '''
    df = pd.read_csv('results/demo_fingerprint.csv')
    fp = extract_circuit_signature_single_df(df)
    print(fp['fingerprint_dict'])

    

    #%%
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #%%

