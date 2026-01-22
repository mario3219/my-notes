Adaptive boosting. Manually, as a designer you choose the base model, and the amount of iterations to run the algorithm.

Uses sequential construction:
Make a model
Modify the training set with emphasis on poorly predicted data
Make a new model on that set
And so on

The final prediction is a majority vote among the models.

It is not possible to parallelize the learning.

Performs worse with noisy data, because the algorithm uses exponential loss. Outliers and mislabelled data returns large weight changes.