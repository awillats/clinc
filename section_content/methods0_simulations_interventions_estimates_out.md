<!-- PANDOC ERROR HERE - thinks its yaml -->
@ import "methods0_0_overview.md"
<!-- PANDOC ERROR HERE - undefined ctrl sequence -->
<!--imported from "methods0_1_simulations.md" -->
## Modeling network structure and dynamics
!!!! - 70% done
<details><summary>↪to do</summary>

- [~] read e.g.
- [ ] discuss networks - adj ✅
- discuss 2 key dimensions of complexity
  - linear-gaussian v.s. spiking (LIF - Poisson?) 💫
  - contemporaneous v.s. delayed connections 💫
- [ ] discuss brian implementation (supplement) 💫

</details>


We sought to understand both general principles (abstracted across particulars of network implementation) as well as some practical considerations introduced by dealing with spikes and synapses.

### Stochastic network dynamics

The first approach is accomplished with a network of nodes with gaussian noise sources, linear interactions, and linear dynamics. The second approach is achieved with a network of nodes consisting of populations of leaky integrate-and-fire (LIF) neurons. These differ from the simpler case in their nonlinear-outputs, arising from inclusion of a spiking threshold. Interactions between neurons happen through spiking synapses, meaning information is passed between neurons sparsely in time[^fr]. 

*Neuron dynamics:*
\[
\frac{dV}{dt} = \frac{V_0 + I - V}{\tau_m} + \sigma_m \sqrt{\tau_m} \xi(t)
\]


[^fr]: However, depending on overall firing rates and population sizes, this sparse spike-based transmission can be coarse-grained to a firing-rate-based model.

### Time-resolvable interactions

Additionally we study two domains of interactions between populations; contemporaneous and delay-resolvable connections. These domains represent the relative timescales of measurement versus timescale of synaptic delay.

==DANGER doesnt work with pandoc==
<!-- \[
\text{domain} = 
\begin{cases}
\text{contemporaneous}, &\delta_{syn} \lt \Delta_{sample}\\
\text{delay-resolvable}, &\delta_{syn} \geq \Delta_{sample}\\
\end{cases}
\] -->

>correlation across positive and negative lags between two outputs 

In the delay-resolvable domain, directionality of connections may be inferred even under passive observations by looking at temporal precedence - whether the past of one signal is more strongly correlated with future lags of another signal *(i.e. cross-correlation)*. In the contemporaneous domain, network influences act within the time of a single sample[^contemp_sample] so this temporal precedence clue is lost (although directionality can still be inferred in the presence of intervention).

The following work is presented with the linear-Gaussian and contemporaneous domains as the default for simplicity and conciseness. 

!!!! - talk about the extension to time-resolvable, spiking if it ends up being included

[^contemp_sample]: the effective $\Delta_{sample}$ would be broadened in the presence of jitter in connection delay, measurement noise, or temporal smoothing applied post-hoc, leading

<details><summary>↪concept figures</summary>

![](figures/whiteboard/concept_time_resolved.png)
![](figures/whiteboard/concept_open_loop_contemporaneous.png)

</details>

### Code implementation
Software for data generation, analysis, and plotting is available at https://github.com/awillats/clinc.
Both linear-gaussian and spiking networks are simulated with code built from the [Brian2](https://elifesciences.org/articles/47314) spiking neural network simulator. This allows for highly modular code with easily interchanged neuron models and standardized output preprocessing and plotting. It was necessary to write an additional custom extension to Brian2 in order to capture delayed linear-gaussian interactions, available at [brian_delayed_gaussian](https://github.com/awillats/brian_delayed_gaussian). With this added functionality, it is possible to compare the equivalent network parameters only changing linear-gaussian versus spiking dynamics and inspect differences solely due to spiking.
<!-- - introduces additional difficulties associated with estimation based on spiking observations, nonlinearities -->

!!!! - talk about parameter choices and ranges?

*see [_network_parameters_table.md](_network_parameters_table.md) for list of relevant parameters*


<!-- end of import from "methods0_1_simulations.md" -->
<!-- works! -->
<!--imported from "methods0_2_interventions.md"-->

## Implementing interventions
!!!! - 70% done
!!!! - assumed: effect of interventions on theory already address

![](figures/core_figure_sketches/figure1_sketch.png)

To study the effect of various interventions we simulated inputs to nodes in a network. In the **passive setting**, nodes receive additive drive from *private* Gaussian noise sources common to all neurons within a node, but independent across nodes. The variance of this noise is specified by $\sigma_m \sqrt{\tau_m}$.[^eq_index]

\[
\frac{dV}{dt} = \frac{V_0 + I - V}{\tau_m} + \sigma_m \sqrt{\tau_m} \xi(t)
\]

To emulate **open-loop intervention** we simulated current injection from an external source. This is intended to represent experiments involving stimulation from microelectrodes or optogenetics *(albeit simplifying away any impact of actuator dynamics)*. By default, open-loop intervention is specified as white noise sampled at each timestep from Gaussian distribution with mean and variance $\mu_{intv.}$ and $\sigma^2_{intv.}$[^res_cont_dyn]

\[
I_{open-loop} \sim \mathcal{N}(\mu_{intv.},\,\sigma^{2}_{intv.})\\
\]
Ignoring the effect of signal means in the linear-Gaussian setting:
\[
X_k = f(\sigma^2_m, \sigma^{2}_{intv.})
\]
`per-node indexing needs resolving here also`

Ideal **closed-loop control** is able to overwrite the output of a node, setting it precisely to the specified target. 
`making up notation as I go here, needs tightening up:`
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

In the full discrete-time simulation, closed-loop interventions are instead simulated through a proportional-integral-derivative (PID) control policy with control efficacy determined functionally by the strength of controller gains $K = \{k_P, k_I, k_D\}$ relative to the dynamics of the network.

\[I_{PID} = \text{PID}(X,T| K)\]

Another interesting intervention to study is **open-loop replay of a closed-loop stimulus**, *that is* taking a particular injected current $I_{CL,\,prev}$ used to drive nodes to a target $T_{prev}$ and adding it back to the network in a separate trial.

Because the instantiation of noise in the network will be different from trial to trial, this "replay" stimulus will no longer adapt sample-by-sample (therefore it should be considered open-loop) and the node's output cannot be expected to match the target precisely, however the statistics of externally applied inputs will be the same. In effect, the comparison between closed-loop and open-loop replay conditions reveals the specific effect of feedback intervention while controlling for any confounds from input statistics.


[^dynamic_clamp]: NEED dynamic clamp refs - http://www.scholarpedia.org/article/Dynamic_clamp
[^res_cont_dyn]: need to resolve differences in implementation between contemporaneous and voltage simulation cases
[^eq_index]: need to triple check indexing w.r.t. nodes, neurons

<!-- end of import from "methods0_2_interventions.md" -->
<!-- works! -->
<!--imported from "methods0_3_circuit_estimates.md"-->

## Extracting circuit estimates 
!!!! - 10% done
<!-- ![](figures/core_figure_sketches/methods_overview_pipeline_sketch.png) -->
> *refer to methods overview figure*

[^inf_techniques]: *inference techniques mentioned in the intro...*
[^corr_prototype]: what does "prototype" mean here? something like MI and corr are equivalent in the linear-Gaussian case, ...
[^corr_hyperparameter]: not sure how important this is. would prefer to set this threshold at some ad-hoc value since we're sweeping other properties. But a more in-depth analysis could look at a receiver-operator curve with respect to this threshold

While a broad range of techniques[^inf_techniques] exist for inferring functional relationships from observational data, `(for the majority of this work)` we choose to focus on simple bivariate correlation as a measure of dependence in the linear-Gaussian network. The impact of intervention on this metric is analytically tractable *(see [methods1_predicting_correlation.md](methods1_predicting_correlation.md))*, and can be thought of as a prototype[^corr_prototype] for more sophisticated measures of dependence such as time-lagged cross-correlations, bivariate and multivariate transfer entropy.


We implement a naive comparison strategy to estimate the circuit adjacency from emprical correlations; Thresholded empirical correlation matrices are compared to correlation matrices predicted from each circuit in a hypothesis set. Any hypothesized cirucits which are predicted to have a similar correlation structure as is observed (i.e. corr. mats equal after thresholding) are marked as "plausible circuits."[^circuit_search] If only one circuit amongst the hypothesis set is a plausible match, this is considered to be the estimated circuit. The threshold for "binarizing" the empirical correlation matrix is treated as a hyperparameter to be swept at the time of analysis.[^corr_hyperparameter]

[^circuit_search]: TODO? formalize notation for this
<!-- end of import from "methods0_3_circuit_estimates.md" -->
