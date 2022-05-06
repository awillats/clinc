# Purpose / scope

🚧

----
# Organization
*see [README.md](/README.md) for more, high-level overview*

most analysis files with many functions will also have an 
```python 
if __name__ == "__main__":
  use_functions()
```
section at the bottom which executes if you call the file as a script (but not if you simply import it). This section is intended as a soft test of basic functionality, but also a demonstration of how to use functions.


most commonly the following functions are imported with aliases like so:
```python
#external libraries
import numpy as np
import networkx as nx
import pandas as pd

#data
import network_data_functions as net_data
import example_circuits as egcirc
#sim
import sim_simple_network_functions as sim
#analysis
import network_analysis_functions as net
import network_plotting_functions as netplot
import coreachability_source_classification as cor
#plotting
import matplotlib.pyplot as plt
import plotting_functions as myplot
```

## network_analysis/

- `simulation_functions/`  :star:
  <!-- - <details><summary>sim_simple_network_functions.py</summary> -->
  -sim_simple_network_functions
    - takes a circuit specification and generates output data
      - generates various forms of random noise
      - uses several ways of "realizing" network dynamics 
        - `sim_contemporaneous`
        $$X^-:=E+Bu  \\X := X^-\bar{W} + X^- = X^-\widetilde{W}$$
          - matrix computation (faster)
          - for-loop computation (more flexible)
        - `sim_dynamic`
        $$X_{t+1} := X_t W + E + Bu$$
  
</details>

- `analysis_functions/` :star:
  - <details><summary>network_analysis_functions.py</summary>
  
    - sever_inputs()
    - reachability_weight()
    - reachability() [binary]
    - closed_loop_reachability()
    - correlation_matrix_from_reachability()
      - correlation_from_reachability()
    </details>

  - network_pattern_entropy.py
    - quantifying how diverse a set of observed correlation patterns are across hypotheses (using Shannon entropy)
  - coreachability_source_classification.py
    - predicting whether a source at a particular location increases or decreases correlation at certain edges

- `circuit_data/`
  - network_data_functions.py - misc. utilities
    - `mermaid_str_to_networkx()` - parses a mermaid-js syntax string to a networkx Graph object
      <details><summary>demo</summary>  
      
      ![](code/network_analysis/_demo_imgs/mermaid_parser_demo.png) </details>
    - `nx_to_np_adj()` - extracts numpy adjacency from networkx Graph
  - example_circuits.py - functions for generating sets of circuit hypotheses
  - `motif_data/` - circuit motifs transcribed from other papers

  
- `scripts/` :star:
  - simple_gaussian_SNR.py
  - sweep_gaussian_SNR.py
    <details><summary>demo</summary>  
    
    ![](/figures/from_code/bidirectional_correlation.png) </details>
  - plot_hypotheses_x_interventions.py
  - **fig_circuit_walkthrough.py, fig_3circuit_walkthrough.py**
  
- `plotting_functions/`
    - network_plotting_functions.py
    
- `prototyping/`
    - gradient_of_r2_demo.py - $\nabla_S \,{r^2}$
      <details><summary>demo</summary>  
      
      ![](code/network_analysis/_demo_imgs/correlation_reachability_gradient_results.png) </details>
      
  
  
- `results/` - output images and tables 
- `_demo_imgs/` - screenshots of progress
  
## MATLAB/
Some early prototype code for computing reachability and correlation was written in MATLAB ... 

## _plotting/
eventually plotting functions will get moved here ...

----
# Computing coreachability 
## Key functions 
```python 
df = coreach.compute_coreachability_tensor(net.reachability(adj))
#which calls
coreach.compute_coreachability_from_src(reach, idx)
```
# Plotting 
## Key functions 

- use `myplot.subplots()` as a wrapper to matplotlib's subplots, with better detault sizing for network plots s

```python 
netplot.draw_adj_reach_corr(A, ax)
netplot.draw_controlled_adj_correlations(ax, A)
# effect_of_control_horiz.png
netplot.draw_controlled_representations(ax, A)
# effect_of_control_grid

```
## Plotting interventions 


```python
plot_funs = {
      NetPlotType(0):         lambda adj,ax,intv_loc: adj*2,
      NetPlotType.ADJ:        lambda adj,ax,intv_loc: draw_np_adj(adj,ax=ax),
      NetPlotType.REACH:      lambda adj,ax,intv_loc: draw_reachability(adj,ax=ax),
      NetPlotType.CORR:       lambda adj,ax,intv_loc: draw_correlations(adj,ax=ax,grey_correlations=grey),
      NetPlotType.ADJ_CTRL:   lambda adj,ax,intv_loc: __draw_ctrl_adj_at_source(adj=adj,ax=ax,intv_loc=intv_loc),
      NetPlotType.CORR_CTRL:  lambda adj,ax,intv_loc: __draw_ctrl_correlations_at_source(adj=adj,ax=ax,intv_loc=intv_loc,grey_correlations=grey),
      # NetPlotType.REACH_CTRL :  lambda adj,ax,intv_loc: netplot.__draw_coreachability_at_source(adj,ax=ax,intv_loc=intv_loc),
      # NetPlotType.CTRL :  lambda adj,ax,intv_loc: netplot.__draw_coreachability_at_source(adj,ax=ax,intv_loc=intv_loc),
      NetPlotType.OPEN:       lambda adj,ax,intv_loc: __draw_coreachability_at_source(adj=adj,ax=ax,intv_loc=intv_loc,grey_correlations=grey),
  }
  ```
## Styling network plots 
🚧 ... 
