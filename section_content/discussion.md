<!-- NOTE: see also __conclusions_from_th.md -->

<!-- TODO:
- [ ] add half a paragraph or so in the discussion about how causal inference tools can help above correlation analysis (e.g., PC algorithm) 
  - see also /section_content/methods_circuit_estimates.md
  
-->

```
Restate themes!
- narrowing search space 
- where you intervene matters
```

### limitations
The examples explored in this work simplify several key features that may have relevant contributions to circuit identification in practical experiments. [...]

`spiking networks`

`full observability`

### results summary → summary of value closed-loop generally
Closed-loop control has the disadvantages of being more complex to implement and requires specialized real-time hardware and software, however it has been shown to have multifaceted usefulness in clinical and basic science applications. Here we focused on two advantages in particular; First, the capacity for functional lesioning which (reversibly) severs inputs to nodes and second, closed-loop control's capacity to precisely shape variance across nodes. Both of these advantages facilitate opportunities for closed-loop intervention to reveal more circuit structure than passive observation or even open-loop experiments.

### summary of guidelines for experimenters
In studying the utility of various intervention for circuit inference we arrived at a few general guidelines which may assist experimental neuroscientists in designing the right intervention for the quesiton at hand.
First, more ambiguous hypotheses sets require "stronger" interventions to distinguish. Open-loop intervention may be sufficient to determine directionality of functional relationships, but as larger numbers of similar hypotheses [...] closed-loop intervention reduces the hypothesis set more efficiently.
Second, we find that dense networks with strong reciprocal connections tend to result in many equivalent circuit hypotheses, but that well-placed closed-loop control can disrupt loops and simplify correlation structure to be more identifiable.[^corrob_fiete] Recurrent loops are a common feature of neural circuit, and represent key opportunities for successful closed-loop intervention. The same is true for circuits with strong indirect correlations 

`hidden confounds`

### "funnel out", future work → broad impact

`sequential experimental design`

*see [limitations_future_work.md](/sketches_and_notation/discussion/limitations_future_work.md)*

[^corrob_fiete]: this corroborates Ila Fiete's paper on bias as a function of recurrent network strength


<!-- 
NOTE: additional sections worth considering adding here 
/sketches_and_notation/discussion/limitations_future_work.md
/sketches_and_notation/discussion/value_of_cl_case_studies.md
/sketches_and_notation/discussion/value_of_closed_loop_notes.md
/sketches_and_notation/identifiability/variance_notes.md (firing rate section)
-->

