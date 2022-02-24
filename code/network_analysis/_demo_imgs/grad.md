The gradient of $r^2$ tells us, from a starting vector of source variances $S$, what direction we should adjust these variances ($\Delta S$) to maximize $r^2$
\[
\nabla{r^2} (s_1, s_2, s_3) = 
\begin{bmatrix}
\frac{\partial r^2}{\partial s_1} \\\\
\frac{\partial r^2}{\partial s_2} \\\\
\frac{\partial r^2}{\partial s_3} \\
\end{bmatrix}
\]

If the sign of $\nabla{r^2} (S)$ is independent of $S$, this gives us a global understanding of what directions in $S$ maximize $r^2$.