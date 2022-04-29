---
panflute-filters: [cleanup_filter]
panflute-path: 'publish/panflute_filters'
title: Closed-Loop Identifiability in Neural Circuits
author:
  - name: Adam Willats, Matthew O'Shaughnessy
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
<!-- !!!! - 70% done -->

@import "/section_content/background_causal_network_id.md"

## Interventions in neuroscience & causal inference
<!-- !!!! - 70% done -->

@import "/section_content/background_intervention_causal_inf.md"

## Representations & reachability
<!-- !!!! - 60% done -->

@import "/section_content/representation_reach.md"

@import "/section_content/background_id_demo.md"

# Theory / Prediction
<!-- <img src="/figures/core_figure_sketches/figure2_sketch.png" width="500"/> -->
![](/figures/core_figure_sketches/methods_overview_pipeline_sketch.png)
> **Figure OVERVIEW:** ...

<!-- ![](/figures/misc_figure_sketches/intervention_identifiability_concept.png) -->
## Predicting correlation structure (theory)
@import "/section_content/methods_predicting_correlation.md"

# Simulation Methods

<!-- were compiled in 
 @ import "/section_content/methods0_simulations_interventions_estimates.md" 
 -->
@import "/section_content/methods_simulations.md" 
<!-- works! -->
@import "/section_content/methods_interventions.md"
<!-- works! -->
@import "/section_content/methods_circuit_estimates.md"

## Information-theoretic measures of hypothesis ambiguity
*see [_steps_of_inference.md](_steps_of_inference.md) for entropy writeup*

# Results
<!-- !!!! - overall, 60% done -->

## Impact of intervention on estimation performance
### Intervening provides (categorical) improvements in inference power beyond passive observation
@import "/section_content/results_impact_of_intervention.md"
  
<!-- @ import "results_data_efficiency_and_bias.md" -->
    
<!-- 
## Interaction of intervention & circuit structure
@ import "/section_content/near_future_work/results2_circuit_x_intervention.md" -->

# Discussion
<!-- !!!! - overall, 30% done -->
@import "/section_content/discussion.md"

# References
*see [pandoc pandoc-citations](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/pandoc-bibliographies-and-citations.md)*

# Supplement
@import "/section_content/supplement.md"
