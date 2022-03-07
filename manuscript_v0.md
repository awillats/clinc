**Title:** ...
**Authors:** Adam Willats, Matt O'Shaughnessy
# Table of Contents 



<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->
- [Table of Contents](#table-of-contents)
- [Table of Contents](#table-of-contents)
- [Abstract](#abstract)
- [Introduction](#introduction)
  - [Estimating causal interactions in the brain](#estimating-causal-interactions-in-the-brain)
  - [Interventions in neuroscience & causal inference](#interventions-in-neuroscience-causal-inference)
  - [Representations & reachability](#representations-reachability)
  - [Figure DEMO: Applying CLINC to distinguish a pair of circuits](#figure-demo-applying-clinc-to-distinguish-a-pair-of-circuits)
- [Theory / Prediction](#theory-prediction)
  - [Computing reachability (theory)](#computing-reachability-theory)
  - [Predicting correlation structure (theory)](#predicting-correlation-structure-theory)
- [Predicting network correlations](#predicting-network-correlations)
  - [Building blocks](#building-blocks)
    - [Derivation of expression for (co)variances](#derivation-of-expression-for-covariances)
    - [Expression for $r(i,j)$ under passive observation](#expression-for-rij-under-passive-observation)
  - [Impact of control](#impact-of-control)
    - [Open-loop control](#open-loop-control)
    - [Closed-loop control](#closed-loop-control)
    - [Impact of CL control on $r(i,j)$](#impact-of-cl-control-on-rij)
- [Simulation](#simulation)
  - [Network simulations (simulation)](#network-simulations-simulation)
  - [Implementing interventions (simulation)](#implementing-interventions-simulation)
  - [Extracting circuit estimates (empirical)](#extracting-circuit-estimates-empirical)
  - [Information-theoretic measures of hypothesis ambiguity](#information-theoretic-measures-of-hypothesis-ambiguity)
- [Results](#results)
  - [Interaction of intervention on circuit estimation](#interaction-of-intervention-on-circuit-estimation)
    - [Intervening provides (categorical) improvements in inference power beyond passive observation](#intervening-provides-categorical-improvements-in-inference-power-beyond-passive-observation)
    - [Stronger intervention shapes correlation, resulting in more data-efficient inference with less bias](#stronger-intervention-shapes-correlation-resulting-in-more-data-efficient-inference-with-less-bias)
      - [Impact of intervention location and variance on pariwise correlations](#impact-of-intervention-location-and-variance-on-pariwise-correlations)
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

@ import "/section_content/background_causal_network_id.md"

## Interventions in neuroscience & causal inference
@ import "/section_content/background_intervention_neuro.md"
@ import "/section_content/background_intervention_causal_inf.md"

## Representations & reachability
@import "/section_content/background_representation_reach.md"


## Figure DEMO: Applying CLINC to distinguish a pair of circuits
<!-- @ import "section_content/background_id_demo.md" -->

----
# Theory / Prediction 

## Computing reachability (theory)
## Predicting correlation structure (theory)
![](/figures/misc_figure_sketches/intervention_identifiability_concept.png)
@import "/section_content/methods1_predicting_correlation.md"

----
# Simulation

## Network simulations (simulation)

## Implementing interventions (simulation)

## Extracting circuit estimates (empirical)
@import "/section_content/methods0_simulations_interventions_estimates.md"

## Information-theoretic measures of hypothesis ambiguity
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