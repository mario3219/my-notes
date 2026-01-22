Adds an extra punishing term in the minimization function
$\hat{\theta}=argmin_{\theta}\frac{1}{n}||X\theta-y||^2_2+\lambda||\theta||^2_2$
Depending on which $\lambda$ to use, the parameter optimization follows different courses, and optimize differently.

The model gets *punished* for being too complex. The model gets higher bias, but lower variance. The model stabilizes parameter adaptions, and smooths when data has variance.

![[Pasted image 20260106203746.png]]
**Example of beneficial case**:
Using $L^2$ Regularization lead to 4 out of 11 parameters being non-zero, and achieved same performance.

Using $L^2$ results in ridge regression.