## (old draft)
<!-- %identifying circuits in the brain is a major goal of neuroscience -->
A primary goal of neuroscience is identifying causal relationships between portions of the brain[^1],
[^1]:make this sound more neuro-legit
<!-- %it's difficult. -->
a task that is challenging `(impossible?)` when only interventional data is available despite increasing volumes of data.
<!-- % interventions have been used before -- crude and newer -->
Interventions that stimulate parts of the brain, such as lesioning and optogenetics[^N], have been proposed to partially overcome this difficulty.
<!-- % but open-loop interventions insufficient -->
These open-loop interventions, however, do not fully eliminate confounding, limiting their ability to reveal casual structure in some circuits. This is especially problematic when circuits feature reciprocal connections or strong feedback at fast timescales.
<!-- % closed loop + causal inference -->
In this paper, we show that interventions using closed-loop control can overcome these limitations.
<!-- % more specifics on paper
% - when is observational/open-loop sufficient / when is closed-loop required?
% - "what are the requirements for spatial and temporal degrees of freedom to meet our identification goals?"
% - how can aspects of an experiment be designed in order to strengthen (and make more data-efficient) our inferential power? -->
We provide a practical framework for applying closed-loop control to circuit identification problems[^3] and propose rules that predict when observational data or open-loop interventions are sufficient, and when closed-loop control is needed. Using a wide range of simulated circuits, we then characterize how key process and intervention parameters affect successful identification. This characterization builds towards an understanding of the limits of identification[^4]  and suggests methods for improving the next generation of circuit identification.
<!-- % broader impact -->
Our approach could complement existing technology developments and guide the next generation of (identification in neural circuits).

[^N]: add more neuro
[^3]: specify we're focusing on 3-node for now?
[^4]: mention interventional budget?


<!-- %further problem - we can execute closed-loop, but we don't know how to do so best for identification -->
In this work, we aim to provide a practical framework for applying closed-loop control to circuit identification problems. (The hope is this work) will (open up, further develop) a dialog between those designing and executing systems neuroscience experiments and computational neuroscientists about how to conduct identification experiments moving forward[^5]. We aim to start answering questions such as
- what additional value does closed-loop control offer?
- in which circuits is closed-loop control necessary? in which circuits is open-loop control sufficient? What are the requirements for spatial and temporal degrees of freedom to meet our identification goals?
- what can be (said about) the connections identified from such experiments?
- How can aspects (parameters?) of an experiment be designed in order to strengthen (and make more data-efficient) our (hypothesis-testing power, the conclusions about circuits)

[^5]: make less condescending

<!-- %results overview? -->
Overall, this paper summarizes the intersection of causal inference, neuroscience, and control theory, highlight why and where intervention facilitates circuit identification. We then demonstrate how these principles apply to a simple case study of a 3-node circuit. Then we show a broad characterization of how several key process and intervention parameters affect successful identification. This characterization builds towards and understanding of the (limits of identification) and (begins to suggest) ways to (make the most of the next generation of circuit identification)

<!-- % broader impact - why -->
This is important because statements of causality are what we mean fundamentally when we talk about how the brain works. Statements of causality are also what we need when seeking to develop new therapies to treat disorders of the brain.