> Evolution of entropy, as the space of hypotheses is narrowed from experiments and inference.

\[
\begin{align}
H^{pre}(C):& \text{ uncertainty before intervention (starts at\,} H^{max}(C))\\
H(C|S_i):& \text{ expected information gain from a given intervention}\\
H^{post}(C|S_i) =\\ H^{pre} - H(C|S_i):& \text{expected remaining uncertainty after intervention}
\end{align}
\]
If $H(X|S_i)\approx0 \,\forall i$, none of the candidate interventions provide additional information, and the identification process has converged.
If $H^{post} = 0$ the initial hypothesis set has been reduced down to a single circuit hypothesis consistent with the observed data[^bad_convergence].
If $H^{post} > 0$, some uncertainty remains in the posterior belief over the hypotheses. In this case a Maximum A Posteriori (MAP) estimate could be chosen as:
$$ \hat{c}_{\text{MAP}} = \underset{c}{\text{argmax}} \,L(\text{Corr} | c)\,\pi(c) $$
or the posterior belief can be used as a prior for the next iteration.

[^bad_convergence]: what about the scenario where the ground truth circuit is not in the hypotheses set?
[^markov_equiv]: connect this section to the idea of the markdov equivalence class, and its size