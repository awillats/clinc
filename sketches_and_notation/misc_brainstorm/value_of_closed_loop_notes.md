### 1.) manipulating variability (often reducing it) 🎯
a.) this may mean you get a high resolution picture of the subparts of the system state you want to study without having to wait for the system to randomly find its way into that state

b.) say you want to study the impact of thalamic firing rate on the likelihood of detecting an incoming stimulus. In open-loop you could deliver a fixed low versus high amplitude optogenetic stimulus, measure the hit rate when stimulus is low compared to high and call that difference your effect size. However, if behavior really depends on thalamic rate not optogenetic input and there are inputs you can't measure and suppress in open loop (e.g. internal variability within the thalamus, somewhere you don't want to shutdown, or an external region whose pathways to thalamus are poorly understood) your effect size for this question will be blurred by the variability in thalamic firing rate as a function of the fixed optogenetic inputs. CL gives you a want to control more directly the variables you actually want to study.

c.) this is also closely related to classic disturbance rejection properties from control theory.
>  Although it is possible to separately image native dynamics and then try to evoke a similar response in open loop fashion by designing light stimuli before the experiment, such an approach is highly sensitive to model misspecification, calibration, and state changes in the system (habituation, plasticity, motor state, etc.), and without simultaneous measurement it cannot be confirmed that the response was accurately evoked. Closed-loop feedback control now allows real-time adjustment of input parameters to keep the observed output as close as possible to a target level or time-varying trajectory (Figure 4E).[^grosenick]

d.) while you can deliver open-loop inputs with titrated amounts of variance, you're often only able to add variance rather than subtract it, and the amount of variance you would add to the system is hard to predict a priori
     
### 2.) severing dependencies ✂️
- this is especially relevant in recurrent circuits.
- functional lesions (like chemogenetics) or structural lesions (like genetic variants, or surgical intervention) may do this completely, but with side effects.
- think of two reciprocally connected populations and a third dowstream A <-> B -> C. If you "lesion" A to B by delivering large negative currents to A, in order to better study B->C, now flutuations in A don't blur your picture of B->C great!. But you've also changed the baseline current from A to B, likely B is now firing at some altered rate based on its resting condition (maybe a rate it never reaches in the intact brain, or at which the relationship between B->C is different).
    
### 3.) changing or leaving in-tact naturalistic operating domains :frame_with_picture:
- avoiding stimulus domains which damage biological systems[^wolff]
- avoiding domains where input-output curves aren't representative, don't generalize to other domains

### 4.) finding a stimulus which achieves a complex multifaceted (time-varying) goal 🔢
(this connects to your comment about trying to achieve some multi-dimensional target). In a sense this is more about using an iterative method to solve a problem, than about the sample-by-sample correction for disturbance.

This could be achieved through model-based stimulus-optimization rather than closed-loop control, but we leverage the fact that the right closed-loop setup can solve the problem even with an imperfect model)

### 5.) studying relationships where relative timing matters ⏰
this has mostly been the domain of reactive / triggered stimulus delivery).
Whatever time an experimenter decides to deliver a particular stimulus is likely irrelevant compared to some sense of time that's relative to ongoing activity
I think it's also important to emphasize here that it's not clear that closed-loop control is universally superior to open-loop control, but it's a way of gaining additional degrees of freedom for studying relationships between variables (at the cost of algorithmic complexity, and introducing new dependencies)

## Additional themes

### inducing dependency *(related to 4, 5 above)*
- add virtual connections
- gain of function experiment

---
### For any intervention to outperform the passive case:
	The indirect correlations need to be strong enough to confound correlations
  - Strong enough weights 
  - But second order effects need to be comparable to direct effects
   (weights not too strong, rates roughly balanced)

### For closed-loop to outperform open-loop replay:
- Feedback needs to matter
  - There needs to be enough variability that replaying the stimulus leads to a different outcome 
  - There also need to be strong within-network disturbances to reject 
  - The target can’t be so strong that this feedforward effect swamps potential disturbances
  - Flat targets emphasize the closed-loop open-loop difference most strongly!
 - Closed-loop control needs to be effective
    - The network properties can’t be so extreme that the controller is unable to reject the disturbances

---

[^wolff]: promise and perils of causal manipulations