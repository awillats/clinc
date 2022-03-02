
> **Theme B.** Experiments for circuit inference can be thought of as **narrowing the set of plausible explanations**, refining a hypotheses space[^refine]

[^refine]: see [Advancing functional connectivity](https://www.nature.com/articles/s41593-019-0510-4), fig. 2
[^more_expt]: more than just an experiment, this is a "hypothesis search." Is this procedure what we're going to brand as the "CLINC" process?


!!!! - Structure of an experiment / CLINC framework - 85% done - (move to methods/discussion?)
**We envision the structure of an experiment[^more_expt]** to include the following broad stages:

1. First, explicitly **enumerate the set of hypothesized circuits.** Hypotheses about the structure of the circuit would be based on multiple sources of information including prior recordings, anatomical constraints revealed by `experiments where you look at the fiber bundles connecting regions`, or commonly observed connectivity patterns in other systems `[🚧 add other sources of priors for circuit hypotheses]`[^bonus_causal][^more_assumptions] These hypotheses should be expressed as a set of circuits (adjacency matrices) each with a probability representing the prior belief about the relative likelihood of these options. This hypothesis set can be thought of as a space of possible explanations for the observed data so far, which will be narrowed down through further intervention, observation, and inference. [(Fig.DISAMBIG top row)](#fig-disambig)

[^most]: verify whether this is reasonable to say
2. Second, *in silico*, **forecast patterns of correlation** which could result from applying candidate interventions.
Most algorithms[^most] for circuit inference quantify and threshold measures of dependence between pairs of nodes. Correlations are often used to measure the linear component of dependence between outputs of two nodes, although the approach described here should generalize to other nonlinear measures of dependence such as mutual information. As such, the observed pattern of dependence (correlations) in a given experiment summarizes the input to an inference procedure to recover an estimated circuit.  
    A detailed forecast of the observed outputs could be achieved by simulating biophysical networks across candidate interventions and hypothesized ground-truth circuits. However, for large networks or large hypothesis sets this may be expensive to compute. Instead, for the sake of rapid iteration in designing interventions, we propose using the reachability representation of a linear (linearized) network to succinctly and efficiently predict the observed correlations[^bivar_pred] across nodes[^node_repr]. The methods described in `[ref. prediction methods]` allow us to anticipate how open and closed-loop interventions across nodes in the network might increase, decrease, or sever dependencies between node outputs.

[^bivar_pred]: using binary reachability, we can be more general above predicting the "sign/slope" (when will they increase/decrease) of other measures of bivariate dependence like transfer entropy

3. `{Survey / analyze / compare / summarize}` `{diversity / equivalence /  distinguishability of}` patterns of correlation across each hypothesized circuit.
A useful experiment (intervention) is one which produces highly distinct outcomes when applied to each of the hypothesized circuits, while an experiment which produces the same outcome across all hypothesized circuits would be redundant.
    Before collecting experimental data we do not know the ground-truth circuit with certainty, therefore it is useful to understand the range of possible observed patterns of dependence. To distill this range of possibilities to a make a decision about which intervention to apply, it is also useful to summarize the expected information we would gain about circuit identity across the range of hypotheses. [(across columns of Fig.DISAMBIG)](#fig-disambig)
>-*Here we generalize across specific values of synaptic weights and divide observed patterns into categories: increased correlation, decreased correlation, no correlation.*

🚧
`Entropy as a measure of information about circuit hypotheses`
Shannon entropy provides a scalar summarizing the diversity of a set of outcomes..
...how uniform a discrete probability function is...
...how surprising...(in expectation)

$$H(X) = E[I(X)] = E[\log\frac{1}{p(X)}] = \sum_{i=1}^{N} p(x_i) \log\frac{1}{p(x_i)} $$

`interpretting high and low entropy`
>a highly predictable experimental outcome means an experiment where not much was learned 

[^alt_equiv]: i.e. if you took a PMF and counted the number of categories with probability greater than $p_th$. A distribution with 16 possible outcomes, but only 2bits of uncertainty is *as* uncertain as a uniform distribution with $2^2$ equally likely outcomes

An intervention associated with a higher entropy across circuits will, on average, provide more information to narrow the set of hypotheses. In fact, one interpretation of entropy is that it describes the (uncertainty associated with the equivalent) number of *equally-likely* outcomes[^alt_equiv] of a probability mass function. In this setting $N_{equal}$ can be thought of as the number of hypotheses that can be distinguished under a given experiment[^markov_equiv].
$$ H(C) = \log_2 N_{equal} \\
N_{equal} = 2^{H(C)}$$
For instance, open-loop intervention at node $x_0$ in [(Fig.DISAMBIG right column)](#fig-disambig) results in an entropy across the hypotheses of $H(C|S_0) \approx 1.5$bits or $N_{equal} \approx 2.8$. Looking at the patterns of correlation, there are $N=3$ distinct patterns, with the +++ pattern somewhat more likely than the others (+--, 0--).[^entropy_num] This intuition also helps understand the maximum entropy achievable for a given set of hypotheses:
$$H^{max}(C) = log_2 N$$
for this example set:
$$H^{max}(C) = log_2 6 \approx 2.6$$ 

[^entropy_num]: since $H(C)\leq H^{max}(C)$, $N_{equal} \leq N$

`select intervention - (is this its own step, or the last part of step 3)`
Here, we describe a "greedy" approach for choosing an effective single-node intervention, but extending the approach above to predict joint entropy would allow a joint or sequential experimental design which would be optimal over multiple interventions.
>- possible interventions consist of open-loop and closed-loop stim at each of N nodes 
>   - but more constraints on the set of interventions can easily be incorporated at this stage

For selecting the first intervention type and location, we propose choosing the intervention which results in the maximum expected circuit information, that is:
$$S_i^* = \underset{i}{\arg\max}\,H(C|S_i)$$[^intv_notation]


[^intv_notation]: will need to tighten up notation for intervention summarized as a variable, annotating its type (passive, open-, closed-loop) as well as its location. Also have to be careful about overloading $S_i$ as the impact of private variance and as a particular open-loop intervention

🚧🚧🚧
4. *(in experiment or detailed biophysical simulation)* apply intervention, collect data
Using entropy as a metric to select a useful intervention, the next step is to conduct that interventional experiment, in-vivo or in a detailed simulation. Such an experiment may reveal outputs not fully captured by the linearized reachability representation. 

`[extract correlations ...]`
[^practicalities]. 

[^practicalities]: Omitting several quantitative practicalities in this step. Notably choosing the amplitude / frequency content of an intervention w.r.t. estimated parameters of the circuit


5. **Given the observed dependency pattern, form a posterior belief over hypotheses**
`[🚧 transition text]`  
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
$$ \hat{c}_{\text{MAP}} = \underset{c}\argmax \,L(\text{Corr} | c)\,\pi(c) $$
or the posterior belief can be used as a prior for the next iteration.

[^bad_convergence]: what about the scenario where the ground truth circuit is not in the hypotheses set?
[^markov_equiv]: connect this section to the idea of the markdov equivalence class, and its size
<!-- ![](../figures/misc_figure_sketches/circuit_intervention_entropy_mockup.png) -->
<!-- **Figure DISAMBIG: Stronger intervention facilitates disambiguating equivalent hypotheses** -->