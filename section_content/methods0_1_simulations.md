> scope markers:
> - ✅ - currently in scope 
> - 💫 - want to be in scope, have a head-start
> - 🚀  - want to be in scope, would require substantial work
> - 🙈 - not intended to be in scope, future work


---
## Network simulations

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

## Network simulations - outline
> <a name='figure-gaussian'></a>
> ![](/figures/misc_figure_sketches/gaussian_vs_spiking_network_eg.png)
> <details><summary>see also</summary>
> 
> ![](/figures/whiteboard/signal_aggregation.jpeg)
> </details>
> ### Figure GAUSSIAN: Gaussian and spiking networks simulated in Brian2
> 🥡 **takeaway:** ??? 🚧
> 
> - all networks built on [Brian2](https://elifesciences.org/articles/47314) spiking neural network simulator 
> - (delayed) linear-gaussian network 
>   - required custom functionality to implement 
>     - [[brian_delayed_gaussian] repository ](https://github.com/awillats/brian_delayed_gaussian)
>     - allows us to understand impact of variability in simplest setting
> - spiking network 
>   - introduces additional difficulties associated with estimation based on spiking observations, nonlinearities
> 
> [^intv_type2]: see [causal_vs_expt.md](sketches_and_notation/intro-background/causal_vs_expt.md)


