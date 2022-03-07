# alternatives
- alt. methods for quantifying dependence 
- alt. control policies  
  - here we focus on model-free control
  - multi-target control may require model-based control
- discuss arguments *against* closed-loop control 
  - requires specialized hardware + software 
  - more complex dependencies between experiment design, outcomes of experiment
- relationship between this approach and "network controllability" view  
- graph-search approach v.s. reachability matrix
  - reachability matrix approach provides concise summary for small, dense networks
  - but graph-search may be more (space, memory) efficient for large, sparse networks
  - the end result calculations should be equivalent
---
# limitations / untested assumptions
## nonlinear outputs
  - non-negativity means total variance can't be linear as a function of inputs 
    - moreover, this nonlinearity affects each junction between nodes, meaning **nonlinearity can't just be considered at the final output node**
      - a description of the full nonlinear path of influence is likely required 
        - could be accomplished with a graph search / "path tracing" approach 
        - the result would be a nonlinear function of inputs $S$ and network parameters $\Theta$
          - this function would also depend on external disturbances in a more complicated way
    - nodes being inhibited to 0 activity have 0 variance
      - sort of like a "half closed-loop intervention"
        - in that inhibitory inputs won't be propagated downstream, effectively severing inputs 
        - but sufficiently excitatory inputs might push the system back above the 0 activity threshold 
      
    - Poisson spiking means mean and variance are now coupled 
      - 0 activity = 0 variance can be seen as a natural consequence of this

  - higher order neuron dynamics - more biophysically rich neuron models
## other limitations
- ⚠️ mostly considered the "contemporaneous" case where the timescale of interaction is less than or equal to the sampling period
  - time lags can, potentially provide more distinguishability than estimatated here
- heterogeneous neuronal dynamics / weights / parameters
- only considered "direct current" injection 
  - opsin dynamics, actuator limits not considered
  - highly spatially-correlated actuation not considered[^spatial]
- we assume full observation - partial observation not considered
  - particularly unobserved common inputs
- impact of time-bin size[^bin_size]
- only looked at small networks
  - small, in terms of # populations
- *mostly focused on excitatory synapse weights*
- haven't considered state-dependent or nonstationary networks 
  - e.g. synaptic plasticity

- *(see also [technical_questions.md](sketches_and_notation/planning_big_picture/technical_questions.md) )*

[^bin_size]: see Assessing the significance, and "The influence of filtering and downsampling on the estimation of transfer entropy", also **Figure 6. Short bin widths generally improve performance** from "Extending Transfer Entropy Improves...", also also "bin size" tag on Zotero

[^spatial]: see Pairwise Optogenetic Stimulation by Kording & Lepperod
--- 
# future work
- **sequential experimental design**
  - intervene at one location, measure dependence 
  - use updated model to pick next location to intervene
- multi-site control, combining inference across multiple experiments
- measuring dependence from higher-order signal features 
  - e.g. frequency domain

---

# blue sky future work
- multi-objective control
  - controlling variance while leaving mean intact
- virtual-connection control
  - by recording one region and stimulating elsewhere, closed-loop control could induce a conditional relationship
  - is this useful for circuit id?
