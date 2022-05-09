
<!-- ## Extracting circuit estimates  -->

<!-- ![](/figures/core_figure_sketches/methods_overview_pipeline_sketch.png) -->

<!-- NOTE: see also
second half of /section_content/methods_entropy_selection.md which talks about 
convergence criteria for choosing a circuit hypothesis
-->
<!-- NOTE: we're leaving a lot of information on the table with this simple approach
- PC algorithm can help us infer direction, even with /just/ correlation
- reachability X changes in correlation can help us infer direction!

-->

<!-- [^inf_techniques]: TODO: restate inference techniques mentioned in the intro... -->

<!-- [^corr_prototype]: what does "prototype" mean here? something like MI and corr are equivalent in the linear Gaussian case, ... -->

<!-- [^circuit_search]: TODO: formalize notation for plausible circuits -->

<!-- TODO: refer to Fig. OVERVIEW, estimate -->

While a broad range of techniques[^inf_techniques] exist for inferring functional relationships from observational data, for this investigation we choose to focus on simple bivariate correlation as a measure of dependence in the linear Gaussian network. The impact of intervention on this metric is analytically tractable *(see Methods [# predicting correlation](#sec:methods-predict-corr))*, and can be thought of as a prototype for more sophisticated measures of dependence such as time-lagged cross-correlations, bivariate and multivariate transfer entropy.

We implement a naive comparison strategy to estimate the circuit adjacency from empirical correlations; Thresholded empirical correlation matrices are compared to correlation matrices predicted from each circuit in a hypothesis set. Any hypothesized circuits which are predicted to have a similar correlation structure as is observed (i.e. correlation matrices equal after thresholding) are marked as "plausible circuits." If only one circuit amongst the hypothesis set is a plausible match, this is considered to be the estimated circuit. The threshold for "binarizing" the empirical correlation matrix is treated as a hyperparameter to be swept at the time of analysis.


<!-- [^corr_hyperparameter]: not sure how important this is. would prefer to set this threshold at some ad-hoc value since we're sweeping other properties. But a more in-depth analysis could look at a receiver-operator curve with respect to this threshold -->

