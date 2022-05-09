
## Implementing interventions
<!-- !!!! - 70% done -->
<!-- NOTE: assumed: effect of interventions on theory already addresses (some things) -->
<!-- NOTE: consider changing sigma_m to something else, for case where membrane voltages are not concrete simulated... in Gaussian case, output is like a pseudo-voltage -->

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

for the case of leaky integrate and fire neurons:
The variance of this noise is specified by $\sigma_m \sqrt{\tau_m}$.[^eq_index]
\[
\frac{dV}{dt} = \frac{V_0 + I - V}{\tau_m} + \sigma_m \sqrt{\tau_m} \xi(t)
\]

To emulate **open-loop intervention** we simulated current injection from an external source. This is intended to represent experiments involving stimulation from microelectrodes or optogenetics *(albeit simplifying away any impact of actuator dynamics)*. By default, open-loop intervention is specified as white noise sampled at each timestep from a Gaussian distribution with mean and variance $\mu_{intv.}$ and $\sigma^2_{intv.}$[^res_cont_dyn]

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
In practice, near-ideal control is only possible with very fast measurement and computation relative to the network's intrinsic dynamics, such as in the case of dynamic clamp[^dynamic_clamp]. To demonstrate a broader class of closed-loop interventions (such as those achievable with extracellular recording and stimulation), imperfect "partial" control is simulated by linearly interpolating the output of each node between the target $T$ and the uncontrolled output based on a control effectiveness parameter $\gamma$

\[
X | CL_{k, \gamma} = \gamma T + (1-\gamma) X
\]

<details><summary>↪out of scope: full-loop discrete-time simulation
</summary>

In the full discrete-time simulation, closed-loop interventions are instead simulated through a proportional-integral-derivative (PID) control policy with control efficacy determined functionally by the strength of controller gains $K = \{k_P, k_I, k_D\}$ relative to the dynamics of the network.

\[I_{PID} = \text{PID}(X,T| K)\]

Another interesting intervention to study is **open-loop replay of a closed-loop stimulus**, *that is* taking a particular injected current $I_{CL,\,prev}$ used to drive nodes to a target $T_{prev}$ and adding it back to the network in a separate trial.

Because the instantiation of noise in the network will be different from trial to trial, this "replay" stimulus will no longer adapt sample-by-sample (therefore it should be considered open-loop) and the node's output cannot be expected to match the target precisely, however the statistics of externally applied inputs will be the same. In effect, the comparison between closed-loop and open-loop replay conditions reveals the specific effect of feedback intervention while controlling for any confounds from input statistics.


</details>


[^dynamic_clamp]: NEED dynamic clamp refs - http://www.scholarpedia.org/article/Dynamic_clamp
[^res_cont_dyn]: need to resolve differences in implementation between contemporaneous and voltage simulation cases
