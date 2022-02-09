see also https://beta.workflowy.com/#/f32ad4b2290a


summary of ideas 
- recording more isn't always enough 
  - more sophisticated inference isn't always enough!
- not all pertubations are created equal


## Reid, Calhoun, Cole et al. [Advancing functional connectivity research from association to causation](https://www.nature.com/articles/s41593-019-0510-4)
<!-- <details><summary>Abstract</summary> -->

> Cognition and behavior emerge from brain network interactions, such that investigating causal interactions should be central to the study of brain function. Approaches that characterize statistical associations among neural time series—functional connectivity (FC) methods—are likely a good starting point for estimating brain network interactions. Yet only a subset of FC methods (‘effective connectivity’) is explicitly designed to infer causal interactions from statistical associations. Here we incorporate best practices from diverse areas of FC research to illustrate how FC methods can be refined to improve inferences about neural mechanisms, with properties of causal neural interactions as a common ontology to facilitate cumulative progress across FC approaches. We further demonstrate how the most common FC measures (correlation and coherence) reduce the set of likely causal models, facilitating causal inferences despite major limitations. Alternative FC measures are suggested to immediately start improving causal inferences beyond these common FC measures.
<!-- </details> -->



## Ila Fiete , Abhranil Das - [Systematic errors in connectivity inferred from activity in strongly recurrent networks](https://www.nature.com/articles/s41593-020-0699-2)
<!-- <details><summary>Abstract</summary> -->

> Understanding the mechanisms of neural computation and learning will require knowledge of the underlying circuitry. Because it is difficult to directly measure the wiring diagrams of neural circuits, there has long been an interest in estimating them algorithmically from multicell activity recordings. We show that even sophisticated methods, applied to unlimited data from every cell in the circuit, are biased toward inferring connections between unconnected but highly correlated neurons. This failure to ‘explain away’ connections occurs when there is a mismatch between the true network dynamics and the model used for inference, which is inevitable when modeling the real world. Thus, causal inference suffers when variables are highly correlated, and activity-based estimates of connectivity should be treated with special caution in strongly connected networks. Finally, performing inference on the activity of circuits pushed far out of equilibrium by a simple low-dimensional suppressive drive might ameliorate inference bias.

### transcription
- **big goal:** structure - function
  - difficult to do
- **surprising result - challenge for field:**  
  > We show that even sophisticated methods, applied to unlimited data from every cell in the circuit, are biased toward inferring connections between unconnected but highly correlated neurons. 
  
- **explanation for why**
- **method/result for partial mitigation:** low-dimensional suppresive drive (open-loop stim) might ameliorate inference bias

<!-- </details> -->

## Fakhar, Hilgetag - [Systematic Perturbation of an Artificial Neural Network: A Step Towards Quantifying Causal Contributions in The Brain](https://www.biorxiv.org/content/10.1101/2021.11.04.467251v1)

> **Author summary** The motto “No causation without manipulation” is canonical to scientific endeavors. In particular, neuroscience seeks to find which brain elements are causally involved in cognition and behavior of interest by perturbing them. However, due to complex interactions among those elements, this goal has remained challenging. 
>
>In this paper, we used an Artificial Neural Network as a ground-truth model to compare the inferential capacities of lesioning the system one element at a time against sampling from the set of all possible combinations of lesions.
>
>We argue for employing more exhaustive perturbation regimes since, as we show, lesioning one element at a time provides misleading results. We further advocate using simulated experiments and ground-truth models to verify the assumptions and limitations of brain-mapping methods.

### transcription
- lesion analysis has been useful historically 
  - optogenetics facilitate making this more precise
