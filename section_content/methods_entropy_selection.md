> Selecting the optimal intervention ...

Here, we describe a greedy approach for choosing an effective single-site intervention, but extending the approach above to predict joint entropy would allow a joint or sequential experimental design which could be optimized over multiple interventions *(see Discussion)*.

For selecting the first intervention type and location, we propose choosing the intervention which results in the maximum expected circuit information, that is:
$$S_i^* = \underset{i}{\arg\max}\,H(\mathbf{C}|S_i)$$[^intv_notation]

Alongside intervention type and location, additional constraints could be incorporated at this stage, such as using estimated circuit weights to balance using high variance stimuli while avoiding excess stimulus amplitudes.
<!-- NOTE: basically you'd add them to the cost/value function with some weighting term
*[# specifying interventions](/section_content/methods_interventions.md)*
 -->
 <!-- NOTE: [^practicalities] 
 several quantitative practicalities in this step. Notably choosing the amplitude / frequency content of an intervention w.r.t. estimated parameters of the circuit
  -->

[^intv_notation]: will need to tighten up notation for intervention summarized as a variable, annotating its type (passive, open-, closed-loop) as well as its location. Also have to be careful about overloading $S_i$ as the impact of private variance and as a particular open-loop intervention.

<!-- 
TODO: NOTE: how to choose variance of intervention
-->

      
> Evolution of entropy, as the space of hypotheses is narrowed from experiments and inference.

\[
\begin{aligned}
H^{pre}(C):& \text{ uncertainty before intervention (starts at}\, H^{max}(C))\\
H(C|S_i):& \text{ expected information gain from a given intervention}\\
H^{post}(C|S_i) = H^{pre} - H(C|S_i):& \text{ expected remaining uncertainty after intervention}
\end{aligned}
\]

If $H(X|S_i)\approx0 \,\forall i$, none of the candidate interventions provide additional information, and the identification process has converged.
If $H^{post} = 0$ the initial hypothesis set has been reduced down to a single circuit hypothesis consistent with the observed data[^bad_convergence].
If $H^{post} > 0$, some uncertainty remains in the posterior belief over the hypotheses. In this case a Maximum A Posteriori (MAP) estimate could be chosen as:
$$ \hat{c}_{\text{MAP}} = \underset{c}{\text{argmax}} \,L(\text{Corr} | c)\,\pi(c) $$
or the posterior belief can be used as a prior for the next iteration.

[^bad_convergence]: what about the scenario where the ground truth circuit is not in the hypotheses set?

<hr>

