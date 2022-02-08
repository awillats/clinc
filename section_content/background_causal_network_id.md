## Why? - Estimating causal interactions in the brain
  - understanding relationship between structure and function
    - for basic science
    - and for discovering new therapies
      - optimize therapeutic targets for existing approaches

## How? - Causal methods for network discovery from time-series
  - Challenges faced when estimating network connectivity
    - [...]
  - measures of dependence
    - correlation (granger causality, cross-correlation)
    - info theoretic (transfer entropy)
  - role of conditioning
    - bivariate v.s. multivariate approaches
  - *( statistical testing )*
    - need for group effect and post-hoc tests
    - issue of multiple comparisons
    - `in the end we were leaning on IDTxl for this... may be appropriate to leave this out of scope`
  - *( perspective on role, limitations of granger causality in neuro )*
    - `are some of these limitations alleviated by intervention?`*
  - *cite J.Runge*

see also `sketches_and_notation/background_why_control.md`

**copied from proposal**
Many hypotheses about neural circuits are best stated in terms of causal relationships: “Activity in this region causes an observed change in that downstream region. These regions are connected.” Furthermore, the development of effective therapeutic interventions requires knowledges of how potential therapies will change patient outcomes. However, for experiments without causal intervention, a key ambiguity remains as to whether observed outputs are caused by known/controlled inputs versus recurrent activity or unseen “confounds.” Historically causal interventions have been conducted through chemical and surgical lesion experiments to remove possible confounds; however, these are likely to dramatically disrupt circuits from their typical function. As such causal conclusions drawn from these experiments may no longer hold in naturalistic settings.

What is necessary is to bolster the toolbox of causal methods for investigating neural circuits. To meet this need, we will need to draw from theory and methods of causal inference (Pearl 2009; Maathuis and Nandy 2016), and structural identifiability (Chis, Banga, and Balsa-Canto 2011) developed outside neuroscience. These fields have developed to answer questions about what classes of models can be distinguished under a given set of input output experiments, and what experiments are necessary to determine internal connections uniquely. Insights from structural identifiability will likely inform our approach for answering these questions about neural circuits but a significant gap remains in evaluating which techniques will be useful under the constraints and assumptions of systems neuroscience.

Second, carefully designed closed-loop control experiments have the potential to move from correlative to causal statements about neural circuits. We understand broadly that moving from experiments involving passive observation to more complex levels of intervention such as closed-loop control (Table 1) allows experimenters to better tackle challenges to circuit identification (Table 2). However, we do not yet fully understand which of these challenges can be overcome in neural circuits, nor how best to design these closed-loop interventions. What is needed is a foundational characterization of how closed-loop control improves identification in representative simulations of neural circuits. Such a characterization could be used to explore how closed-loop interventions can be designed to meet specific needs for different circuit motifs and noise levels. By integrating these approaches from control theory and causal inference with the domain-specific assumptions of neuroscience, it will be possible to guide effective closed-loop experiments and better uncover the connections which underly neural circuit function.

## Initial outline
- our goal: estimating causal interactions in the brain
    - why? basic science
    - clinical value
        - discovering new therapies
        - optimizing therapeutic targets for existing therapies
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
- how to infer causal interactions from time series?
    - challenges
        - confounding
        - indirect correlations
        - cite/read \cite{chicharro2012when}
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
