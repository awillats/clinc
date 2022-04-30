<!-- ## Interaction of intervention on circuit estimation
!!!! - overall, 40% done -->


[^node_repr]: nodes in such a graphical model may represent populations of neurons, distinct cell-types, different regions within the brain, or components of a latent variable represented in the brain.

<!-- - [ ] why link severing - difficult, might leave to later -->

<!-- ### Intervening provides (categorical) improvements in inference power beyond passive observation -->
<!-- NOTE: Application to demo set, entropy over hypotheses - 50% done -->

<details><summary>↪notes, see also </summary>

going to assume these have already been discussed:

- predicting correlation
- measuring dependence
- markov equivalence

[Methods: Procedure for choosing & applying intervention](_steps_of_inference.md)

</details>

Next, we apply (steps 1-3 of) this circuit search procedure to a collection of closely related hypotheses for 3 interacting nodes[^node_repr] to illustrate the impact of intervention. 🚧 `most of the story in the figure caption for now` 🚧

<a id="fig-disambig"></a>
![](/figures/core_figure_sketches/circuit_entropy_sketch.png)
<!-- ![](/figures/misc_figure_sketches/circuit_intervention_entropy_mockup.png) -->
> **Figure DISAMBIG: Interventions narrow the set of hypotheses consistent with observed correlations** 
*source: [google drawing](https://docs.google.com/drawings/d/1CBp1MhOW7OGNuBvo7OkIuzqnq8kmN8EEX_AkFuKpVtM/edit)*
>**(A)** Directed adjacency matrices represent the true and hypothesized causal circuit structure
>**(B)** Directed reachability matrices represent the direct *(black)* and indirect *(grey)* influences in a network. Notably, different adjacency matrices can have equivalent reachability matrices making distinguishing between similar causal structures difficult, even with open-loop control.
>**(C)** Correlations between pairs of nodes. Under passive observation, the direction of influence is difficult to ascertain. In densely connected networks, many distinct ground-truth causal structures result in similar "all correlated with all" patterns providing little information about the true structure.
>**(D-F)** The impact of open-loop intervention at each of the nodes in the network is illustrated by modifications to the passive correlation pattern. Thick orange[^edge_color] edges denote correlations which increase above their baseline value with high variance open-loop input. Thin blue[^edge_color] edges denote correlations which decrease, often as a result of increased connection-independent "noise" variance in one of the participating nodes. Grey edges are unaffected by intervention at that location.
> A given hypotheses set (A) will result in an "intervention-specific fingerprint", that is a distribution of frequencies for observing patterns of modified correlations *(across a single row within D-F)*. If this fingerprint contains many examples of the same pattern of correlation (such as **B**), many hypotheses correspond to the same observation, and that experiment contributes low information to distinguish between structures. A maximally informative intervention would produce a unique pattern of correlation for each member of the hypothesis set.
:construction:`caption too long`

<!-- - purpose of the figure 
  - conclusion: stronger intervention facilitates disambiguating equivalent hypotheses
    - more distinct patterns in a row 
    - few hypotheses have equivalent patterns
- explain distribution across hypothesis for a given intervention
  - build intuition for "more different circuits = better inference" -->

[^edge_color]: will change the color scheme for final figure. Likely using orange and blue to denote closed and open-loop interventions. Will also add in indication of severed edges

!!!! - Explain why closed-loop helps - link severing - 5% done

**Why does closed-loop control provide a categorical advantage?** Because it severs indirect links
`is this redundant with intro?`
`needs to be backed here up by aggregate results?`
- this is especially relevant in recurrently connected networks where the reachability matrix becomes more dense. 
- more stuff is connected to other stuff, so there are more indirect connections, and the resulting correlations look more similar (more circuits in the equivalence class)
- patterns of correlation become more specific with increasing intervention strength 
  - more severed links → more unique adjacency-specific patterns of correlation  
  
> **Where you intervene**[^where_place] strongly determines the inference power of your experiment.
> **secondary point:** having (binary) prediction helps capture this relationship

[^where_place]: Figure VAR shows this pretty well, perhaps sink this section until after discussing categorical and quantitative?


<!-- NOTE: - Quantitative impact of closed-loop - 70% done -->

### Stronger intervention shapes correlation, resulting in more data-efficient inference with less bias

<!-- NOTE: - Explain why closed-loop helps - bidirectional variance control - 60% done -->

[^dof]: need a more specific way of stating this. I mean degrees of freedom in the sense that mean and variance can be controlled independent of each other. And also, that the range of achievable correlation coefficients is wider for closed-loop than open-loop (where instrinsic variability constrains the minimum output variance)
  
[^intrinsic_var]: below the level set by added, independent/"private" sources
  
While a primary advantage of closed-loop interventions for circuit inference is its ability to functionally lesion indirect connections, another, more nuanced `(quantitative)` advantage of closed-loop control lies in its capacity to bidirectionally control output variance. While the variance of an open-loop stimulus can be titrated to adjust the output variance at a node, in general, an open-loop stimulus cannot reduce this variance below its instrinsic[^intrinsic_var] variability. That is, if the system is linear with Gaussian noise,`...`

**`@ import "/section_content/methods_intervention_variance"`**

<!-- TODO: reference [figvar](#fig-var) to empricially show this bidirectional control of output variance? -->


#### Impact of intervention location and variance on pairwise correlations
<!-- > - Implications for ID: more precise shaping of codependence across network
> - wider dynamic range of observable correlations
>   - important because we sometimes want to minimize correlations for indirect links
>   - allows for more distinct outcomes w.r.t. circuit -->

[related methods](methods1_predicting_correlation.md)

<!-- TODO: - again, feels very backgroundy / discussiony ... where to put this? -->

We have shown that closed-loop interventions provide more flexible control over output variance of nodes in a network, and that shared and independent sources of variance determine pairwise correlations between node outputs. Together, this suggests closed-loop interventions may allow us to shape the pattern of correlations with more degrees of freedom[^dof] `[why do we want to?...]`

One application of this increased flexibility is to increase correlations associated with pairs of directly correlated nodes, while decreasing spurious correlations associated with pairs of nodes without a direct connection (but perhaps are influenced by a common input, or are connected only indirectly). While "correlation does not imply causation," intervention may decrease the gap between the two. 

Our hypothesis is that this shaping of pairwise correlations will result in reduced false positive edges in inferred circuits, "unblurring" the indirect associations that would otherwise confound circuit inference. However care must be taken, as this strategy relies on a hypothesis for the ground truth adjacency and may also result in a "confirmation bias" as new spurious correlations can be introduced through closed-loop intervention.

**`@ import "/section_content/methods_coreach_sign.md"`**

<a id="fig-predict"></a>
<!-- <X id="fig-var"></X> -->
<!-- <img src"/figures/misc_figure_sketches/quant_r2_prediction_common.png" width=300> -->
![](/figures/misc_figure_sketches/quant_r2_prediction_common.png)
![](/figures/from_code/bidirectional_correlation.png "generated by sweep_gaussian_SNR.py")

> 🚧(Final figure will be a mix of these two panels, caption will need updating) **Figure VAR: Location, variance, and type of intervention shape pairwise correlations**
> **(CENTER)** A two-node linear Gaussian network is simulated with a connection from A→B. Open-loop interventions *(blue)* consist of independent Gaussian inputs with a range of variances $\sigma^2_S$. Closed-loop interventions *(orange)* consist of feedback control with an independent Gaussian target with a range of variances. *Incomplete closed-loop interventions result in node outputs which are a mix of the control target and network-driven activity*. Connections from sources to nodes are colored by their impact on correlations between A and B; green denotes $dR/dS > 0$, red denotes $dR/dS<0$.
> **(lower left)** Intervention "upstream" of the connection A→B increases the correlation $r^2(A,B)$.
> **(lower right)** Intervention at the terminal of the connection A→B decreases the correlation $r^2(A,B)$ by adding connection-independent noise.
> **(upper left)** Intervention with shared inputs to both nodes generally increases $r^2(A,B)$, *(even without A→B, see supplement)*.
> **(upper right)** The impact of shared interventions depends on relative weighted reachability $\text{Reach}(S_k→A) / \text{Reach}(S_k→B)$, with highest correlations when these terms are matched (see *)
> Closed-loop interventions *(orange)* generally result in larger changes in correlation across $\sigma^2_S$ than the equivalent open-loop intervention. Closed-loop control at B effectively lesions the connection A→B, resulting in near-zero correlation.
> [^var_compare]


[^var_compare]: compare especially to ["Transfer Entropy as a Measure of Brain Connectivity"](https://www.frontiersin.org/articles/10.3389/fncom.2020.00045/full), ["How Connectivity, Background Activity, and Synaptic Properties Shape the Cross-Correlation between Spike Trains"](https://www.jneurosci.org/content/29/33/10234) Figure 3.



<details><summary>↪ additional notes:</summary>

- contextualize increasing correlation is sometimes good, sometimes bad!
- having (quantitative) prediction helps capture this relationship
- **(incidental) subfigure PREDICT: Comparing predicted and empirical correlation, identification performance**
</details>

🚧
The change in correlation as a function of changing intervention variance ($\frac{dr^2_{ij}}{dS}$) can therefore be used as an additional indicator of presence/absence and directionality of the connection between A,B *(see [fig. disambig. D.)](fig-disambig))*
🚧


[Fig. variance](#fig-var) also demonstrates the relative dynamic range of correlations achievable under passive, open- and closed-loop intervention. In the passive case, correlations are determined by instrinsic properties of the network $\sigma^2_{base}$. These properties have influence over the observed correlations in a way that can be difficult to separate from differences due to the ground-truth circuit. With open-loop intervention we can observe the impact of increasing variance at a particular node, but the dynamic range of achievable correlations is bounded by not being able to reduce variance below its baseline level. With closed-loop control, the bidirectional control of the output variance for a node means a much wider range of correlations can be achieved [(blue v.s. orange in fig. variance)](#fig-var), resulting in a more sensitive signal reflecting the ground-truth connectivity.



*see also [results1B_data_efficiency_and_bias.md](results1B_data_efficiency_and_bias.md)*

<details><summary>↪todo items:</summary>

<!-- TODO: -->
- [ ] comparison signs in rows of DISAMBIG figure
- [ ] merge from "box style" where entire story is in caption, to having something in body of results text 
- [ ] write "explain why CL is better" section, ? exile it to discussion section?
- [ ] connect DISAMBIG caption to quantitative variance explanation section
- [ ] collapse figvar - do we need to make shared input point here? or is discussion fine?
- [ ] dR/dS needs to mention R as r^2 corr
 
</details>

<details><summary>↪Notes from matt</summary>

- [super minor] First part of fig DISAMBIG: subsections (A) through (C) work really well
- [super minor] in caption for (D-F): "modifications to the passive correlation pattern" is a bit confusing in the context of open-loop intervention
- [super minor] also in caption for (D-F): really like "intervention-specific fingerprint" terminology. The last sentence of the (D-F) caption really hits the message home, possible to emphasize that this is the take-home message earlier?
- [narrative/organization] fig DISAMBIG feels really example-y, more like a proof of concept than 'results.' The writing in Sec 5.1.1 also has this flavor, like it could be in a methods section. (The plot in the top right feels much more results-ey.) Not necessarily a bad thing, maybe just a consideration for thinking about article vs perspective flavor.
- [missing] Section 5.1.2.1: what are the definitions of S_k, CoReach(i,j|S_k), and R_{ij}?
- [narrative] Section 5.1.2.1: the narrative here really works for me, but it's a little unclear whether this is more of a 'result' or a 'recipe' -- the figures here also feel more example/proof-of-concept-ey, and the math here helps ground things in
- [missing] discussion of partial closed-loop control?
</details>