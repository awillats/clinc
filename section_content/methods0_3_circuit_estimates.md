
## Extracting circuit estimates 
!!!! - 10% done

<a name='figure-pipeline'></a>
![](/figures/misc_figure_sketches/network_estimation_pipeline_sketch.png)

<details><summary>↪outline</summary>

> be sure to reference / not reinvent
section: **Inferring causal interactions from time series.**  in [background_causal_network_id.md](background_causal_network_id.md)

### Outputs of network 
<!-- - spikes from populations of neurons  -->

### What is cross-correlation
<details><summary> see also </summary>

![](/figures/whiteboard/methods_xcorr_features.jpeg)
![](/figures/whiteboard/methods_circuit_xcorr_sketch.png)
![](/figures/core_figure_sketches/figure4a_sketch.png)
![](/figures/misc_figure_sketches/data_xcorr_gaussian.png)
</details>

### Figure PIPELINE: Process of detecting connections in a network model

</details>

<details><summary>↪longer outline</summary>

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

</details>
