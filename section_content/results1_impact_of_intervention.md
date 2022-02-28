<details><summary>going to assume these have already been discussed</summary>

- predicting correlation
- measuring dependence
- markov equivalence
</details>

[^node_repr]: nodes in such a graphical model may represent populations of neurons, distinct cell-types, different regions within the brain, or components of a latent variable represented in the brain.

---

### Intervening provides (categorical) improvements in inference power beyond passive observation

> **Theme B.** Experiments for circuit inference can be thought of as **narrowing the set of plausible explanations**, refining a hypotheses space

🚧 figure request: flowchart for steps of intervention experiment 🚧

[^more_expt]: more than just an experiment, this is a "hypothesis search." Is this procedure what we're going to brand as the "CLINC" process?
 
**We envision the structure of an experiment[^more_expt]** to include the following broad stages:

1. First, explicitly **enumerate the set of hypothesized circuits.** Hypotheses about the structure of the circuit would be based on multiple sources of information including prior recordings, anatomical constraints revealed by `experiments where you look at the fiber bundles connecting regions`, or commonly observed connectivity patterns in other systems `[🚧 add other sources of priors for circuit hypotheses]`[^bonus_causal][^more_assumptions] These hypotheses should be expressed as a set of circuits (adjacency matrices) each with a probability representing the prior belief about the relative likelihood of these options.


2. Second, *in silico*, **forecast patterns of correlation** which could result from applying candidate interventions.
A detailed forecast of the observed outputs could be achieved by simulating detailed biophysical networks across both candidate interventions, and hypothesized ground-truth circuits. However, for large networks or large hypothesis sets this may be infeasible. Instead, using the reachability representation of a linear (linearized) network we can succinctly and efficiently predict the observed correlations[^bivar_pred] across nodes[^node_repr]. The methods described in `[ref. prediction methods]` allow us to anticipate how open and closed-loop interventions across nodes in the network might increase, decrease, or sever dependencies between node outputs.

[^bivar_pred]: using binary reachability, we can be more general above predicting the "direction" (when will they increase/decrease) of other measures of bivariate dependence like transfer entropy

3. `{Survey / analyze / compare / summarize}` `{diversity / equivalence /  distinguishability of}` patterns of correlation across each hypothesized circuit.
Our goal is to reduce the set of `[...]`
- if there are many distinct patterns of correlation for a given intervention depending on the ground-truth circuit structure then an experimenter is likely to learn a lot
  - then we can consider these hypotheses to be "distinguishable" under that intervention
  - this situation would allow `[...]`
However, since the ground-truth circuit is not known *a priori*, it is useful to measure the expected information gained across the set of possible circuits. `[...]`
- uniqueness / diversity of observed patterns can be summarized across a hypothesis set with (Shannon) entropy, a scalar which quantifies the expected information gained `[...]`

4. *(in expt. or detailed biophysical simulation)* Apply intervention, collect data
- guidance choosing a target / stimulus


5. **Given the observed dependency pattern, form a posterior belief over hypotheses**
  - remaining entropy quantifies the "realized" information (which may be larger or smaller than the expectation), and equivalently the remaining size and uncertainty of the posterior belief over the hypothesis set
  - Can choose the most likely (MAP) circuit amongst this posterior hypotheses
    - *(optionally, this posterior distribution can be used as an updated prior for the next iteration)*

----
Next, we apply (steps 1-3 of) this circuit search procedure to a collection of closely related hypotheses for 3 interacting nodes[^node_repr] to illustrate the impact of intervention. 

![](../figures/misc_figure_sketches/circuit_intervention_entropy_mockup.png)
**Figure DISAMBIG: Stronger intervention facilitates disambiguating equivalent hypotheses**
- lay out rows
- lay out columns 
- draw attention to "sameness" of correlations row
- explain color scheme
  - grey for indirect edges 
  - color1 for increasing correlation
  - color2 for decreasing correlation 
  - color3 for severed edges
- explain distribution across hypothesis for a given intervention
  - build intuition for "more different circuits = better inference"




**Why does closed-loop control provide a categorical advantage?** Because it severs indirect links
- this is especially relevant in recurrently connected networks where the reachability matrix becomes more dense.
- more stuff is connected to other stuff, so there are more indirect connections, and the resulting correlations look more similar (more circuits in the equivalence class)


---

**Where you intervene** strongly determines the inference power of your experiment.

**secondary:** having (binary) prediction helps capture this relationship

shows a dataset with many correlations, multiple plausible circuit hypotheses 
  - patterns of correlation become more specific with increasing intervention strength 
- in aggregate: focuses on reduced bias, higher accuracy for "infinite" data limit
- closed-loop > open-loop > passive 

### Stronger intervention results in more efficient, accuracy inference 
> - quantitative
> - "here's additional nuance"
> - 
<!-- Figure DATA: Analysis of simulated circuits suggest stronger intervention facilitates identification with less data  -->

![](../figures/misc_figure_sketches/quant_r2_prediction_common.png)

**Figure VAR: Stronger intervention allows better control of covariance**

**shaping covariance** is the focus of this paper.
  - this is a key advantage of closed-loop control
    - which can have bidirectional influence over variance
    
- while you can deliver open-loop inputs with titrated amounts of variance, you're often only able to add variance rather than subtract it, and the amount of variance you would add to the system is hard to predict a priori


- having (quantitative) prediction helps capture this relationship
  - **Figure PREDICT: Comparing predicted and empirical correlation, identification performance**


### Stronger intervention results in more efficient, accuracy inference 
<details><summary> figure sketches </summary>

![](../figures/misc_figure_sketches/idtxl_eg_datareq_passive_open_loop.png) 
![](../figures/literature_figs/spike_field_shanechi_crop.png)
</details>

> Figure DATA: Analysis of simulated circuits suggest stronger intervention facilitates identification with less data 




[^bonus_causal]: **[future work]** use causality + graph theory to find "lurking look-alikes" i.e. Markov-equivalent circuits
[^more_assumptions]: should also enumerate assumptions about the dynamics of the network, signs of network weights, approximate timescales of interaction.