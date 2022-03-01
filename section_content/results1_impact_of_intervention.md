<details><summary>going to assume these have already been discussed</summary>

- predicting correlation
- measuring dependence
- markov equivalence
</details>

[^node_repr]: nodes in such a graphical model may represent populations of neurons, distinct cell-types, different regions within the brain, or components of a latent variable represented in the brain.

- [~] quick readthrough, round out `structure of an experiment`
- [ ] 20 minutes on Figure DISAMBIG
- [ ] 20 minutes scaffolding quantitative section

---

### Intervening provides (categorical) improvements in inference power beyond passive observation

> **Theme B.** Experiments for circuit inference can be thought of as **narrowing the set of plausible explanations**, refining a hypotheses space[^refine]

[^refine]: see Advancing functional connectivity, fig. 2

🚧 figure request: flowchart for steps of intervention experiment 🚧

[^more_expt]: more than just an experiment, this is a "hypothesis search." Is this procedure what we're going to brand as the "CLINC" process?

!!!! - Structure of an experiment / CLINC framework - 70% done
**We envision the structure of an experiment[^more_expt]** to include the following broad stages:

1. First, explicitly **enumerate the set of hypothesized circuits.** Hypotheses about the structure of the circuit would be based on multiple sources of information including prior recordings, anatomical constraints revealed by `experiments where you look at the fiber bundles connecting regions`, or commonly observed connectivity patterns in other systems `[🚧 add other sources of priors for circuit hypotheses]`[^bonus_causal][^more_assumptions] These hypotheses should be expressed as a set of circuits (adjacency matrices) each with a probability representing the prior belief about the relative likelihood of these options. This hypothesis set can be thought of as a space of possible explanations for the observed data so far, which will be narrowed down through further intervention, observation, and inference.

[^most]: verify whether this is reasonable to say
2. Second, *in silico*, **forecast patterns of correlation** which could result from applying candidate interventions.
Most algorithms[^most] for circuit inference are designed to quantify and threshold measures of dependence between pairs of nodes. Correlations are often used to measure the linear component of dependence between outputs of two nodes, although the approach described here should generalize to other nonlinear measures of dependence such as mutual information. As such, the observed pattern of dependence (correlations) in a given experiment summarizes the input to an inference procedure to recover an estimated circuit.
A detailed forecast of the observed outputs could be achieved by simulating biophysical networks across candidate interventions and hypothesized ground-truth circuits. However, for large networks or large hypothesis sets this may be infeasible. Instead, using the reachability representation of a linear (linearized) network we can succinctly and efficiently predict the observed correlations[^bivar_pred] across nodes[^node_repr]. The methods described in `[ref. prediction methods]` allow us to anticipate how open and closed-loop interventions across nodes in the network might increase, decrease, or sever dependencies between node outputs.

[^bivar_pred]: using binary reachability, we can be more general above predicting the "direction" (when will they increase/decrease) of other measures of bivariate dependence like transfer entropy

3. `{Survey / analyze / compare / summarize}` `{diversity / equivalence /  distinguishability of}` patterns of correlation across each hypothesized circuit.

A useful experiment (intervention) is one which produces highly distinct outcomes when applied to each of the hypothesized circuits, while an experiment which produces the same outcome across all hypothesized circuits would be redundant.

Before collecting experimental data we do not know the ground-truth circuit with certainty, therefore it is useful to understand the range of possible observed patterns of dependence. To distill this range of possibilities to a make a decision about which intervention to apply, it is also useful to summarize the expected information we would gain about circuit identity across the range of hypotheses.

Shannon entropy provides a scalar summarizing how diverse a set of outcomes..
...how uniform a discrete probability function is...
...how surprising...(in expectation)
>- possible interventions consist of open-loop and closed-loop stim at each of N nodes 
>  - but more constraints on the set of interventions can easily be incorporated at this stage
>- a highly predictable experimental outcome means an experiment where not much was learned 
>-*Here we generalize across specific values of synaptic weights and divide observed patterns into categories: increased correlation, decreased correlation, no correlation.*
>- entropy joint across multiple interventions
 
An intervention associated with a higher entropy across circuits will, on average, provide more information to narrow the set of hypotheses.

4. *(in expt. or detailed biophysical simulation)* Apply intervention, collect data
Using entropy as a metric to select a useful intervention, the next step is to conduct that interventional experiment in-vivo or in a detailed simulation.  
>- guidance choosing a target / stimulus

5. **Given the observed dependency pattern, form a posterior belief over hypotheses**
  - remaining entropy quantifies the "realized" information (which may be larger or smaller than the expectation), and equivalently the remaining size and uncertainty of the posterior belief over the hypothesis set
  - Can choose the most likely (MAP) circuit amongst this posterior hypotheses
    - *(optionally, this posterior distribution can be used as an updated prior for the next iteration)*

----
!!!! - Application to demo set, entropy over hypotheses - 10% done
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



!!!! - Explain why closed-loop helps - link severing - 5% done
**Why does closed-loop control provide a categorical advantage?** Because it severs indirect links
- this is especially relevant in recurrently connected networks where the reachability matrix becomes more dense.
- more stuff is connected to other stuff, so there are more indirect connections, and the resulting correlations look more similar (more circuits in the equivalence class)
- patterns of correlation become more specific with increasing intervention strength 
  - more severed links → more unique adjacency-specific patterns of correlation  
  
> **Where you intervene**[^where_place] strongly determines the inference power of your experiment.

[^where_place]: Figure VAR shows this pretty well, perhaps sink this section until after discussing categorical and quantitative?

> **secondary point:** having (binary) prediction helps capture this relationship

---

!!!! - Quantitative impact of closed-loop - 10% done
### Stronger intervention shapes correlation, resulting in more data-efficient inference with less bias
> - "here are the quantitative advantages"
> - "here's additional nuance"
> - wider range of observable correlations
>   - important because we sometimes want to minimize correlations for indirect links
>   - allows for more distinct outcomes w.r.t. circuit
>   - summarized as "closed-loop allows bidirectional control of variance"
> - higher infinite-data accuracy (i.e. less bias)
>    - lower bias likely comes from the categorical advantages above
> - less data required to get to threshold level of accuracy (more data-efficient)
>      - likely comes from improved "SNR" which can be thought of as a derived property of the per-edge correlations
> - breakdown false positives, false negatives
> - (quantitative prediction helps)
<!-- Figure DATA: Analysis of simulated circuits suggest stronger intervention facilitates identification with less data  -->

!!!! - Explain why closed-loop helps - bidirectional variance control - 10% done
**Figure VAR: Stronger intervention allows better control of covariance**
**shaping covariance**
- while you can deliver open-loop inputs with titrated amounts of variance, you're often only able to add variance rather than subtract it, and the amount of variance you would add to the system is hard to predict a priori
- this is a key advantage of closed-loop control
  - which can have bidirectional influence over variance
    
- having (quantitative) prediction helps capture this relationship
  - **Figure PREDICT: Comparing predicted and empirical correlation, identification performance**
  

![](../figures/misc_figure_sketches/quant_r2_prediction_common.png)



!!!! - Explain why closed-loop helps - less bias - 5% done

!!!! - Explain why closed-loop helps - more data efficient - 5s% done

<details><summary> figure sketches </summary>

![](../figures/misc_figure_sketches/idtxl_eg_datareq_passive_open_loop.png) 
![](../figures/literature_figs/spike_field_shanechi_crop.png)
</details>

> Figure DATA: Analysis of simulated circuits suggest stronger intervention facilitates identification with less data 



[^bonus_causal]: **[future work]** use causality + graph theory to find "lurking look-alikes" i.e. Markov-equivalent circuits
[^more_assumptions]: should also enumerate assumptions about the dynamics of the network, signs of network weights, approximate timescales of interaction.