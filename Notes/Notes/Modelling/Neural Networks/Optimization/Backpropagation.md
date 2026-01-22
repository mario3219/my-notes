The network optimizes:
$\theta=[vec(W^{(1)})^T \ b^{(1)T} vec(W^{(2)})^T \ b^{(2)T}]^T$
by minimizing $J(\theta)$.

For regression, error uses *squared error loss*
$L(x,y,\theta)=(y-f(x;\theta))^2$

For classification, error uses *cross-entropy loss*
$L(x,y,\theta)=-ln \ g_y ( f(x;\theta) ) = -z_y+ln\sum^M_{j=1}e^{z_j}$
which has no closed form solution, and uses gradient-based approaches.

**Optimizing**
Does this through stochastic gradient descent, and updates $\theta$ using backpropagation algorithm.

Essentially, all parameters are initialized, an initial prediction is made, the error is calculated:
$E(\theta)=L(y,\hat{y})$
and the gradient is calculated for each $\theta$, updating backwards layer by layer:
$w_{t+1}=w_t-\epsilon\frac{\partial E(\theta)}{\partial w}$
$b_{t+1}=b_t-\epsilon \frac{\partial E(\theta)}{\partial b}$

**Backpropagation and chain-rule**
Consider a chain:
$w\rightarrow z \rightarrow a \rightarrow L$
And we use the loss to ask *How much does w affect L?*
This is hard to track, because in reality, w affects z, that affects a, that affects L.

The chain rules couples how w changes L by incorporating how all in-between layers depend on each other.

What is actually being back-propagated? We use the chain rule.
At the output, we calculated how L is affected by a, we get $\frac{\partial L}{\partial a}$. That result is then used one layer propagated back, in that equation.
$\frac{\partial L}{\partial z}=\frac{\partial L}{\partial a}\cdot \frac{da}{dz}$
Then THAT result is used in the derivate of the NEXT equation.

This is the chain-rule used, so instead of calculating a big closed form update equation, which would mean that the symbolic derivative have millions of terms, and a lot of partial derivatives will be recalculated.

If we wrote one big closed-form derivative of the loss with respect to all parameters, and then updated each parameter using its partial derivative, it would still be equivalent to backpropagation. The difference is that backprop avoids recomputing the same partial derivatives by doing things layer by layer.