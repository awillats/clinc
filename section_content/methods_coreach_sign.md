<!-- NOTE:
context needed: 
S_k 
-->
<!-- NOTE: 
used to use convention dR/dS to represent change in correlation (R) with respect to source variance (S). For consistency with other sections, changed this to dr^2. 
But this needs verifying. and it might be nice to have a more general notation like D for dependence ... ?
 -->
<!-- TODO:
this section already provides a good walk-through of the figure ... 
perhaps we should be using these indices in the figure itself?
 -->
<!-- TODO: [mechanical] 
turn this section back into "cases" format
- beware, cases might not play nicely with pandoc
-->

<!-- NOTE: for now, removing text about co-reachability. most of what we want to convey can be expressed in terms of multiple reachability statements instead, which is perhaps simpler -->
<!-- The impact of intervention on correlations can be summarized through an expression we label co-reachability $\text{CoReach}(i,j|S_k)$ which extends the notation of reachability to three nodes. Specifically, $\text{CoReach}(i,j|S_k)\neq0$ indicates that source $S_k$ has direct or indirect connections to both nodes $i$ and $j$. A useful distillation of this mapping is... -->

The impact of intervention on correlations can be understood from the intervention's location relative to causal circuit connections. One useful distillation of this concept is to understand the sign of $\frac{dr^2_{ij}}{dS_k}$, that is whether increasing the variance of an intervention at node $k$ increases or decreases the correlation between nodes $i$ and $j$

In a simulated network A→B [(fig. variance)](#fig-var) we demonstrate predicted and emprirical correlations between a pair of nodes as a function of intervention type, location, and variance. A few features are present which provide a general intuition for the impact of intervention location in larger circuits: First, interventions "upstream" of a true connection [(lower left, fig. variance)](#fig-var) tend to increase the connection-related variance, and therefore strengthen the observed correlations.

![](/figures/misc_figure_sketches/quant_r2_prediction_common.png)


`if:`
$$\text{Reach}(S_k→i) \neq 0 \\ \text{Reach}(i→j) \neq 0$$
`then:`
$$ \frac{dr^2}{dS_k} > 0$$

Second, interventions affecting only the downstream node [(lower right, fig. variance)](#fig-var) of a true connection introduce variance which is independent of the connection A→B, decreasing the observed correlation.  

`if:`
$$\text{Reach}(S_k → j) = 0 \\ \text{Reach}(S_k → j) \neq 0 $$
`then:`
$$ \frac{dr^2}{dS_k} < 0$$

Third, interventions which reach both nodes will tend to increase the observed correlations [(upper left, fig. variance)](#fig-var), moreover this can be achieved even if no direct connection $i→j$ exists.

`if:`
$$\text{Reach}(S_k → i) \neq 0 \\ \text{Reach}(S_k → j) \neq 0 \\ \text{Reach}(i → j) = 0 $$
`then:`
$$\frac{dr^2}{dS_k} > 0$$

Notably, the impact of an intervention which is a "common cause" for both nodes depends on the relative weighted reachability between the source and each of the nodes. Correlations induced by a common cause are maximized when the input to each node is equal, that is $\widetilde{W}_{S_k→i} \approx \widetilde{W}_{S_k→j}$ (upper right * in [fig. variance](#fig-var)). If i→j are connected $\widetilde{W}_{S_k→i} \gg \widetilde{W}_{S_k→j}$ results in an variance-correlation relationship similar to the "upstream source" case (increasing source variance increases correlation $\frac{dr^2}{dS_k} > 0$),
 while $\widetilde{W}_{S_k→i} \ll \widetilde{W}_{S_k→j}$ results in a relationship similar to the "downstream source" case ($\frac{dr^2}{dS_k} < 0$)[^verify_drds]

[^verify_drds]: TODO: verify not 100% sure this is true, the empirical results are really pointing to dr^2/dW<0 rather than dr^2/dS<0. Also this should really be something like $\frac{d|R|}{dS}$ or $\frac{dr^2}{dS}$ since these effects decrease the *magnitude* of correlations. I.e. if $\frac{d|R|}{dS} < 0$ increasing $S$ might move $r$ from $-0.8$ to $-0.2$, i.e. decrease its magnitude not its value.