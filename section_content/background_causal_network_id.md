!!!!! outline-section: our goal: estimating causal interactions in the brain

Many hypotheses about neural circuits are best stated in terms of causal relationships: "changes made in to activity in this region of the brain will produce corresponding changes in that downstream region." Understanding these causal relationships is critical to developing effective therapeutic interventions, which require knowledge of how potential therapies will change brain activity and patient outcomes.

A range of mathematical and practical challenges make it difficult to determine these causal relationships. In studies that rely only observational data, it is often impossible to determine whether observed patterns of activity are due to known and controlled inputs, or whether they are caused by recurrent activity, indirect relationships, or unseen "confounders." The chemical and surgical lesion experiments that have historically been employed to remove the influence of possible confounds are likely to dramatically disrupt circuits from their typical functions, making conclusions about underlying causal structure drawn from these experiments unlikely to hold in naturalistic settings \cite{chicharro2012when}.

In this paper we demonstrate when and how *closed-loop interventions* can reveal the causal structure governing neural circuits. It is generally understood that moving from experiments involving passive observation to more complex levels of intervention allows experimenters to better tackle challenges to circuit identification. However, it is not yet fully understood when more complex intervention strategies can provide additional inferential power or how these interventions should be designed. To meet this need, we draw from tools used in causal inference \cite{pearl2009causality} \cite{maathuis2016review} \cite{chis2011structural}, which answer questions about what classes of models can be distinguished under a given set of input output experiments, and what experiments are necessary to determine internal connections uniquely.

We first propose a mathematical framework that describes how open- and closed-loop interventions impact the observable qualities of neural circuits. Using both simple controlled models and in silico models of neural circuits, we explore factors that govern the efficacy of these types of interventions. Guided by the results of this exploration, we present a set of recommendations that can guide the design of open- and closed-loop experiments that can better uncover the connections which underly neural circuit function.

!!!!! outline-section: how to infer causal interactions from time series?

A number of measures have been proposed to quantify the strength of interaction between variables. Wiener-Granger (or predictive) causality states that a variable $X$ *Granger-causes* $Y$ if $X$ contains information relevant to $Y$ that is not contained in $Y$ itself or any other variable \cite{wiener1956theory}. This requirement that *all* potentially causative variables be considered makes these notions of dependence susceptible to unobserved confounders (cite ?). Granger causality has traditionally been operationalized with vector autoregressive models \cite{granger1969investigating}. ==Drawbacks of Granger causality.==

Our work initially focuses on measures of directional interaction that are based on cross-correlation. These metrics look at the correlation of time series collected from two nodes at various lags, taking a peak at a negative time lag as evidence for the existence of a potential causative relationship (==more precise description==). While cross-correlation-based measures are generally limited to detecting linear functional relationships between nodes, it is computationally inexpensive, making it a metric of choice for many real-world problems. ==More about correlation-based measures.==

Other metrics quantify directional interaction stemming from nonlinear functional relationships (==more precise description==). Information-theoretic methods use information measures to assess the reduction in entropy knowledge of one variable provides about another, and is closely related to Granger causality in simple circuits \cite{barnett2009granger}. Transfer entropy ==...== \cite{bossomaier2016transfer}. Conditional transfer entropy ==... (see bossomaier2016transfer sec 4.2.3)== ==Definition, extension of intuition== ==How conditional TE can address challenges== ==Connection to causality (janzing2013quantifying, ay2008information, lizier2010differentiating) ==Estimation strategies (start with shorten2021estimating ?)==

There are several important aspects to consider when comparing metrics for causal influence. ==bivariate vs multivariate approaches== ==statistical testing [group effect/post-hoc tests; issues of multiple comparisons]== ==note that we are leaning on IDTxl for this; no need to dive too deeply==

==GC in neuro [@Adam]==

!!!!! note todo - skim through these papers for methods/material to cite

- reviews to read/cite:
    - broad background
        - \cite{TODO-runge2018causal} [in progress]
        - \cite{TODO-runge2019inferring}
        - \cite{TODO-peters2020causal}
    - specific to neuro
        - \cite{TODO-chicharro2012when}
        - \cite{TODO-dean2016dangers}
        - \cite{TODO-garofalo2009evaluation}
        - \cite{TODO-knox1981detection
        - \cite{TODO-salinas2001correlated}
        - \cite{TODO-wibral2014directed}
    - maybe...
        - \cite{TODO-lacasa2015network}
        - \cite{TODO-melssen1987detection}
- see `sketches_and_notation/background_why_control.md`
