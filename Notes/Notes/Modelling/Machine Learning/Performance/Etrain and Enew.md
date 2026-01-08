**Generalization gap**
Different cases of the generalization gap implies different outcomes to handle
* Low E-train, big generalization gap
		Overfit
* High training error, big generalization gap
		Underfit

It also scales differently depending on how much data, and how complex the model is

![[Pasted image 20260107210139.png]]

![[Pasted image 20260107210256.png]]

The optimal case is reaching the minima in E-new.

![[Pasted image 20260107210430.png|600]]

A simple model won't be able to capture the full dynamics of the data, and be biased. A too complex model will capture too much of the dynamics, and essentially be modelling noise as well, hence increasing variance. The noise in the data will prevent the training performance to be equal to performance for new data.

