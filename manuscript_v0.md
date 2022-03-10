# Closed-Loop Identifiability in Neural Circuits {ignore=True}
**Authors:** Adam Willats, Matt O'Shaughnessy
<!-- see also _meta folder, consider formatting as "YAML front matter" for pandoc -->

# Table of Contents 

<!-- @ import "[TOC]" {cmd="toc" depthFrom=1 depthTo=2 orderedList=false} -->
<!-- code_chunk_output -->
- [Table of Contents](#table-of-contents)
- [Abstract](#abstract)
- [Introduction](#introduction)
  - [Estimating causal interactions in the brain](#estimating-causal-interactions-in-the-brain)
  - [Interventions in neuroscience & causal inference](#interventions-in-neuroscience-causal-inference)
  - [Representations & reachability](#representations-reachability)
- [Theory / Prediction](#theory-prediction)
  - [Predicting correlation structure (theory)](#predicting-correlation-structure-theory)
- [Simulation](#simulation)
  - [Methods overview](#methods-overview)
  - [Implementing interventions](#implementing-interventions)
  - [Extracting circuit estimates](#extracting-circuit-estimates)
  - [Information-theoretic measures of hypothesis ambiguity](#information-theoretic-measures-of-hypothesis-ambiguity)
- [Results](#results)
  - [Interaction of intervention on circuit estimation](#interaction-of-intervention-on-circuit-estimation)
  <!-- - [Interaction of intervention & circuit structure](#interaction-of-intervention-circuit-structure) -->
- [Discussion](#discussion)
- [References](#references)
- [Supplement](#supplement)
<!-- /code_chunk_output -->

# Abstract
@import "/section_content/abstract.md"
----
# Introduction

## Estimating causal interactions in the brain
<img src="/figures/core_figure_sketches/figure1_sketch.png" width="400"/>

> 🚧 (very rough draft) **Figure INTRO: (conceptual overview of interacting regions, intervention, DAGs etc.)**

!!!! - 40% done:
@import "/section_content/background_causal_network_id.md"

## Interventions in neuroscience & causal inference
!!!! - 50% done:
@import "/section_content/background_intervention_causal_inf.md"

## Representations & reachability
!!!! - 60% done:
@import "/section_content/background_representation_reach.md"

!!!! - 15% done
@import "/section_content/background_id_demo.md"

- [ ] @adam sketch the flow of the argument
- [ ] @matt to round out writing demo / example walkthrough

----
# Theory / Prediction 
>*(Draft overview)*
![](/figures/misc_figure_sketches/intervention_identifiability_concept.png)

<!-- ![](/figures/misc_figure_sketches/intervention_identifiability_concept.png) -->
<!-- ## Computing reachability (theory) -->
## Predicting correlation structure (theory)
    
@import "/section_content/methods1_predicting_correlation.md"

----
# Simulation Methods

<!-- ## Network simulations (simulation)
## Implementing interventions (simulation)
## Extracting circuit estimates (empirical) -->
@import "/section_content/methods0_simulations_interventions_estimates.md"

<!-- ## Information-theoretic measures of hypothesis ambiguity -->
@import "/section_content/methods2_hypothesis_entropy.md"

----
  
# Results
!!!! - overall, 40% done

## Impact of intervention on estimation performance
@import "/section_content/results1_impact_of_intervention.md"

## Interaction of intervention & circuit structure
!!!! - needs significant technical work and theory!
@import "/section_content/near_future_work/results2_circuit_x_intervention.md"

----

# Discussion
@import "/section_content/discussion.md"

# References
*see [pandoc pandoc-citations](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/pandoc-bibliographies-and-citations.md)*

# Supplement
@import "/section_content/supplement.md"
