# Building blocks

Let $s \in \mathbb{R}^p$ denote exogenous inputs to each of the $p$ nodes, and $W \in \mathbb{R}^{p \times p}$ denote the matrix of connection strengths such that $$W_{ij} = \text{strength of $j \rightarrow i$ connection}.$$

We'll assume for now that all functional relationships between nodes are linear, and all exogenous noise is iid gaussian.[^lingauss]

For intuition, note that:
 - $(s)_j$ denotes variance in node $j$ due to length-0 connections,
 - $(W s)_j$ denotes variance in node $j$ due to length-1 connections
 - $(W^2 s)_j$ denotes variance in node $j$ due to length-2 connections
 - ...
 - $(\sum_{i=1}^p W^{i-1} s)_j$ denotes the total variance in node $j$.

## Derivation of expression for (co)variances

In a linear/gaussian network, we have $x = Wx + e$, where $x \in \mathbb{R}^p$ is the vector of values taken by the $p$ nodes of the circuit and $e \sim \mathcal{N}(0,\mathrm{diag}(s))$. Rearranging this expression yields $X = (I-W)^{-1} s$.

Defining $X \in \mathbb{R}^{p \times n}$ and $E \in \mathbb{R}^{p \times n}$ as the matrix of $n$ observations of $x$ and $s$, we can write
$$
\begin{align*}
\Sigma = \mathrm{cov}(X) &= \mathbb{E}\left[X X^T\right] \\
&= \mathbb{E}\left[ (I-W)^{-1} E E^T (I-W)^{-1} \right] \\
&= (I-W)^{-1} \mathrm{cov}(E) (I-W)^{-T} \\
&= (I-W)^{-1} \mathrm{diag}(s) (I-W)^{-T}.
\end{align*}
$$

It is a fact that $(I-A)^{-1} = \sum_{n=0}^{\infty} A^n$ when $|\lambda_i(A)| < 1$ for all eigenvalues $\lambda_i$ of $A$. We'll make use of the matrix $\widetilde{W} = \sum_{k=0}^{p-1} W^k$, which intuitively denotes the "effective" or "total" connection strengths between every pair of nodes in the circuit, including both direct and indirect links. That is, $\widetilde{W}_{ij}$ tells us how much variance at node $i$ would result from injecting a unit of variance at node $j$.[^sumlim]

To simplify a bit, we can equivalently write $$\Sigma_{ij} = \sum_{k=1}^p \widetilde{W}_{ik} \widetilde{W}_{jk} s_k.$$

## Expression for $r^2(i,j)$ under passive observation

Using the expression for $\Sigma$ above, we have
$$
\begin{align*}
r^2(i,j) &= \frac{\Sigma_{ij}}{\sqrt{\Sigma_{ii} \Sigma_{jj}}} \\
&= \frac{\sum_{k=1}^p \widetilde{W}_{ik} \widetilde{W}_{jk} s_k}{\sqrt{\left(\sum_{k=1}^p \widetilde{W}_{ik}^2 s_k\right)\left(\sum_{k=1}^p \widetilde{W}_{jk}^2 s_k\right)}}.
\end{align*}
$$

## Impact of control

### Open-loop control

The application of open-loop control on node $c$ can be modeled as:
1. Add an arbitrary amount of variance to $s_c$: $s_c \leftarrow s_c + s_c^{(OL)}$.

### Closed-loop control

The application of closed-loop control on node $c$ can be modeled as:
1. Sever the inputs to node $c$ by setting $W_{c,:} = 0$, then
2. Set the exogenous noise of node $c$ by setting $s_c$ to any arbitrary value. Because $c$'s inputs have been severed, this exogenous noise will be node $c$'s output variance.

Note that step 1 above will result in $\widetilde{W}_{i,:} = 0$ except for $\widetilde{W}_{i,i} = 1$.

### Impact of CL control on $r^2(i,j)$

We might be interested in $\Delta_c^{(CL)}r^2(i,j)$, defined as "the amount that $r^2(i,j)$ increases when we place closed-loop control on node $c$." Unfortunately, writing out a general expression for this gets ugly fairly quickly.

[^sumlim]: We can use $p-1$ as an upper limit on the sum $\widetilde{W} = \sum_{k=0}^{p-1} W^k$ when there are no recurrent connections. Later we can characterize what type of recurrent connections are ok.
