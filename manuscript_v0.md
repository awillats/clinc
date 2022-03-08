# Closed-Loop Identifiability in Neural Circuits {ignore=True}
**Authors:** Adam Willats, Matt O'Shaughnessy
<!-- see also _meta folder, consider formatting as "YAML front matter" for pandoc -->

# Table of Contents 



<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=2 orderedList=false} -->
<!-- code_chunk_output -->
- [Table of Contents](#table-of-contents)
- [Table of Contents](#table-of-contents)
- [Abstract](#abstract)
- [Introduction](#introduction)
  - [Estimating causal interactions in the brain](#estimating-causal-interactions-in-the-brain)
  - [Interventions in neuroscience & causal inference](#interventions-in-neuroscience-causal-inference)
  - [Outline](#outline)
  - [See also](#see-also)
  - [Draft](#draft)
  - [Representations & reachability](#representations-reachability)
  - [Figure DEMO: Applying CLINC to distinguish a pair of circuits](#figure-demo-applying-clinc-to-distinguish-a-pair-of-circuits)
- [Theory / Prediction](#theory-prediction)
  - [Computing reachability (theory)](#computing-reachability-theory)
  - [Predicting correlation structure (theory)](#predicting-correlation-structure-theory)
- [Predicting network correlations](#predicting-network-correlations)
  - [Building blocks](#building-blocks)
  - [Impact of control](#impact-of-control)
- [Simulation](#simulation)
  - [Network simulations (simulation)](#network-simulations-simulation)
  - [Implementing interventions (simulation)](#implementing-interventions-simulation)
  - [Extracting circuit estimates (empirical)](#extracting-circuit-estimates-empirical)
  - [Information-theoretic measures of hypothesis ambiguity](#information-theoretic-measures-of-hypothesis-ambiguity)
- [Results](#results)
  - [Interaction of intervention on circuit estimation](#interaction-of-intervention-on-circuit-estimation)
  - [Interaction of intervention & circuit structure](#interaction-of-intervention-circuit-structure)
- [Discussion](#discussion)
- [References](#references)
- [Supplement](#supplement)
- [Supplement](#supplement)
<!-- /code_chunk_output -->


# Abstract
@import "/section_content/abstract.md"
----
# Introduction

## Estimating causal interactions in the brain
<img src="/figures/core_figure_sketches/figure1_sketch.png" width="400"/>

!!!! - 40% done:
@ import "/section_content/background_causal_network_id.md"

## Interventions in neuroscience & causal inference
!!!! - 50% done:
@import "/section_content/background_intervention_causal_inf.md"

## Representations & reachability
!!!! - 60% done:
@import "/section_content/background_representation_reach.md"


## Figure DEMO: Applying CLINC to distinguish a pair of circuits
<!-- @ import "section_content/background_id_demo.md" -->

----
# Theory / Prediction 
>*(OVERVIEW)*
![](/figures/misc_figure_sketches/intervention_identifiability_concept.png)
<!-- ![](figures/misc_figure_sketches/intervention_identifiability_concept.png) -->
## Computing reachability (theory)
## Predicting correlation structure (theory)
@import "/section_content/methods1_predicting_correlation.md"

----
# Simulation

<!-- ## Network simulations (simulation)
## Implementing interventions (simulation)
## Extracting circuit estimates (empirical) -->
@import "/section_content/methods0_simulations_interventions_estimates.md"


<!-- ## Information-theoretic measures of hypothesis ambiguity -->
@import "/section_content/methods2_hypothesis_entropy.md"


----

# Results
<!-- ## Characterizing circuit-pair ambiguity through reachability properties -->
<!-- ## Impact of node, network parameters on estimation performance -->

## Interaction of intervention on circuit estimation
<!-- ## Impact of intervention on estimation performance -->
@import "/section_content/results1_impact_of_intervention.md"

## Interaction of intervention & circuit structure
@import "/section_content/results2_circuit_x_intervention.md"

----

# Discussion
@import "/section_content/discussion.md"
# References
*see [pandoc pandoc-citations](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/pandoc-bibliographies-and-citations.md)*

# Supplement
@import "/section_content/supplement.md"
