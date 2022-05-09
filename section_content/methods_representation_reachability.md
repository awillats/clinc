<!-- [^exog]: the most important property of $e$ for the math to work, i believe, is that they're random variables independent of each other. This is not true in general if E is capturing input from common sources, other nodes in the network. I think to solve this, we'll need to have an endogenous independent noise term and an externally applied (potentially common) stimulus term. -->



<!-- 
NOTE:able references
@fornito2016connectivity does a good job establishing what a connectivity matrix means, and (awkward) indexing convention
@skiena2011transitive covers algorithms for computing reachability
 -->
<!-- Representations of network connectivity. {#sec:methods-reach} -->

Different mathematical representations of circuits can elucidate different connectivity properties. For example, consider the circuit $A \rightarrow B \leftarrow C$. This circuit can be modeled by the dynamical system
\[
\begin{cases}
\dot{x}_A &= f_A(e_A) \\
\dot{x}_B &= f_B(x_A, x_C, e_B) \\
\dot{x}_C &= f_C(e_C),
\end{cases}
\]
where $e_A$, $e_B$, and $e_C$ represent independent private noise sources for each node.
<!-- exogenous inputs that are inputs from other variables and each other[^exog]. -->

When the system is linear we can use matrix notation to describe the impact of each node on the others [@fornito2016connectivity]:
\[
\mathbf{x}_{t+1} = \mathbf{W x}_t + \mathbf{Se}_t,
\]
where $\mathbf{x_t} \in \mathbb{R}^p$ denotes the state of each of the $p$ nodes at time $t$, $\mathbf{e_t} \in \mathbb{R}^p$ denotes the instantiation of each node's (independent and identically-distributed) private noise variance at time $t$, and $\mathbf{S} \in \mathbb{R}^{p \times p}$ represents a diagonal matrix where entries $s_{i} = \mathbf{S}_{ii}$ represent the noise variance at node $i$.

$\mathbf{W}$ represents the *adjacency matrix*:
<!-- \[
\mathbf{W} = \begin{bmatrix}
    w_{AA} & w_{AB} & w_{AC} \\
    w_{BA} & w_{BB} & w_{BC} \\
    w_{CA} & w_{CB} & w_{CC}
\end{bmatrix}.
\] -->
\[
\mathbf{W} = \begin{bmatrix}
    w_{A→A} & w_{B→A} & w_{C→A} \\
    w_{A→B} & w_{B→B} & w_{C→B} \\
    w_{A→C} & w_{B→C} & w_{C→C}
\end{bmatrix}.
\]
The adjacency matrix captures directional first-order connections in the circuit. The entries of $\mathbf{W}_{ij} = w_{j→i}$ describe how activity in one node $x_j$ changes in response to activity in another $x_i$. For example, the circuit $A \rightarrow B \leftarrow C$, would be representted by $w_{A→B} \neq 0$ and $w_{C→B} \neq 0$.

<!-- @fornito2016connectivity -->

**Reachability.**
Our goal is to reason about the relationship between underlying causal structure (which we want to understand) and the correlation or information shared by pairs of nodes in the circuit (which we can observe). Quantities based on the  adjacency matrix and weighted reachability matrix bridge this gap, connecting the causal structure of a circuit to the correlation structure its nodes will produce.

The directional $k^{\mathrm{th}}$-order connections in the circuit are similarly described by the matrix $\mathbf{W}^k$, so the *weighted reachability matrix*
\[
    \mathbf{\widetilde{W}} = \sum_{k=0}^{\infty} \mathbf{W}^k
\]
describes the total impact -- through both first-order (direct) connections and higher-order (indirect) connections -- of each node on the others [@skiena2011transitive]. Whether node $j$ is "reachable" from node $i$ by a direct or indirect connection is thus indicated by $\mathbf{\widetilde{W}}_{j→i} \neq 0$, with the magnitude of $\mathbf{\widetilde{W}}_{j→i}$ indicating sensitive node $j$ is to a change in node $i$.

This notion of reachability, encoded by the pattern of nonzero entries in $\mathbf{\widetilde{W}}$, allows us to determine when two nodes will be correlated (or more generally, contain information about each other). Moreover, as described in sections [# predicting correlation](#sec:methods-predict-corr), [# intervention and variance](#sec:methods-intervention-var) quantities derived from these representations can also be used to describe the impact of open- and closed-loop interventions on circuit behavior, allowing us to quantitatively explore the impact of these interventions on the identifiability of circuits.




<!-- TODO: Adam, write out the dynamical system version of this -->

<!-- Topologically sorted implementation:
\[
\begin{align}
X^- &:= E\\
X &:= X^-W + E
\end{align}
\] -->

<!-- NOTE: have to be careful with this. this almost looks like a dynamical system, but isn't. In simulation we're doing something like an SCM, where the circuit is sorted topologically then computed sequentially. have to resolve / compare these implementations -->



<!-- 
TODO: or in the contemporaneous domain ..

\[
\mathbf{x_{t}} = \mathbf{\widetilde{W}Se_t},
\]
-->