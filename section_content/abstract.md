<!-- ## Feb 8th 2022 draft  -->
<!-- ## Short version
A primary goal of neuroscience is identifying causal relationships in the brain, a task often aided by interventions which stimulate activity in portions of the brain such as lesioning and optogenetics. These open-loop interventions, however, do not fully eliminate potential confounding influences, often limiting their ability to reveal causal structure. 

In this paper, we use tools from causal inference, control theory, and neuroscience to show *when* and *how* closed-loo interventions can more effectively reveal causal relationships. Using a variety of simulated neural circuits, we examine how key process and intervention parameters affect identifiability, developing guidance to help experimentalists determine when closed-loop control is needed to infer causal structure, and when observational data or open-loop stimulation is sufficient. Our results build toward a practical framework that will aid experimental neuroscientists design and interpret experiments that, by revealing more causal structure in the brain, could open the door to new and more effective therapies.

<!-- [^N3]: is "lesioning" really an open-loop stimulation? -->
<!-- [^N4]: could make this more precise, e.g., with ", particularly in neural circuits that feature reciprocal connections or strong feedback and fast timescales" -->
<!-- [^N6]: will "identifiability" be understood, or should this be defined -->
<!-- [^N7]: if we're confident the conclusions drawn from xcorr generalize to TE (and discuss this in the paper) I think the abstract would be stronger without specializing it to a specific algorithm --- but if all the results are pretty xcorr-specific we should mention that here. -->
<!-- [^N8]: how much to focus on the "control" aspect here? (closed-loop interventions? closed-loop control?) --> 

## Abstract
The necessity of intervention in inferring cause has long been understood in neuroscience. Recent work has highlighted the limitations of passive observation and single-site lesion studies in accurately recovering causal circuit structure. The advent of optogenetics has facilitated increasingly precise forms of intervention including closed-loop control which may help eliminate confounding influences. However, it is not yet clear how best to apply closed-loop control to leverage this increased inferential power. In this paper, we use tools from causal inference, control theory, and neuroscience to show *when* and *how* closed-loop interventions can more effectively reveal causal relationships. We also examine the performance of standard network inference procedures in simulated spiking networks under passive, open-loop and closed-loop conditions. We demonstrate a unique capacity of feedback control to distinguish competing circuit hypotheses by disrupting connections which would otherwise result in equivalent patterns of correlation. Our results build toward a practical framework to improve design of neuroscience experiments to answer causal questions about neural circuits.

## Prior work + "extended abstract" (feb 10th)
<!-- *this draft is intended as an independent attempt at an abstract, with the core goal of positioning this work relative to similar papers in the field (see [exemplars.md](../sketches_and_notation/planning_big_picture/exemplars.md) )* -->

The necessity of intervention (e.g. stimulation, lesion experiments) in inferring cause has long been understood in neuroscience. Recent work has highlighted the importance of a causal perspective in answering questions about network structure and function[^pearl][^advance][^quasi]. It is increasingly clear that recording from more of the brain and using sophisticated inference approaches is necessary but not sufficient to understand how the brain functions[^fiete]. Indeed, it has been shown that open-loop stimulation and single-site lesioning experiments may also be insufficient [^promise][^lepperod][^jonas][^fakhar]. In tandem, the advent of optogenetics has facilitated increasingly precise and useful forms of intervention including closed-loop control[^grosenick] - a form of stimulation which adapts inputs in response to measured activity and which shows promise in overcoming limitations of other interventions.
<!-- gap, remaining challenges -->
However, the potential of closed-loop stimulation for network inference has not yet been achieved. A major challenge remains in integrating established techniques from control theory, causal inferences, and design of experiments in neuroscience. It is not yet clear how best to design the particulars of closed-loop control to leverage the increased inferential power granted by these approaches.
<!-- new expected results section -->
Here, we attempt to lay out these complementary ideas from causal inference and control theory in a unified description, with the goal of discovering how and where closed-loop interventions are best applied. In support of this aim, we demonstrate the performance of standard network inference procedures in simulated spiking networks under passive, open-loop and closed-loop conditions. This investigation reveals general principles of how intervention interacts with circuit structure to shape the pattern of dependence across groups. In particular, we demonstrate a unique capacity of feedback control to distinguish competing circuit hypotheses by disrupting connections which would otherwise result in equivalent patterns of correlation.
<!-- significance -->
This work continues the conversation around seeking causal answers to questions of how the brain functions and how best to use the tools at our disposal. We hope it aids those designing experiments in choosing how and where to apply stimulation in order to efficiently distinguish between competing hypotheses.



[^pearl]: Pearl, J. (2009). Causality. Cambridge university press.

[^advance]: ["Advancing functional connectivity research from association to causation"](https://www.nature.com/articles/s41593-019-0510-4) Reid et al. - Discusses concept of multiple circuit hypotheses being compatible with an observed pattern of correlation. Details a framework for understanding how methods may narrow the space of plausible hypotheses

[^quasi]: ["Quasi-experimental causality in neuroscience and behavioral research"](https://www.nature.com/articles/s41562-018-0466-5) Marinescu et al. - argues for use of instrumental variables to make causal statements even in observational settings

[^fiete]: ["Systematic errors in connectivity inferred from activity in strongly recurrent networks"](https://www.nature.com/articles/s41593-020-0699-2) Das & Fiete - demonstrates irreducible bias in connectivity estimates from highly-connected networks observed in passive settings. Suppresive open-loop stimulation was shown to reduce this bias

[^jonas]: ["Could a Neuroscientist Understand a Microprocessor?"](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005268) Jonas & Kording - demonstrates the insufficiency of single-site lesioning and other common analysis techniques in neuroscience in reverse engineering the ground-truth structure of an aritificial neural network.

[^fakhar]: [Systematic Perturbation of an Artificial Neural Network: A Step Towards Quantifying Causal Contributions in The Brain](#systematic-perturbation-of-an-artificial-neural-network-a-step-towards-quantifying-causal-contributions-in-the-brain) - building on [^jonas], this paper demonstrates the necessity of multi-site (rather than single-site) lesions in understanding the structure of artificial neural networks.

[^lepperod]: ["Inferring causal connectivity from pairwise recordings and optogenetics"](https://www.biorxiv.org/node/138945.full) *(preprint)* Lepperød et al. - discusses practical issues in inferring connectivity from stimulation which may provide common input to many neurons. Highly biased connectivity estimates can be greatly improved by applying instrumental variables. 

[^promise]: ["The promise and perils of causal circuit manipulations "](https://www.sciencedirect.com/science/article/abs/pii/S0959438817302246) Wolff, Olveczky - discusses acute v.s. chronic and disruptive v.s. physiological perturbations. Also mentions the promise of closed-loop control in this respect.

[^grosenick]: ["Closed-loop and Activity-Guided Optogenetic Control"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4775736/) Grosenick, Marshel, Deisseroth - reviews the motivation and methods for closed-loop optogenetic control for basic science and therapeutic applications