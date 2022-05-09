<!-- 
NOTE: 
> **Theme B.** Experiments for circuit inference can be thought of as **narrowing the set of plausible explanations**, refining a hypotheses space[^refine]

[^refine]: see [Advancing functional connectivity](https://www.nature.com/articles/s41593-019-0510-4), fig. 2

TODO: overall, this section needs the single-circuit and multi-circuit hypotheses integrating better.
The figure currently describes the process for a single circuit, which is the simplest to describe. But the body of the text is mostly pointed towards the multi-hypothesis perspective that follows in Figure DISAMBIG

<!-- TODO:
- [ ] combine any of the steps? 
  - i.e. 3+4 ? 5+6?
- [~] callback to overview figure !
-->

</details>

![](/figures/core_figure_sketches/methods_overview_pipeline_sketch.png)

> **Figure OVERVIEW: Components of a circuit identification experiment.**
> The ground-truth or hypothesized circuit can be represented either as a graph depicting connections between nodes or, equivalently, as an adjacency matrix. While the adjacency matrix describes the direct causal relationships, it's useful to understand the net direct and indirect effect of nodes on each other, called reachability. This reachability representation is key for predicting observed correlations, as well as the impact of intervention. The generative model for this network describes how connections and sources of variance contribute to network dynamics, and observed time-series data (either simulated or measured *in vivo*). From these time-series, pairwise dependence can be measured through quantities like correlation coefficients. Alternately, in the design phase, correlations can be predicted directly from the intervention-adjusted reachability matrices. Circuit inference typically consists of thresholding or statistical tests to determine significant connections to reconstruct an estimated circuit.




<!-- NOTE: [^more_expt]: TODO: might reword. This is more than just an experiment, this is a "hypothesis search." May be more explicit about branding this procedure as the "CLINC" process? -->

We envision the structure of a set of experiments to identify a circuit through intervention to include the following broad stages:


<!--
Methods [# circuit representations](/section_content/methods_representation_reachability.md)
`Fig. OVERVIEW, circuit`
-->

1. First, explicitly enumerate the set of hypothesized circuits. Hypotheses about the structure of the circuit are often based on multiple sources of information including prior recordings, anatomical constraints revealed by tract tracing experiments, or commonly observed connectivity patterns in other systems. These hypotheses should be expressed as a set of circuits (adjacency matrices, *`Fig. OVERVIEW circuit`*) each with a probability representing the prior belief about the relative likelihood of these options. This hypothesis set can be thought of as a space of possible explanations for the observed data so far, which will be narrowed down through further intervention, observation, and inference *(see also [Fig.DISAMBIG (A)](#fig-disambig)).*

<!-- TODO:
explicitly reference examples here of priors over circuits
[🚧 add other sources of priors for circuit hypotheses]
[^bonus_causal]: **[future work]** use causality + graph theory to find "lurking look-alikes" i.e. Markov-equivalent circuits
[^more_assumptions]: should also enumerate assumptions about the dynamics of the network, signs of network weights, approximate timescales of interaction.
-->



<!-- NOTE:OUTLINE
- representations 
- predicting correlation structure (via generative model / dynamics)
- impact of intervention on pairwise dependence 
-->
<!--
Methods 
[# predicting correlation](/section_content/methods_predicting_correlation.md)
[# specifying interventions](/section_content/methods_interventions.md)
[# predicting impact of intervention](/section_content/methods_intervention_variance.md)
`Fig. OVERVIEW, prediction`
-->
2. Second, forecast patterns of correlation which could result from applying candidate interventions.<!-- TODO: Many ? Most? verify --> Most algorithms for circuit inference quantify and threshold measures of dependence between pairs of nodes. Correlations are often used to measure the linear component of dependence between outputs of two nodes, although the approach described here should generalize to other nonlinear measures of dependence such as mutual information. As such, the observed pattern of dependence (correlations) in a given experiment summarizes the input to an inference procedure to recover an estimated circuit.  
    A detailed forecast of the observed outputs could be achieved by simulating biophysical networks across candidate interventions and hypothesized ground-truth circuits. However, for large networks or large hypothesis sets this may be expensive to compute. Instead, for the sake of rapid iteration in designing interventions, we propose using the reachability representation of a linear (or linearized) network to succinctly and efficiently predict the observed correlationsacross nodes. The methods described in Methods [# predicting correlations](REF-SECTION-HERE) allow us to anticipate how open and closed-loop interventions across nodes in the network might increase, decrease, or sever dependencies between node outputs (*see also `Fig. OVERVIEW intervention, prediction`*).

<!-- NOTE: [^bivar_pred]: using binary reachability, we can be more general about predicting the "sign/slope" (when will they increase/decrease) of other measures of bivariate dependence like transfer entropy -->

<!-- NOTE: Alt. titles 
distinguishability, redundancy, identifiability, 
`{Survey / analyze / compare / summarize}` `{diversity / equivalence /  distinguishability of}` patterns of correlation across each hypothesized circuit.
 -->
<!-- TODO: style
 - ?? how much to discuss here, versus wait til it comes up by fig disambig?
 - ?? should we reference ahead, or just re-state what we need when we get to it?
-->
3. Third, assess distinguishability of patterns of correlation across hypothesized circuits and interventions. A useful experiment is one which produces highly distinct outcomes when applied to each of the hypothesized circuits, while an experiment which produces the same outcome across all hypothesized circuits would be redundant.
    Before collecting experimental data we do not know the ground-truth circuit with certainty, therefore it is useful to understand the range of possible observed patterns of dependence. To distill this range of possibilities to a make a decision about which intervention to apply, it is also useful to summarize the expected information we would gain about circuit identity across the range of hypotheses (e.g. across columns of [Fig. DISAMBIG)](#fig-disambig).<!-- TODO: ^ some run-ons and redundancies going on here --><!-- NOTE: DANGER: redundant with results -->
    While the magnitudes of correlation will depend on particular values of system parameters, here we focus on only the presence or absence of a significant correlation between two nodes, as well as whether correlations increase or decrease from their baseline. In this way, we build towards an understanding of the categorical impact of intervention on observed pairwise dependence, which should be general across particular parameter values or algorithms for circuit inference.
    The set of patterns of pairwise dependences across the hypothesis set form an "intervention-specific fingerprint." This fingerprint summarizes the outcomes of a particular experiment with intervention, and therefore shows which hypotheses are observationally equivalent under this observation. To quantify this hypothesis distinguishability based on the diversity of a set of possible outcomes, we compute the Shannon entropy over the distribution of patterns of dependence (See Methods [# across-hypothesis entropy](/section_content/methods_entropy.md)). The maximum achievable entropy is simply the logarithm of the number of hypotheses and would correspond to an experiment wherein the outcome is sufficient to uniquely determine the correct hypothesis from the set. 

<!-- >-*Here we generalize across specific values of synaptic weights and divide observed patterns into categories: increased correlation, decreased correlation, no correlation.* -->

<!-- TODO: condense this paragraph, allow longer version to fold out in results 
> The set of patterns of pairwise dependences across the hypothesis set form an "intervention-specific fingerprint" 
`(i.e. a single row of `Fig. DISAMBIG`)`. This fingerprint summarizes the outcomes of a particular experiment with intervention, and therefore shows which hypotheses are observationally equivalent under this observation. If this fingerprint contains many examples of the same pattern
`<!--`(such as the all-to-all correlation pattern seen under passive observation, `Fig. DISAMBIG Ba`)`, many different circuits correspond to the same observation, and that experiment contributes low information to distinguish between hypotheses. On the other hand, a maximally informative experiment would result in unique observations corresponding to each hypothesis. Observations from such an experiment would be sufficient to narrow the inferred circuit down to a single hypotheses.
-->

<!-- NOTE:
lead out:
- could also hint towards size of Markov equivalency
- next section deals with using this distinguishability to choose an intervention (or several)
-->

<!-- NOTE: potentially useful results text for entropy 
The set of patterns of pairwise dependences across the hypothesis set form an "intervention-specific fingerprint" (i.e. a single row of `Fig. DISAMBIG`). This fingerprint summarizes the outcomes of a particular experiment with intervention, and therefore shows which hypotheses are observationally equivalent under this observation. If this fingerprint contains many examples of the same pattern (such as the all-to-all correlation pattern seen under passive observation, `Fig. DISAMBIG Ba`), many different circuits correspond to the same observation, and that experiment contributes low information to distinguish between hypotheses. On the other hand, a maximally informative experiment would result in unique observations corresponding to each hypothesis. Observations from such an experiment would be sufficient to narrow the inferred circuit down to a single hypotheses.

To quantify this hypothesis ambiguity based on the diversity of a set of possible outcomes, we compute the Shannon entropy over the distribution of patterns (See Methods [entropy](#methods-entropy)). Because our hypotheses set contains circuits with relatively dense connectivity, 5 of the 6 hypotheses result in all-to-all correlations, with the final hypothesis resulting in a unique V-shaped pattern of correlation (A~B, and A~C, `Fig. DISAMBIG row Ba`). The entropy of this distribution is 0.65 bits. To interpret this entropy value, it is useful to understand the maximum achievable entropy, which is simply the logarithm of the number of hypotheses. In this case, $H_{max} = \log_2(6)\approx 2.58 
-->

<!-- NOTE:
alt. titles 
  Choose optimal intervention 
  Select an effective intervention
Methods 
  [# selecting intervention](/section_content/methods_entropy_selection.md)
-->
4. Fourth, select intervention type and location.We describe briefly a greedy approach for choosing an effective single-site intervention, but extending the approach above to predict joint entropy would allow a joint or sequential experimental design which could be optimized over multiple interventions *(see Discussion)*. For selecting the first intervention type and location, we propose choosing the intervention which results in the maximum expected circuit information across the prior hypothesis set, that is, the intervention type and location with the highest entropy (see Methods [# selecting intervention](/section_content/methods_entropy_selection.md)). On subsequent iterations, an updated prior over hypotheses should be used to select the next intervention. 

<!-- NOTE: additional points
- possible interventions consist of open-loop and closed-loop stim at each of N nodes 
   - but more constraints on the set of interventions can easily be incorporated at this stage
 -->

 <!-- 
 Methods 
 *[# specifying interventions](/section_content/methods_interventions.md)*
 *[# extracting circuit estimates](/section_content/methods_circuit_estimates.md)*
 [# collecting data from simulations](/section_content/methods_simulations.md)
 [# quantifying dependence](/section_content/methods_circuit_estimates.md)
 `Fig. OVERVIEW, data, estimate`
 -->
5. Fifth, apply intervention, collect data, and estimate between-node dependence. Using entropy as a metric to select a useful intervention, the next step is to conduct that interventional experiment, in-vivo or in a detailed simulation. Such an experiment may reveal outputs patterns not fully captured by the linearized reachability representation. Time-series observations from each node are used to compute between-node measures of dependence such as pairwise correlations.
<!-- NOTE: see Methods_entropy_selection for additional practicalities like choosing stimulus variance -->


<!-- Methods 
*[# extracting circuit estimates](/section_content/methods_circuit_estimates.md)* -->
<!-- NOTE: 
don't want to lean too hard on particulars here.  
details of this step are likely to be very application-specific
-->
<!-- ... executed by combining the prior and likelihood of each model to form a posterior distribution over hypotheses.  -->
6. Finally, given the observed pairwise dependencies, the last step is to form a posterior belief over circuit hypotheses. With prior beliefs about the hypothesis set, and pairwise dependencies quantified under intervention, these can be combined in a Bayesian fashion to form a posterior distribution over circuit hypotheses. This step is likely to be highly application-specific and depend strongly on the goals for inference (`Fig. OVERVIEW, inference`). A simple strategy would be to compare thresholded empirical correlation matrix to the discretized predicted correlations under each hypothesis given the specified intervention. Any hypothesized circuits with correlations structure inconsistent with the observed correlations could be eliminated from the candidate hypothesis set (see Methods [# circuit estimates](/section_content/methods_circuit_estimates.md)).<!-- NOTE: see also [# determining directionality from changes in correlation](/section_content/methods_coreach_sign.md) -->
    More generally, an iterative identification procedure may update the prior for the next round from the posterior distribution over hypotheses. At a predefined convergence criteria, a *maximum a posteriori* (MAP) estimate of the circuit identity can be estimated and iterations can be stopped (see Methods [# estimate convergence](/section_content/methods_entropy_selection.md)). If this convergence criteria is not met, the steps of inference outlined in this section can be repeated with the updated prior.
<!-- criterion? -->

<!-- Alternately, individual connections can be inferred through simpler strategies such as using statistical tests to define thresholds for determining significant empirical correlations. -->

<!-- NOTE: outline
- several approaches 
  - discuss reconstruction of single circuit from reachability 
  - see entropy_selection for choosing circuit amongst hypothesis set 
lead out 
- not prescriptive 
- note process is iterative!
- but key phases are likely to be useful for 
- funnel out / transition to fig disambig ?

... executed by combining the prior and likelihood of each model to form a posterior distribution over hypotheses.  -->