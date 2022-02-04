```latex
\subsubsection{Notation}

We first need to map our notions of ambiguity between circuits to observational and interventional probability distributions. The first step is defining candidate functional circuits as structural causal models (SCMs). Let $\G_1 = (V,E_1)$ and $\G_2 = (V,E_2)$ denote SCMs of two candidate circuits describing the same set of nodes $V$, where $E_1$ and $E_2$ describe the set of edges and functional relationships in each candidate circuit.\footnote{Later we might be able to extend this to the case where there are unobserved nodes affecting the observed nodes.}

We denote the application of closed-loop control to fix a subset of nodes $X \subset V$ to the control signal $x(t)$ by $\CL_{x(t)}(X)$. We denote the application of open-loop control to add the control signal $w(t)$ to the subset of nodes $W \subset V$ by $\OL_{w(t)}(W)$. Recall that (with slight abuse of notation), $E_1$ and $E_2$ denote not only the presence or absence of edges between variables in $V$, but the functional relationships governing these edges. Because knowledge of the SCM $\G$ is equivalent to knowledge of every possible interventional distribution involving variables in $V$, \emph{a functional connection $X \to Y$ is identifiable if and only if we can compute $p(Y \mid \CL_{x(t)}(X))$}.

From a \emph{connection} perspective:
\begin{itemize}
    \item We say that a connection between $X$ and $Y$ ($X, Y \subset V$) is \emph{ambiguous under control scheme $\mathbb{C}$} if there exist multiple causal structures that are consistent with the data collected under $\mathbb{C}$ but have different connections between $X$ and $Y$ (that is, if $\exists$ $\G_1 \neq \G_2$ consistent with the data collected under $\mathbb{C}$ such that $(E_1)_{X,Y} \neq (E_2)_{X,Y}$).
    \item We say that a connection between $X$ and $Y$ is \emph{identifiable under control scheme $\mathbb{C}$} if every casual structure consistent with the data collected under $\mathbb{C}$ has the same causal relationship between $X$ and $Y$ (that is, if $\nexists~ \G_1 \neq \G_2$ such that $\G_1$ and $\G_2$ are both consistent with the data collected under $\mathbb{C}$ but $(E_1)_{X,Y} \neq (E_2)_{X,Y}$).
\end{itemize}

From a \emph{whole circuit} perspective:
\begin{itemize}
    \item We say that a circuit is \emph{ambiguous under control scheme $\mathbb{C}$} if there exist multiple causal structures that are consistent with the data collected under the control scheme but that have different edge sets (that is, if $\exists$ $\G_1 \neq \G_2$ consistent with the data collected under $\mathbb{C}$).
    \item We say that a circuit is \emph{identifiable under control scheme $\mathbb{C}$} if there is only one possible causal structure consistent with the data collected using the control scheme (that is, if $\nexists$ $\G_1 \neq \G_2$ consistent with the data collected under $\mathbb{C}$).
\end{itemize}
%More mathematically, let $\mathbb{C} = \left(X, w(t), C\right)_{i}$, $i = 1, \dots$, represent a control scheme consisting of (1) a set of nodes $X \subset V$ that control is applied to, (2) a control signal $w(t) \in \R$ ($t \geq 0$) that is used for control of $X$, and (3) the method of control $C \in \{\OL,\CL\}$ (open- or closed-loop). If $C = \OL$, then application of control fixes $X(t) \leftarrow X(t) + w(t)$; if $C = \CL$, then application of control fixes $X(t) \leftarrow w(t)$. Further let $p_{\mathbb{C}}(V)$ denote the joint distribution over $V$ under application of control scheme $\mathbb{C}$. (Todo: continue here.)
```