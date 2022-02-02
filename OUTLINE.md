# Overview 
## Intended audience
  - **systems neuroscientists** interested in making more rigorous conclusions in circuit ID problems 
  - **experimental neuroscientists** looking for guidance on evaluating required intervention to answer circuit hypothesis questions
## Goal -  Provide a practical conceptual framework for applying closed-loop to circuit identification problems
- What’s the value of closed-loop?
- What can i say about causal connections given the experiments i’m doing?
- How do I design an intervention which improves the strength of hypothesis testing?




- [Methods](#methods)
  - [Multiple complementary perspectives (represenations) of the same underlying network structure:](#multiple-complementary-perspectives-represenations-of-the-same-underlying-network-structure)
  - [Interventions in causal identification](#interventions-in-causal-identification)
  - [Reachability](#reachability)
  - [Understanding identification through derived properties of circuits (reachability rules)](#understanding-identification-through-derived-properties-of-circuits-reachability-rules)
  - [Network simulations](#network-simulations)
    - [Figure GAUSSIAN: Gaussian and spiking networks simulated in Brian2](#figure-gaussian-gaussian-and-spiking-networks-simulated-in-brian2)
  - [Extracting circuit estimates](#extracting-circuit-estimates)
    - [Figure PIPELINE: Process of detecting connections in a network model](#figure-pipeline-process-of-detecting-connections-in-a-network-model)
    - [Outputs of network](#outputs-of-network)
    - [lagged cross-correlation](#lagged-cross-correlation)
    - [multivariate transfer entropy (muTE)](#multivariate-transfer-entropy-mute)
    - [statistical testing](#statistical-testing)
- [Results](#results)
  - [Figure DEMO: Applying CLINC to distinguish a pair of circuits (case-study)](#figure-demo-applying-clinc-to-distinguish-a-pair-of-circuits-case-study)
  - [[Binary Sim.] - Characterizing circuit-pair ambiguity through binary reachability properties](#binary-sim-characterizing-circuit-pair-ambiguity-through-binary-reachability-properties)
  - [Characterization of network estimation performance](#characterization-of-network-estimation-performance)
    - [Extracting circuit estimates](#extracting-circuit-estimates-1)
    - [Quantifying successful identification](#quantifying-successful-identification)
    - [*Impact of node, network parameters*](#impact-of-node-network-parameters)
    - [Figure PROPS: impact of intrinsic network properties on identifiability](#figure-props-impact-of-intrinsic-network-properties-on-identifiability)
    - [Figure MOTIF: Interaction of network structure and intervention location on identifiability](#figure-motif-interaction-of-network-structure-and-intervention-location-on-identifiability)
    - [*Impact of intervention*](#impact-of-intervention)
    - [Figure DATA: Analysis of simulated circuits suggest stronger intervention facilitates identification with less data](#figure-data-analysis-of-simulated-circuits-suggest-stronger-intervention-facilitates-identification-with-less-data)
    - [Figure PREDICT: Comparing predicted and emprical identification performance](#figure-predict-comparing-predicted-and-emprical-identification-performance)
    - [Figure DISAMBIG: Stronger intervention facilitates disambiguating equivalent hypotheses](#figure-disambig-stronger-intervention-facilitates-disambiguating-equivalent-hypotheses)
- [Discussion](#discussion)
- [Supplement](#supplement)

<!-- /code_chunk_output -->




# Table of Contents
- [Introduction](#introduction)
- [Methods](#methods)
    - [Multiple complementary represenations](#multiple-complementary-perspectives-represenations-of-the-same-underlying-network-structure)
    - [Interventions in causal identification](#interventions-in-causal-identification)
    - [Reachability](#reachability)
    - [Network simulations](#network-simulations)
      - [Figure GAUSSIAN: Gaussian and spiking networks simulated in Brian2](#figure-gaussian-gaussian-and-spiking-networks-simulated-in-brian2)
    - [Extracting circuit estimates](#extracting-circuit-estimates)
      - [Figure PIPELINE: Process of detecting connections in a network model](#figure-pipeline)
- [Results](#results)
  - [Understanding the binary setting](#figure-demo)
    - [Figure DEMO: Applying CLINC to distinguish a pair of circuits (case-study)](#figure-demo)
    - [[Binary Sim.] - Characterizing circuit-pair ambiguity through binary reachability properties](#binary-sim-characterizing-circuit-pair-ambiguity-through-binary-reachability-properties)
  - [Impact of node, network parameters](#impact-of-node-network-parameters)
    - [Figure PROPS: impact of intrinsic network properties on identifiability](#figure-props)
    - [Figure MOTIF: Interaction of network structure and intervention location on identifiability](#figure-motif)
  - [Impact of intervention](#impact-of-intervention)
    - [Figure DATA: Analysis of simulated circuits suggest stronger intervention facilitates identification with less data](#figure-data)
    - [Figure PREDICT: Comparing predicted and emprical identification performance](#figure-predict)
    - [Figure DISAMBIG: Stronger intervention facilitates disambiguating equivalent hypotheses](#figure-disambig)
- [Discussion](#discussion)
- [Supplement](#supplement)

---
# Introduction 
- Interventions in neuro 
  - lesion studies in neuro
    - disadvantages of lesioning
  
- What is closed-loop control?
    - Responsive and per-sample feedback control in neuro
    - Comparison to standard neuro system identification procedures (stim, lesions)
    - Stanley, Rozell prior work in closed-loop opto

- **Causal methods for network discovery from time-series**
  - What challenges are faced when estimating network connectivity?
    - [...]
  - background building from granger causality towards more complex methods
    - highlight limitations with current approaches
  - *cite J.Runge*
  
- Interventions from the perspective of causal inference
  - core idea is that "stronger" interventions lead to "higher inferential power"
    - may mean identifying circuits with less data 
    - but may also mean distinguishing circuits which may have been "observationally equivalent" under weaker interventions 
  
---
# Methods 
## Multiple complementary perspectives (represenations) of the same underlying network structure:
- The circuit view
  - (A) → (B) ↔ (C)
- The dynamical system view

\[
\begin{cases}{x' = Ax + Bu}\\
y=Cx+\eta
\end{cases}
\]

- The connectivity (adjacency matrix) view
\[
\underbrace{\begin{bmatrix} \dot{x}_A \\ \dot{x}_B \\ \dot{x}_C \end{bmatrix}}_{\dot{x}} =
\underbrace{\begin{bmatrix}
    w_{AA} & w_{AB} & w_{AC} \\
    w_{BA} & w_{BB} & w_{BC} \\
    w_{CA} & w_{CB} & w_{CC}
\end{bmatrix}}_{A}
\underbrace{\begin{bmatrix}
    x_A \\
    x_B \\
    x_C
\end{bmatrix}}_{x}
\]
- why consider multiple 

## Interventions in causal identification
- intervention types 
  - passive observation 
  - open-loop stimulation 
    - simulated as direct current injection
    - but uniform across a population 
    - ( see [Kyle Johnsen's cleosim toolbox](https://cleosim.readthedocs.io/en/latest/index.html) for more detailed simulation of stimulation )
  - closed-loop stimulation
    - approaches for control 
      - going with "model-free" PID control of output rates
    - comparison to randomization in traditional experiment design
  
## Reachability
- concept of **binary reachability** as a "best case scenario" for identification.
  - binary reachability describes which pairs of nodes we expect to have any correlation
  - can be used to predict "equivalence classes", i.e. circuits which may be indistinguishable under certain interventions
  - how binary reachability is computed 
    - [...equations here...]
- **graded reachability** can help predict the influence of parameter values (e.g. edge weights, time-constants) on identifiability
  - quantifies impact of inputs, noise on outputs
  - easiest to describe/understand in linear-gaussian setting
  - [...equations here...]

<a name='figure-reachability'></a>
🏞️ **Figure:** illustrate reachability 🏞️


## Understanding identification through derived properties of circuits (reachability rules)
- connect **binary reachability** to classes of ambiguity 
  - a pair of networks are ambiguous (given some intervention) if they are in the same markov equivalence class 
  - ambiguity x intervention leads to the following classes 
    - passively unambiguous
    - open-loop unambiguous 
    - (single-site) closed-loop unambiguous
    - 
- connect **graded reachability** to ID-SNR 
  - $\mathrm{IDSNR}_{ij}$ measures the strength of signal related to the connection $i→j$ relative to in the output of node $j$ 
  - for true, direct connections this quantity increasing means a (true positive) connection will be identified more easily (with high certainty, requiring less data)
  - for false or indirect connections, this quantity increasing means a false positive connection is more likely to be identified
  - as a result we want to maximize IDSNR for true links, and minimize it for false/indirect links 

## Network simulations 
<a name='figure-gaussian'></a>
![](figures/misc_figure_sketches/gaussian_vs_spiking_network_eg.png)
### Figure GAUSSIAN: Gaussian and spiking networks simulated in Brian2

- built on [Brian2](https://elifesciences.org/articles/47314) spiking neural network simulator 
- (delayed) linear-gaussian network 
  - required custom functionality to implement 
    - [[brian_delayed_gaussian] repository ](https://github.com/awillats/brian_delayed_gaussian)
- spiking network 

## Extracting circuit estimates 

<a name='figure-pipeline'></a>
![](figures/misc_figure_sketches/network_estimation_pipeline_sketch.png)
<!-- ![](figures/core_figure_sketches/figure4a_sketch.png) -->
<!-- ![](figures/misc_figure_sketches/data_xcorr_gaussian.png) -->
### Figure PIPELINE: Process of detecting connections in a network model
### Outputs of network 
- spikes from populations of neurons 
### lagged cross-correlation 
- connection to / equivalence with Granger Causality (GC)
  - review of GC in neuro
  - requisite assumptions
  - limitations of GC
- xcorr features 
  - peak-SNR
  - prominence 
  - time of peak
- window of time-lags considered for direct connections
  - some multiple of expected synaptic delay

### multivariate transfer entropy (muTE)
- advantages above usual GC approach

### statistical testing 
- *for muTE, handled by IDTxl*
  - includes appropriate multiple-comparison testing


---
# Results 
<a name='figure-demo'></a>
🏞️
## Figure DEMO: Applying CLINC to distinguish a pair of circuits (case-study)
  - explanation using binary reachability rules
    - consider postponing until we introduce intervention? 
    - i.e. have one figure that walks through both reachability and impact of intervention
  - *(e.g. Advancing functional connectivity research from association to causation, Combining multiple functional connectivity methods to improve causal inferences)*

<a name='figure-binary'></a>
## [Binary Sim.] - Characterizing circuit-pair ambiguity through binary reachability properties
  - proportion of each ambiguity class as a function of circuit size
  - possibly weight proportions by observed frequency of triplet motifs
✂️️ **Figure:** ambiguity class by circuit size✂️ 🏞️
    - SCOPE: cut?
    
## Characterization of network estimation performance 

### Extracting circuit estimates 
- *(see methods for xcorr, muTE)*

### Quantifying successful identification
- binary "classification" metrics
  - accuracy, F1 score (Wang & Shanechi 2019)
  - AUC (Pastore)
  - Jaccard index (Lepage, Ching, and Kramer 2013)
  - true/false positives, true/false negatives 
- graded metrics (*not a core focus here*)
  - distance between identified connection strength and ground-truth
    - MSE [(Lepperod et al. 2018)](https://www.biorxiv.org/content/10.1101/463760v2)
  - error in output reconstruction
- *relevant "negative control" for comparison (?)*
  - identified connectivity for random network?
  - some shuffled data-surrogate procedure?
- *relevant "positive control" for comparison (?)*


### *Impact of node, network parameters*

- **gaussian network simulation**

  <details><summary> ↪️ click to expand </summary>
  
  - **parameters**
    - synaptic (edge) weights - $w$
    - synaptic (edge) delay - $\delta$
    - time-constants - $\tau$
    - node noise - $\sigma$
  - **expected results**
    - weight increases xcorr peaks
    - $\tau$ blurs xcorr peak in time 
    - delay $\delta$ increases time-separability of sources 
      - at $\delta = 0$ limit, connections are harder to distinguish
        - especially direct v.s. indirect
    - noise $\sigma$ has a "location specific" impact describe by IDSNR transfer function 
      - generally, high noise "upstream" of a connection increases the strength of a hypothesized connection 
        - as long as any path is present between $i→→j$
      - high noise "downstream" of a connection, but impinging on the output node competes with / blurs / corrupts  
      - **The location-dependent impact of noise on connection identifiability may be one key way in which different forms of intervention impact circuit estimates**
  </details>
  
- **spiking network simulation**
  - all gaussian params, plus ...
  - spiking nonlinearity
    - gain
    - bias 
    - spiking threshold 
    
<a name='figure-props'></a>
![](figures/misc_figure_sketches/intrinsic_network_params.png)
### Figure PROPS: impact of intrinsic network properties on identifiability   
  - *(e.g. Identification of excitatory-inhibitory links and network topology in large-scale neuronal assemblies from multi-electrode recordings)*
  - comparison to predicted IDSNR 

- **impact of circuit structure**
- degree of nodes 
  - in/out-degree 
  - of source - $i$
  - of target - $j$
- presence of indirect correlations 
- presence of feedback loops
- \# of circuits in equivalence class 


<a name='figure-motif'></a>
🏞️
### Figure MOTIF: Interaction of network structure and intervention location on identifiability
### *Impact of intervention*
- intervention types 
  - passive observation 
  - open-loop stimulation 
  - closed-loop stimulation
    - controller stregnth
      - gain
      - bandwidth
    - controller delay
    
  - additional stimulation factors (open- & closed-loop)
    <details><summary> ↪️ click to expand </summary>
    
    - **stimulus location** 
      - single-site
      - multi-site
      - location relative to features of network
        - in-degree/out-degree
        - upstream/downstream of hypothesized connection 
    - stimulus intensity 
      - expected mean output rate 
      - frequency content 
      </details>
  
<a name='figure-data'></a>
![](figures/misc_figure_sketches/intervention_eg.png)
![](figures/literature_figs/spike_field_shanechi_crop.png)
![](figures/misc_figure_sketches/idtxl_eg_datareq_passive_open_loop.png)  
### Figure DATA: Analysis of simulated circuits suggest stronger intervention facilitates identification with less data 
  - *metric:* \# of samples required to reach accuracy threshold
  - closed-loop > open-loop > passive 


<a name='figure-predict'></a>
🏞️
### Figure PREDICT: Comparing predicted and emprical identification performance
  - layout: scatterplot and curve fit of emprical vs predicted accuracy (false positives, false negatives)
    - segmented by circuit type?
  - could be part of figures above 
  
<a name='figure-disambig'></a>
🏞️
### Figure DISAMBIG: Stronger intervention facilitates disambiguating equivalent hypotheses
  - SCOPE: can this be combined with case-study walkthrough?
  - like a quantitative version of [binary proportion figure](#figure-binary)
  - in example: shows a dataset with many correlations, multiple plausible circuit hypotheses 
    - patterns of correlation become more specific with increasing intervention strength 
  - in aggregate: focuses on reduced bias, higher accuracy for "infinite" data limit
  - closed-loop > open-loop > passive 
  

---
# Discussion 
- Comparison to related work
  - comparison to work in ANNs 
    - Kording, fakhar 
  - comparison to Shanechi
  - comparison to Bassett "network controllability" view

- Limitations of evaluated interventions 
  - quantifying the impact of imperfect / realistic control 
  - barriers such as low spatial / temporal precision may prevent high-performing control
  
- Limitations of network extraction approach
  - limitations of bivariate xcorr 
  - effect of design / hyperparameters
    - nonlinear TE estimators
    - time bin size
  - extraction from spiking, firing rates, LFP
  
- Limitations of **network simulation**
  - small number of nodes
  - simple neuron dynamics 
  - didn't focus on intricate connectivity that has been observed 
    - future work - apply to more complex Brian2 network models
  - assumed measurement from entire network
  - homogeneity in network parameters
  - understanding mediating effect of spike counts

- **Recommendations for designing network discovery experiments**
  - At the experiment-design phase, analyze competing hypotheses
    - through the lens of CLINC reachability / IDSNR 
    - evaluate what can be distinguished under different interventions 
  
  - A spectrum of interventions - pick the right tool for the job
    - stronger interventions generally come with cost 
      - increased experiment complexity 
    - depending on challenges, similarity of hypothesized circuits...
      - passive observation may be enough
      - or stronger interventions may be required 
  
- Future work
  - tighter integration of knowledge of intervention into network estimation procedure 
    - stimulus-conditional transfer entropy 
---
# Supplement 
- organization of clinc-gen, clinc-analysis codebases