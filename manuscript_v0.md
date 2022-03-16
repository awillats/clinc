---
title: Closed-Loop Identifiability in Neural Circuits

output:
  pdf_document:
     path: /publish/manuscript_pandoc.pdf
xnumberedsections: true
author:
  - name: Adam Willats, Matthew O'Shaughnessy
---

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

!!!! Todo 3/16: - Mention basic science applications of CL control - Maybe more forecasting idea of shaping correlations? (don't want reader to be surprised by structure of paper's argument)

@import "/section_content/abstract.md"


# Introduction

## Estimating causal interactions in the brain

!!!! - 70% done

!!!! Todo 3/16: - "We first propose..." paragraph (could build out or move or change focus away from the 'framework') - think about condensing and/or moving "Inferring causal interactions from time series" subsection - Maybe add half a paragraph or so in the discussion about how causal inference tools can help above correlation analysis (e.g., PC algorithm)

@import "/section_content/background_causal_network_id.md"

## Interventions in neuroscience & causal inference

!!!! - 70% done

!!!! Todo - Get language more precise and effective *(see writing_tasks)*

@import "/section_content/background_intervention_causal_inf.md"

## Representations & reachability

!!!! - 60% done

!!!! todo - Rewrite X=XW+E as vector version - Describe what 'reachability' is *(see writing_tasks)*

@import "/section_content/background_representation_reach.md"

!!!! - 70% done

!!!! todo - Talk about what 'reachability' means (total direct+indirect impact) - [Matt:] Rewrite first paragraph to not use notation (place this box before any theory/notation sections) - [Matt:] Set expectation here that we're talking about linear Gaussian circuits

@import "/section_content/background_id_demo.md"


# Theory / Prediction
<!-- <img src="/figures/core_figure_sketches/figure2_sketch.png" width="500"/> -->
![](/figures/core_figure_sketches/methods_overview_pipeline_sketch.png)
> **Figure OVERVIEW:** ...

<!-- ![](/figures/misc_figure_sketches/intervention_identifiability_concept.png) -->
## Predicting correlation structure (theory)

@import "/section_content/methods1_predicting_correlation.md"

!!!! todo - Some redundancy with simulation methods; cut and paste anything useful in 4.2 and put into 3.1 / 3.2

# Simulation Methods

!!!! todo - reorganize / split sections 

<!-- ## Network simulations (simulation)
## Implementing interventions (simulation)
## Extracting circuit estimates (empirical) -->
@import "/section_content/methods0_simulations_interventions_estimates.md"

<!-- ## Information-theoretic measures of hypothesis ambiguity -->
@import "/section_content/methods2_hypothesis_entropy.md"

# Results
!!!! - overall, 60% done

## Impact of intervention on estimation performance
<!-- PANDOC YAML MAPPING ERROR -->
!!!! todo - comaprison signs in rows of DISAMBIG figure
!!!! todo - merge from "box style" where entrire story is in caption, to having something in body of results text 
!!!! todo - write "explain why CL is better" section, ? exile it to discussion section?
!!!! todo - connect DISAMBIG caption to quantitative variance explanation section
!!!! todo - collapse figvar - do we need to make shared input point here? or is discussion fine?
!!!! todo - dR/dS needs to mention R as r^2 corr
@import "/section_content/results1_impact_of_intervention.md"
 
<details><summary>↪Notes from matt</summary>

- [super minor] First part of fig DISAMBIG: subsections (A) through (C) work really well
- [super minor] in caption for (D-F): "modifications to the passive correlation pattern" is a bit confusing in the context of open-loop intervention
- [super minor] also in caption for (D-F): really like "intervention-specific fingerprint" terminology. The last sentence of the (D-F) caption really hits the message home, possible to emphasize that this is the take-home message earlier?
- [narrative/organization] fig DISAMBIG feels really example-y, more like a proof of concept than 'results.' The writing in Sec 5.1.1 also has this flavor, like it could be in a methods section. (The plot in the top right feels much more results-ey.) Not necessarily a bad thing, maybe just a consideration for thinking about article vs perspective flavor.
- [missing] Section 5.1.2.1: what are the definitions of S_k, CoReach(i,j|S_k), and R_{ij}?
- [narrative] Section 5.1.2.1: the narrative here really works for me, but it's a little unclear whether this is more of a 'result' or a 'recipe' -- the figures here also feel more example/proof-of-concept-ey, and the math here helps ground things in
- [missing] discussion of partial closed-loop control?
</details>

 
<!-- ## Interaction of intervention & circuit structure
!!!! - needs significant technical work and theory!
@ import "/section_content/near_future_work/results2_circuit_x_intervention.md" -->

# Discussion
@import "/section_content/discussion.md"

# References
*see [pandoc pandoc-citations](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/pandoc-bibliographies-and-citations.md)*

# Supplement
@import "/section_content/supplement.md"
