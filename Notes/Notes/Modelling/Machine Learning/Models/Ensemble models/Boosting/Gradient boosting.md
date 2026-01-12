Based on AdaBoost, but adds a smaller model that predicts the error, and nudges the prediction in the right direction.

Uses sequential construction:
Make a model
Make predictions
Calculate the error
Calculate the negative gradient for the error
Make a small model to predict that gradient
Add that model to the next model
Modify the training set with emphasis on poorly predicted data
Make a new model on that set together with the error predictor model
And repeat

Have a long fit time, but a short predict time