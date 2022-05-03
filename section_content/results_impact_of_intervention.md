### Intervening provides categorical improvements in inference power beyond passive observation

In the previous sections, we established how open-loop interventions modify observed pairwise correlations, and how closed-loop interventions modify a circuit's functional connectivity. Figure `ID-DEMO` demonstrated a simple example of how removing connections in a circuit can sometimes reveal more distinct patterns of dependence, and distinguish hypotheses which are indistinguishable through passive observation and open-loop control. Here, we systematize this approach to choose an appropriate intervention to narrow down a hypothesis set. The following sections will address how to evaluate the relative effectiveness of a particular intervention. Multiple intervention types and locations are compared for a larger circuit hypothesis set to build towards general principles for where and how to intervene.

While the ground truth connectivity is rarely available during experiments, it is valuable to explicitly lay out our prior hypothesis in the form of a directed graph or adjacency matrix. Panel A of `Fig. DISAMBIG` shows the adjacency and reachability of 6 candidate circuit hypotheses. `Row Ba` illustrates the presence of pairwise correlation for each hypotheses under passive observation. While the magnitudes of correlation will depend on particular values of system parameters, here we focus on only the presence or absence of a significant correlation between two nodes, as well as whether correlations increase or decrease from their baseline. In this way, we build towards an understanding of the categorical impact of intervention on observed pairwise dependence, which should be general across particular parameter values or algorithms for circuit inference. *(More concrete, quantitative effects will be explored in the next section).*

The set of patterns of pairwise dependences across the hypothesis set  form an "intervention-specific fingerprint" (i.e. a single row of `Fig. DISAMBIG`). This fingerprint summarizes the outcomes of a particular experiment with intervention, and therefore shows which hypotheses are observationally equivalent under this observation. If this fingerprint contains many examples of the same pattern (such as the all-to-all correlation pattern seen under passive observation, `row Ba`), many different circuits correspond to the same observation, and that experiment contributes low information to distinguish between hypotheses. On the other hand, a maximally informative experiment would result in unique observations corresponding to each hypothesis. Observations from such an experiment would be sufficient to narrow the inferred circuit down to a single hypotheses.

To quantify this hypothesis ambiguity based on the diversity of a set of possible outcomes, we compute the Shannon entropy over the distribution of patterns (See Methods [entropy](#methods-entropy)). Because our hypotheses set contains circuits with relatively dense connectivity, 5 of the 6 hypotheses result in all-to-all correlations, with the final hypothesis displaying a unique V-shaped pattern of correlation (A~B, and A~C, `row Ba`). The entropy of this distribution is 0.65 bits. To interpret this entropy value, it is useful to understand the maximum achievable entropy, which is simply the logarithm of the number of hypotheses. In this case, $H_{max} = \log_2(6)\approx 2.58 \text{bits}$, which indicates the information gained from passive observation is 25% efficient ($H_{passive} / H_{max} \approx 0.25 $). 

As discussed in section [#](), high-variance open-loop intervention tends to increase correlations between pairs of nodes downstream of the intervention, and decreases correlations when only one node is downstream of the stimulus location. This can produce more distinct, hypothesis-specific patterns of pairwise dependence. `Fig. DISAMBIG, row Bb` shows how open-loop intervention at node A distinguishes hypotheses $\{C_1,C_2,C_3\}$ (where node A has reachability to nodes B and C) from hypotheses $\{C_4,C_5\}$ (where node A can only reach node C). This increased distinguishability is reflected in the distribution of correlation patterns in the fingerprint, and the entropy of that distribution $(H_{OL→A} \approx 1.46 \text{bits}, H_{OL→A}/H_{max} = 0.56)$. In expectation, this intervention provides more information about the hypothesis set than passive observation alone.

For some sets of circuit hypotheses, the capability of closed-loop intervention to remove indirect connections uncovers distinct patterns of resulting correlations that would otherwise be equivalent under other interventions. Because $C_4$ and $C_5$ have equivalent reachability matrices, their pairwise correlations will be similar even under open-loop intervention. But in `Row Bb`, closed-loop intervention at node A, severs the inputs to this node. Under hypothesis $C_4$, nodes C and B remain correlated through their direct connection, however, under $C_5$, severing inputs to A also severs the indirect influence of C on B, which is sufficient to remove the correlation between nodes C and B. The distribution of observed patterns `(Row Dc)`, contains more distinct entries, and leads to a higher across-hypothesis entropy of $H_{CL→A} \approx 1.79 \text{bits}, H_{CL→A}/H_{max} = 0.69$.

This example highlighted a location for intervention where closed-loop control provides a categorical for distinguishing circuit hypotheses above open-loop control (and passive observation). This advantage is notable, in that it represents an improvement in circuit estimation bias which would be unlikely to be mitigated through collecting more data. However, `Fig. DISAMBIG` further highlights the importance of not only intervention *type*, but also intervention *location* in determining successful circuit inference. For a given intervention type, different locations for delivering stimuli result in categorically different hypothesis-narrowing information *(e.g. $H(OL_B) < H(OL_A) < H(OL_C)$, Fig. `DISAMBIG` Column D)*. On the other hand, for interventions at nodes B and C, open-loop and closed-loop control result in identical correlation fingerprints for this hypothesis set &mdash; closed-loop control at these locations does *not* provide a categorical benefit beyond the information learned through open-loop control. This equivalence between open-loop and closed-loop interventions arises in cases where severing inputs at the target node does not interrupt an indirect connection which otherwise makes circuits in the hypothesis set ambiguous.

To summarize, by understanding the relationship between circuit structure, the effect of interventions, and changes to the observed patterns of correlation, we were able to demonstrate the relative utility of passive observation, open-loop control, and closed-loop control. Open-loop control improves the capacity to distinguish circuits by increasing the diversity of outcomes as correlations increase or decrease. In addition, closed-loop control is capable of providing a categorical improvement in the ability to distinguish between and narrow down a set of competing hypotheses. It results in distinct patterns of observed dependence in additional cases even with equivalent reachability by severing ambiguous indirect connections. These categorical differences in across-circuit entropy are likely to reflect fundamental differences in the best-case conditions for evaluating similar hypotheses, regardless of data volume or algorithms used for circuit inference. 

However, the utility of a given intervention does depend strongly on the location of control relative to paths in the hypothesized circuits. Circuits and hypothesis sets where closed-loop is likely to outperform open-loop control would consist of similar circuits, where direct and indirect connections are difficult to distinguish, such as those with recurrent loops. In highly sparse or largely-feedforward circuits, open-loop and closed-loop intervention are likely to result in similar circuit information.

<!-- 
see 
/code/analyze_hypothesis_entropy.py 
and 
/code/network_pattern_entropy.py

H {5xA, 1xB}        = 0.650
H {3xA, 2xB, 1xC} ) = 1.4591
H {4,1,1}           = 1.2516
H {3,1,1,1}         = 1.7925
log2(6)             = 2.58496

0.650 / log2(6) = 0.2514543247
-->
<a id="fig-disambig"></a>
<!-- NOTE: source [google drawing](https://docs.google.com/drawings/d/1CBp1MhOW7OGNuBvo7OkIuzqnq8kmN8EEX_AkFuKpVtM/edit)* -->
![](/figures/core_figure_sketches/circuit_entropy_sketch.png)

> **Figure DISAMBIG: Interventions narrow the set of hypotheses consistent with observed correlations** 

> **(A)** Directed adjacency matrices represent the true and hypothesized causal circuit structure. Directed reachability matrices represent the direct *(black)* and indirect *(grey)* influences in a network. Notably, different adjacency matrices can have equivalent reachability matrices making distinguishing between similar causal structures difficult, even with open-loop control.
> **(B)** Correlations between pairs of nodes. **a)** Under passive observation, the direction of influence is difficult to ascertain. 
> **(B b-g)** The impact of open-loop intervention at each of the nodes in the network is illustrated by modifications to the passive correlation pattern. Thick orange[^edge_color] edges denote correlations which increase above their baseline value with high variance open-loop input. Thin blue edges denote correlations which decrease, often as a result of increased connection-independent "noise" variance in one of the participating nodes. Grey edges are unaffected by intervention at that location.
> **(C)** Across-circuit entropy for each intervention type and location. Grey lines correspond to a single intervention location. Circle markers represent the mean entropy for a given intervention type across all intervention locations. Green dotted lines represents the maximum achievable entropy for this hypothesis set.
**(D)** Distributions of patterns of pairwise correlation across hypotheses, for each intervention location and type. Distributions with more observed patterns, and more uniform probabilities correspond to experiments which reveal more information to narrow the set of candidate hypotheses.

```
text for choosing an intervention ... 
```

<!-- 
- purpose of the figure 
  - conclusion: stronger intervention facilitates disambiguating equivalent hypotheses
    - more distinct patterns in a row 
    - few hypotheses have equivalent patterns
- explain distribution across hypothesis for a given intervention
  - build intuition for "more different circuits = better inference" 
  -->



<!--
**Why does closed-loop control provide a categorical advantage?** 
*Because it severs indirect links*
!!!! - Explain why closed-loop helps - link severing
-->

<!--
NOTE:
is this redundant with intro?`
`needs to be backed here up by aggregate results?`
-->

<!-- TODO:  **SUMMARY**
- reachability can anticipate what open-loop buys 
- modified reachability anticaptes what closed-loop buys 
- benefit should be inference-algorithm agnostic

- Where you intervene matters!

- closed-loop doesnt always help 

- this is especially relevant in recurrently connected networks where the reachability matrix becomes more dense. 

- more stuff is connected to other stuff, so there are more indirect connections, and the resulting correlations look more similar (more circuits in the equivalence class)

- patterns of correlation become more specific with increasing intervention strength 
  - more severed links → more unique adjacency-specific patterns of correlation  
  
> **Where you intervene**[^where_place] strongly determines the inference power of your experiment.
> **secondary point:** having (binary) prediction helps capture this relationship

-->

<!-- [^node_repr]: nodes in such a graphical model may represent populations of neurons, distinct cell-types, different regions within the brain, or components of a latent variable represented in the brain. -->

[^edge_color]: will change the color scheme for final figure. Likely using orange and blue to denote closed and open-loop interventions. Will also add in indication of severed edges




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