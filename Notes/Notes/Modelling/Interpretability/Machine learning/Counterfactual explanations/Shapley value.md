Determines the contribution of each parameter, which is the average of all marginal contributions in all possible coalitions.

"The feature values enter the room in random order, all features contribute to the prediction. The shapley value of a feature is the average change in prediction that the feature contributes compared to what the coalition already in the room contributes."

In its essence, investigates single predictions, but can be turned local or global as an average.

**Advantages**
* Legally compliant method

**Disadvantages**
* Computationally expensive
* Returns a simple value, not a model