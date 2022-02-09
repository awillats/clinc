## Feb 2022 draft

A primary goal of neuroscience is identifying causal relationships in the brain[^N1], a task often aided by interventions which stimulate activity in portions of the brain such as lesioning and optogenetics. These open-loop interventions[^N2][^N3], however, do not fully eliminate potential confounding influences, often limiting their ability to reveal causal structure[^N4]. In this paper, we use tools from causal inference, control theory, and neuroscience to show *when* and *how* closed-loop[^N5] interventions can more effectively reveal causal relationships. Using a variety of simulated neural circuits, we examine how key process and intervention parameters affect identifiability[^N6][^N7], developing guidance to help experimentalists determine when closed-loop control[^N8] is needed to infer causal structure, and when observational data or open-loop stimulation is sufficient. Our results build toward a practical framework that will aid experimental neuroscientists[^N9] design and interpret experiments that, by revealing more causal structure in the brain, could open the door to new and more effective therapies.[^N10]

[^N1]: make this language more neuro-specific
[^N2]: necessary to define "interventions" or "open-loop"?
[^N3]: is "lesioning" really an open-loop stimulation?
[^N4]: could make this more precise, e.g., with ", particularly in neural circuits that feature reciprocal connections or strong feedback and fast timescales"
[^N5]: will most readers be familiar with "closed-loop"? or should this be defined / a different phrase used?
[^N6]: will "identifiability" be understood, or should this be defined
[^N7]: if we're confident the conclusions drawn from xcorr generalize to TE (and discuss this in the paper) I think the abstract would be stronger without specializing it to a specific algorithm --- but if all the results are pretty xcorr-specific we should mention that here.
[^N8]: how much to focus on the "control" aspect here? (closed-loop interventions? closed-loop control?)
[^N9]: not sure what word to use here --- "systems neuroscientists"? "experimentalists"?
[^N10]: perhaps somewhat redundant with previous sentence? trying to go for broader impact here.
