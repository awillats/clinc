---
panflute-filters: [cleanup_filter]
panflute-path: 'publish/panflute_filters'
title: Closed-Loop Identifiability in Neural Circuits
author:
  - name: Adam Willats, Matthew O'Shaughnessy, Christopher Rozell
bibliography: [bib/moshaughnessy.bib, bib/misc.bib, bib/mega_causal_bib.bib, bib/clinc_sync.bib]
output:
  pdf_document:
     path: /publish/other_formats/manuscript_v0_pandoc.pdf
classoption: twocolumn
geometry: margin=1.5cm
numbersections: true
---
<!-- 
id: "hide-todo" 
NOTE: uncomment `id: hide-todo` to hide to-do list items and collapsible section
NOTE: requires MPE Use Pandoc Parser to be off 
 -->
<!-- @ import "publish/publish_style.less" -->

<!-- see also _meta folder, consider formatting as "YAML front matter" for pandoc -->

<!-- # Table of Contents {ignore=True} -->

<!-- @ import "[TOC]" {cmd="toc" depthFrom=1 depthTo=2 orderedList=false} -->
<!-- code_chunk_output -->
<!-- - [Abstract](#abstract)
- [Introduction](#introduction)
  - [Estimating causal interactions in the brain](#estimating-causal-interactions-in-the-brain)
  - [Interventions in neuroscience & causal inference](#interventions-in-neuroscience-causal-inference)
  - [Draft](#draft)
  - [Representations & reachability](#representations-reachability)
- [Theory / Prediction](#theory-prediction)
  - [Predicting correlation structure (theory)](#predicting-correlation-structure-theory)
- [Simulation Methods](#simulation-methods)
- [Results](#results)
  - [Impact of intervention on estimation performance](#impact-of-intervention-on-estimation-performance)
  - [Interaction of intervention & circuit structure](#interaction-of-intervention-circuit-structure)
- [Discussion](#discussion)
- [References](#references) -->
<!-- /code_chunk_output -->


# Abstract

@import "/section_content/abstract.md"

# Introduction

## Estimating causal interactions in the brain
@import "/section_content/background_causal_network_id.md"

## Interventions in neuroscience & causal inference
@import "/section_content/background_intervention_causal_inf.md"


<!-- NOTE: GAP in field -->
Despite the promise of these closed-loop strategies for identifying causal relations in neural circuits, however, it is not yet fully understood *when* more complex intervention strategies can provide additional inferential power, or *how* these experiments should be optimally designed. In this paper we demonstrate when and how closed-loop interventions can reveal the causal structure governing neural circuits. Drawing from ideas in causal inference
[@pearl2009causality; @maathuis2016review; @chis2011structural], we describe the classes of models that can be distinguished by a given set of input-output experiments, and what experiments are necessary to uniquely determine specific causal relationships.

<!-- NOTE: PAPER SUMMARY -->
We first propose a mathematical framework that describes how open- and closed-loop interventions impact observable qualities of neural circuits. Using this framework, experimentalists propose a set of candidate hypotheses describing the potential causal structure of the circuit under study, and then select a series of interventions that best allows them to distinguish between these hypotheses. Using simplified *in silico* networks, we explore factors that govern the efficacy of these types of interventions. Guided by the results of this exploration, we present a set of recommendations that can guide the design of open- and closed-loop experiments to better uncover the causal structure underlying neural circuits.


<!-- ## ? Representations & reachability (minimal, dupe)
```
consider:
@ import "/section_content/methods_representation_reachability.md"
@ import "/section_content/background_id_demo.md"
``` -->

# Results
@import "/section_content/results_overview.md"

## Demonstrating interventions and circuit inference
@import "/section_content/background_id_demo.md"

## Steps of inference 
@import " /section_content/overview_steps_of_inference.md "

<!-- ### Intervening provides categorical improvements in inference power beyond passive observation -->
@import "/section_content/results_impact_of_intervention.md"

<!-- ### Stronger intervention shapes correlation, resulting in more data-efficient inference with less bias - *bidirectional var control* (5.1.2) -->
<!-- #### Impact of intervention location and variance on pairwise correlations-->
@import "/section_content/results_impact_variance.md"


<!-- 
@ import "results_data_efficiency_and_bias.md"
## Interaction of intervention & circuit structure
@ import "/section_content/near_future_work/results2_circuit_x_intervention.md" -->

# Discussion
@import "/section_content/discussion.md"

<hr>

# Methods


## Modeling network structure and dynamics (4.1) --- Simulation Methods
@import "/section_content/methods_simulations.md" 
### Stochastic network dynamics (4.1.1)
### Delayed interactions (4.1.2)
### Code implementation (4.1.3)
## Implementing interventions (4.2)
@import "/section_content/methods_interventions.md" 


## Predicting correlation structure (3.1) --- Theory / Prediction
### Representations & reachability (2.3?)
@import "/section_content/methods_representation_reachability.md"
```
see also:
@ import "/section_content/background_id_demo.md"
```
### Predicting correlation structure (3.1) {#methods-predict-corr}
@import "/section_content/methods_predicting_correlation.md"
<hr>
@import "/section_content/methods_coreach_sign.md"

### Impact of interventions - theory, pred (3.1?, 5.1?)

<hr>
@import "/section_content/methods_intervention_variance.md"
```
see also:
@ import "/section_content/methods_predicting_correlation.md"
@ import "/section_content/results_impact_of_intervention.md"`
```

## Extracting circuit estimates (4.3)
@import "/section_content/methods_circuit_estimates.md"
### Time-resolvable interactions *XCORR* (4.1.2)
`@ import "/section_content/methods_simulations.md" time-resolvable domain`

### Information-theoretic measures of hypothesis ambiguity (4.4) {#sec:entropy}
<!-- *see [steps_of_inference.md](section_content/overview_steps_of_inference.md) for entropy writeup* -->
@import "/section_content/methods_entropy.md"
### Selecting interventions (...) {#sec:entropy-selection}
@import "/section_content/methods_entropy_selection.md"



# References
*see [pandoc pandoc-citations](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/pandoc-bibliographies-and-citations.md)*

# Supplement
@import "/section_content/supplement.md"
