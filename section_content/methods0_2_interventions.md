> scope markers:
> - ✅ - currently in scope 
> - 💫 - want to be in scope, have a head-start
> - 🚀  - want to be in scope, would require substantial work
> - 🙈 - not intended to be in scope, future work

> be sure to reference / not reinvent [background_intervention_causal_inf.md](background_intervention_causal_inf.md)

## Implementing interventions
### passive
- baseline drive comes from independent, "private", noise sources

### open-loop 
- variance modulated ✅ 
- replay 💫

### closed-loop
- perfect
- emulated partial
- practical PID

<!-- ## Implementing interventions (binary?) -->

- :rocket: stimulus-conditional transfer entropy 

## Implementing interventions (outline)
> - passive observation 
> - open-loop stimulation 
>   - simulated as direct current injection
>   - but uniform across a population 
>   - ( see [Kyle Johnsen's cleosim toolbox](https://cleosim.readthedocs.io/en/latest/index.html) for more detailed simulation of stimulation )
>   - ⚠️ closed-loop replay ? ⚠️ 
> - closed-loop stimulation
>   - approaches for control 
>     - going with "model-free" PID control of output rates
>   - comparison to randomization in traditional experiment design[^intv_type2]
>   - controller stregnth
>     - gain
>     - bandwidth
>   - controller delay
>   
> - additional stimulation factors (open- & closed-loop)
>   <details><summary> ↪️ click to expand </summary>
>   
>   - **stimulus location** 
>     - single-site
>     - multi-site
>     - location relative to features of network
>       - in-degree/out-degree
>       - upstream/downstream of hypothesized connection 
>   - stimulus intensity 
>     - expected mean output rate 
>     - frequency content 
>     </details>
>     
>     
> ![](/figures/misc_figure_sketches/intervention_timeseries_flat.png)
> 


[^intv_type2]: see [causal_vs_expt.md](sketches_and_notation/intro-background/causal_vs_expt.md)