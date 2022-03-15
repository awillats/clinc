# First thoughts on identifiability

We begin with the simple linear dynamical system
\[
\begin{cases} \dot{x} = Ax \\ y = Cx + \eta \end{cases}
\]
where $A$ is the adjacency matrix
\[
\underbrace{\begin{bmatrix} \dot{x}_A \\ \dot{x}_B \\ \dot{x}_C \end{bmatrix}}_{\dot{x}} =
\underbrace{\begin{bmatrix}
    w_{AA} & w_{AB} & w_{AC} \\
    w_{BA} & w_{BB} & w_{BC} \\
    w_{CA} & w_{CB} & w_{CC}
\end{bmatrix}}_{A}
\underbrace{\begin{bmatrix}
    x_A \\
    x_B \\
    x_C
\end{bmatrix}}_{x}
\]

Our first question is: What can $A$ tell us about the identifiability of causal relationships between elements of $x$?

## Some definitions

**Let $\mathrm{Reach}(\cdot) \colon \R^{n \times n} \to \{0,1\}^{n \times n}$** be the operator that maps an adjacency matrix to the binary reachability matrix, in which entry $(i,j)$ is $1$ if $x_i$ is reachable from $x_j$ and $0$ otherwise. 
- In a directed graph, we say that $x_i$ is reachable from $x_j$ if there exists a series of head-to-tail connections from $x_j$ to $x_i$.[^fn][^index]
- In an undirected graph, we say that $x_i$ is reachable from $x_j$ if there exists a series of undirected connections from $x_j$ to $x_i$.
[^fork]

[^fork]: 🚧 in code I've also implemented what I call "fork-shaped" reachability which captures whether a node `i` can be reached by any of *the parents of* node `j` and "collider-shaped" reachability which captures whether a node `i` and node `j` shared descendants - *verify this, include above if useful*

[^index]: to-do resolve indexing convention
[^fn]: Note that for a binary adjacency matrix $A$, $A^k_{ij} = 1$ $\iff$ $x_i$ is reachable from $x_j$ in $k$ "hops." Using this fact and the fact that $e^A = \sum_{k \geq 0} \tfrac{1}{k!} A^k$, we can compute $\mathrm{Reach}(\cdot)$ as $\mathrm{Reach}(A) = \mathrm{Binarize}(\mathrm{expm}(\mathrm{Binarize}(A)))$.


**Let $\kappa_i \colon \R^{n \times n} \to \R^{n \times n}$** be the operator that applies closed-loop control to fix the output of node $x_i$ regardless of the value of its parents.[^ctrl_row]
 
 [^ctrl_row]: This can be implemented as removing node $i$'s parents, i.e., setting row $i$ of $A$ to zero.

**Let $\mathcal{U} \colon \R^{n \times n} \to \R^{n \times n}$** be the operator that transforms an adjacency matrix to its "undirected" equivalent.[^undirect]

[^undirect]: This can be implemented as $\mathcal{U}(A) = (A \neq 0) ~\vert~ (A \neq 0)^T)$ where $\vert$ denotes the element-wise OR operator.

## Supporting observations 
- The outputs of nodes $i,j$ are uncorrelated if $\mathrm{Reach}(\mathcal{U}(A))_{ij} = 0$.
- Closed-loop control "severs a connection" if $\mathrm{Reach}(A)_{ij} \neq 0$, but $\mathrm{Reach}(\kappa_i(A))_{ij} = 0$.

## Classes of ambiguity
- Two circuits are "passively ambiguous" if 
  $\mathrm{Reach}(\mathcal{U}(A)) == \mathrm{Reach}(\mathcal{U}(B))$.
- Two circuits are "open loop ambiguous" if
$\mathrm{Reach}(A) == \mathrm{Reach}(B)$.
- Two circuits are "closed loop ambiguous" *(given control at node i)* if $\mathrm{Reach}(\kappa_i(A)) == \mathrm{Reach}(\kappa_i(B))$.
- Two circuits are "closed loop ambiguous" *(given control at any one node)* if 
$\mathrm{Reach}(\kappa_i(A)) == \mathrm{Reach}(\kappa_i(B)) \\
\forall i = 1, \dots, n$.


<details><summary> original LaTeX </summary>
```latex
\def\Reach{\mathcal{R}}%{\mathrm{Reach}}
\def\Control{\kappa_i}
\def\CL{\mathcal{C}}
\def\OL{\mathcal{O}}
\def\pluseqq{\mathrel{{+}{=}}}
\def\Undirect{\mathcal{U}}%{\mathcal{U}}

\paragraph{Some definitions.}
\begin{enumerate}
    \item Let $\mathrm{Reach}(\cdot) \colon \R^{n \times n} \to \{0,1\}^{n \times n}$ be the operator that maps an adjacency matrix to the binary reachability matrix, in which entry $(i,j)$ is $1$ if $x_i$ is reachable from $x_j$ and $0$ otherwise. In a directed graph, we say that $x_i$ is reachable from $x_j$ if there exists a series of head-to-tail connections from $x_j$ to $x_i$.\footnote{Note that for a binary adjacency matrix $A$, $A^k_{ij} = 1$ $\iff$ $x_i$ is reachable from $x_j$ in $k$ "hops." Using this fact and the fact that $e^A = \sum_{k \geq 0} \tfrac{1}{k!} A^k$, we can compute $\mathrm{Reach}(\cdot)$ as $\mathrm{Reach}(A) = \mathrm{Binarize}(\mathrm{expm}(\mathrm{Binarize}(A)))$.} In an undirected graph, we say that $x_i$ is reachable from $x_j$ if there exists a series of undirected connections from $x_j$ to $x_i$.
    \item Let $\kappa_i \colon \R^{n \times n} \to \R^{n \times n}$ be the operator that applies closed-loop control to fix the output of node $x_i$ regardless of the value of its parents.\footnote{This can be implemented as removing node $i$'s parents, i.e., setting row $i$ of $A$ to zero.}
    \item Let $\mathcal{U} \colon \R^{n \times n} \to \R^{n \times n}$ be the operator that transforms an adjacency matrix to its "undirected" equivalent.\footnote{This can be implemented as $\mathcal{U}(A) = (A \neq 0) ~\vert~ (A \neq 0)^T)$ where $\vert$ denotes the element-wise OR operator.}
\end{enumerate}

\paragraph{Supporting observations.}
\begin{enumerate}
    \item The outputs of nodes $i,j$ are uncorrelated if $\mathrm{Reach}(\mathcal{U}(A))_{ij} = 0$.
    \item Closed-loop control "severs a connection" if $\mathrm{Reach}(A)_{ij} \neq 0$, but $\mathrm{Reach}(\kappa_i(A))_{ij} = 0$.
\end{enumerate}

\paragraph{Adam's rules of ID.}
\begin{enumerate}  
    \item Two circuits are "passively ambiguous" if $\mathrm{Reach}(\mathcal{U}(A)) == \mathrm{Reach}(\mathcal{U}(B))$.
    \item Two circuits are "open loop ambiguous" if $\mathrm{Reach}(A) == \mathrm{Reach}(B)$.
    \item Two circuits are "closed loop ambiguous" \textit{given control at node i} if $\mathrm{Reach}(\kappa_i(A)) == \mathrm{Reach}(\kappa_i(B))$.
    \item Two circuits are "closed loop ambiguous" \textit{(given control at any one node)} if $\mathrm{Reach}(\kappa_i(A)) == \mathrm{Reach}(\kappa_i(B))$ for $i = 1, \dots, n$.
\end{enumerate}
```
</details>