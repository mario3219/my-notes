**Dropout**
Neural network version of regularization. A node is dropped, which forms a subnetwork. The gradient is calculated for that subnetwork, and the parameters for that subnetwork are updated. The dropout node is reinserted, and a new node is dropped. This repeats until a condition is fulfilled.

**Other regularization methods**
* $L_1$ and $L_2$ regularization
* Early stopping
* Sparse representations
But dropout is the most popular. A popular method is to extend a model until it overfits, then extend it a bit more, and finally add a regularization like dropout to avoid overfitting.