import numpy as np
import networkx as nx
import network_data_functions as netdata
'''
write case studies for exampination as a function returning multiple candidate hypotheses

---
TODO 
- [ ] import "generate all N-node circuits" functions
'''

#single N-node circuit
# N = 10
# p = 0.8*N/N**2
# G = nx.fast_gnp_random_graph(N,p, directed=True)

def gen_random_circuit_set(N_circ=6, N_nodes=3, p_connect=.1):
    nx_circs = [nx.fast_gnp_random_graph(N_nodes, p_connect,directed=True) for i in range(N_circ)]
    return [netdata.nx_to_np_adj(nxc,N_nodes) for nxc in nx_circs]

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