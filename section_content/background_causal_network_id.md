!!!!! outline-section: our goal: estimating causal interactions in the brain

Many hypotheses about neural circuits are best stated in terms of causal relationships: "changes made in to activity in this region of the brain will produce corresponding changes in that downstream region." Understanding these causal relationships is critical to developing effective therapeutic interventions, which require knowledge of how potential therapies will change brain activity and patient outcomes.

A range of mathematical and practical challenges make it difficult to determine these causal relationships. In studies that rely only observational data, it is often impossible to determine whether observed patterns of activity are due to known and controlled inputs, or whether they are caused by recurrent activity, indirect relationships, or unseen "confounders." The chemical and surgical lesion experiments that have historically been employed to remove the influence of possible confounds are likely to dramatically disrupt circuits from their typical functions, making conclusions about underlying causal structure drawn from these experiments unlikely to hold in naturalistic settings.

`TODO - cite/read \cite{chicharro2012when}`

In this paper we demonstrate how *closed-loop interventions* can elucidate the causal structure governing neural circuits. It is generally understood that moving from experiments involving passive observation to more complex levels of intervention allows experimenters to better tackle challenges to circuit identification. However, it is not yet fully understood when more complex intervention strategies can provide additional inferential power or how these interventions should be designed. To meet this need, we draw from tools used in causal inference (Pearl 2009; Maathuis & Nandy 2016; Chis, Banga, & Balsa-Canto 2011), which answer questions about what classes of models can be distinguished under a given set of input output experiments, and what experiments are necessary to determine internal connections uniquely.

We first propose a mathematical framework that describes how open- and closed-loop interventions impact the observable qualities of neural circuits. Using both simple controlled models and in silico models of neural circuits, we explore factors that govern the efficacy of these types of interventions. Guided by the results of this exploration, we present a set of recommendations that can guide the design of open- and closed-loop experiments that can better uncover the connections which underly neural circuit function.

!!!!! outline-section: how to infer causal interactions from time series?

- measures of dependence
    - granger / predictive causality \cite{granger1969investigating}
    - correlation (granger causality, cross-correlation)
    - info theoretic (TE)
        - general characteristics of info theoretic methods (e.g., beyond linear)
        - measures the information the past of one process provides about a target process above the target process' past \cite{bossomaier2016transfer}
        - connection to causality \cite{janzing2013quantifying} \cite{ay2008information} \cite{lizier2010differentiating}
        - relationship to granger causality \cite{barnett2009granger}
        - conditional TE (e.g., bossomaier2016transfer sec 4.2.3)
            - how this can address challenges
            - definition, extension of intuition
        - estimation strategies (maybe start with \cite{TODO-shorten2021estimating})
- some aspects we need to consider when comparing methods
    - bivariate vs multivariate approaches
    - statistical testing
        - group effect / post-hoc tests
        - issues of multiple comparisons
        - (note: we are leaning on IDTxl for this; no need to dive too deeply)
- GC in neuro [@Adam]

!!!!! note todo - skim through these papers for methods/material to cite

- reviews to read/cite:
    - broad background
        - \cite{TODO-runge2018causal}
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
