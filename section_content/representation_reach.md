[^exog]: the most important property of $e$ for the math to work, i believe, is that they're random variables independent of each other. This is not true in general if E is capturing input from common sources, other nodes in the network. I think to solve this, we'll need to have an endogenous independent noise term and an externally applied (potentially common) stimulus term.
[^sim_repr]: have to be careful with this. this almost looks like a dynamical system, but isn't. In simulation we're doing something like an SCM, where the circuit is sorted topologically then computed sequentially. have to resolve / compare these implementations

Different mathematical representations of circuits can elucidate different connectivity properties. For example, consider the circuit $A \rightarrow B \leftarrow C$. This circuit can be modeled by the dynamical system
\[
\begin{cases}
\dot{x}_A &= f_A(e_A) \\
\dot{x}_B &= f_B(x_A, x_C, e_B) \\
\dot{x}_C &= f_C(e_C),
\end{cases}
\]
where $e_A$, $e_B$, and $e_C$ represent exogenous inputs that are inputs from other variables and each other[^exog].

When the system is linear we can use matrix notation to describe the impact of each node on the others:[^sim_repr]
\[
x_{t+1} = W x_t + e_t,
\]
where $x_t \in \mathbb{R}^p$ denotes the state of each of the $p$ nodes at time $t$, and $e_t \in \mathbb{R}^p$ denotes the instantiation of each node's (independent and identically-distributed) private noise variance at time $t$.

<!-- TODO: Adam, write out the dynamical system version of this -->

<!-- <details><summary>various implementations</summary>

Topologically sorted implementation:
\begin{align}
X^- &:= E\\
X &:= X^-W + E
\end{align}


</details> -->

where $W$ represents the *adjacency matrix*
\[
W = \begin{bmatrix}
    w_{AA} & w_{AB} & w_{AC} \\
    w_{BA} & w_{BB} & w_{BC} \\
    w_{CA} & w_{CB} & w_{CC}
\end{bmatrix}.
\]
In the circuit $A \rightarrow B \leftarrow C$, we would have $w_{AB} \neq 0$ and $w_{CB} \neq 0$.

The adjacency matrix captures directional first-order connections in the circuit: $w_{ij}$, for example, describes how activity in $x_j$ changes in response to activity in $x_i$.

Our goal is to reason about the relationship between underlying causal structure (which we want to understand) and the correlation or information shared by pairs of nodes in the circuit (which we can observe). Quantities based on the  adjacency matrix and weighted reachability matrix bridge this gap, connecting the causal structure of a circuit to the correlation structure its nodes will produce.

The directional $k^{\mathrm{th}}$-order connections in the circuit are similarly described by the matrix $W^k$, so the *weighted reachability matrix*
\[
    \widetilde{W} = \sum_{k=0}^{\infty} W^k
\]
describes the total impact -- through both first-order (direct) connections and higher-order (indirect) connections -- of each node on the others. Whether node $j$ is "reachable" (Skiena 2011) from node $i$ by a direct or indirect connection is thus indicated by $\widetilde{W}_{ij} \neq 0$, with the magnitude of $\widetilde{W}_{ij}$ indicating sensitive node $j$ is to a change in node $i$.

This notion of reachability, encoded by the pattern of nonzero entries in $\widetilde{W}$, allows us to determine when two nodes will be correlated (or more generally, contain information about each other). Moreover, as we will describe in Sections [REF] and [REF], quantities derived from these representations can also be used to describe the impact of open- and closed-loop interventions on circuit behavior, allowing us to quantitatively explore the impact of these interventions on the identifiability of circuits.
