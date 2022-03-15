
## Extracting circuit estimates 
!!!! - 10% done
<!-- ![](/figures/core_figure_sketches/methods_overview_pipeline_sketch.png) -->
> *refer to methods overview figure*

[^inf_techniques]: *inference techniques mentioned in the intro...*
[^corr_prototype]: what does "prototype" mean here? something like MI and corr are equivalent in the linear-Gaussian case, ...
[^corr_hyperparameter]: not sure how important this is. would prefer to set this threshold at some ad-hoc value since we're sweeping other properties. But a more in-depth analysis could look at a receiver-operator curve with respect to this threshold

While a broad range of techniques[^inf_techniques] exist for inferring functional relationships from observational data, `(for the majority of this work)` we choose to focus on simple bivariate correlation as a measure of dependence in the linear-Gaussian network. The impact of intervention on this metric is analytically tractable *(see [methods1_predicting_correlation.md](methods1_predicting_correlation.md))*, and can be thought of as a prototype[^corr_prototype] for more sophisticated measures of dependence such as time-lagged cross-correlations, bivariate and multivariate transfer entropy.


We implement a naive comparison strategy to estimate the circuit adjacency from emprical correlations; Thresholded empirical correlation matrices are compared to correlation matrices predicted from each circuit in a hypothesis set. Any hypothesized cirucits which are predicted to have a similar correlation structure as is observed (i.e. corr. mats equal after thresholding) are marked as "plausible circuits."[^circuit_search] If only one circuit amongst the hypothesis set is a plausible match, this is considered to be the estimated circuit. The threshold for "binarizing" the empirical correlation matrix is treated as a hyperparameter to be swept at the time of analysis.[^corr_hyperparameter]

[^circuit_search]: TODO? formalize notation for this