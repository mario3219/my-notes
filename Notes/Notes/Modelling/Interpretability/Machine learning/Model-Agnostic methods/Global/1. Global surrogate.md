You have a finished black box model. Select a dataset, get the predictions for that dataset, and then select other interpretable models and train them on the same dataset, and form predictions. The new models form the surrogate models, used to replicate the black box model. Use the surrogate models to interpret the black box.

**Advantages**
* Intuitive
* Any interpretable model can be used
* R-squared measure can easily measure how good approximations of the black-box is

**Disadvantages**
* Conclusions are drawn on the model, not the data
* Unclear where the cut-off for R-squared to estimate how close to the black-box model
* Depends on dataset chosen
