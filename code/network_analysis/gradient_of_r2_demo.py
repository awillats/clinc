
import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt
import numdifftools as nd

import network_analysis_functions as naf
import scipy.linalg as linalg
#%%
R = np.eye(3,3)
R[1,2]=1.5
R[0,2]=1.5
S_0 = [0.1, 0.1, 0.1]
   
Rw = linalg.expm(R)
print(R) 
print(Rw)
print(naf.correlation_from_reachability(0,2, Rw, S_0))
#%% markdown
'''
$\nabla{r^2} (S)$
'''
# > see grad.md
#%%
r2 = lambda S: naf.correlation_from_reachability(0,2,Rw,S)
gradR2 = nd.Gradient(r2)
#%%
n = 3
S = np.linspace(1e-2,9,n)
for i, s0 in enumerate(S):
    for j,s1 in enumerate(S):
        for k, s2 in enumerate(S):
            # print(s0,s1,s2)
            _grad = gradR2(np.array([s0,s1,s2]))
            gs0, gs1, gs2 = np.array(_grad)
            gs0n, gs1n, gs2n = np.array(_grad)/np.linalg.norm(_grad)
            print(f'{s0:.2f}, {s1:.2f}, {s2:.2f}    {gs0:.2f}, {gs1:.2f}, {gs2:.2f}    {gs0n:.2f}, {gs1n:.2f}, {gs2n:.2f}')
            # print(f'')