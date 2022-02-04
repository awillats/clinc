```latex 
\subsection{Identifiability with closed-loop control}

What causal relationships in a graph are identifiable when closed-loop control is applied to certain nodes? Here we approach this question by deriving a form of the do-calculus to the linear dynamical system \eqref{eq:lds}.

\subsection{Identifiability with open-loop control}
\begin{figure}
    \centering
    \begin{tabular}{ccc}
        \begin{tikzpicture}
            \node (X) {$X$};
            \node[right of=X] (Y) {$Y$};
            \node[left of=X, yshift=+1.5em] (Z1) {$Z_1$};
            \node[left of=X, yshift=-1.5em] (Z2) {$Z_2$};
            \node[below of=X] (W) {$W$};
    	    \path[->] (Z1) edge (X);
    	    \path[->] (Z2) edge (X);
    	    %\path[->] (W) edge (X);
    	    \path[->] (X) edge (Y);
    	    \path[->, bend left=45] (Z1) edge (Y);
    	\end{tikzpicture} \qquad & \qquad
    	\begin{tikzpicture}
    	    \node (X) {$X$};
            \node[right of=X] (Y) {$Y$};
            \node[left of=X, yshift=+1.5em] (Z1) {$Z_1$};
            \node[left of=X, yshift=-1.5em] (Z2) {$Z_2$};
            \node[below of=X] (W) {$W$};
    	    %\path[->] (Z1) edge (X);
    	    %\path[->] (Z2) edge (X);
    	    \path[->] (W) edge (X);
    	    \path[->] (X) edge (Y);
    	    \path[->, bend left=45] (Z1) edge (Y);
	    \end{tikzpicture} \qquad & \qquad
	    \begin{tikzpicture}
            \node (X) {$X$};
            \node[right of=X] (Y) {$Y$};
            \node[left of=X, yshift=+1.5em] (Z1) {$Z_1$};
            \node[left of=X, yshift=-1.5em] (Z2) {$Z_2$};
            \node[below of=X] (W) {$W$};
    	    \path[->] (Z1) edge (X);
    	    \path[->] (Z2) edge (X);
    	    \path[->] (W) edge (X);
    	    \path[->] (X) edge (Y);
    	    \path[->, bend left=45] (Z1) edge (Y);
	    \end{tikzpicture} \\~\\
	    (a) Original circuit \qquad & \qquad (b) CL control \qquad & \qquad (c) OL control
	\end{tabular}
	\caption{Modifications of circuit to represent closed- and open-loop control. $Z_1$ denotes nodes that are parents of both $X$ and $Y$; $Z_2$ denotes nodes that are parents of $X$ but not $Y$.}
    \label{fig:effective-dags-after-control}
\end{figure}

In \cite[Ch.~4.2]{pearl2009causality}, Pearl proposes an identification framework for a broader class of interventions that can be described as $x \coloneqq g(z)$, where $g$ is some (potentially stochastic) function depending on a separate set of nodes $z$. The effect on $Y$ of an intervention on $X$ that depends on another set of nodes\footnote{This must be true in an acyclic graph because $Z \to X$. However, this non-descendants assumption does not necessarily hold in presence of feedback, in which case the analysis in this section breaks down.} $W$ is
\begin{align}
    p(y \mid do(x=g(w))) &= \int_w p(y \mid do(x=g(w)), w) p(w \mid do(x=g(w))) dw \qquad \text{(marginalization)} \\
    &= \int_w p(y \mid do(x=g(w)), w) p(w) dw \qquad \text{($W \notin \mathrm{De}(X)$)} \\
    &= \E_{w} \left[ p(y \mid do(x=g(w)), w) \right].
\end{align}

Therefore, \emph{we can determine the causal influence of $x$ on $y$, $p(y \mid \widehat{x})$, if we can obtain $p(y \mid \widehat{x}, w)$ and $p(w)$ using measurements from our control scheme}.

To see how we can apply this framework to our model, denote $Z \coloneqq \mathrm{Pa}(X)$, and represent the (open- or closed-loop) control input by $W$. Compared to the original circuit (Figure \ref{fig:effective-dags-after-control}a), applying closed-loop control replaces the causal link(s) $Z \to X$ with $W \to X$ (Figure \ref{fig:effective-dags-after-control}b), while applying open-loop control simply adds the causal link $W \to X$ (Figure \ref{fig:effective-dags-after-control}c).

Applying similar analysis to our model of \emph{closed-loop control} (Figure \ref{fig:effective-dags-after-control}(b)) yields
\begin{align}
    p(y \mid do(x = W)) &= \int_w \int_{z_2} p(y \mid do(x = W), W, z_2) p(W, z_2 \mid do(x = W)) dw dz_2 \qquad \text{(marginalization)} \\
    &= \int_w \int_{z_2} p(y \mid do(x=W), W, z_2) p(W,z_2) dw dz_2 \qquad \text{($W,Z_2 \notin De(X)$)} \\
    &= \int_w \int_{z_2} p(y \mid do(x=W), W, z_2) p(W) p(z_2) dw dz_2 \qquad \text{($W \perp Z_2$)} \\
    &= \int_{z_2} p(y \mid do(x=W), z_2) p(z_2) dz_2 \qquad \text{($p(W) = \delta_{W=W}$)} \\
    &= \E_{z_2} \left[ p(y \mid do(x=W), z_2) \right].
\end{align}
Therefore, \emph{we can determine the causal influence of $x$ on $y$, $p(y \mid \widehat{x})$, if we can obtain $p(y \mid \widehat{x}, z_2)$ and $p(z_2)$}.

Applying similar analysis to our model of \emph{open-loop control} (Figure \ref{fig:effective-dags-after-control}(c)) yields
\begin{align}
    p(y \mid do(x = f(z) + W)) &= \int_w \int_z p(y \mid do(x = f(z) + W), W, z) p(W, z \mid do(x=f(z)+W)) dw dz \\
    &= \int_w \int_z p(y \mid do(x = f(z) + W), W, z) p(W, z) dw dz \\
    &= \int_w \int_z p(y \mid do(x = f(z) + W), W, z) p(W) p(z) dw dz \\
    &= \int_z p(y \mid do(x = f(w) + \what), \what, w) p(w) dw \qquad \text{(since $p(W) = \delta_{W=\what}$)} \\
    &= \E_w \left[ p(y \mid do(x=f(w)+\what), w) \right].
\end{align}
This relationship tells us that applying open-loop control tells us something less than $p(y \vert \xhat)$.
```
- Pearl, "A probabilistic calculus of actions," Proc. UAI 1994.
- Kuroki and Miyakawa, "Covariate selection for estimating the causal effect of control plans using causal diagrams," J. Royal Stat. Soc. Ser. B, 2003.`