Word count:

<!-- @ import "OUTLINE_high_level_april6.md" -->

<hr>
# Hopper 
- [ ] make it clear what nodes represent
  - in introduction ( and again in methods ) 
  > [^node_repr]: nodes in such a graphical model may represent populations of neurons, distinct cell-types, different regions within the brain, or components of a latent variable represented in the brain.
  
  - referenced in results_impact_of_intervention
  
- [ ] background - representations & reachability, but light on methods?
  - into /section_content/background_representation_reachability.md
  - from @ import "/section_content/methods_representation_reachability.md"
  - from @ import "/section_content/background_id_demo.md"

- [~] detailed steps of inference to methods 
  - overview version in early-results
  
- ( ) NOTE: don't have to get all the way through all the methods before hitting rest of results 
  - under this results-first model, can postpone details  til later

# Writing 
## Easy tasks 
- [ ] fill out any caption
## Soft results (background, methods)
- [~] decide where first few figures go 
  - start with DEMO and generalize through OVERVIEW 
  - or start with OVERVIEW then apply it in a demo 
  
  - DEMO figure similar to `systematic errors`
  - pipeline figure similar to `could a neuro`,`advancing FC`
  
- [~] sketch, pull in raw material 
  - ( ) from outline 
  - ( ) from figure DEMO ?
    - does figure DEMO require steps of inference first? 
    - should steps of inference be very early in results?
    - *is* a good result! 
    
- (~) section name `followup`
    - use overview figure as guide?
    - something about the circuit? 
    - could go without a name for the first chunk 
    - exemplar style might be to name the section as tackling a simple circuit 
    - could be named after themes
      - i.e. Narrowing the space of hypotheses 
    
- [~] compare to examples 

- [ ] just write 
  - [ ] overview - challenges `followup`
    - only a paragraph or so 
  - [ ] network section - should should be abbreviated intro to methods 
  - [~] steps of inference 
  
## Hard results (results)
- [x] just write 
- [~] edit

## Figures
- [~] every caption needs filling out 
  - [~] then pull some caption into body 

## Intro / abstract
<!-- Intro TODO: https://beta.workflowy.com/#/c310f6ea7ec9 -->

- [ ] Maybe more forecasting idea of shaping correlations? (don't want reader to be surprised by structure of paper's argument)

- [ ] Describe what 'reachability' is (we're interested in net directional impact of one node on another, which includes both effects from direct and indirect connections)

`from: "/section_content/background_causal_network_id.md"`  
- [ ] 3/16: - "We first propose..." paragraph (could build out or move or change focus away from the 'framework') 

- [ ] (in background-interventions) get language more precise and effective about value of intervention
  - ([Adam:] revisit related work, try to distill down our core argument about why intervention > passive observation)
  - **(Matt-done)** Reframe $x \to y$ vs $x \leftarrow y$ argument to focus on distinguishing between members of a hypotheses set (hypothesis first, data second)
  - Add example demonstrating why location of stimulation matters to "The inferential power of interventions..." paragraphs
  - **(Matt-done)** editing pass on last paragraph, qualify last paragraph (lean toward 'we are starting simple, blazing a trail for future research')



- [x] pull from `th`
- [~] 3/16 - Mention basic science applications of CL control 

`from: "/section_content/background_causal_network_id.md"`  
- [~] think about condensing and/or moving "Inferring causal interactions from time series" subsection 

## Discussion 
- [ ] pull from `th`
- [ ] - Maybe add half a paragraph or so in the discussion about how causal inference tools can help above correlation analysis (e.g., PC algorithm)


# Organization / structure / flow

- [~] split sim methods elsewhere
    - [ ] pull all into theory / methods overview section
    - [ ] 4.1.2 - time-resolvable goes in discussion?
    - [ ] 4.3 - merge "estimating circuits" into inference pipeline steps
    - [ ] 4.4 - info theoretic measures could simply be combined with results section

- [ ] Tentatively, bump 2.3 into theory section

<details><summary>↪see also</summary>

![](/planning/__local/clinc_org_whiteboard_20220316.jpg)

</details>

- [.] ? proposed methods order - could be overwritten by order suggested by "steps of intervention"
  - *simple linear Gaussian case*
  - Interventions - 2.2 → to end of introduction 
  - reachability - 2.3→ new 3.1 
  - predicting corr  - 3.1→ new 3.2 
  - inferring cause from time series  - 2.1B→ new 3.3 
    - minimize granger, IDTxl
    
- [.] ? from methods1_prediction_correlation: Some redundancy with simulation methods; 
  - cut and paste anything useful in 4.2 and put into 3.1 / 3.2

- [ ] where does methods pipeline figure go?

- [ ] integrate steps_of_inference.md as overview at the end of intro
  - [ ] also use steps as sections of methods overview
  - [ ] merge more detailed content into sections of methods overview
  - [ ] ? create hypotheses-set-focused methods overview figure ?
    - current figure really focuses on the fate of one circuit at a time

- [ ] Either need to write a "results summary" section or smooth transition from quantitative results to discussion

- [ ] consider variance control *before* categorical impact? - `[ORG]`

- Simulation methods section sketch 
  - Network simulations (simulation)
  - Implementing interventions (simulation)
  - Extracting circuit estimates (empirical)

**Impact of intervention location and variance on pairwise correlations**
  - again, feels very backgroundy / discussiony ... where to put this?


<hr>





# Mechanical
- [ ] deemphasize / soften language around "tools for causality"
  - really bringing in ideas from causality, but not using formal tools

- [ ] 🔧 flip matrix convention
  - use dynamical system throughout
    - live with $W_{j→i} = W[i,j]$

- [ ] 🔧 Rewrite X=XW+E as vector version (and resolve contemporaneous setting in methods>simulation section)

- [ ] (in background) Talk about what 'reachability' means (total direct+indirect impact)


# Technical 
- [ ] ? push for a last results section

----
# Archive

<details><summary>↪see more tasks</summary>



## Mostly complete
- [~] cut entropy to it's own chapter, then sink to methods 
- [~] split results_impact_of_intervention.md
  - [~] pull variance notes out of Stronger Intervention shapes
  

- [~] re-arrange sections 
  - [x] scan as-is 
    - minimally filtered two-column pdf
  - [x] verify flow against examples
    - see /planning/__local/exemplar_section_structures.md
    
  - [~] make prior arrangement changes (to outline)
    - see writing tasks 
    - discussion to set order of certain subsections
    - [x] new outline?  
    
  - [x] make intro-results changes (to outline)
  - [~] compartmentalize sections so they can be moved flexibly 
    - [ ] impact of intervention section needs splitting in two
    
  - [~] move sections to new outline
    - `outline to imports script?`
    - [~] new sections as needed from outline

- [~] pandoc filter to remove to-do list items?

- [~] update causal notation for open-loop inputs? 
  - how would you write x = x + u_OL ? - see [causal_vs_expt.md](sketches_and_notation/intro-background/causal_vs_expt.md)

- [x] reading through [10 simple rules for structuring papers](https://www.biorxiv.org/content/10.1101/088278v5.full.pdf+html)<details><summary>↪
<details><summary>↪ details
</summary>  

  - [x] transcribe followup tasks
    - [ ] what's the one idea we're communicating
    - [ ] check context-content-conclusion structure
    - [ ] diagram out threads of logic → should be as serial as possible
      - avoid "why was i told that?" (missing context) and "so what?" (missing conclusion)
        - ask yourself these questions to emulate a naive reader

      - in intro, check for
        - Ans: why does the paper matter?
        - connection to big problem in science
        - statement of what the field knows
        - refinement to narrow paper gap
        - summary of our approach, our results
          - shouldn't restate context
          - shouldn't preview conclusion (much)
      - in results check for
        - METHODS SUMMARY (high-level): FIRST, what question are we trying to answer
          - then OVERVIEW of methods (pipeline summary)
          - basic components
          - answer we're looking for
          - overall approach
          - key innovative methods
          - assume readers aren't going to pore over the details

        - RESULTS:
          - [ ] what are the sequence of statements we're trying to prove? → turn these into headers
            - support these steps with figures
            - connect these steps to final conclusion
          - [ ] verify paragraphs start with "to verify that..." "we tested whether..."
          - [ ] verify paragraphs end with answer to question
          - [ ] verify each title states a conclusion
          - [ ] verify each legend tells how the trick was done
          - ( ) use my highlight color-code to check for context-content-conclusion?

          - need to show
          - how? by doing x
          - thus we know
          - FLOW
            - raw data
            - processed data
            - metrics
            - final summary statistics


</details>

# Low priority
## writing tasks

- [ ] write methods overview 1k words
  - find a good example of this
  
- [ ] write methods sections

---
- [.] quarantine speculative methods
  - "currently in scope"
  - "would like this to be in scope but isn't currently"
  - "definitely future work"

- [ ] poll CotN about circuit ambiguity, entropy
- [ ] pandoc [crossref](https://github.com/lierdakil/pandoc-crossref) for equations, figures
- [ ] better metadata integration *see "front matter"*
----

## code tasks
- [ ] demo python notebooks for improved documentation, usability

## intro / methods tasks

 - [ ] add more closed-loop references to intro[^ctrl_sys_id]
 - [ ] Describe the methods for identifying circuits[^FC_measures][^connect_infer]
  - xcorr procedure
  - IDTxl recap
    - cover multivariate transfer entropy
 - evaluate dimensions of parameter sweeps[^FC_measures]
 - sketch a short review of closed-loop in neuro
  - Grosenick/Deisseroth, Kording

 - [~] write up "tutorial" + latex for different ways of representing a circuit

 [^FC_measures]: "A systematic framework for functional connectivity measures" includes a broad comparison of performance of Granger causality vs transfer entropy vs other methods. also discusses role of weights, noise
 [^connect_infer]: "Connectivity inference from neural recording data: Challenges, mathematical bases and research directions"
 [^ctrl_sys_id]: "A control-theoretic system identification framework and a real-time closed-loop clinical simulation testbed for electrical brain stimulation"

## theory
- [x] write python to compute via reachability
- [x] write input → connection notation
- [~] evaluate python on simple circuit
  - see [code/network_analysis/simple_gaussian_SNR.py](code/network_analysis/simple_gaussian_SNR.py)  

- [~] 🎁 relate noise → connection SNR to sensitivity transfer function
  - see [Astrom feedback fundamentals](https://www.cds.caltech.edu/~murray/courses/cds101/fa02/caltech/astrom-ch5.pdf)
- [?] copy over notation from 2020 brainstorming [overleaf link](https://www.overleaf.com/project/5e8232cd6157d200014b52d4)
  - rules for identifiability
- [ ] 🎁 discuss the role of prior anatomical knowledge in reducing search space



## formatting tasks
- [ ] read the Guide to Authors for our target journal
- add figure references to table of contents  

## organization tasks
- move exemplars to sketches/intro-background ?


-----

<details><summary>↪Archived:
</summary>

## planning tasks
- evaluate scope, potentially combine / cut figures
- how much should this be a perspective / review / prospectus
  - v.s. focusing on new empirical research results
- decide flow between
  - params (weight, delay)
  - intervention
- possible journals
  - connect with Lepperod/Kording?
  - perspectives
    - Nature Neuro
  - technical
    - Neuron
    - PLOS Comp Bio
    - JNE
- **remaining scope**
  - probably
    - linear theory (IDSNR)
    - impact of OL ctrl on IDSNR
    - spiking results
    - open-loop design
  - maybe
    - optimizing closed-loop policy via IDSNR
      - can we do design of experiments without brute-force search of all control locations?
  - probably not
    - predicting nonlinear case

</details>

<!-- end of see-more-tasks -->
</details>
