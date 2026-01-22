**Decision tree - Splitting criterion**
![[Pasted image 20260106190013.png]]
Shows cost vs misclassification. If r=0, all classes are guessed correctly, and 
therefore cost is zero. If 50% are guessed incorrectly, cost value is at max.

Workflow: a decision tree tests all possible splits and thresholds. For a given test,
it computes the cost function, and after all iterations, chooses the split that gave
the lowest cost. The cost function can be a synonym to how "pure" a split it.

Different splitting criterions have different benefits.
* Misclassification rate
		Equal care for positive and negative outcomes
* Gini
		Punishes negative outcomes more
* Entropy
		Heavier compute
		Sensitive to rare class separation

The Gini criterion is the default. Tracks impurity, meaning how many classes are in a node, and Gini importance tracks how much the impurity got lowered because of a specific feature.