<details><summary>↪notes</summary>

> **Theme B.** Experiments for circuit inference can be thought of as **narrowing the set of plausible explanations**, refining a hypotheses space[^refine]

<!-- 
TODO: overall, this section needs the single-circuit and multi-circuit hypotheses integrating better.
The figure currently describes the process for a single circuit, which is the simplest to describe. But the body of the text is mostly pointed towards the multi-hypothesis perspective that follows in Figure DISAMBIG
 -->

</details>


![](/figures/core_figure_sketches/methods_overview_pipeline_sketch.png)

> **Figure OVERVIEW: Components of a circuit identification experiment.**
> The ground-truth or hypothesized circuit can be represented either as a graph depicting connections between nodes or, equivalently, as an adjacency matrix. While the adjacency matrix describes the direct causal relationships, it's useful to understand the net direct and indirect effect of nodes on each other, called reachability. This reachability representation is key for predicting observed correlations, as well as the impact of intervention. The generative model for this network describes how connections and sources of variance contribute to network dynamics, and observed time-series data (either simulated or measured *in vivo*). From these time-series, pairwise dependence can be measured through quantities like correlation coefficients. Alternately, in the design phase, correlations can be predicted directly from the intervention-adjusted reachability matrices. Circuit inference typically consists of thresholding or statistical tests to determine significant connections to reconstruct an estimated circuit.


[^refine]: see [Advancing functional connectivity](https://www.nature.com/articles/s41593-019-0510-4), fig. 2

[^more_expt]: TODO: might reword. This is more than just an experiment, this is a "hypothesis search." Is this procedure what we're going to brand as the "CLINC" process?

**We envision the structure of an experiment[^more_expt]** to include the following broad stages:

1. First, explicitly **enumerate the set of hypothesized circuits.** Hypotheses about the structure of the circuit are often based on multiple sources of information including prior recordings, anatomical constraints revealed by tract tracing experiments, or commonly observed connectivity patterns in other systems. These hypotheses should be expressed as a set of circuits (adjacency matrices, *`Fig. OVERVIEW circuit`*) each with a probability representing the prior belief about the relative likelihood of these options. This hypothesis set can be thought of as a space of possible explanations for the observed data so far, which will be narrowed down through further intervention, observation, and inference *(see also [Fig.DISAMBIG (A)](#fig-disambig)).*

<!-- TODO:
explicitly reference examples here of priors over circuits
[🚧 add other sources of priors for circuit hypotheses]
[^bonus_causal]: **[future work]** use causality + graph theory to find "lurking look-alikes" i.e. Markov-equivalent circuits
[^more_assumptions]: should also enumerate assumptions about the dynamics of the network, signs of network weights, approximate timescales of interaction.
-->

2. Second, **forecast patterns of correlation** which could result from applying candidate interventions.<!-- TODO: Many ? Most? verify --> Most algorithms for circuit inference quantify and threshold measures of dependence between pairs of nodes. Correlations are often used to measure the linear component of dependence between outputs of two nodes, although the approach described here should generalize to other nonlinear measures of dependence such as mutual information. As such, the observed pattern of dependence (correlations) in a given experiment summarizes the input to an inference procedure to recover an estimated circuit.  
    A detailed forecast of the observed outputs could be achieved by simulating biophysical networks across candidate interventions and hypothesized ground-truth circuits. However, for large networks or large hypothesis sets this may be expensive to compute. Instead, for the sake of rapid iteration in designing interventions, we propose using the reachability representation of a linear (or linearized) network to succinctly and efficiently predict the observed correlations[^bivar_pred] across nodes. The methods described in Methods [# predicting correlations](REF-SECTION-HERE) allow us to anticipate how open and closed-loop interventions across nodes in the network might increase, decrease, or sever dependencies between node outputs (*see also `Fig. OVERVIEW intervention, prediction`*).

[^bivar_pred]: using binary reachability, we can be more general above predicting the "sign/slope" (when will they increase/decrease) of other measures of bivariate dependence like transfer entropy

3. `{Survey / analyze / compare / summarize}` `{diversity / equivalence /  distinguishability of}` patterns of correlation across each hypothesized circuit.
A useful experiment (data collected in the presence of an intervention) is one which produces highly distinct outcomes when applied to each of the hypothesized circuits, while an experiment which produces the same outcome across all hypothesized circuits would be redundant.
    Before collecting experimental data we do not know the ground-truth circuit with certainty, therefore it is useful to understand the range of possible observed patterns of dependence. To distill this range of possibilities to a make a decision about which intervention to apply, it is also useful to summarize the expected information we would gain about circuit identity across the range of hypotheses. [(across columns of Fig.DISAMBIG)](#fig-disambig)
>-*Here we generalize across specific values of synaptic weights and divide observed patterns into categories: increased correlation, decreased correlation, no correlation.*
<!-- TODO: ^ some run-ons and redundancies going on here -->

🚧
`Entropy as a measure of information about circuit hypotheses`
**`@ import "/section_content/methods_entropy.md"`**

`select intervention - (is this its own step, or the last part of step 3)`
Here, we describe a "greedy" approach for choosing an effective single-node intervention, but extending the approach above to predict joint entropy would allow a joint or sequential experimental design which would be optimal over multiple interventions *(see Discussion)*.
>- possible interventions consist of open-loop and closed-loop stim at each of N nodes 
>   - but more constraints on the set of interventions can easily be incorporated at this stage

For selecting the first intervention type and location, we propose choosing the intervention which results in the maximum expected circuit information, that is:
$$S_i^* = \underset{i}{\arg\max}\,H(C|S_i)$$[^intv_notation]


[^intv_notation]: will need to tighten up notation for intervention summarized as a variable, annotating its type (passive, open-, closed-loop) as well as its location. Also have to be careful about overloading $S_i$ as the impact of private variance and as a particular open-loop intervention

🚧
4. **Apply intervention and collect data.**
Using entropy as a metric to select a useful intervention, the next step is to conduct that interventional experiment, in-vivo or in a detailed simulation. Such an experiment may reveal outputs patterns not fully captured by the linearized reachability representation. 

`[extract correlations ...]`
[^practicalities]. 

[^practicalities]: Omitting several quantitative practicalities in this step. Notably choosing the amplitude / frequency content of an intervention w.r.t. estimated parameters of the circuit


5. **Given the observed dependency pattern, form a posterior belief over hypotheses**
`[🚧 transition text]`  

**`@ import "/section_content/methods_entropy_selection.md"`**

<!-- ![](/figures/misc_figure_sketches/circuit_intervention_entropy_mockup.png) -->
<!-- **Figure DISAMBIG: Stronger intervention facilitates disambiguating equivalent hypotheses** -->