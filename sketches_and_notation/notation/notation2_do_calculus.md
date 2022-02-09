```latex
\subsubsection{Do-calculus}

The do-calculus tells us when and how we can compute interventional distributions from observational data. Our goal is to extend this result to control, including the possibility of open loop (i.e., imperfect) interventions.

\begin{theorem}[Rules of $do$-calculus]
    \label{thm:do-calculus}
    Let $\G$ be a directed acyclic graph associated with a causal model inducing probability distributions $p(\cdot)$. Define $\G_{\underline{X}}$ to be the causal graph with connections leaving $X$ removed, and $\G_{\overline{X}}$ to be the causal graph with connections entering $X$ removed. Then for any disjoint subsets of variables $X, Y, Z, W$:
    \begin{enumerate}
        \item (Insertion/deletion of observations) $p(y \mid do(x), z, w) = p(y \mid do(x), w)$ if $Y \perp Z \mid X, W$ in $\G_{\overline{X}}$.
        \item (Action/observation exchange) $p(y \mid do(x), do(z), w) = p(y \mid do(x), z, w)$ if $Y \perp Z \mid X, W$ in $\G_{\overline{X},\underline{Z}}$.
        \item (Insertion/deletion of actions) $p(y \mid do(x), do(z), w) = p(y \mid do(x), w)$ if $Y \perp Z \mid X, W$ in $\G_{\overline{X},\overline{Z(W)}}$, where $Z(W)$ is the set of nodes that are not ancestors of any node in $W$ in $\G_{\overline{X}}$.
    \end{enumerate}
\end{theorem}

\begin{proof} The following proofs can be found in the appendix of \cite{pearl1995causal}:
    \begin{enumerate}
        \item Intervening on $X$ in $\G$ produces the modified graph $\G_{\overline{X}}$, the graph with arrows entering $X$ removed. Since by assumption $Y \perp Z \mid X, W$ in this modified graph, we have the conditional independence statement $p(y \mid do(x), z, w) = p(y \mid do(x), w)$.
        \item Intervening on $X$ in $\G$ produces the modified graph $\G_{\overline{X}}$, and the assumption $Y \perp Z \mid X, W$ in $\G_{\overline{X},\underline{Z}}$ therefore guarantees that all backdoor paths from $Z$ to $Y$ in $\G_{\overline{X}}$ are blocked\footnote{A backdoor path from $Z$ to $Y$ is which the arrow connected to $Z$ \emph{enters} $Z$.}. The effect on $Y$ of conditioning and intervening on $Z$ are therefore the same.
        \item todo
    \end{enumerate}
\end{proof}

\begin{theorem}[Completeness of the $do$-calculus (todo-citation)]
    \label{thm:do-calculus-completeness}
    The $do$-calculus is complete. That is, a quantity $p(y \mid do(x), z)$ is identifiable (from observational data\footnote{Todo: work through proof of this fact using open/closed loop control}) if and only if it can be reduced to a $do$-free expression using the $do$-calculus.
\end{theorem}

\begin{corollary}[Identifiability of neural circuits using control]
    The connection $X \to Y$ is identifiable under closed-loop control scheme $\mathbb{C}$ if and only if $p(y \mid do(x))$ can be computed from the distributions induced by $\mathbb{C}$ using the rules of Theorem \ref{thm:do-calculus}.
\end{corollary}
```