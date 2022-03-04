import numpy as np
from numpy.random import default_rng
rng = default_rng()
import network_analysis_functions as net

#%%
# SIMULATION HELPER FUNCTIONS
flat_fn = lambda nt: np.ones(nt)
def gen_poisson(nt, lam=1):
    '''
    scaling up Poisson noise post-hoc doesn't work the same way as for gaussian noise ... 
    '''
    return np.random.poisson(lam, nt)

def gen_gauss(nt,seed=None):
    _rng = default_rng(seed)
    return _rng.standard_normal(nt)
def sample_gauss(t):
    return gen_gauss(1)
    
def g(nt, noise_type='gaussian'):
    '''
    signal generator for gaussian noise
    '''
    gen_fn = {'gaussian':gen_gauss,'poisson':gen_poisson}[noise_type]
    return gen_fn(nt)
    
def gu(nt, signal_type='gaussian'):
    '''
    signal generator for shared input (u)
    '''
    t_fn = lambda nt: np.arange(0,nt)
    t = t_fn(nt)
    
    period = 100 #parameter used to set period of sine, saw-tooth, flip-flop
    extra_noise = 1/5
    signal_fns = {
        'flip-flop': lambda nt: np.mod(np.cumsum(np.random.rand(nt)<1/period),2),
        'gaussian': lambda nt: gen_gauss(nt),
        'saw-tooth': lambda nt: np.mod(t_fn(nt),period)/period,
        'sine': lambda nt: np.sin(t/period),
    }
    # choose the signal generation type
    signal_fn = signal_fns.get(signal_type, g)
    wave = signal_fn(nt)+g(nt)*extra_noise
    
    #standarize the signal to have mean 0, variance 1
    wave = (wave-np.mean(wave))/np.std(wave)
    return wave.T
#%%
def gen_ctrl_fn_from_spec(ctrl):
    if ctrl is None or ctrl['location'] is None:
        return None
    def ctrl_fn(X):
        nt = X.shape[0]
        ef = ctrl['effectiveness']
        ctrl_idx = ctrl['location']
        targ = ctrl['target_fn'](nt)
        X[:,ctrl_idx] = ef*targ + (1-ef)*X[:,ctrl_idx]
        return X
    return ctrl_fn
DEFAULT_CTRL = {'location':0, 'target_fn':gen_gauss,'effectiveness':0.1}
NONE_CTRL = {k:None for k in DEFAULT_CTRL}

#%%
def sim_contemporaneous(nt, W, Rw, S,B,u,ctrl_fn=None):
    '''
    This strategy side-steps having to simulate a dynamical system, 
    network influence happens within a single timestep
    NOTE - influence of control is "hardcoded"
        - that is, the way control affects the flow of correlation is 
        - alt. implementation would be to to sim_contemporaneous
            - but with W instead of W~
            - at each iteration, implementing closed-loop control
            - is this any less heavy handed?
    
    with ctrl_fn applied twice, control effectivness might be skewed?
    '''
    N = Rw.shape[0]
    E = np.random.randn(nt,N)
    
    #Wt_ represents the sum n from 1 to inf of W^n
    # Wt_ =  net.inf_sum_mat(W) - np.eye(W.shape[0])
    # X += X @ Wt_ 
    # Wt_ =  net.inf_sum_mat(W)
    
    X = E @ np.diag(S) + u @ B
    if ctrl_fn: X = ctrl_fn(X)

    #HARDCODED REACHABILITY - DOES NOT HANDLE PARTIAL CONTROL
    # X = X @ Rw 
    # if ctrl_fn: X = ctrl_fn(X)
    
    #only works without cycles! - not convinced this is the "right" way to sim
    Xp = X
    for i in range(1,N):    
        Xp = Xp @ W
        X += Xp
    if ctrl_fn: X = ctrl_fn(X)
    
    return X
    
def sim_discrete_time_dynamics_step(X,W,S,B,u):
    '''
    for ti in range(nt):
        E_t = E[ti,:]
        # print(S @ E_t, '_')
        u_t = u[ti]
        if ctrl:
            Targ_t = ctrl['target_fn'](ti)
        # 
        # print('__')
        # print((X_prev @ W).shape)
        # print(S * E_t)
        # NOTE: relies on assumption that u_t is scalar
        # X_t = X_prev @ W + B*u_t + S * E_t
        X_t = S*E_t
        X_t += X_t @ W + B*u_t 
        
        """
        Control can override state here:
        """
        
        X[ti,:] = X_t
        X_prev = X_t
    '''
    pass

    
def sim_dg(nt, W, S, B,u, ctrl=None, noise_gen=gen_gauss, input_gen=gen_gauss):
    '''
    Simulate  a directed graph
    S - Nx1 vector of noise !standard deviations!
    u - 1xnt vector of stimulus intensities (scalar for now)
    TODO: 
    - enforce dimension checks
    - verify against hardcoded example
    '''
    N = W.shape[0] #number of nodes
    # noise is independent of any input, can be precomputed 
    # E = np.random.randn(nt, N)
    # X = np.zeros((nt,N))
    # X_prev = X[0,:]

    # Wc = net.sever_inputs(W,ctrl['location']) #NOTE: DEBUG ONLY
    Wc = net.__sever_inputs(W,ctrl) #NOTE: DEBUG ONLY

    Rw = net.reachability_weight_w_ctrl(W,ctrl)

    ctrl_fn = gen_ctrl_fn_from_spec(ctrl)

    X = sim_contemporaneous(nt, Wc, Rw, S,B,u, ctrl_fn)
    
    '''
    This strategy treats the system as a discrete-time dynamical system 
    and uses the previous sample's values to compute the current sample 
    - this is slower to compute 
    - to look at the first type of correlation with the second type of data
        - could consider down-sampling/binning
    '''
    
    '''
    for ti in range(nt):
        E_t = E[ti,:]
        # print(S @ E_t, '_')
        u_t = u[ti]
        if ctrl:
            Targ_t = ctrl['target_fn'](ti)
        # 
        # print('__')
        # print((X_prev @ W).shape)
        # print(S * E_t)
        # NOTE: relies on assumption that u_t is scalar
        # X_t = X_prev @ W + B*u_t + S * E_t
        X_t = S*E_t
        X_t += X_t @ W + B*u_t 
        
        """
        Control can override state here:
        """
        
        X[ti,:] = X_t
        X_prev = X_t
    '''
    return X
