
# Severing inputs, interrupting indirect connections
<img src="/figures/misc_figure_sketches/circuit_walkthrough_2circuits_key_sketch.png" width=500>

3-circuit version:
<img src="/code/network_analysis/results/circuit_walkthrough_3circuits.png" width=500>
# Severing inputs, rejecting confounds
<img src="/figures/misc_figure_sketches/closed_loop_severs_inputs.png" width=500>
<br>
<img src="/sketches_and_notation/discussion/CL_unobserved_confounds.png" width=500>
### Passive
with latent confounds everything looks connected,
estimated weights will mix confound and circuit-related effects. 
Critically, correlations will suggest a connection even if no causal link exists. A←H→B

### Open-loop (at node A)
with **open-loop intervention**, if you observe an *increase* in corr(A,B) you have evidence A drives B ... but this conclusion must be made quantitatively and strong confounds will still lead to false positives.
The strength of the inferred connection will tend to be an *over*estimate
\[
\hat{w}_{A→B} \propto f(w_{A→B},\,w_{H→A}w_{H→B},\,w_{B→A}) \geq w_{A→B}
\]

### Closed-loop (at node A)
with **closed-loop intervention**, again, an increase in corr(A,B) provides evidence A drives B. Importantly, the common input confounding influence of H is eliminated (or greatly diminished).
As a result of closed-loop control severing the inputs to A, the estimated connection strength is no longer inflated y the hidden confound, or the presence of recurrent connections. (The influence of H→B will tend to decrease the inferred connection strength, potentially leading to an *under*estimate of $w_{A→B}$
  
\[
\hat{w}_{A→B} \propto \frac{f(w_{A→B})}{g(w_{H→B})} \leq w_{A→B}
\]


# Breaking loops

<img src="/sketches_and_notation/discussion/CL_in_loops.png" width=500>

Consider a circuit of nodes connected in a large loop. With fast interactions, the direction of that loop would be difficult to tell from passive observation or even open-loop experiments (because all nodes would be correlated with each other).

We have some prior intuition that one of the benefits of closed-loop intervention is that in severing inputs, it can "break" loops. One way of thinking about that effect is that it turns looped circuits into chains, whose directionality can be easily identified with open-loop stimulation.

### Closed-loop (at A)
Closed-loop intervention severs the part of the loop connected into A (either node B or node F depending on the ground truth circuit). With this intervention alone, because of the indirect correlations present in a chain circuit, all nodes are still correlated with each other. This closed-loop intervention by itself is insufficient to distinguish the direction of the loop, However, by modifying the adjacency to no longer include recurrent, looped influences the stage is set for other interventions to help.

### Closed-loop at A with open-loop at B

Given the change in adjacency afforded by closed-loop control at node A, open-loop intervention at B is now sufficient to determine the direction of the original loop. If correlations between node B and nodes C-F increase, those connections are "downstream" of node B, providing evidence for the "clockwise" hypothesis. Whereas if open-loop intervention at B results in decreases correlations between B and other nodes, node B has been shown to be "downstream" of the others, providing evidence for the "counterclockwise hypothessis. Notably, open-loop control at B *without* simultaneously severing inputs through closed-loop control would result in increases all-to-all correlations regardless of the direction of the loop.

In summary, even though single-site closed-loop control is insufficient to distinguish these particular hypotheses, it is a necessary precursor to simplify the circuit for further interventions.


<!-- # Specific, more concrete case study -->



