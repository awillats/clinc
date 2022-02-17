import numpy as np

def get_all_2node():
    A0 = np.array([[0,0],[0,0]])
    A1 = np.array([[0,1],[0,0]])
    A2 = np.array([[0,0],[1,0]])
    A3 = np.array([[0,1],[1,0]])
    As = [A0,A1,A2,A3]
    
def get_chainlike_3node():
    A_ = np.array([[0,0,0],
                   [1,0,0],
                   [1,0,0]])
    
    A0 = np.array([[0,1,0],
                   [0,0,0],
                   [1,0,0]])
    
    A1 = np.array([[0,1,0],
                   [1,0,0],
                   [1,0,0]])
    
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