
import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt
import numdifftools as nd

import network_analysis_functions as naf
import scipy.linalg as linalg
#%%
# TODO: check against's matt's non-monotonic common cause circuit example
# TODO: visualize gradient field

A = np.eye(3,3)*0
A[1,2]=0.8
A[0,1]=0.5
S_0 = [0.1, 0.1, 0.1]
   
Rw = linalg.expm(A)
print(A) 
print(Rw)
#%%
# print(naf.correlation_from_reachability(0,2, Rw, S_0))

R2 = naf.correlation_matrix_from_reachability(Rw,S_0)
print('R2 w/o ctrl')
print(R2)
print('--')
ctrl_R2s = naf.correlation_matrix_from_each_control(A, S_0)
[print(f'ctrl {i}  R2: \n',c,'\n') for i,c in enumerate(ctrl_R2s)];

#%% markdown
'''
$\nabla{r^2} (S)$
'''
# > see grad.md
#%%
'''
- seems to break down with reciprocal circuits?
'''
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