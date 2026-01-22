![[Pasted image 20260108222710.png]]

Utilizes feedback loops, can also be used for each AR component.

![[Pasted image 20260108222753.png]]

Note the different activation function, being tanh.

**Vanishing/exploding gradient problem**
Due to the same weights being used for each calculation of y, and the presence of a feedback loop, weights can result in exploding gradients or vanishing gradients. For example, if a weight is equal to zero, a past sample will be forgotten.