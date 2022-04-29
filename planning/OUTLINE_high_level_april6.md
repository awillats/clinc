# **April 6th outline / section numbers:**  
see `/publish/outputs/manuscript_v0_mpe.html`

# Abstract - 1.
# Introduction - 2.
## Estimating causal interactions in the brain - 2.1
## Interventions in neuroscience & causal inference - 2.2 
## Representations & reachability - 2.3

# Theory / Prediction - 3. 
## Predicting correlation structure (theory) - 3.1

# Simulation Methods - 4. 
## Modeling network structure and dynamics - 4.1 
### Stochastic network dynamics - 4.1.1
### Time-resolvable interactions - 4.1.2
### Code implementation - 4.1.3 
## Implementing interventions - 4.2
## Extracting circuit estimates - 4.3
## Information-theoretic measures of hypothesis ambiguity - 4.4 

# Results - 5.
## Impact of intervention on estimation performance - 5.1 
### Intervening provides (categorical) improvements in inference power beyond passive observation - 5.1.1
### Stronger intervention shapes correlation, resulting in more data-efficient inference with less bias - 5.1.2
#### Impact of intervention location and variance on pairwise correlations - 5.1.2.1

# Discussion - 6. 
## limitations
## results summary → summary of value closed-loop generally
## summary of guidelines for experimenters
## "funnel out", future work → broad impact

---

# **April 29th - merged**
# Introduction (2.)
## Estimating causal interactions in the brain (2.1)
## Interventions in neuroscience & causal inference (2.2)
## Representations & reachability (2.3, partial)

# Results 
## Overview - Challenges (+)
## Overview - Network (4.1?)
<!-- where does methods pipeline figure go? -->

## Steps of inference - *overview of CLINC approach* (+)
<!-- Inference pipeline  -->
## Predicting corr (3.1)
### Representations & reachability - 2.3
<!-- Predicting correlation structure -->
### Extracting circuit estimates (4.3)
### Impact of intervention on pairwise dependence (3.1?, 5.1?)

## Impact of intervention on estimation performance - 5.1 
### Intervening provides *(categorical)* improvements in inference power beyond passive observation (5.1.1)
### Stronger intervention shapes correlation, resulting in more data-efficient inference with less bias - *bidirectional var control* (5.1.2)
#### Impact of intervention location and variance on pairwise correlations (5.1.2.1)

# Discussion (6.0)
## limitations
## results summary → summary of value closed-loop generally
## summary of guidelines for experimenters
## "funnel out", future work → broad impact
# Methods 

## Predicting correlation structure (3.1)
### Representations & reachability (2.3?)
### Predicting correlation structure (3.1)
### Impact of interventions - theory, pred (3.1?, 5.1?)

## Modeling network structure and dynamics (4.1)
### Stochastic network dynamics (4.1.1)
### Delayed interactions (4.1.2)
### Code implementation (4.1.3)
## Implementing interventions (4.2)

## Extracting circuit estimates (4.3)
### Time-resolvable interactions *XCORR* (4.1.2)
### Information-theoretic measures of hypothesis ambiguity (4.4)
---

# **April 29th - from examples**
# Introduction 
## Estimating causal interactions in the brain
## Interventions in neuroscience & causal inference
## Representations & reachability

# Results 
## *Challenges* 

## Overview - network
<!-- where does methods pipeline figure go? -->
## Inference pipeline
<!-- ## Representations & reachability - 2.3 -->
### Predicting corr (3.1)
### Extracting circuit estimates - 4.3 

## Impact of intervention on pairwise dependence 
<!-- Predicting correlation structure -->

## *Steps of inference - overview of CLINC approach*

## Intervening provides *(categorical)* improvements in inference power beyond passive observation
## Stronger intervention shapes correlation, resulting in more data-efficient inference with less bias - *bidirectional var control*
### Impact of intervention location and variance on pairwise correlations

# Discussion 
## limitations
## results summary → summary of value closed-loop generally
## summary of guidelines for experimenters
## "funnel out", future work → broad impact
# Methods 

## Predicting correlation structure
### Representations & reachability
### Predicting correlation structure
### Impact of interventions 

## Stochastic network dynamics
### Modeling network structure and dynamics
### Stochastic network dynamics
### Delayed interactions 
### Code implementation
## Implementing interventions

## Extracting circuit estimates
### Time-resolvable interactions *XCORR*
### Information-theoretic measures of hypothesis ambiguity

<!-- ## Measuring inference error -->

---

# **April 29th - from draft**

`methods order - could be overwritten by order suggested by "steps of intervention"`
```
Each results section could be structured like 
- Idea 
- Approach 
- Example 
- Explanation / insight 
- (Quant)
- (Explanation)
```

# Abstract - 1.
# Introduction - 2.
## Estimating causal interactions in the brain - 2.1
## Interventions in neuroscience & causal inference - 2.2 
## Representations & reachability - 2.3 *minimal*

<!-- integrate steps_of_inference.md as overview at the end of intro -->
# Results - 5.
## Overview - network

<!-- where does methods pipeline figure go? -->
## Inference pipeline
<!-- ## Representations & reachability - 2.3 -->
### Predicting corr (3.1)
### Extracting circuit estimates - 4.3 
<!-- - inferring cause from time series -->

## Impact of intervention on estimation performance - 5.1 
### Intervening provides (categorical) improvements in inference power beyond passive observation - 5.1.1
#### Information-theoretic measures of hypothesis ambiguity - 4.4 
### Stronger intervention shapes correlation, resulting in more data-efficient inference with less bias - 5.1.2
#### Impact of intervention location and variance on pairwise correlations - 5.1.2.1

# Discussion - 6. 
## limitations
## results summary → summary of value closed-loop generally
## summary of guidelines for experimenters
## "funnel out", future work → broad impact

# Methods 
## Theory / Prediction - 3. 
### Representations & reachability - 2.3
### Predicting correlation structure (theory) - 3.1

## Simulation Methods - 4. 
### Modeling network structure and dynamics - 4.1 
#### Stochastic network dynamics - 4.1.1
#### Time-resolvable interactions - 4.1.2
#### Code implementation - 4.1.3 
### Implementing interventions - 4.2
### Information-theoretic measures of hypothesis ambiguity - 4.4 


