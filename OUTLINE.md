# Overview 
## Intended audience
  - systems neuroscientists interested in making more rigorous conclusions in circuit ID problems 
  - experimental neuroscientists looking for guidance on evaluating required intervention to answer circuit hypothesis questions
## Goal -  Provide a straightforward and practically useful conceptual framework for applying closed-loop to circuit identification problems
- What’s the value of closed-loop?
- What can i say about causal connections given the experiments i’m doing?
- How can we make experimental design decisions which improve the strength of our hypothesis testing?


# Table of Conents
- [Introduction](#introduction)
- [Methods](#methods)
- [Results](#results)
- [Discussion](#discussion)
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
- built on [Brian2](https://elifesciences.org/articles/47314) spiking neural network simulator 
- (delayed) linear-gaussian network 
  - required custom functionality to implement 
    - [[<img src="figures/external_imgs/GitHub-Mark-Light-32px.png" alt="drawing" style="width:15px;"/> brian_delayed_gaussian]](https://github.com/awillats/brian_delayed_gaussian)
- spiking network 
  - [...]

## Extracting circuit estimates 
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

## Case Study: Applying CLINC to distinguish a pair of circuits
  - explanation using binary reachability rules ?
🏞️ **Figure:** walk-through / case-study 🏞️
  - *(e.g. Advancing functional connectivity research from association to causation, Combining multiple functional connectivity methods to improve causal inferences)*

## [Binary Sim.] - Characterizing circuit-pair ambiguity through binary reachability properties
  - proportion of each ambiguity class as a function of circuit size
  - possibly weight proportions by observed frequency of triplet motifs
✂️️ **Figure:** ambiguity class by circuit size✂️

## ... Characterization ...
🏞️ **Figure:** simulation, evaluation pipeline figure here 🏞️

### Extracting circuit estimates 
- *(see methods for xcorr, muTE)*

### Quantifying successful identification
- binary "classification" metrics
  - accuracy
  - F1 score 
  - true/false positives, true/false negatives 
- graded metrics (*not a core focus here*)
  - distance between identified connection strength and ground-truth
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
- **impact of circuit structure**
  - degree of nodes 
    - in/out-degree 
    - of source - $i$
    - of target - $i$
  - presence of indirect correlations 
  - presence of feedback loops
  - \# of circuits in equivalence class 

- 🏞️ **Figure:** impact of intrinsic network properties on identifiability 
  - may include component xcorr plots 
    - *(e.g. Identification of excitatory-inhibitory links and network topology in large-scale neuronal assemblies from multi-electrode recordings)*
  - comparison to predicted IDSNR 
  
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
    
    - stimulus location 
      - single-site
      - multi-site
      - location relative to features of network
        - in-degree/out-degree
        - upstream/downstream of hypothesized connection 
    - stimulus intensity 
      - expected mean output rate 
      - frequency content 
      </details>

- 🏞️ **Figure:** Analysis of simulated circuits suggest stronger intervention facilitates identification with less data 🏞️
  - *(e.g Estimating Multiscale Direct Causality Graphs in Neural Spike-Field Networks)*
  - *metric:* \# of samples required to reach accuracy threshold
  - closed-loop > open-loop > passive 
  
- 🏞️ **Figure:** Stronger intervention facilitates disambiguating equivalent hypotheses 🏞️
  - in example: shows a dataset with many correlations, multiple plausible circuit hypotheses 
    - patterns of correlation become more specific with increasing intervention strength 
  - in aggregate: focuses on accuracy
  - closed-loop > open-loop > passive 

### Comparing predicted and emprical identification performance 

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

## Supplement 
- 
- organization of clinc-gen, clinc-analysis codebases