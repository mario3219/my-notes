* There are some models pretrained on ImageNet, and used in reports analyzing histopathology. How viable is this?
Domain gap, not viable

* The models:
	* A linear prediction head called ResNet for simplicity
	* Image2Count consisting of purely residual FFW networks
	* Image2Count utilizing residual graph convolutions with attention (GAT)
	* FFW networks which used the constructed cell graph from SimCLR
Where these used in all parts of the report, for all the datasets?

* "Training based on bulk spatial-molecular ROI samples"
Does this mean that the training is based on essentially one vector per ROI, containing molecular profiles for gene expression, protein abundance etc?

* Do the datasets contain images with healthy cells too?
Probably, as the images used are contrastive images.

* How is it possible for the model to be trained on low-plex images, and predict high-plex profiles?