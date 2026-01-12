Uses logistic regression, optimizes parameters to fit, in the binary case, to a sigmoid function.

![[Pasted image 20260106204545.png]]

Different theta after training results in different probability boundaries for positive class. 
$g(x)$ is the cost function, and is optimized to be maximum for positive- and minimum for negative class.

* Model: $P(y=1|x)=\sigma(w^Tx+b)$
	$\sigma(z)=\frac{1}{1+e^{-z}}$ (probability function)

Then to make the labelling:

$\hat{y}=\begin{cases} 1 & \text{if } P(y=1|x) \ge \tau \\ 0 & \text{otherwise} \end{cases}$

Where $\tau$ is the threshold, default is 0.5, which weights both classes equally. The function you see in the picture above is **FIXED**, $\theta$ decides the output of z, and only the positions on the z axis, which is the output of $z=f_{\theta}(x)$.

There is no closed form solution, and the optimization approach uses minimization of cost functions, usually the cross-entropy loss. The solution is still hyperbolic and convex, so a steepest descent algorithm is normal.

If multiclass, softmax is used, which is an extension of the sigmoid function:

$P(y=k|x)=\frac{e^{z_k}}{\sum_{j=1}^{K}e^{z_j}}$

Essentially calculates the probability sum of each class.

![[Pasted image 20260106211407.png]]
So given two features in this case, probability in the z axis, distributes boundaries like so.