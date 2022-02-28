# Top 3 highest priority writing / planning tasks:

## Monday Feb 28th
- [.] scaffold methods, results - @adam 
  - **planning**
    - for now, set aside unresolved technical details 
    - topic sentences for each paragraph
    - how many figures?
  - [.] review outline, check which outline is most up-to-date
    - [~] outline.md
    - [~] workflowy 
      - [text outline](https://beta.workflowy.com/#/232d9f5210ee)
        - includes some takeaway points
      - [figure plan board](https://beta.workflowy.com/#/60a88f9b8aaa)
  
  - [~]🧿 map chapter files if needed
  - [ ]🧿 write topic sentences into outline, then manuscript
  <!-- - [ ] write results forecasts  -->
  - *switch to figures*
  - [ ] describe figures 
  
- [ ] Resketch figures - @adam
  - **planning**
    - make sure they're aligned towards a core takeaway 
    - make them concrete
      - if there's a lot of missing content, hide the figure sketch
    - write the takeaway via caption 
  - [~] review outline 
  - [x] rescan demos folder, slides for new material 
    - [x] rescanned figures folder 
    - [x] created figures/figure_requests.md
    - [x] scan whiteboard archive
    - [x] scan demos 
    - [x] scan slides
  <!-- - [ ] point to where source files (svg / g-drawing) -->
  
- [ ] gather info from citations for intro - @matt 
- [ ] automatic writing session - results - @matt, @adam
  - evaluate alignment with core takeaways
  - (look at teletype?)
  
- [ ] automatic writing session - methods - @matt, @adam

----

# Technical loose-ends 
- [ ] predicting time-lagged correlation 
- [ ] quantitative match between gaussian sims & theory
- [ ] summarizing relationship between intervention utility and circuit properties 

--- 
see also [technical_tasks.md](sketches_and_notation/technical_tasks.md) and [low_priority_tasks.md](sketches_and_notation/low_priority_tasks.md)


---
Add this to reachability section
I used a simple derived quantity of the circuit’s adjacency matrix: its reachability (Skiena 2011). This quantity measures which nodes can be “reached” by direct and indirect connections starting from a target node. Moreover, this measure allows us to predict which node’s signals will be correlated. If the reachability of two circuits are equal, they will have similar correlational structure and be difficult to distinguish with that level of intervention. For instance looking at hypotheses for cortical gain control in open-loop (Figure 12, left column), in both circuit 2a and 2b, PV cells are reachable from the Som cell node since Som activity can influence PV activity indirectly through the Pyr node. As such these circuits cannot be distinguished in open loop.

If the reachability of two circuits are unequal for a given intervention, differences in correlation between observed regions will be sufficient to distinguish between the two hypotheses. Looking at these same circuits under closed-loop control of the pyramidal population (Figure 12, right column), dashed lines reveal that there is no longer an indirect functional connection from Som to PV cells. As such, in circuit 2a, PV cells are no longer reachable from the Som population, whereas they are reachable under circuit 2b. This difference in reachability corresponds to the difference in correlational structure that allows us to distinguish these two hypotheses under closed-loop control.