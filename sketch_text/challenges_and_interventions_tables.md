
### Challenges to identification

|                                         | examples                                                                                                       |
| ---------------------------------------:| -------------------------------------------------------------------------------------------------------------- |
|                   additive disturbances | voltage noise                                                                                                  |
|                         data efficiency | complex models require more data to be estimated well                                                          |
|                   limited observability | extracellular recordings currently sample from 10s of neurons simultaneously                                   |
|                       limited acutation | standard optogenetic stimulation has few spatial degrees of freedom, leading to highly correlated inputs [^LK] |
|                    unobserved confounds | hidden, common inputs to recorded areas may induce spurious correlations. especially neuromodulatory systems   |
| model mismatch / structural uncertainty | unmodelled nonlinearity, higher-order dynamics                                                                 |
|                        non-stationarity | synaptic plasticity                                                                                            |

### Types of interventions
|                | static                                               | time-varying                                          |
| --------------:| ---------------------------------------------------- | ----------------------------------------------------- |
|        passive | anesthetized recordings                              | awake recordings during behavior                      |
|      open-loop | step-response characterization                       | white-noise characterization, f-I curve sweeps        |
| trial-adaptive | active-learning, Bayesian experimental design        | trial-adaptive stimulus design                        |
|    closed-loop | voltage-clamp, condition-triggered stimulus delivery | closed-loop replay experiments, time-varying tracking |


[^LK]: [Lepperod Kording](https://www.biorxiv.org/content/10.1101/463760v2.full.pdf) Figure 2: Optogenetic stimulation induces spurious correlations.