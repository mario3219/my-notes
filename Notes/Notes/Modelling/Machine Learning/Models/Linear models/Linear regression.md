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