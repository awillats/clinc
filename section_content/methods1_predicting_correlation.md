A linear Gaussian circuit can be described by 1) the variance of the Gaussian private (independent) noise at each node, and 2) the weight of the linear relationships between each pair of connected nodes. Let $s \in \mathbb{R}^p$ denote the variance of each of the $p$ nodes in the circuit, and $W \in \mathbb{R}^{p \times p}$ denote the matrix of connection strengths such that $$W_{ij} = \text{strength of $i \to j$ connection}.$$

Note that $\left[(W^T) s\right]_j$ gives the variance at node $j$ due to length-1 (direct) connections, and more generally, $\left[ (W^T)^k s \right]_j$ gives the variance at node $j$ due to length-$k$ (indirect) connections. The *total* variance at node $j$ is thus $\left[ \sum_{k=0}^{\infty} (W^T)^k s \right]_j$.

Our goal is to connect private variances and connection strengths to observed pairwise correlations in the circuit. Defining $X \in \mathbb{R}^{p \times n}$ as the matrix of $n$ observations of each node, we have[^covariance-derivation]
$$
\begin{aligned}
    \Sigma &= \mathrm{cov}(X) = \mathbb{E}\left[X X^T\right] \\
    &= (I-W^T)^{-1} \mathrm{diag}(s) (I-W^T)^{-T} \\
    &= \widetilde{W} \mathrm{diag}(s) \widetilde{W}^T,
\end{aligned}
$$
where $\widetilde{W} = \sum_{k=0}^{\infty} (W)^k$ denotes the *weighted reachability matrix*, whose $(i,j)^\mathrm{th}$ entry indicates the total influence of node $i$ on node $j$ through both direct and indirect connections.[^sum-limits] That is, $\widetilde{W}_{ij}$ tells us how much variance at node $j$ would result from injecting a unit of private variance at node $i$. We can equivalently write $\Sigma_{ij} = \sum_{k=1}^p \widetilde{W}_{ik} \widetilde{W}_{jk} s_k$.

Under passive observation, the squared correlation coefficient can thus be written as
$$
\begin{aligned}
    r^2(i,j) &= \frac{\Sigma_{ij}}{\Sigma_{ii} \Sigma_{jj}} \\
    &= \frac{\left( \sum_{k=1}^p \widetilde{W}_{ik} \widetilde{W}_{jk} s_k \right)^2}{\left(\sum_{k=1}^p \widetilde{W}_{ik}^2 s_k\right)\left(\sum_{k=1}^p \widetilde{W}_{jk}^2 s_k\right)}.
\end{aligned}
$$

This framework also allows us to predict the impact of open- and closed-loop control on the pairwise correlations we expect to observe. To model the application of open-loop control on node $c$, we add an arbitrary amount of private variance to $s_c$: $s_c \leftarrow s_c + s_c^{(OL)}$. To model the application of closed-loop control on node $c$, we first sever inputs to node $c$ by setting $W_{k,c} = 0$ for $k = 1, \dots p$, and then set the private variance of node $c$ by setting $s_c$ to any arbitrary value[^arb-variance]. Because $c$'s inputs have been severed, this private noise will become exactly node $c$'s output variance.

[^arb-variance]: TODO: to any target value?

!!!! todo [Matt:] add table from `sketches_and_notation/intro-background/causal_vs_expt.md` and modify text above to match

[^covariance-derivation]: To see this, denote by $E \in \mathbb{R}^{p \times n}$ the matrix of $n$ private noise observations for each node. Note that $X = W^T X + E$, so $X = E(I-W^T)^{-1}$. The covariance matrix $\Sigma = \mathrm{cov}(X) = \mathbb{E}\left[X X^T\right]$ can then be written as $\Sigma = \mathbb{E}\left[ (I-W^T)^{-1} E E^T (I-W^T)^{-1} \right] = (I-W^T)^{-1} \mathrm{cov}(E) (I-W^T)^{-T} = (I-W^T)^{-1} \mathrm{diag}(s) (I-W^T)^{-T}$.

[^sum-limits]: We can use $p-1$ as an upper limit on the sum $\widetilde{W} = \sum_{k=0}^{\infty} W^k$ when there are no recurrent connections.
