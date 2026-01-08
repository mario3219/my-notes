Different activation functions results in different types of models
Logistic: $h(z)=\frac{1}{1+e^{-z}}$
ReLU: $h(z)=max(0,z)$

**Multiclass logistic regression**
Uses a SoftMax activation function at the final layer

![[Pasted image 20260108210404.png]]

The role of the bias inside the neural network function, is to be able to push the output so that it can pass the threshold.

**tanh**
Used for time series networks