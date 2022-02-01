We begin with the simple linear dynamical system
\[
\begin{equation}
    \begin{cases} \dot{x} = Ax \\ y = Cx + \eta \end{cases}
\end{equation}
\]
where $A$ is the adjacency matrix
\[
\underbrace{\begin{bmatrix} \dot{x}_A \\ \dot{x}_B \\ \dot{x}_C \end{bmatrix}}_{\dot{x}} =
\underbrace{\begin{bmatrix}
    w_{AA} & w_{AB} & w_{AC} \\
    w_{BA} & w_{BB} & w_{BC} \\
    w_{CA} & w_{CB} & w_{CC}
\end{bmatrix}}_{A}
\underbrace{\begin{bmatrix}
    x_A \\
    x_B \\
    x_C
\end{bmatrix}}_{x}
\]

----

### PLDS, SISO w/Inputs
*(Poisson linear dynamical system, single-input single-output)*:
\[
\dot{x} = Ax + Q\omega + Bu\\
y = Cx + \eta\\
z = \exp(y)\\
\mathrm{spikes} = \mathrm{Poiss}(z)
\]