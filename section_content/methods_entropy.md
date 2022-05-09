Shannon entropy provides a scalar summarizing the diversity of a set of outcomes.
<!-- ...how uniform a discrete probability function is... -->
<!-- ...how surprising...(in expectation) -->

$$H(X) = E[I(X)] = E[\log\frac{1}{p(X)}] = \sum_{i=1}^{N} p(x_i) \log\frac{1}{p(x_i)} $$

**Interpreting high and low entropy.**
<!-- >a highly predictable experimental outcome means an experiment where not much was learned  -->
[^alt_equiv]: i.e. if you took a PMF and counted the number of categories with probability greater than $p_{th}$. A distribution with 16 possible outcomes, but only 2bits of uncertainty is *as* uncertain as a uniform distribution with $2^2$ equally likely outcomes

An intervention associated with a higher entropy across circuits will, on average, provide more information to narrow the set of hypotheses. In fact, one interpretation of entropy is that it describes the (uncertainty associated with the equivalent) number of *equally-likely* outcomes[^alt_equiv] of a probability mass function. In this setting $N_{equal}$ can be thought of as the number of hypotheses that can be distinguished under a given experiment[^markov_equiv].
$$ H(C) = \log_2 N_{equal} \\
N_{equal} = 2^{H(C)}$$
For instance, open-loop intervention at node $x_0$ in [(Fig.DISAMBIG right column)](#fig-disambig) results in an entropy across the hypotheses of $H(C|S_0) \approx 1.5$bits or $N_{equal} \approx 2.8$. Looking at the patterns of correlation, there are $N=3$ distinct patterns, with the +++ pattern somewhat more likely than the others (+--, 0--).[^entropy_num] This intuition also helps understand the maximum entropy achievable for a given set of hypotheses:
$$H^{max}(C) = log_2 N$$
for this example set:
$$H^{max}(C) = log_2 6 \approx 2.6$$ 

[^entropy_num]: since $H(C)\leq H^{max}(C)$, $N_{equal} \leq N$

[^markov_equiv]: connect this section to the idea of the Markov equivalence class, and its size