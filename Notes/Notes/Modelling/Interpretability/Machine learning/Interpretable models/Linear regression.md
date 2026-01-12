![[Pasted image 20260112155424.png]]

In linear regression, uses a naive model being the prediction is always the mean of the data, and compares the estimated model with the naive.

The reference variance is:
$SSE=\sum^n_{i=1}(y^{(i)}-\hat{y}^{(i)})^2$
being the estimation error variability in the data

Compared with the total variability in the data:
$SST=\sum^n_{i=1}(y^{(i)}-\overline{y})^2$

Using:
$R^2=1-\frac{SSE}{SST}$

0 means bad, 1 is good.

**Feature importance**
$t_{\hat{\beta}_j}=\frac{\hat{\beta_j}}{SE(\hat{\beta_j})}$
If increasing the weight leads to higher model variance, the parameter therefore has more importance.

**Weight effect**

![[Pasted image 20260112160254.png]]

It's hard to compare how important a feature is if they have large values, as a large feature doesn't necessarily mean an important feature. The effect (right plot) downscales the feature weights for easier comparison, showing directly how influential a parameter is.

![[Pasted image 20260112160430.png]]

Parameters that are statistically around zero are unimportant.

**Disadvantages of linear regression**
* Can only represent linear relationships
* Nonlinearity needs handcrafted transformations
* Usually oversimplifies reality
* Correlated features can occur
