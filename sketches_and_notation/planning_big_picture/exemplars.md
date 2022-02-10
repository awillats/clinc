see also https://beta.workflowy.com/#/f32ad4b2290a

# Table of Conents {ignore=true}
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=2 orderedList=false} -->
<!-- code_chunk_output -->

  - [summary of core ideas](#summary-of-core-ideas)
  - [other misc. themes](#other-misc-themes)
- [Similar articles](#similar-articles)
  - [Advancing functional connectivity research from association to causation](#advancing-functional-connectivity-research-from-association-to-causation)
  - [Inferring causal connectivity from pairwise recordings and optogenetics](#inferring-causal-connectivity-from-pairwise-recordings-and-optogenetics)
  - [Systematic errors in connectivity inferred from activity in strongly recurrent networks](#systematic-errors-in-connectivity-inferred-from-activity-in-strongly-recurrent-networks)
  - [Could a Neuroscientist Understand a Microprocessor?](#could-a-neuroscientist-understand-a-microprocessor)
  - [Systematic Perturbation of an Artificial Neural Network: A Step Towards Quantifying Causal Contributions in The Brain](#systematic-perturbation-of-an-artificial-neural-network-a-step-towards-quantifying-causal-contributions-in-the-brain)
  - [Quasi-experimental causality in neuroscience and behavioral research](#quasi-experimental-causality-in-neuroscience-and-behavioral-research)
  - [Evaluation of the Performance of Information Theory-Based Methods and Cross-Correlation to Estimate the Functional Connectivity in Cortical Networks](#evaluation-of-the-performance-of-information-theory-based-methods-and-cross-correlation-to-estimate-the-functional-connectivity-in-cortical-networks)

<!-- /code_chunk_output -->
---

## summary of core ideas
- we **seek causal answers** to questions we have about brain[^quasi]
  - bridging structure and function 
  >  In neuroscience we have many causal questions. For example, we are interested in how one brain area affects another brain area, as opposed to how the two brain areas are correlated.
  
  > The central goal of neuroscience, arguably, is to understand the mechanisms or causal chains that give rise to activity in the brain, to perception, cognition, and action.

- core **challenges to causal understanding**
  - key challenge is tangling / overlap of potential sources[^fakhar][^jonas][^lepperod]
    > Complex systems such as the brain are hard to understand because of the numerous ways the contributing elements may interact internally (Jonas and Kording, 2017) [^lepperod][^jonas] 
    
    - lack of spatial specificity in optogenetics makes this worse[^lepperod]
    - recurrence as a more specific form of this [^fiete]
    
  - issue of **confounding** [^advance] [^quasi] [^pearl2009]
    > Confounding is the big threat to causal validity (Pearl, 2009) irrespective of the use of simple regression techniques or advanced functional connectivity techniques (Stevenson et al., 2008; Honey et al., 2009; Aitchison and Lengyel, 2017; Pfau et al., 2013)
    
    - bigger issue with passive observation
      > But if we can only observe a system, then confounding is a serious problem; we can never know if an apparent interaction between X and Y is real or is confounded by the other variables. First, there are many variables that we cannot easily set, e.g., the activity of neurons somewhere in the brain. [^quasi]

- **limitations of current approaches**
  - **recording more isn't always enough**[^fiete]
    - more sophisticated inference isn't always enough!
  - assume unconfoundedness, and cross fingers [^quasi]
    - e.g. Granger Causality
  - limitations of **excess intervention** (lesions, knockout) [^promise][^vaidya][^sprague]
  - not all pertubations are created equal[^fakhar]

- intervention as gold standard[^quasi]


## other misc. themes 
- discussion of methods focused on **reducing bias** in network estimation
- integrating successful techniques from other disciplines[^quasi][^lepperod]
  - mostly econometrics
  - see Grosenick for discussion of bridging engineering and biology[^grosenick_bridge]

- value of studying a complex system with known ground-truth connectivity [^jonas]
- use / critique of Granger causality
  - conditional GC described in [^GCtheory]
- "reduce the set of likely models"[^advance]

[^grosenick_bridge]: "This [lack of applications so far] is unlikely to be due to the technical and experimental challenges involved in undertaking such investigations, since neurobiologists are accustomed to the design and implementation of experiments characterized by computational and technical complexity. -- There may be, however, a cultural gap between biologists and engineers regarding available tools, techniques, and motivation for closed-loop optical control and related technologies in systems engineering. Here we seek to address the latter challenge by helping to unite the relevant literatures" Closed-loop and Activity-Guided Optogenetic Control

---
# Similar articles
## Advancing functional connectivity research from association to causation
by Reid, Calhoun, Cole et al. - [link](https://www.nature.com/articles/s41593-019-0510-4)
 
<details><summary>Abstract</summary>

> Cognition and behavior emerge from brain network interactions, such that investigating causal interactions should be central to the study of brain function. Approaches that characterize statistical associations among neural time series—functional connectivity (FC) methods—are likely a good starting point for estimating brain network interactions. Yet only a subset of FC methods (‘effective connectivity’) is explicitly designed to infer causal interactions from statistical associations. Here we incorporate best practices from diverse areas of FC research to illustrate how FC methods can be refined to improve inferences about neural mechanisms, with properties of causal neural interactions as a common ontology to facilitate cumulative progress across FC approaches. We further demonstrate how the most common FC measures (correlation and coherence) reduce the set of likely causal models, facilitating causal inferences despite major limitations. Alternative FC measures are suggested to immediately start improving causal inferences beyond these common FC measures.
</details>

### transcription
- **big goal** understand structure - function
- **gap** not all functional connectivity approaches infer causal interactions
  - lots of theoretical and practical limitations with current FC approaches
  > 1. The need for an account of FC as both a theoretical and methodological construct.
  > 2. the need to integrate functional (and effective) con- nectivity approaches into a single framework
  > 3. the need to validate FC methods to improve map- ping of FC results to properties of theoretical interest
- **solution** summarize best practices, illustrate how to refine inference
  - identify likely issues
  - lay out systematic perspective for understanding layers
    - structural
    - observational 
    - inferential
  - presents framework for understanding space of hypotheses
    - demonstrate how methods reduce the set of likely causal models
- **impact/guidance** suggestions for refined FC methods to use

---
## Inferring causal connectivity from pairwise recordings and optogenetics
by Lepperod, Stober, Hafting, Fyhn, Kording - [link](https://www.biorxiv.org/node/138945.full)
<details><summary>abstract</summary>


> To study how the brain works, it is crucial to identify causal interactions between neurons, which is thought to require perturbations. However, when using optogenetics we typically perturb multiple neurons, producing a confound - any of the stimulated neurons can have affected the postsynaptic neuron. Here we show how this produces large biases, and how they can be reduced using the instrumental variable (IV) technique from econometrics. The interaction between stimulation and the absolute refractory period produces a weak, approximately random signal which can be exploited to estimate causal connectivity. When simulating integrate-and-fire neurons, we find that estimates from IV are better than na ̈ıve techniques (R2 = 0.77 vs R2 = 0.01). The difference is important as the estimates disagree when applied to experimental data from stimulated neurons with recorded spiking activity. Presented is a robust analysis framework for mapping out network connectivity based on causal neuron interactions.
</details>

### transcription
- **big goal** to study how the brain works, perturbations are key. How can we overcome limitations of current opotgenetic perturbations?
- **challenge** opto stim provides common input to many neurons
  - this is a potential confound
  - leads to high bias
  > any postsynaptic activity induced by stimulation could in principle come from any of the stimulated neurons, introducing problematic confounders.
  
- **proposed solution** borrow instrumental variables (IV) from econ.
  - stimulus + refratory period provides approx. random signal
  - also uses cross-correlation
    > We compare these estimates with a na ̈ıve, although widely used, cross-correlation histogram (CCH) method that fails to distinguish respective pairs.
    
- **results** much higher recovery
  - > The difference is important as the estimates disagree when applied to experimental data from stimulated neurons with recorded spiking activity.
- **impact** robust analysis framework for mapping connectivity based on causal interaction


---

## Systematic errors in connectivity inferred from activity in strongly recurrent networks
by Ila Fiete & Abhranil Das - [link](https://www.nature.com/articles/s41593-020-0699-2)

<details><summary>Abstract</summary>

> Understanding the mechanisms of neural computation and learning will require knowledge of the underlying circuitry. Because it is difficult to directly measure the wiring diagrams of neural circuits, there has long been an interest in estimating them algorithmically from multicell activity recordings. We show that even sophisticated methods, applied to unlimited data from every cell in the circuit, are biased toward inferring connections between unconnected but highly correlated neurons. This failure to ‘explain away’ connections occurs when there is a mismatch between the true network dynamics and the model used for inference, which is inevitable when modeling the real world. Thus, causal inference suffers when variables are highly correlated, and activity-based estimates of connectivity should be treated with special caution in strongly connected networks. Finally, performing inference on the activity of circuits pushed far out of equilibrium by a simple low-dimensional suppressive drive might ameliorate inference bias.
</details>

### transcription
- **big goal:** understand structure - function
  - difficult to do
- **surprising result - challenge for field:**  
  > We show that even sophisticated methods, applied to unlimited data from every cell in the circuit, are biased toward inferring connections between unconnected but highly correlated neurons. 
  
- **explanation for why**
- **solution - method/result for partial mitigation:** low-dimensional suppresive drive (open-loop stim) might ameliorate inference bias

---
## Could a Neuroscientist Understand a Microprocessor?
Jonas & Kording - [link](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005268)
<details><summary> abstract</summary>

>There is a popular belief in neuroscience that we are primarily data limited, and that producing large, multimodal, and complex datasets will, with the help of advanced data analysis algorithms, lead to fundamental insights into the way the brain processes information. These datasets do not yet exist, and if they did we would have no way of evaluating whether or not the algorithmically-generated insights were sufficient or even correct.
>
>To address this, here we take a classical microprocessor as a model organism, and use our ability to perform arbitrary experiments on it to see if popular data analysis methods from neuroscience can elucidate the way it processes information. Microprocessors are among those artificial infor- mation processing systems that are both complex and that we understand at all levels, from the overall logical flow, via logical gates, to the dynamics of transistors. 
>
>We show that the approaches reveal interesting structure in the data but do not meaningfully describe the hierarchy of information processing in the microprocessor. This suggests current analytic approaches in neuroscience may fall short of producing meaningful understanding of neural systems, regardless of the amount of data. Additionally, we argue for scientists using complex non-linear dynamical systems with known ground truth, such as the microprocessor as a validation platform for time-series and structure discovery methods.
</details>

<details><summary>author summary</summary>

Neuroscience is held back by the fact that it is hard to evaluate if a conclusion is correct; the complexity of the systems under study and their experimental inaccessability make the assessment of algorithmic and data analytic technqiues challenging at best. We thus argue for testing approaches using known artifacts, where the correct interpretation is known. Here we present a microprocessor platform as one such test case. We find that many approaches in neuroscience, when used naïvely, fall short of producing a meaningful understanding.
</details>

### transcription
- **current state of neuro:** more data, better analysis will be a primary driver of insight about the brain 
- **gap:** do not yet know whether this assumption is valid
- **solution:** test it in-silico, in a known but non-insular[^noninsular] example 
- **result:** indeed, current approaches are insufficient to uncover hierarchy of causes 
- **impact:** argue for scientists using complex nonlinear systems with known ground truth as a rigorous validation
- **methods:**
  - lesioning a single transistor at a time
  - uses conditiional granger causality [^GCtheory]

[^noninsular]: meaning a system which steps outside a perfect match of the assumptions used to develop the analysis techniques

---
## Systematic Perturbation of an Artificial Neural Network: A Step Towards Quantifying Causal Contributions in The Brain
by Fakhar, Hilgetag - [link](https://www.biorxiv.org/content/10.1101/2021.11.04.467251v1)
<details><summary>abstract</summary>

>lesion inference analysis is a fundamental approach for characterizing the causal contributions of neural elements to brain function. Historically, it has helped to localize specialized functions in the brain after brain damage, and it has gained new prominence through the arrival of modern optogenetic perturbation techniques that allow probing the functional contributions of neural circuit elements at unprecedented levels of detail.
>
>While inferences drawn from brain lesions are conceptually powerful, they face methodological difficulties due to the brain’s complexity. Particularly, they are challenged to disentangle the functional contributions of individual neural elements because many elements may contribute to a particular function, and these elements may be interacting anatomically as well as functionally. Therefore, studies of real-world data, as in clinical lesion studies, are not suitable for establishing the reliability of lesion approaches due to an unknown, potentially complex ground truth. Instead, ground truth studies of well-characterized artificial systems are required.
>
>Here, we systematically and exhaustively lesioned a small Artificial Neural Network (ANN) playing a classic arcade game. We determined the functional contributions of all nodes and links, contrasting results from single-element perturbations and perturbing multiple elements simultaneously. Moreover, we computed pairwise causal functional interactions between the network elements, and looked deeper into the system’s inner workings, proposing a mechanistic explanation for the effects of lesions.
>
>We found that not every perturbation necessarily reveals causation, as lesioning elements, one at a time, produced biased results. By contrast, multi-site lesion analysis captured crucial details that were missed by single-site lesions. We conclude that even small and seemingly simple ANNs show surprising complexity that needs to be understood for deriving a causal picture of the system. In the context of rapidly evolving multivariate brain-mapping approaches and inference methods, we advocate using in-silico experiments and ground-truth models to verify fundamental assumptions, technical limitations, and the scope of possible interpretations of these methods.
</details>

<details><summary>author summary</summary>

> **Author summary** The motto “No causation without manipulation” is canonical to scientific endeavors. In particular, neuroscience seeks to find which brain elements are causally involved in cognition and behavior of interest by perturbing them. However, due to complex interactions among those elements, this goal has remained challenging. 
>
>In this paper, we used an Artificial Neural Network as a ground-truth model to compare the inferential capacities of lesioning the system one element at a time against sampling from the set of all possible combinations of lesions.
>
>We argue for employing more exhaustive perturbation regimes since, as we show, lesioning one element at a time provides misleading results. We further advocate using simulated experiments and ground-truth models to verify the assumptions and limitations of brain-mapping methods.
</details>

### transcription
- **historical intro:** lesion analysis has been useful
  - optogenetics facilitate making this more precise
- **remaining challenges** with lesion analysis
  - lesions are powerful but methodologically difficult
    - difficult to disentagle causes 
    
- **proposed solution** use more extensive perturbation - combinations of lesion experiemtns
  > We found that not every perturbation necessarily reveals causation, as lesioning elements, one at a time, produced biased results. By contrast, multi-site lesion analysis captured crucial details that were missed by single-site lesions. 


---

## Quasi-experimental causality in neuroscience and behavioral research
by Marinescu, Lawlor, Kording - [link](https://www.nature.com/articles/s41562-018-0466-5)
<details><summary>abstract</summary>


>in many scientific domains, causality is the key question. For example, in neuroscience, we might ask whether a medication affects perception, cognition, or action. Randomized controlled trials (RCTs) are the gold standard to establish causality, but they are not always practical. The field of empirical economics developed rigorous methods to establish causality even when RCTs are not available. Here we review these quasi-experimental methods and highlight how neuroscience and behavioral researchers can use them to do research that can credibly demonstrate causal effects.

> In response to the confounding problem in observational data, there are two important schools of thought. One school attempts to builds large, complex models that observe and model all confounders. [...] This second school of thought mainly comes from econometrics, and over the last few decades has developed a number of ways in which meaningful causal estimates can be obtained without randomization.

>Here we review these alternatives to randomization. We take published examples, and explain the methods. For each method, we then sketch how it could be used more widely across behavioral and neuroscience research using existing and emerging data. By systemically replacing correlational techniques with causal techniques, economics went through what they call a credibility revolution. Perhaps as a result, empirical work in economics has progressively overtaken theoretical work both in terms of citations within economics [15], and in terms of citations to economics papers made by articles in other fields 
</details>

### transcription
- **big goal:** causality is key (at the heart of what we want)
- **challenge:** establishing causality is not always practical 
  - via fully randomized control trials
  - then confounding is a major challenge
- **limitations of existing solutions:**
  - assume unconfoundedness / over-model the system
- **solution:** bring in methods from economics for practical establishment of causality
- **impact:** neuroscientists can, should use these techniques too

---

## Evaluation of the Performance of Information Theory-Based Methods and Cross-Correlation to Estimate the Functional Connectivity in Cortical Networks
by M Garofalo, T Nieus, P Massobrio, S Martinoia - [link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0006482)
<details><summary>abstract</summary>

> functional connectivity of in vitro neuronal networks was estimated by applying different statistical algorithms on data collected by Micro-Electrode Arrays (MEAs). First we tested these ‘‘connectivity methods’’ on neuronal network models at an increasing level of complexity and evaluated the performance in terms of ROC (Receiver Operating Characteristic) and PPC (Positive Precision Curve), a new defined complementary method specifically developed for functional links identification. Then, the algorithms better estimated the actual connectivity of the network models, were used to extract functional connectivity from cultured cortical networks coupled to MEAs. Among the proposed approaches, Transfer Entropy and Joint-Entropy showed the best results suggesting those methods as good candidates to extract functional links in actual neuronal networks from multi-site recordings.
</details>

### transcription
- **goal** seek to leverage multi-electrode arrays to estimate functional connectivity
- **challenge** prior methods are only partially effective, novel methods are relatively untested
  - **gap** prior work mostly considers linear networks or very small networks
  - 
- **result** Tranfer Entropy and Joint Entropy based measures perform best
- **impact** - use info theoretic measures, inhibitory connections are still hard to ID


[^GCtheory]: **Granger Causality:** Basic Theory and Application to Neuroscience. Handbook of Time Series Analysis. - outlines procedure for conditional GC, used in [^jonas]

[^jonas]: [Could a Neuroscientist Understand a Microprocessor?](#could-a-neuroscientist-understand-a-microprocessor)
[^fiete]: [Systematic errors in connectivity inferred from activity in strongly recurrent networks](#systematic-errors-in-connectivity-inferred-from-activity-in-strongly-recurrent-networks)
[^sprague]: "Perturbation-driven paradoxical facilitation of visuo-spatial function: Revisiting the ‘Sprague effect’"
[^fakhar]: [Systematic Perturbation of an Artificial Neural Network: A Step Towards Quantifying Causal Contributions in The Brain](#systematic-perturbation-of-an-artificial-neural-network-a-step-towards-quantifying-causal-contributions-in-the-brain)
[^advance]: [Advancing functional connectivity research from association to causation](#advancing-functional-connectivity-research-from-association-to-causation)
[^quasi]: [Quasi-experimental causality in neuroscience and behavioral research](#quasi-experimental-causality-in-neuroscience-and-behavioral-research)
[^paradox]: Perturbation-driven paradoxical facilitation of visuo-spatial function: Revisiting the ‘Sprague effect’
[^lepperod]: [Inferring causal connectivity from pairwise recordings and optogenetics](#inferring-causal-connectivity-from-pairwise-recordings-and-optogenetics)
[^pearl2009]: Pearl, J. (2009). Causality. Cambridge university press.

[^vaidya]: ["Lesion Studies in Contemporary Neuroscience"](https://pubmed.ncbi.nlm.nih.gov/31279672/) Vaidya et al.
[^promise]: ["The promise and perils of causal circuit manipulations
"](https://www.sciencedirect.com/science/article/abs/pii/S0959438817302246) (2018) Wolff, Olveczky - discusses acute v.s. chronic and disruptive v.s. physiological perturbations. Also mentions the promise of closed-loop control in this respect

