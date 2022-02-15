Our goal is to develop clean answers, phrased in neuro terms, to the following questions:
- Given a pair of neural circuits, is it possible to disambiguate them using observational data, or is open- or closed-loop control needed?  If control is needed, where should it be applied?
- Given a fixed control budget and some kind of ranking of potential causal links we'd like to uncover, where should control be applied, and how much inference power do we have?
- How do these answers change in the face of **imperfect** control (for example, when other observed or unobserved variables still have some limited effect on the circuit)?


## Open methodological questions
- **how to predict/describe the impact of delays on SNR** 
- is it useful to sum component-wise identifiability across nodes → net identifiability?
- connect quotient vector product form of SNR calculations to existing model structures
  - does this connect to transfer functions in Laplace domain for instance?

- is the distinction between reachability and controlability relevant?
  - [see discussion here](https://math.stackexchange.com/questions/3030305/what-is-the-difference-between-controllability-and-reachability)
- should a node be considered reachable from itself?
  - would splitting nodes into Sin | Sout help make this clearer
- do we need to consider "fork-shaped" reachability?