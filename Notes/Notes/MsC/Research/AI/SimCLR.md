Self-supervised learning method used in neural networks.

**How it works**
* Creates two augmented versions of an image (augmented being introducing colour jitter, random crops, blur)
* An encoder network maps the images
* A projection head, which is a MLP on top of the encoder, maps h to z
* InfoNCE, another algorithm, pulls together embeddings that are similar in both images, and pushes away embeddings that are different, using z from the projection head.
* The pulled together embeddings are the learned *representations*.
* Throughout training, the learned representations are backwards propagated to the encoder layer.
* The projection head is removed, and the encoder layer then becomes the feature extractor.