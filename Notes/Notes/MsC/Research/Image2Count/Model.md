Trained a ResNet model with SimCLR to learn visual representations. 

The SimCLR was used as a prediction head to pre-train the ResNet, and sampled equally using KMeans clusters.

The trained visual embeddings functioned as nodes in a cell graph, on which a GNN learned neighbourhood information, to then predict cell expressions. 

Alongside this, the same visual embeddings were used to train a non-linear FFW network to predict without neighbourhood context, for comparison with the GNN.

**The compared models**
The comparison of performance was done with three different models.
* A linear prediction head called ResNet for simplicity
* Image2Count consisting of purely residual FFW networks
* Image2Count utilizing residual graph convolutions with attention (GAT)
* FFW networks which used the constructed cell graph from SimCLR

The model trains on low-plex images (meaning that the model can be trained using only four contrastive images), and can predict high-plex profiles.

**In my words**
Visual feature backbone, learns visual features for the high-contrast images
These visual features becomes embedding functions (from visual to numbers)
and gets forwarded to the Image2Count model. This model in turns predicts the cell expression profile. Meaning, from numbers representing how the contrast features look like, to how many of certain proteins are present in the cell. Therefore, predicting single cell expression.

The model predicts single cell expression by also associating neighbouring cells in the prediction, by using the visual embeddings as part of graphical nodes.