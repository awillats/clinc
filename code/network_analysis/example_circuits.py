import numpy as np
import networkx as nx
import network_data_functions as netdata
import pickle
'''
write case studies for exampination as a function returning multiple candidate hypotheses

---
TODO 
- [ ] import "generate all N-node circuits" functions
'''

#%%
#single N-node circuit
# N = 10
# p = 0.8*N/N**2
# G = nx.fast_gnp_random_graph(N,p, directed=True)

def merge_lists_of_circuits(A, B=None, min_nodes=None):
    '''
    note this set function may lose original ordering
    '''
    if B is None:
        B = A
        
    def hash_np(A):
        return pickle.dumps(A)
    def unhash_np(H):
        return pickle.loads(H)
    unique_circs = set(hash_np(S) for S in A+B)
    
    #DEBUG only

    return [unhash_np(u) for u in unique_circs]
#%%
#NOTE: this now has a dedicated function in network_data_functions
def _all_arrow_str_to_adj(all_arrow_strings, min_nodes=3):
    '''TODO: move to network_data_functions'''
    return [netdata.arrow_str_to_np_adj(g,line_delim=';',min_nodes=min_nodes) for g in all_arrow_strings]

def _are_all_adj_unique(As):
    '''
    TODO: move to network_data_functions
    '''
    return len(As) == len(merge_lists_of_circuits(As))
    
def get_all_3node_motifs():
    '''
    ignores rotations and reflections of these graphs 
    ignores self-connections
        - that should lead to 2^9 = 512 graphs
    https://mathinsight.org/image/three_node_motifs
    could put this motifs on the x-ticks with this approach:
    https://stackoverflow.com/questions/8733558/how-can-i-make-the-xtick-labels-of-a-plot-be-simple-drawings-using-matplotlib
    '''
    g0 = ''
    g1 = 'A→B'
    g2 = 'A↔B'
    g3 = 'A→B,C'
    
    g4 = 'A←B,C'
    g5 = 'C→A→B'
    g6 = 'C→A↔B'
    g7 = 'C←A↔B'
    
    g8 = 'C↔A↔B'
    g9 = 'C←A→B←C'   
    g10 = 'C→A→B→C' 
    g11 = 'C→A,B; A↔B'
    
    g12 = 'A↔B; A→C→B'
    g13 = 'A↔B; A,B→C'
    g14 = 'C↔A↔B←C'
    g15 = 'C↔A↔B↔C'
    gs_circs = [g0,g1,g2,g3, g4,g5,g6,g7, g8,g9,g10,g11, g12,g13,g14,g15]
    return _all_arrow_str_to_adj(gs_circs,min_nodes=3)
    
def get_walkthrough_trio():
    g0 = 'A→B←C→A' #C-A-B triangle
    g1 = 'A↔B←C'
    g2 = 'A↔B←C→A'
    gs_circs = [g0,g1,g2]
    return netdata.all_arrow_str_to_np_adj(gs_circs, min_nodes=3)

def get_hypothesis_fig_set():
    '''
    should be same as get_chainlike_3node (but reverse order)
    '''
    g0 = 'A↔B↔C↔A'    # all-to-all
    g1 = 'A→B,C; C→B' # A-C-B triangle
    g2 = 'A→B,C'      # fork
    g3 = 'C→A→B; C→B' # C-A-B triangle
    g4 = 'C→A→B'      # chain
    g5 = 'B,C→A'      # collider
    gs_circs = [g0,g1,g2,g3,g4,g5]
    return _all_arrow_str_to_adj(gs_circs)
 
def get_large_hypothesis_set():
    g0 = 'A↔B←C'
    g1 = 'A↔B←C→A'
    
    g2 = 'A↔B↔C↔A'    # all-to-all
    g3 = 'A→B,C; C→B' # A-C-B triangle
    g4 = 'A→B,C'      # fork
    g5 = 'C→A→B; C→B' # C-A-B triangle
    g6 = 'C→A→B'      # chain
    g7 = 'B,C→A'      # collider
    gs_circs = [g0,g1,g2,g3,g4,g5,g6,g7]
    return _all_arrow_str_to_adj(gs_circs)
 
    
      
#%%
def _get_circuit_size():
    pass
    
def gen_random_circuit_set(N_circ=6, N_nodes=3, p_connect=.1):
    # print(N_circ)
    nx_circs = [nx.fast_gnp_random_graph(N_nodes, p_connect,directed=True) for i in range(N_circ)]    
    # for nxc in nx_circs:
    #     print(nxc.edges())
    #     a = netdata.nx_to_np_adj(nxc,min_nodes=N_nodes) 
    #     if a.shape[0] < N_nodes:
    #         print(nxc)
    return [netdata.nx_to_np_adj(nxc, min_nodes=N_nodes) for nxc in nx_circs]
    # return nx_circs 
    
def gen_random_unique_circuit_set(N_circ=6, N_nodes=3, p_connect=.1, n_tries_max=200):
    '''
    WARNING: uses a while loop, could be (non-deterministically) slow
    '''
    As = []
    N_unique = 0
    n_tries = 0
    
    while (N_unique < N_circ) and (n_tries < n_tries_max):
        A_gen = gen_random_circuit_set(N_circ-N_unique, N_nodes, p_connect)
        # print(f'lens: {len(As)}+{len(A_gen)}')
        As = merge_lists_of_circuits(A=As, B=A_gen, min_nodes=N_nodes)
        # DEBUG: this re-merging should NOT be necessary
        As = merge_lists_of_circuits(A=As,min_nodes=N_nodes)
        
        # print(f'={len(As)}')
        # for a in A_gen:
        #     if a.shape[0] < N_nodes:
        #         print(a)
        
        N_unique = len(As)
        n_tries += 1
        # print(N_unique)
    print(n_tries,'attempts')
    assert(n_tries < n_tries_max) # took too long to generate circuits
    return As

def get_all_2node():
    A0 = np.array([[0,0],[0,0]])
    A1 = np.array([[0,1],[0,0]])
    A2 = np.array([[0,0],[1,0]])
    A3 = np.array([[0,1],[1,0]])
    As = [A0,A1,A2,A3]
    return As

def get_recur_dense_3node():
    '''
    inspired by examples used in prior talks
    - intended to be as similar as possible
    - possibly requiring specifically closed-loop intervention to distinguish 
        - because their reachabilities are equal
    see "How Cortical Circuits Implement Cortical Computations: Mouse Visual Cortex as a Model" for canonical neural circuits
    https://www.annualreviews.org/doi/pdf/10.1146/annurev-neuro-102320-085825
    '''
    # pseudo fork shaped 
    A0 = np.array([[1,0,1],
                   [0,1,1],
                   [0,1,1]])
    #fork shaped - 
    #e.g. [thalamus, Pv-Inh, Exc]              
    A1 = np.array([[1,1,1],
                   [0,1,1],
                   [0,1,1]])
    
    #pseudo collider 
    # e.g. Exc, VIP-Inh, Som-Inh
    A2 = np.array([[1,0,0],
                   [0,1,1],
                   [1,1,1]])
    #collider shaped          
    A3 = np.array([[1,0,0],
                   [1,1,1],
                   [1,1,1]])
    As = [A0,A1,A2,A3]
    return As
def get_pyloric_3node():
    '''
    Successful Reconstruction of a Physiological Circuit with Known Connectivity from Spiking Activity Alone
    
    https://www.researchgate.net/figure/Inferring-network-connectivity-of-the-pyloric-circuit-of-the-crab-stomatogastric-ganglion_fig1_250925489
    '''    
    true = np.array([[0,1,1],
                     [1,0,1],
                     [1,0,0]])
    full = np.array([[0,1,1],
                     [1,0,1],
                     [1,1,1]])




def kumar_fig2_3node():
    A = np.array([[0,1,0],
                  [0,0,1],
                  [0,0,0]])
    B = np.array([[0,1,0],
                 [0,0,1],
                 [0,1,0]])
    "In the toy example with five populations, this requires 52 different stimulation patterns involving 1–5 populations."
    return [A,B]
     
def kumar_fig2_5node():
    GC = nx.DiGraph({'1':['5'],'2':['3'],'3':['2'],'4':['1'],'5':['2','3','4']})
    AC = nx.to_numpy_matrix(GC)
    return AC
     
def get_chainlike_3node():
    '''
    handpicked collection of similar circuits
    '''
    A_ = np.array([[0,0,0],
                   [1,0,0],
                   [1,0,0]])
    
    A0 = np.array([[0,1,0],
                   [0,0,0],
                   [1,0,0]])
    
    A1 = np.array([[0,1,0],
                   [0,0,0],
                   [1,1,0]])
    
    A2 = np.array([[0,1,1],
                   [0,0,0],
                   [0,0,0]])                 
    
    A3 = np.array([[0,1,1],
                   [0,0,0],
                   [0,1,0]])      
    
    A4 = np.array([[0,1,1],
                   [1,0,1],
                   [1,1,0]])                
    As = [A_,A0,A1,A2,A3,A4]
    return As
    
def get_common_3node():
    '''
    "from highly nonrandom features of synaptic connectivity" figure 4
    '''
    #NOTE: same as pattern 3 in gal et al.
    A4 = np.array([[0,1,1],[0,0,0],[0,0,0]])
    
    #NOTE: similar to pattern 4 in gal et al., curto A
    A10 = np.array([[0,1,1],
                   [0,0,1],
                   [0,0,0]])
    A11 = np.array([[0,1,0],
                    [0,0,1],
                    [1,0,0]])
    
    #NOTE: same as 11 in gal et al.                
    A12 = np.array([[0,0,1],
                    [1,0,1],
                    [1,0,0]])
    A13 = np.array([[0,1,1],
                    [0,0,1],
                    [1,0,0]])    
    #NOTE: same as 10 in gal et al.
    A14 = np.array([[0,1,1],
                    [0,0,0],
                    [1,1,0]])
    A15 = np.array([[0,1,1],
                    [1,0,1],
                    [1,0,0]])
    A16 = np.array([[0,1,1],
                    [1,0,1],
                    [1,1,0]])    
    #should probably be a dictionary
    return [A10,A11,A12,A13,A14,A15,A16]
    
def get_curto_overrepresented_3node():
    '''
    see Curto & Morrison which reference other connectomics studies
    Relating network connectivity to dynamics: opportunities and challenges for theoretical neuroscience
    '''    
                
    A = np.array([[0,1,1],
                  [0,0,1],
                  [0,0,0]]) #NOTE:'pattern 4 in Gal et al.'
    B = np.array([[0,1,1],
                  [0,0,1],
                  [0,1,0]])
    return [A,B]
    
def get_curto_5node():
    GB = nx.DiGraph({1:[2,4],2:[3],3:[4,5],4:[5],5:[1,2]})
    GC = nx.DiGraph({1:[2,4],2:[5],3:[2],4:[5,3],5:[1,3]})
    GD = nx.DiGraph({1:[2,4],2:[5],3:[2,4],4:[5],5:[1,3]})
    GE = nx.DiGraph({1:[4,5],2:[5],3:[2,4],4:[3],5:[1,2]})
    return [nx.to_numpy_matrix(G) for G in [GB,GC,GD,GE]]

def get_nonrandom_3node():
    '''
    "from highly nonrandom features of synaptic connectivity" figure 4
    1-10 without 4,8
    '''
    A1 = np.array([[0,0,0],
                   [0,0,0],
                   [0,0,0]])
    A2 = np.array([[0,0,0],
                    [0,0,0],
                    [1,0,0]])
    A3 = np.array([[0,0,1],
                    [0,0,0],
                    [1,0,0]])
    A5 = np.array([[0,0,0],
                    [1,0,0],
                    [1,0,0]])    
    A6 = np.array([[0,0,1],
                    [1,0,0],
                    [0,0,0]])
    A7 = np.array([[0,0,1],
                    [1,0,0],
                    [1,0,0]])
    A9 = np.array([[0,1,1],
                    [1,0,0],
                    [1,0,0]]) 
    return [A1,A2,A3,A5,A6,A7,A9]

#%%

if __name__ == "__main__":
    import numpy as np
    import network_plotting_functions as netplot
    import matplotlib.pyplot as plt
    import plotting_functions as myplot
    import _svg_draw as svg
    # import netgraph
    # import pyviz
    # netv = pyvis.network.Network(notebook=True)
    
    
    M = get_all_3node_motifs()
    assert(_are_all_adj_unique(M))
    Gs = [nx.DiGraph(m) for m in M]
    
    fig,ax = myplot.subplots(4,4)
    pos = netplot.clockwise_circular_layout(initial_rot=np.pi/6, do_relabel_abc=False)
    
    draw_opts = {'connectionstyle':'arc3,rad=0','node_size':300,'node_color':'k'}
    draw_opts.update({'pos':pos})
    
    
    do_save_plots = True
    
    for i in range(4):
        for j in range(4):
            k = i*4 + j
            
            # netplot.draw_np_adj(M[k],ax[i][j],more_options=draw_opts)
            this_png_name = f'motif_data/motif{k}.png' if do_save_plots else None
            _,svgg = svg.nx_to_svg_img(Gs[k],node_size=8,do_label=False,
                arrow_head_width=20,
                arrow_width=6,
                arrow_displace_ratio = 0.7,
                node_face_color='black',pos=pos,
                border_padding=0,
                save_png_file=this_png_name
                )
                
            myplot.imshow_png(ax[i][j],svgg,do_unbox=True)
            ax[i][j].text(0,0,f'{k+1}',ha='center')

    myplot.expand_bounds(ax[0][0])
    # myplot.savefig('3node_motifs.png')
    fig
    
    