![[Pasted image 20260106150507.png]]
**Generalization gap**
How big the gap is between training error and validation error

If the gap is large, means overfitting
If the gap is small, then its optimal

If the training error is large, then the model isn't complex enough, which
means underfitting

**Baseline**
For regression: prediction is the mean of past data
For classification: The most occurring class

Another way is the *achievable performance*. You compare with current
models and their accuracy.

**The different model approaches**

![[Pasted image 20260106151426.png]]

**Decision tree - Splitting criterion**
![[Pasted image 20260106190013.png]]
Shows cost vs missclassification. If r=0, all classes are guessed correctly, and 
therefore cost is zero. If 50% are guessed incorrectly, cost value is at max.

Workflow: a decision tree tests all possible splits and tresholds. For a given test,
it computes the cost function, and after all iterations, chooses the split that gave
the lowest cost. The cost function can be a synonym to how "pure" a split it.

Different splitting criterions have different benefits.
* Missclassification rate
		Equal care for positive and negative outcomes
* Gini
		Punishes negative outcomes more
* Entropy
		Heavier compute
		Sensitive to rare class separation