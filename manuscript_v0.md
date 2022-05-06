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


[ `current focus` ](#results)


# Abstract

@import "/section_content/abstract.md"

# Introduction

## Estimating causal interactions in the brain
@import "/section_content/background_causal_network_id.md"

## Interventions in neuroscience & causal inference
@import "/section_content/background_intervention_causal_inf.md"

<!-- ## ? Representations & reachability (minimal, dupe)
```
consider:
@ import "/section_content/representation_reach.md"
@ import "/section_content/background_id_demo.md"
``` -->

# Results
@import "/section_content/results_overview.md"

## ( Box 1: )
@import "/section_content/background_id_demo.md"

## Steps of inference - *overview of CLINC approach* (+)
```
how do these steps help address established challenges 
```
![](/figures/core_figure_sketches/methods_overview_pipeline_sketch.png)

> **Figure OVERVIEW:** ...

- `reference extended methods`
@import "/section_content/overview_steps_of_inference.md"


<!-- NOTE: Cutting lots of sections here. Anything that needs to be re-included from this section should go into steps of inference 

<!-- ### Extracting circuit estimates (4.3)
`@ import "/section_content/methods_circuit_estimates.md"` 
<!-- NOTE: background_id_demo here instead? before or after methods are introduced 

## Impact of intervention on estimation performance 
### (predicting) impact of intervention on pairwise dependence (3.1?, 5.1?)
<!-- NOTE: ^ this H2 will likely be removed from, be implicit in final draft

#### Representations & reachability
`extract minimum from:`
`@ import "/section_content/representation_reach.md"`

<!-- @ import "/section_content/background_id_demo.md" 

#### Predicting correlation structure (theory)
```
extract minimum from: 
@ import "/section_content/methods_predicting_correlation.md"
```

```
extract minimum from: 
@ import "/section_content/methods_interventions.md"
@ import "/section_content/results_impact_of_intervention.md"
```
-->


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
@import "/section_content/representation_reach.md"
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
<!-- *see [_steps_of_inference.md](_steps_of_inference.md) for entropy writeup* -->
@import "/section_content/methods_entropy.md"
### Selecting interventions (...) {#sec:entropy-selection}
@import "/section_content/methods_entropy_selection.md"



# References
*see [pandoc pandoc-citations](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/pandoc-bibliographies-and-citations.md)*

# Supplement
@import "/section_content/supplement.md"
