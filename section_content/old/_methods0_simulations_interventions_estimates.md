> scope markers:
> - ✅ - currently in scope 
> - 💫 - want to be in scope, have a head-start
> - 🚀  - want to be in scope, would require substantial work
> - 🙈 - not intended to be in scope, future work

---
## Methods overview
>- METHODS SUMMARY (high-level): FIRST, what question are we trying to answer
>   - then OVERVIEW of methods (pipeline summary)
>   - basic components
>   - answer we're looking for
>   - overall approach
>   - key innovative methods
>   - assume readers aren't going to pore over the details

---
![](code/network_analysis/_demo_imgs/gaussian_snr_prediction_demo.png)


---
## Network simulations

- contemporaneous vs lagged 💫
![](figures/whiteboard/time_unrolled_representation.png)
<details><summary>see also</summary>

![](figures/whiteboard/concept_open_loop_contemporaneous.png)
![](figures/whiteboard/concept_time_resolved.png)
</details>


- linear-Gaussian v.s. spiking/rate 💫

- matrix series / matrix exponential


- parameter specification 💫
  - :rocket: heterogeneity

## Network simulations - outline
> <a name='figure-gaussian'></a>
> ![](figures/misc_figure_sketches/gaussian_vs_spiking_network_eg.png)
> <details><summary>see also</summary>
> 
> ![](figures/whiteboard/signal_aggregation.jpeg)
> </details>
> ### Figure GAUSSIAN: Gaussian and spiking networks simulated in Brian2
> 🥡 **takeaway:** ??? 🚧
> 
> - all networks built on [Brian2](https://elifesciences.org/articles/47314) spiking neural network simulator 
> - (delayed) linear-Gaussian network 
>   - required custom functionality to implement 
>     - [[brian_delayed_gaussian] repository ](https://github.com/awillats/brian_delayed_gaussian)
>     - allows us to understand impact of variability in simplest setting
> - spiking network 
>   - introduces additional difficulties associated with estimation based on spiking observations, nonlinearities
> 
> [^intv_type2]: see [causal_vs_expt.md](sketches_and_notation/intro-background/causal_vs_expt.md)


--- 

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
> ![](figures/misc_figure_sketches/intervention_timeseries_flat.png)
> 

---
## Extracting circuit estimates 
<a name='figure-pipeline'></a>
![](figures/misc_figure_sketches/network_estimation_pipeline_sketch.png)

### Outputs of network 
- spikes from populations of neurons 

### What is cross-correlation
<details><summary> see also </summary>

![](figures/whiteboard/methods_xcorr_features.jpeg)
![](figures/whiteboard/methods_circuit_xcorr_sketch.png)
![](_archive/figure4a_sketch.png)
![](figures/misc_figure_sketches/data_xcorr_gaussian.png)
</details>
### Figure PIPELINE: Process of detecting connections in a network model
🥡 **takeaway:** ??? 🚧

## Extracting circuit estimates (outline)
> 
> - map of techniques available for inference
  > - see ["Assessing the Significance of Directed and Multivariate Measures of Linear Dependence Between Time Series"](https://arxiv.org/pdf/2003.03887.pdf), [code](https://github.com/olivercliff/assessing-linear-dependence)[^assess] and [Unifying Pairwise Interactions in Complex Dynamics](https://arxiv.org/abs/2201.11941)
  > - bivariate v.s. multivariate 
  > - conditioning
    > - same signals past 
    > - other signals 
    > - on stimulus
  > - measures of dependence 
    > - correlation
      > - partial correlation (conditioning)
      > - time-lagged cross-correlation
    > - granger causality
    > - mutual information
    > - transfer entropy
>     
> [^assess]: "The measures implemented are: mutual information, conditional mutual information, Granger causality, and conditional Granger causality (each for univariate and multivariate linear-Gaussian processes). For completeness we have also included Pearson correlation and partial correlation for univariate processes (with a potentially multivariate conditional process)."
> 
> ### lagged cross-correlation 
> - connection to / equivalence with Granger Causality (GC)
  > - review of GC in neuro
  > - requisite assumptions
  > - limitations of GC [^GC_problems]
> - xcorr features 
  > - peak-SNR
  > - prominence 
  > - time of peak
> - window of time-lags considered for direct connections
  > - some multiple of expected synaptic delay
> 
> [^GC_problems]: a study of problems encountered in Granger causality analysis from a neuroscience perspective
> 
> ### multivariate transfer entropy (muTE)
> - advantages above usual GC approach
> 
> ### statistical testing 
> - *for muTE, handled by IDTxl*
  > - includes appropriate multiple-comparison testing
> 
> ### Quantifying successful identification
> - binary "classification" metrics
  > - accuracy, F1 score (Wang & Shanechi 2019)
  > - AUC (Pastore)
  > - Jaccard index (Lepage, Ching, and Kramer 2013)
  > - true/false positives, true/false negatives 
> - graded metrics (*not a core focus here*)
  > - distance between identified connection strength and ground-truth
    > - MSE [(Lepperod et al. 2018)](https://www.biorxiv.org/content/10.1101/463760v2)
  > - error in output reconstruction
> - *relevant "negative control" for comparison (?)*
  > - identified connectivity for random network?
  > - some shuffled data-surrogate procedure? [^FC_methods]
> - *relevant "positive control" for comparison (?)*
> 
> [^FC_methods]: "METHODS FOR STUDYING FUNCTIONAL INTERACTIONS AMONG NEURONAL POPULATIONS" - comes with MATLAB code, discusses time and trial shuffling, decomposing information (synergistic, redundant, independent)
> 
