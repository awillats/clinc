---
title: Closed-Loop Identifiability in Neural Circuits
author:
-name: Adam Willats
-affiliation: Georgia Institute of Technology and Emory University
-email: awillats3@gatech.edu
-name: Matt O'Shaughnessy
-affiliation: Georgia Institute of Technology
-email: matthewoshaughnessy@gatech.edu
bibliography: bib/closedloopcausal.bib
output:
  pdf_document:
     path: /publish/manuscript_pandoc.pdf
---

# Closed-Loop Identifiability in Neural Circuits {ignore=True}
**Authors:** Adam Willats, Matt O'Shaughnessy
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

!!!! - 40% done -> closer now, awaiting some neuro-writing and status reassessment by Adam
@import "/section_content/background_causal_network_id.md"

## Interventions in neuroscience & causal inference
!!!! - 50% done:
@import "/section_content/background_intervention_causal_inf.md"

## Representations & reachability
!!!! - 60% done:
@import "/section_content/background_representation_reach.md"

!!!! - 15% done -> much closer now, awaiting reassesment by Adam
@import "/section_content/background_id_demo.md"


# Theory / Prediction
<!-- <img src="/figures/core_figure_sketches/figure2_sketch.png" width="500"/> -->
![](/figures/core_figure_sketches/methods_overview_pipeline_sketch.png)
> **Figure OVERVIEW:** ...

<!-- ![](/figures/misc_figure_sketches/intervention_identifiability_concept.png) -->
## Predicting correlation structure (theory)

@import "/section_content/methods1_predicting_correlation.md"

# Simulation Methods

<!-- ## Network simulations (simulation)
## Implementing interventions (simulation)
## Extracting circuit estimates (empirical) -->
@import "/section_content/methods0_simulations_interventions_estimates.md"

<!-- ## Information-theoretic measures of hypothesis ambiguity -->
@import "/section_content/methods2_hypothesis_entropy.md"

# Results
!!!! - overall, 40% done

## Impact of intervention on estimation performance
<!-- PANDOC YAML MAPPING ERROR -->
@import "/section_content/results1_impact_of_intervention.md"

## Interaction of intervention & circuit structure
!!!! - needs significant technical work and theory!
@import "/section_content/near_future_work/results2_circuit_x_intervention.md"


# Discussion
@import "/section_content/discussion.md"

# References
*see [pandoc pandoc-citations](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/pandoc-bibliographies-and-citations.md)*

# Supplement
@import "/section_content/supplement.md"
