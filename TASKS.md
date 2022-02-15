# Top 3 highest priority writing / planning tasks:
- [ ] checking definitions for r2, R2, SNR
- [ ] looking for refs to predict side-band xcorr magnitude
- [ ] linear algebra for computing $I^{+AB}$
  - python verification
- [ ] sketch core figures 

# planning tasks 
- evaluate scope, potentially combine / cut figures
- how much should this be a perspective / review / prospectus 
  - v.s. focusing on new empirical research results
- decide flow between 
  - params (weight, delay)
  - intervention 
- possible journals 
  - [ ] Chris in discussion with editors
  - perspectives 
    - Nature Neuro
  - technical
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

# intro / methods tasks
 - [ ] add more closed-loop references to intro[^ctrl_sys_id]
 - Describe the methods for identifying circuits[^FC_measures][^connect_infer]
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

# theory 
- [ ] write input → connection notation 
  - [ ] basic text form
  - [ ] computing via reachability 
  - [ ] computing via masked noise propagating
  - [ ] update notation to function on "common cause" circuits
- [ ] write python to compute via reachability 
- [~] evaluate python on simple circuit
  - see [code/network_analysis/simple_gaussian_SNR.py](code/network_analysis/simple_gaussian_SNR.py)
  - [ ] conduct a small sweep to verify whether sources add or multiply
  
- [ ] evaluate python on two-path circuit


- [ ] relate noise → connection SNR to sensitivity transfer function 
  - see [Astrom feedback fundamentals](https://www.cds.caltech.edu/~murray/courses/cds101/fa02/caltech/astrom-ch5.pdf)
- [ ] copy over notation from 2020 brainstorming [overleaf link](https://www.overleaf.com/project/5e8232cd6157d200014b52d4)
  - rules for identifiability 
- [ ] discuss the role of prior anatomical knowledge in reducing search space 

# formatting tasks 
- add figure references to table of contents  

# organization tasks
- move exemplars to sketches/intro-background ?