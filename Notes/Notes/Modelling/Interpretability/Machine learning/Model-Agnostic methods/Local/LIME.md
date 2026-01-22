Local interpretable model-agnostic explanations. LIME focuses on training local surrogate models to explain individual predictions

* Select instance of interest
* Perturb data and get black box predictions (perturb, meaning add disturbances)
* Weight new samples according to their proximity to the instance of interest
* Train interpretable model
* Explain the prediction by interpreting the local model

**Example**

![[Pasted image 20260112175241.png]]

* Select a point in the feature space, and randomly select large number of other points around it
* Apply the black-box model on all points and train a simple model to match the predictions

![[Pasted image 20260112175404.png]]

* Apply weights on points far away from the selected points
* Perturb the data
* Fit a local surrogate model
* Use the surrogate model to explain the local characteristics by looking at its structure

**Disadvantages**
* Not sufficient for complete attributions, so less useful in compliance scenarios