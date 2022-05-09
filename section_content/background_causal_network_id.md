<!-- TODO:
- [ ] cut down time-series section 
- [ ] remove or explain remaining notation
 -->
<!-- NOTE: see also /sketches_and_notation/intro-background/__background_causal_inf_th.md -->
<!-- NOTE: prior draft archived at /section_content/spiking_draft/spiking_background_causal_network_id.md -->

Many hypotheses about neural circuits are phrased in terms of causal relationships: "will changes in activity to this region of the brain produce corresponding changes in another region?" Understanding these causal relationships is critical to both scientific understanding and to developing effective therapeutic interventions, which require knowledge of how potential therapies will impact brain activity and patient outcomes.

<!-- TODO: think about condensing and/or moving "Inferring causal interactions from time series" subsection  -->
**Inferring causal interactions from time series.** A number of strategies have been proposed to detect causal relationships between observed variables. Wiener-Granger (or predictive) causality states that a variable $X$ "Granger-causes" $Y$ if $X$ contains information relevant to $Y$ that is not contained in $Y$ itself or any other variable [@wiener1956theory]. This concept has traditionally been operationalized with vector autoregressive models [@granger1969investigating]; the requirement that *all* potentially causative variables be considered makes these notions of dependence susceptible to unobserved confounders [@runge2018causal].

A key methodological differences between approaches for causal inference from time-series is the choice of linear-Gaussian versus nonlinear measures of dependence (e.g. Granger causality @schreiber2000measuring; @barnett2009granger versus transfer entropy @bossomaier2016transfer). Another key difference lies in the choice of what signals to condition on. Bivariate cross-correlation methods look at the correlation of time series collected from pairs of nodes at various lags and detect peaks at negative time lags. Such peaks could indicate the presence of a direct causal relationship -- but they could also stem from indirect causal links or hidden confounders [@dean2016dangers]. In these bivariate correlation methods, it is thus necessary to consider patterns of correlation between many pairs of nodes in order to differentiate between direct, indirect, and confounding relationships [@dean2016dangers]. This distinguishes these strategies from some multivariate methods that "control" for the effects of potential confounders. For example, multivariate conditional transfer entropy approaches use various variable selection schemes which can differentiate between direct interactions, indirect interactions, and common causes, but their results depend on choices such as the binning strategies used to discretize continuous signals, the specific statistical tests used, and the estimator used to compute transfer entropy [@wibral2014directed; @wollstadt2019idtxl].
<!-- see /section_content/spiking_draft/draft_background_causal_time_series.md for extended discussion -->

However, despite their mathematical differences, previous work has found that cross-correlation-based metrics and information-based metrics tend to produce qualitatively similar results, with similar patterns of true and false positives [@garofalo2009evaluation]. In this work, we focus on the simplest approach for discovering interactions from time-series which is to threshold correlations between node outputs. See [# Future Work](REF-SECTION-HERE) for discussion of extending this approach to more sophisticated inference approaches.

<!-- NOTE: section cut
**Inferring causal interactions from time series.** 
cut to /section_content/spiking_draft/spiking_background_causal_timeseries.md-->

<!-- TODO: stuff to bring back  -->
