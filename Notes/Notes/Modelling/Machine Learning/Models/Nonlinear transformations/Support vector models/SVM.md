

![[Pasted image 20260110154351.png]]

Separates points using hyperplanes. During optimization, the hyperplane is chosen so that the distance from nearest points on each side is maximized.

SVM is linear model at heart, but can be nonlinear using transformations. Kernels can change the flexibility of the hyperplane.

![[Pasted image 20260110160045.png]]

SVMS are efficient when data is non-linearly and linearly separable.

**Difference between logistic regression and SVM**
Logistic regression uses decision boundaries, where the data points closest to the boundaries have largest influence on the optimization. Easy predicted data contributes minimally to the model. The loss function is conceptually a function of all points.

In SVM, boundary points are the primary focus, as those points are simply the support vectors.

The performance however is the flexibility of the hyperplane, linear or nonlinear. The choice is problem specific, so requires craftmanship, as some data are better described in different ways.