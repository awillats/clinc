- intuitive explanation using binary reachability rules
  <!-- - consider postponing until we introduce intervention? 
  - i.e. have one figure that walks through both reachability and impact of intervention -->
- *point to the rest of the paper as deepening and generalizing these ideas*
- *(example papers - Advancing functional connectivity research from association to causation, Combining multiple functional connectivity methods to improve causal inferences)*
      
- connect **graded reachability** to ID-SNR 
  - $\mathrm{IDSNR}_{ij}$ measures the strength of signal related to the connection $i→j$ relative to in the output of node $j$ 
  - for true, direct connections this quantity increasing means a (true positive) connection will be identified more easily (with high certainty, requiring less data)
  - for false or indirect connections, this quantity increasing means a false positive connection is more likely to be identified
  - as a result we want to maximize IDSNR for true links, and minimize it for false/indirect links 


( see also `sketches_and_notation/walkthrough_EI_dissection.md` )


