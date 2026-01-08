**<u>Optimization problem "Training method"</u>**
Least squares or maximum likelihood, two approaches of optimizing parameters

Maximum-likelihood is built with the approach of the likelihood of observing y given theta and x.
The approach uses optimization where the likelihood of observing y given x is at its highest,
which means that observations x are highly tied to y.

The closed form solution stems from the cost function $e(n)=y-\hat{y}$. By using the log form, the solution becomes parabolical.

<u>Transformations</u>
Input data gets transformed, for example $x_1^{2}, \ x_2^{3}...$

<u>Regularization</u>
Adds an extra punishing term in the minimization function
$\hat{\theta}=argmin_{\theta}\frac{1}{n}||X\theta-y||^2_2+\lambda||\theta||^2_2$
Depending on which $\lambda$ to use, the parameter optimization follows different courses, and optimize differently.

The model gets *punished* for being too complex. The model gets higher bias, but lower variance. The model stabilizes parameter adaptions, and smooths when data has variance.

![[Pasted image 20260106203746.png]]

**Example of beneficial case**:
Using $L^2$ Regularization lead to 4 out of 11 parameters being non-zero, and achieved same performance.

<u>Linear classification</u>
Uses logistic regression, optimizes parameters to fit, in the binary case, to a sigmoid function.

![[Pasted image 20260106204545.png]]

Different theta after training results in different probability boundaries for positive class. 
$g(x)$ is the cost function, and is optimized to be maximum for positive- and minimum for negative class.

* Model: $P(y=1|x)=\sigma(w^Tx+b)$
	$\sigma(z)=\frac{1}{1+e^{-z}}$ (probablity function)

Then to make the labelling:

$\hat{y}=\begin{cases} 1 & \text{if } P(y=1|x) \ge \tau \\ 0 & \text{otherwise} \end{cases}$

Where $\tau$ is the threshold, default is 0.5, which weights both classes equally. The function you see in the picture above is **FIXED**, $\theta$ decides the output of z, and only the positions on the z axis, which is the output of $z=f_{\theta}(x)$.

There is no closed form solution, and the optimization approach uses minimization of cost functions, usually the cross-entropy loss. The solution is still hyperbolic and convex, so a steepest descent algorithm is normal.

If multiclass, softmax is used, which is an extension of the sigmoid function:

$P(y=k|x)=\frac{e^{z_k}}{\sum_{j=1}^{K}e^{z_j}}$

Essentially calculates the probability sum of each class.

![[Pasted image 20260106211407.png]]
So given two features in this case, probability in the z axis, distributes boundaries like so.

<u>Linear regression</u>
Loss functions are how $y-\hat{y}$ is calculated, but the cost function is the entire function. Loss function is part of the cost function.

![[Pasted image 20260106211750.png]]
![[Pasted image 20260106211802.png]]

Different loss functions result in different punishment for large errors or outliers.
There are also different loss functions for classification

![[Pasted image 20260106211848.png]]

**Other mentions**
* Gradient descent
* 2nd order gradient descent
* Stochastic gradient descent
* ADAM
	Stores past computations of gradients, makes learning rate adaptive. The moments, which are derivations of the derivatives, is part of the correction coefficient for the update function. The function emphasizes recent gradients more than present ones.
* GridSearch