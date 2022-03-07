see also exemplars.md

### Prior work

- Causal / Network ID
  - [^ila] Ila Fiete
  - Kording, Fakhar - lesioning ANNs for causality
  - Advancing FC
  - Lutcke 2013 - Inference of neuronal network spike dynamics and topology from calcium imaging data

  
- CL 
  - reference Grosenick
    > Closing the loop optogenetically (i.e., basing optogenetic stimulation on simultaneously observed dynamics in a principled way) is a powerful strategy for causal investigation of neural circuitry. In particular, observing and feeding back the effects of circuit interventions on physiologically relevant timescales is valuable for directly testing whether inferred models of dynamics, connectivity, and causation are accurate in vivo.
    
    - points to several examples of closed-loop for understanding causal role of related variables
    
    - value of closed-loop over open-loop 
    > Although it is possible to separately image native dynamics and then try to evoke a similar response in open loop fashion by designing light stimuli before the experiment, such an approach is highly sensitive to model misspecification, calibration, and state changes in the system (habituation, plasticity, motor state, etc.), and without simultaneous measurement it cannot be confirmed that the response was accurately evoked. Closed-loop feedback control now allows real-time adjustment of input parameters to keep the observed output as close as possible to a target level or time-varying trajectory (Figure 4E).[^grosenick]
    
    - highlights the major barrier to adoption is not technology but a cultural gap between biologists and engineers
    > to the best of our knowledge only a few papers have utilized feedback control in this way (e.g., Sohal et al., 2009; Paz et al., 2013; O’Connor et al., 2013; Krook-Magnuson et al., 2014, 2015; Siegle and Wilson, 2014; Stark et al., 2014). 
    > This is unlikely to be due to the technical and experimental challenges involved in undertaking such investigations, since neurobiologists are accustomed to the design and implementation of experiments characterized by computational and technical complexity.
    > There may be, however, a cultural gap between biologists and engineers regarding available tools, techniques, and motivation for closed-loop optical control and related technologies in systems engineering. Here we seek to address the latter challenge by helping to unite the relevant literatures

    - points to "where to stimulate matters"
    >  Basic sequential experimental designs are already in use in neuroscience; for example, in vitro studies of mammalian microcircuits have used imaging in hippocampal brain slices to screen for rare, highly connected “hub” neurons that appear to be important for engaging the larger network in oscillations (Bonifazi et al., 2009)
    
    - sequential experimental design to reduce circuit uncertainty 
      - see figure 5, Lewi et al.
      

  - reference CL sys ID Shanechi
  - control *theory* (notion of network controllability) has been used to understand (??)
    - Bassett

[^grosenick-bridge]: "This is unlikely to be due to the technical and experimental challenges involved in undertaking such investigations, since neurobiologists are accustomed to the design and implementation of experiments characterized by computational and technical complexity. --- There may be, however, a cultural gap between biologists and engineers regarding available tools, techniques, and motivation for closed-loop optical control and related technologies in systems engineering. Here we seek to address the latter challenge by helping to unite the relevant literatures"

