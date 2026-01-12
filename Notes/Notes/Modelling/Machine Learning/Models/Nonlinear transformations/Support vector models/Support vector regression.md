
Regression version of SVM. Instead of separating classes, fits functions to data.

![[Pasted image 20260110155640.png]]

The formulation does the following:
* Change loss function to $\epsilon$ - insensitive loss
* Use linear algebraic formulations to change $\theta$ formulation
* Choose kernels and $L_1$ regularization, which leads to sparse $\alpha$ solutions
Results in infinite feature length, but transfers dxd size matrix to dx1 size solution.