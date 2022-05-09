<!-- ## Implementing interventions -->

<!-- NOTE: assumed: effect of interventions on theory already addresses (some things) -->

<!-- TODO: probably needs more context setting up indexing 
- what is a node's index 
- ( what is a neuron's index ) 
- ( what is a circuit's index? )
 
- how to index intervention type? 
 
- X as node's state 
- T as target trajectory  
  
- private versus intrinsic variance  
  
-->


To study the effect of various interventions we simulated inputs to nodes in a network. In the **passive setting**, nodes receive additive drive from *private* Gaussian noise sources common to all neurons within a node, but independent across nodes. The variance of this noise is specified by $\sigma_i$.


To emulate **open-loop intervention** we simulated current injection from an external source. This is intended to represent experiments involving stimulation from microelectrodes or optogenetics *(albeit simplifying away any impact of actuator dynamics)*. By default, open-loop intervention is specified as white noise sampled at each timestep from a Gaussian distribution with mean and variance $\mu_{intv.}$ and $\sigma^2_{intv.}$

\[
I_{open-loop} \sim \mathcal{N}(\mu_{intv.},\,\sigma^{2}_{intv.})\\
\]
Ignoring the effect of signal means in the linear Gaussian setting:
\[
X_k = f(\sigma^2_m, \sigma^{2}_{intv.})
\]
`per-node indexing needs resolving here also`

Ideal **closed-loop control** is able to overwrite the output of a node, setting it precisely to the specified target $T$. 
\[
\begin{aligned}
T &\sim \mathcal{N}(\mu_{intv.},\,\sigma^{2}_{intv.}) \\
I_{closed-loop} &= f(X, T)  \\
X_k | CL_{k} &\approx T
\end{aligned}
\]
Note that in this setting, the *output* of a node $X_k$ under closed-loop control is identical to the target, therefore
\[
X_k | CL_{k} = f(\sigma^{2}_{intv.}) \perp \sigma^2_m
\]
In practice, near-ideal control is only possible with very fast measurement and computation relative to the network's intrinsic dynamics, such as in the case of dynamic clamp [@sharp1993dynamic; @prinz2004dynamic]. To demonstrate a broader class of closed-loop interventions (such as those achievable with extracellular recording and stimulation), imperfect "partial" control is simulated by linearly interpolating the output of each node between the target $T$ and the uncontrolled output based on a control effectiveness parameter $\gamma$

\[
X | CL_{k, \gamma} = \gamma T + (1-\gamma) X
\]

<!-- NOTE: see spiking_methods_interventions.md for model-free discrete-time control -->


