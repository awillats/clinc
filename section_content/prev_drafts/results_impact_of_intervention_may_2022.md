<!--
NOTE:
going to assume these have already been discussed:
- predicting correlation
- measuring dependence
- markov equivalence
[Methods: Procedure for choosing & applying intervention](overview_steps_of_inference.md)
-->

<!--
TODO:
    
- [ ] write lead-in for this section
- [ ] write "why link severing"
- [ ] fill in numerical details on figure 
-->


<!-- ## Interaction of intervention on circuit estimation -->
### Intervening provides categorical improvements in inference power beyond passive observation
`... transition:`
Next, we apply the first three steps of this circuit search procedure to a collection of closely related circuit hypotheses to illustrate the impact of intervention.
<!-- hypotheses for circuits with three interacting nodes[^node_repr] -->


**Outline**   
- adjacency and reachability and correlations (methods)
*(Fig A,B)*

- difficulty of correlations, may hypotheses produce the same pattern [challenge]
*(Fig C)*
> In densely connected networks, many distinct ground-truth causal structures result in similar "all correlated with all" patterns providing little information about the true structure. 

- what does intervention do? - [solution]
  - *(Fig D-F)*
  - changes correlation (methods) 
  - pairwise correlations given an intervention are more distinct across the hypothesis set 
  
- measuring across-hypothesis set similarity [formalizing this]
  - @ `methods_entropy` ?
  - @ `methods_entropy_selection` ?
  - (Methods)  

> A given hypotheses set (A) will result in an "intervention-specific fingerprint", that is a distribution of frequencies for observing patterns of modified correlations *(across a single row within D-F)*. If this fingerprint contains many examples of the same pattern of correlation (such as **B**), many hypotheses correspond to the same observation, and that experiment contributes low information to distinguish between structures. A maximally informative intervention would produce a unique pattern of correlation for each member of the hypothesis set.

- *walk through specific hypothesis set*


<a id="fig-disambig"></a>
![](/figures/core_figure_sketches/circuit_entropy_sketch.png)
<!-- ![](/figures/misc_figure_sketches/circuit_intervention_entropy_mockup.png) -->
 **Figure DISAMBIG: Interventions narrow the set of hypotheses consistent with observed correlations** 
*source: [google drawing](https://docs.google.com/drawings/d/1CBp1MhOW7OGNuBvo7OkIuzqnq8kmN8EEX_AkFuKpVtM/edit)*
**(A)** Directed adjacency matrices represent the true and hypothesized causal circuit structure
**(B)** Directed reachability matrices represent the direct *(black)* and indirect *(grey)* influences in a network. Notably, different adjacency matrices can have equivalent reachability matrices making distinguishing between similar causal structures difficult, even with open-loop control.
**(C)** Correlations between pairs of nodes. Under passive observation, the direction of influence is difficult to ascertain. 
<!-- In densely connected networks, many distinct ground-truth causal structures result in similar "all correlated with all" patterns providing little information about the true structure. -->
**(D-F)** The impact of open-loop intervention at each of the nodes in the network is illustrated by modifications to the passive correlation pattern. Thick orange[^edge_color] edges denote correlations which increase above their baseline value with high variance open-loop input. Thin blue edges denote correlations which decrease, often as a result of increased connection-independent "noise" variance in one of the participating nodes. Grey edges are unaffected by intervention at that location. `point to a good intervention`
<!-- A given hypotheses set (A) will result in an "intervention-specific fingerprint", that is a distribution of frequencies for observing patterns of modified correlations *(across a single row within D-F)*. If this fingerprint contains many examples of the same pattern of correlation (such as **B**), many hypotheses correspond to the same observation, and that experiment contributes low information to distinguish between structures. A maximally informative intervention would produce a unique pattern of correlation for each member of the hypothesis set. -->


<!-- 
- purpose of the figure 
  - conclusion: stronger intervention facilitates disambiguating equivalent hypotheses
    - more distinct patterns in a row 
    - few hypotheses have equivalent patterns
- explain distribution across hypothesis for a given intervention
  - build intuition for "more different circuits = better inference" -->


**Why does closed-loop control provide a categorical advantage?** 
*Because it severs indirect links*

!!!! - Explain why closed-loop helps - link severing

<!--
NOTE:
is this redundant with intro?`
`needs to be backed here up by aggregate results?`
-->

<!-- TODO: 
- reachability can anticipate what open-loop buys 
- modified reachability anticaptes what closed-loop buys 
- benefit should be inference-algorithm agnostic

- Where you intervene matters!


- closed-loop doesnt always help 
-->


<details><summary>↪ <b>OUTLINE</b> </summary>

- this is especially relevant in recurrently connected networks where the reachability matrix becomes more dense. 

- more stuff is connected to other stuff, so there are more indirect connections, and the resulting correlations look more similar (more circuits in the equivalence class)

- patterns of correlation become more specific with increasing intervention strength 
  - more severed links → more unique adjacency-specific patterns of correlation  
  
> **Where you intervene**[^where_place] strongly determines the inference power of your experiment.
> **secondary point:** having (binary) prediction helps capture this relationship

</details>

<!-- [^node_repr]: nodes in such a graphical model may represent populations of neurons, distinct cell-types, different regions within the brain, or components of a latent variable represented in the brain. -->

[^edge_color]: will change the color scheme for final figure. Likely using orange and blue to denote closed and open-loop interventions. Will also add in indication of severed edges

[^where_place]: Figure VAR shows this pretty well, perhaps sink this section until after discussing categorical and quantitative?


<!-- 
NOTE: see also todo items at end of 
/section_content/results_impact_variance.md

TODO:
- [ ] comparison signs in rows of DISAMBIG figure
- [ ] merge from "box style" where entire story is in caption, to having something in body of results text 
- [ ] write "explain why CL is better" section, ? exile it to discussion section?
- [ ] connect DISAMBIG caption to quantitative variance explanation section

NOTE: from matt
- [super minor] First part of fig DISAMBIG: subsections (A) through (C) work really well
- [super minor] in caption for (D-F): "modifications to the passive correlation pattern" is a bit confusing in the context of open-loop intervention
- [super minor] also in caption for (D-F): really like "intervention-specific fingerprint" terminology. The last sentence of the (D-F) caption really hits the message home, possible to emphasize that this is the take-home message earlier?
- [narrative/organization] fig DISAMBIG feels really example-y, more like a proof of concept than 'results.' The writing in Sec 5.1.1 also has this flavor, like it could be in a methods section. (The plot in the top right feels much more results-ey.) Not necessarily a bad thing, maybe just a consideration for thinking about article vs perspective flavor.
-->