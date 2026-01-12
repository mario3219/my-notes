Use white noise as an input, and extract the output of a desired layer. The output will show what the layer got trained on.

* Input noise image
* Get the output of a layer
* Calculate the loss and the gradient
* Resize image in regard to that gradient, to maximize the output
* Repeat N times until the final image visually represents the layer output.

![[Pasted image 20260112182228.png]]

The loss can be plotted, to show how each layer responds to an input, showing if layers got trained on the same features.