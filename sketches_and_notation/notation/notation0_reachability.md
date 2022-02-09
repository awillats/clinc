Our first question is: What can $A$ tell us about the identifiability of causal relationships between elements of $x$?
```latex
\paragraph{Some definitions.}
\begin{enumerate}
    \item Let $\Reach(\cdot) \colon \R^{n \times n} \to \{0,1\}^{n \times n}$ be the operator that maps an adjacency matrix to the binary reachability matrix, in which entry $(i,j)$ is $1$ if $x_i$ is reachable from $x_j$ and $0$ otherwise. In a directed graph, we say that $x_i$ is reachable from $x_j$ if there exists a series of head-to-tail connections from $x_j$ to $x_i$.\footnote{Note that for a binary adjacency matrix $A$, $A^k_{ij} = 1$ $\iff$ $x_i$ is reachable from $x_j$ in $k$ ``hops.'' Using this fact and the fact that $e^A = \sum_{k \geq 0} \tfrac{1}{k!} A^k$, we can compute $\Reach(\cdot)$ as $\Reach(A) = \mathrm{Binarize}(\mathrm{expm}(\mathrm{Binarize}(A)))$.} In an undirected graph, we say that $x_i$ is reachable from $x_j$ if there exists a series of undirected connections from $x_j$ to $x_i$.
    \item Let $\Control \colon \R^{n \times n} \to \R^{n \times n}$ be the operator that applies closed-loop control to fix the output of node $x_i$ regardless of the value of its parents.\footnote{This can be implemented as removing node $i$'s parents, i.e., setting row $i$ of $A$ to zero.}
    \item Let $\Undirect \colon \R^{n \times n} \to \R^{n \times n}$ be the operator that transforms an adjacency matrix to its ``undirected'' equivalent.\footnote{This can be implemented as $\Undirect(A) = (A \neq 0) ~\vert~ (A \neq 0)^T)$ where $\vert$ denotes the element-wise OR operator.}
\end{enumerate}

\paragraph{Supporting observations.}
\begin{enumerate}
    \item The outputs of nodes $i,j$ are uncorrelated if $\Reach(\Undirect(A))_{ij} = 0$.
    \item Closed-loop control ``severs a connection'' if $\Reach(A)_{ij} \neq 0$, but $\Reach(\Control(A))_{ij} = 0$.
\end{enumerate}

\paragraph{Adam's rules of ID.}
\begin{enumerate}  
    \item Two circuits are ``passively ambiguous'' if $\Reach(\Undirect(A)) == \Reach(\Undirect(B))$.
    \item Two circuits are ``open loop ambiguous" if $\Reach(A) == \Reach(B)$.
    \item Two circuits are ``closed loop ambiguous'' \textit{given control at node i} if $\Reach(\Control(A)) == \Reach(\Control(B))$.
    \item Two circuits are ``closed loop ambiguous'' \textit{(given control at any one node)} if $\Reach(\Control(A)) == \Reach(\Control(B))$ for $i = 1, \dots, n$.
\end{enumerate}
```