## Modeling network structure and dynamics
We sought to understand both general principles (abstracted across particulars of network implementation) as well as some practical considerations introduced by dealing with spikes and synapses.

!!!! - 70% done


### Stochastic network dynamics

The first approach is accomplished with a network of nodes with gaussian noise sources, linear interactions, and linear dynamics. The second approach is achieved with a network of nodes consisting of populations of leaky integrate-and-fire (LIF) neurons. These differ from the simpler case in their nonlinear-outputs, arising from inclusion of a spiking threshold. Interactions between neurons happen through spiking synapses, meaning information is passed between neurons sparsely in time[^fr]. 

*Neuron dynamics:*
\[
\frac{dV}{dt} = \frac{V_0 + I - V}{\tau_m} + \sigma_m \sqrt{\tau_m} \xi(t)
\]


[^fr]: However, depending on overall firing rates and population sizes, this sparse spike-based transmission can be coarse-grained to a firing-rate-based model.

### Time-resolvable interactions

Additionally we study two domains of interactions between populations; contemporaneous and delay-resolvable connections. These domains represent the relative timescales of measurement versus timescale of synaptic delay.
[^cases]
[^cases]: cases doesnt work with pandoc yet, also want to talk about positive and negative lags here
<!-- \[
==DANGER cases doesnt work with pandoc==
\text{domain} = 
\begin{cases}
\text{contemporaneous}, &\delta_{syn} \lt \Delta_{sample}\\
\text{delay-resolvable}, &\delta_{syn} \geq \Delta_{sample}\\
\end{cases}
\] -->
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

