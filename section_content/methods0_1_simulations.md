## Modeling network structure and dynamics
!!!! - 60% done
<details><summary>↪to do</summary>

- [~] read e.g.
- [ ] discuss networks - adj ✅
- discuss 2 key dimensions of complexity
  - linear-gaussian v.s. spiking (LIF - Poisson?) 💫
  - contemporaneous v.s. delayed connections 💫
- [ ] discuss brian implementation (supplement) 💫

</details>


We sought to understand both general principles (abstracted across particulars of network implementation) as well as *some* practical considerations introduced by dealing with spikes and synapses.

### Stochastic network dynamics
> - 1. linear-gaussian v.s. spiking/rate 💫

The first approach is accomplished with a network of nodes with gaussian noise sources, linear interactions, and linear dynamics. The second approach is achieved with a network of nodes consisting of populations of leaky integrate-and-fire (LIF) neurons. These differ from the simpler case in their nonlinear-outputs, arising from inclusion of a spiking threshold. Interactions between neurons happen through spiking synapses, meaning information is passed between neurons sparsely in time[^fr]. 

Neuron dynamics:
\[
\frac{dV}{dt} = \frac{V_0 + I - V}{\tau_m} + \sigma_m \sqrt{\tau_m} \xi(t)
\]


[^fr]: However, depending on overall firing rates and population sizes, this sparse spike-based transmission can be coarse-grained to a firing-rate-based model.

> - 2. contemporaneous vs lagged 💫
Additionally we study two domains of interactions between populations; contemporaneous and delay-resolvable connections. These domains represent the relative timescales of measurement versus timescale of synaptic delay.

\[
\text{domain} = 
\begin{cases}
\text{contemporaneous}, &\delta_{syn} \lt \Delta_{sample}\\
\text{delay-resolvable}, &\delta_{syn} \geq \Delta_{sample}\\
\end{cases}
\]

>correlation across positive and negative lags between two outputs 

In the delay-resolvable domain, directionality of connections may be inferred even under passive observations by looking at temporal precedence - whether the past of one signal is more strongly correlated with future lags of another signal *(i.e. cross-correlation)*. In the contemporaneous domain, network influences act within the time of a single sample[^contemp_sample] so this temporal precedence clue is lost (although directionality can still be inferred in the presence of intervention).
<details><summary>↪concept figures</summary>

![](/figures/whiteboard/concept_time_resolved.png)
![](/figures/whiteboard/concept_open_loop_contemporaneous.png)

</details>


[^contemp_sample]: the effective $\Delta_{sample}$ would be broadened in the presence of jitter in connection delay, measurement noise, or temporal smoothing applied post-hoc, leading

> - in the linear gaussian case we focus on "contemporaneous" domain, for simplicity, then extend to the connections-with-delay case

### Code implementation
Code is available at https://github.com/awillats/clinc.
Both linear-gaussian and spiking networks are simulated with code built from the [Brian2](https://elifesciences.org/articles/47314) spiking neural network simulator. This allows for highly modular code with easily interchanged neuron models and standardized output preprocessing and plotting. It was necessary to write an additional custom extension to Brian2 in order to capture delayed linear-gaussian interactions, available at [brian_delayed_gaussian](https://github.com/awillats/brian_delayed_gaussian). With this added functionality, it is possible to compare the equivalent network parameters only changing linear-gaussian versus spiking dynamics and inspect differences solely due to spiking.
<!-- - introduces additional difficulties associated with estimation based on spiking observations, nonlinearities -->

*see [_network_parameters_table.md](_network_parameters_table.md) for list of relevant parameters*

----

<details><summary>↪outline</summary>

![](/code/network_analysis/_demo_imgs/gaussian_snr_prediction_demo.png)

- contemporaneous vs lagged 💫
![](/figures/whiteboard/time_unrolled_representation.png)
<details><summary>see also</summary>

![](/figures/whiteboard/concept_open_loop_contemporaneous.png)
![](/figures/whiteboard/concept_time_resolved.png)
</details>


- linear-gaussian v.s. spiking/rate 💫

- matrix series / matrix exponential


- parameter specification 💫
  - :rocket: heterogeneity
</details>

<details><summary>↪longer outline</summary>

<a name='figure-gaussian'></a>
![](/figures/misc_figure_sketches/gaussian_vs_spiking_network_eg.png)
<details><summary>see also</summary>

![](/figures/whiteboard/signal_aggregation.jpeg)
</details>
### Figure GAUSSIAN: Gaussian and spiking networks simulated in Brian2
🥡 **takeaway:** ??? 🚧

- all networks built on [Brian2](https://elifesciences.org/articles/47314) spiking neural network simulator 
- (delayed) linear-gaussian network 
  - required custom functionality to implement 
    - [[brian_delayed_gaussian] repository ](https://github.com/awillats/brian_delayed_gaussian)
    - allows us to understand impact of variability in simplest setting
- spiking network 
  - introduces additional difficulties associated with estimation based on spiking observations, nonlinearities

[^intv_type2]: see [causal_vs_expt.md](sketches_and_notation/intro-background/causal_vs_expt.md)


</details>



<details><summary>see also</summary>

> - graph → connections: 0. adjacency represents between-population synapses

### key parameters
- parameter specification 💫 (supplement?)
  - :rocket: heterogeneity
    
![](/figures/whiteboard/time_unrolled_representation.png)
![](/figures/whiteboard/concept_time_resolved.png)
![](/figures/whiteboard/concept_open_loop_contemporaneous.png)
</details>