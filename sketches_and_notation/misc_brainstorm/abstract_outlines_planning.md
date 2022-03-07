
## Abstract outline A
- why causal [structure-function]
  - why interventions help 
  - how closed-loop, causal help support this 
  - what are the core challenges 
    - confounds
    - fast reciprocal, highly coupled dynamics
- contribution
  - when and how interventions help
  - simulations as demonstration, basic quantitative understanding
  
- bigger goal (funnel out)
  - help design and interpret experiments
---
## Abstract outline B
- why causal? 
- **gap:** current approaches consider mostly passive and open-loop settings. [^kording_fakhar]
  - prior work shows recording more is sometimes insufficient![^ila]
  - subgap: those papers *that do* explore impact of *strong* interventions mostly focus on lesioning 
    - not always feasible
    - have side effects
- **solution:** closed-loop control can mitigate these drawbacks when applied to the right circuit in the right location 
  - *but* we need to understand the impact of closed-loop control to reap these rewards 
- **contribution:**
  - Provide a straightforward and practically useful conceptual framework for applying closed-loop to circuit identification problems
  - update causal inference theory to accomodate closed-loop interventions 
  - quantitative demonstration in spiking circuits
    - highlights specifics of choosing where to intervene to distinguish competing hypotheses
- **impact:** immediate guidance for design of experiments
  
[^ila]: Ila Fiete , Abhranil Das -Systematic errors in connectivity inferred from activity in strongly recurrent networks 
[^kording_kakhar]: esp. kording, fakhar. *see [exemplars](sketches_and_notation/planning_big_picture/exemplars.md)*
[^wolff]: wolff and olvecszy - promise and perils of causal manipulationss

## Abstract outline C - Statement of specific need - relationship to prior work
Theme of bringing 2 fields[^grosenick-bridge] (CL, CI) to neuroscience for goal of network identification
  - **network id** has always been a central goal - **causal** refines this to get to the heart of what we want 
    - integrating techniques from econ and causal theory to meet this challenge 
  - bring **closed-loop control** to neuroscience 
    - *( need to enumerate types of intervention ? )*
      - *( need to distinguish feedback from reactive control? )*
    - CL is a mature field, revolution in leveraging it for neuroscience
    - facilitated by optogenetics [grosenick]
    - recent success [our work]
    - *restate* value of closed-loop control for ID[^wolff]
      - severing connections in-situ 
      - shaping (co)variance
  - **high-level goal** combine intervention + causal theory for network id
    - theory of causal inference (+dynamical systems + graph theory) gives us the language to predict "what are the implications of intervention"
    - **results so far**
      - observation isn't enough[^ila]
      - kording - single-site lesions aren't enough[^kording_fakhar]
        - *have to be careful about this...we may propose single-site closed-loop control*
    - **remaining challenge** this integration is new, and HOW we intervene matters - need guidance on how to choose
      - **additional challenge** problem has several layers of complexity
        - closed-loop interventions are complex 
        - networks in brain are complex (recurrent, equivalent explanations, unobserved confounds)
    - **solution** - bring theory and simulation together to demonstrate & validate intersection between these approaches for identification with closed-loop control
      - specifically work towards framework for understanding 
    - **impact** - this leads to guidance for designing interventions to maximize identifiability 
        - given prior knowledge, system-specific details, experimental constraints, hypotheses


---
### Abstract decisions / brainstorming
- How much did other abstracts talk about key challenges?
- How much did other abstracts talk about expected results?

- what are our **expected results**?
  - one of the key outcomes of effective iterventions is to eliminate alternate explanations    
    - narrow the space of plausible hypotheses
    
  - one of the key ways closed-loop control efficiently cuts down that hypothesis space is through removing confounding / common input connections 
    - resulting in "less similar, more distinguishable" patterns of correlation
  - closed-loop feedback control is unique in its ability to both... 
    - reduce variance at certain locations
      - open-loop can't do this
    - while leaving other key properties intact
      - i.e. doesn't push into disrupted, non-physiologic activity levels 
      - downside of lesions, even acute reversible lesions
    - changes multi-variate dependence without moving into extreme operating regimes
  
- restate what's **unique** about this work
  - while the field is already thinking about...
    - applications of feedback control 
    - centrality of intervention in answering causal questions 
  - this is the first work to bring insight in *how to use* feedback control as an intervention for efficient network inference
    - efficient both in the sense of requiring less data...
    - but also in the sense of narrowing the search space more (?dramatically) with each experiment configuration
  
- "advancing FC" states the gap very clearly, early 
  > —are likely a good starting point for estimating brain network interactions. Yet only a subset of FC methods (‘effective connectivity’) is explicitly designed to infer causal interactions from statistical associations. Here we incorporate best practices from diverse areas of FC research to illustrate how FC methods can be refined to improve inferences about neural mechanisms ... 
  
  > We further demonstrate how the most common FC measures (correlation and coherence) reduce the set of likely causal models, facilitating causal inferences despite major limitations. 
  
  > Alternative FC measures are suggested to immediately start improving causal inferences beyond these common FC measures.

- start with "structure-function" v.s. start with "intervention is key to understanding causal roles"

- highlight our expected results
  - first we (cover theory)
  - then me demonstrate (sims)
  - (finding) - location matters, CL is best at severing edges which blur (patterns of correlation between) distinct hypotheses
    - "we show..."
    - to do that, apply CL at expected bridges / "ambiguating edges" of candidate hypotheses

- highlight value of closed-loop
  - severing connections in-situ 
  - shaping (co)variance
  - closed-loop could be used to induce virtual dependencies - i.e. "gain of function" experiments to test counterfactuals
    - not something we explore much

- how much to explain types of intervention
  - [^N2] necessary to define "interventions" or "open-loop"?
  - [^N3] is "lesioning" really an open-loop stimulation?
  - [^N5] will most readers be familiar with "closed-loop"? or should this be defined / a different phrase used?
  - [^grosenick] does a good job of distinguishing feedback CL from activity-guided

misc: 

- is optogenetics worth mentioning?
  - facilitates closed-loop control with unprecedented precision
  
- how to state our target audience 
  - systems neuroscientist?
  - experimental neuroscientists?

- how much to commit to a particular algorithmic approach 
  - xcorr vs muTE
  - try an xcorr-heavy description 


- how much "funneling out" is appropriate?
 - instead, could stick to concrete conclusion 
  > Alternative FC measures are suggested to immediately start improving causal inferences beyond these common FC measures.
---

