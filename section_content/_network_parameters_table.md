
|                          descr. | name           | value[^cv] | units                   |                 | also in LG |
| -------------------------------:| -------------- | ----------:|:----------------------- | --------------- | ---------- |
|  number of neurons in each node | $n_{neurons}$  |        100 | #                       | `N_sub`         |            |
|   number of nodes (populations) | $N_{pop}$      |          3 | #                       | `N_pop`         |            |
|        time-step for simulation | $\Delta_t$     |        0.1 | $ms$                    |                 |            |
|             equilibrium voltage | $V_{0}$        |          0 | $mV$                    | `v0`            |            |
|                   reset voltage | $V_{reset}$    |          0 | $mV$[^V_dim]            | `v_r`           | ❌         |
|       spiking threshold voltage | $V_{\theta}$   |          1 | $mV$                    | `v_th`          | ❌         |
|      absolute refractory period | $\tau_{ref}$   |          2 | $ms$                    | `tau_ref`       | ❌         |
|          membrane time-constant | $\tau_{m}$     |         10 | $ms$                    | `tau_syn`       |            |
|      private voltage noise[^xi] | $\sigma_m$     |          1 | $\frac{1}{\sqrt{sec.}}$ | `sigma`         |            |
|                                 |                |            |                         |                 |            |
|   sensitivity to current inputs | $B$            |          1 | $\Omega$                | `R`             |            |
|                                 |                |            |                         |                 |            |
|                 synaptic weight | $w$            |        1.0 |                         | `w`             |            |
| synaptic connection probability | $p$            |        1.0 |                         | `p`             |            |
|                  synaptic delay | $\delta_{syn}$ |    {0,1,2} | $ms$                    | `synapse.delay` |            |


<!-- |             equilibrium voltage | $V_{0}$        |    ?? | $mV$                         | `v_r`     | ❌         |
     |                   reset voltage | $V_{reset}$    |   -65 | $mV$                         | `v_r`     | ❌         |
     |       spiking threshold voltage | $V_{\theta}$   |   -50 | $mV$                         | `v_th`    | ❌         | -->

<details><summary>see also</summary>

tau_syn: synaptic rise-time
</details>
---
Leaky integrate-and-fire dynamics[^LIF_text]
\[
\frac{dV}{dt} = \frac{V_0 + I - V}{\tau_m} + \sigma_m \sqrt{\tau_m} \xi(t)
\]
when a presynaptic neuron spikes, simulate a "dirac delta-function"[^delta_gerstner] current injection from a synapse:
\[
V_j = V_j+w_{ij}
\]

---


Brain2 implementation:
```python
'dv/dt = (v0 + I_bias + I_stim + I_syn - v)/tau_m + sigma*xi*(tau_m**-0.5) :1'
'v_post += w'
```

*see [small_circuit_scripts/circuit_functions/simple_neuron_model.py](https://github.com/awillats/clinc-gen/blob/main/small_circuit_scripts/circuit_functions/simple_neuron_model.py)*

----
<!-- https://neuronaldynamics.epfl.ch/online/Ch1.S3.html -->
[^delta_gerstner]: delta-function synapses: https://courses.edx.org/assets/courseware/v1/cd95b8cdb79e262146d843d5a4635050/c4x/EPFLx/BIO465.1x/asset/slides_lecture1.2.pdf, see also: http://dai.fmph.uniba.sk/courses/comp-neuro/reading/Sterratt_CH7_synapse.pdf
[^V_dim]: in code, voltages are currently implemented as dimensionless
[^LIF_text]: textbook description of LIF: https://neuronaldynamics.epfl.ch/online/Ch1.S3.html
[^xi]: see [brian documentation](https://brian2.readthedocs.io/en/stable/user/models.html#noise) on [stochastic differential equations](https://en.wikipedia.org/wiki/Stochastic_differential_equation), [time scaling of noise](https://brian2.readthedocs.io/en/stable/user/models.html#time-scaling-of-noise). Maybe should be $\sqrt{\frac{2\sigma_m^2}{\tau_m}}$ with sigma in the same units as $V$ to make the noise amplitude$\sigma$ invariant to $\tau_m$ see [Ornstein-Uhlenbeck](http://www.scholarpedia.org/article/Stochastic_dynamical_systems#Ornstein-Uhlenbeck_process)