Importance of a feature is calculated in the following way:
Go over each split, and see how much the feature reduced the variance or the Gini index, compared to the parent node. The sum of all importances is the final importance value.

**Disadvantages**
* Fail to deal with linear relationships
* Slight changes in feature can have big impact
* Trees are quite unstable
* Interpretability gets lower with depth