
---

# Current tasks
*see also [technical_tasks](/sketches_and_notation/planning_big_picture/technical_tasks.md)*

##Entropy
working towards automating:
![](/figures/misc_figure_sketches/circuit_intervention_entropy_mockup.png)



pipeline
```mermaid
graph TD
a[adj]-->|w/ctrl?|c
c(comp. coreach)-->|coreach df|T(mats to string-fingerprint-token)

aggr-->|token freq dict|d-->E[entropy of tokens]
d(distro)-->dp[distro plot]
```

---
```mermaid
graph TD
S[S_k].->|S^/Sv/S=/Sx|ab
subgraph corr
  A(A_i)---ab( )
  ab-->B(B_j)
  end
```

stages:
- adj 
  - ( modified by severing )
- df of coreach tensor: iA	jB	kS src→corr
  ```python
  df = compute_coreachability_tensor(net.reachability(adj))
  ```
  - e.g. demo_fingerprint.csv
  - redundant directionality removed hear on creation so we don't have to think about it at token stage?
  - self-correlation seems to be left in for some reason
    - remove this! so fingerprint will only have 3 ordered subtokens
  - for registering dfs across hypo, maybe it makes sense to have a compact, unique adj ID
- df to compact fingerprint strings:
  - `extract_circuit_signature_single_df()`
- token frequency 
  ```python
  tf = count_unique_frequency(data, do_normalize=True)
  ```
- entropy of tokens 
  ```python
  H = entropy_of_dict(tf, entr_base)
  H_max = max_entropy_of_dict(tf, entr_base)
  ```


### warmup 
- [~] find entropy files
  - `network_pattern_entropy.py`
    - if name main 
  - relies on `coreachability_source_classification.py` 
    - to compute coreach tensor
    - `partition_sources_ab()` is core function
    
  - plot_hypotheses_x_interventions.py
    - handles plotting infrastructure, layout for left side 
    - but doesn't actually compute anything entropy-related
    
- [ ] 🧿 carve out script
- [ ] :dart: needs infrastructure for storing info associated with each hypothesis
  - but which is also accessible across hypotheses 
  - big table?
    - nested df?
    - or just matrix?
       

### Computing infrastructure 
- extract fingerprint string 
  - for OL 
  - for CL :star:
  
### Plotting 
- [~] plot matrix, w/ circuits as columns 
  - [x] labels off to left side then
  - [x] OL effect on CL correlations
- [~] turns correlations grey?

- [ ] plot building block distro
  - use plotly?
  - [ ] mini graphs on x-axis 
- [ ] write / plot H to the side 
  - profile of H/H_max
  
### Layout 
- way too much going on at once ... 
  - may end up needing to subselect intervention locations 
  
### cleanup 
- fig_hypothesis_entropy.py
  - link image and source file
- review 3b1b

--- 
- 🎯 [x] verify quantitative match
  - doesn't work for partially effective control, otherwise works well
- [ ] additional sweeps for impact on variance:
  - [ ] 🧵 sweep common input
  - [ ] 🧵 sweep w com→B

- [~] get sweep infrastructure
- [ ] misc infrastructure
  - [ ] add functionality for multiple control locations
    - [ ] unify specification of ctrl location, B
    - [ ] save more complete results
  - [ ] improve plot, take whole prediction dictionary as input, plot prediction error
  - [ ] extract data functions to utilities file
- [x] add closed-loop control in `sim_contemporaneous`
  - [~] add partial incomplete control parameter
    - 🧵 quantitative prediction w.r.t control effectiveness
    - 🧵 verify whether this (for-loop) contemp. implementation is sensible 
    - 🧵 gen_gauss used in target needs to be reproducible!
      - not across script runs, but within a script run, needs to use the same target in case ctrl_fn is called multiple times
    - [~] clean up $\bar{W}$ implementation
  - [~] simply blends target and un-controlled variance
    - 🧵 external notions of control effectivness 
    - 🧵 external implementations of control in DGs
  - [ ] 🎁 implementation writeup?
- [ ] 🎁 extend implementations to discrete time dynamics
---
## Organization tasks 
- [ ] continue filling out [CODE_OVERVIEW](CODE_OVERVIEW.md)

## miscellaneous
- [ ] transcribe the following as an operation $$\bar{W} = \sum_{i=1}^{n}W^i \\\,\\ X = X^- \bar{W}$$
  
## observations
- high amplitude open loop control is like high-amplitude closed-loop control