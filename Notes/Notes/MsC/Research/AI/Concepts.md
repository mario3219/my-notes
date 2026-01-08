**Multi-layer perceptrons**
Simple, fully connected neural networks.

**Image embeddings**
Encodes image contents into numeric representations

**Subgraph hops**
1-hop, direct neighbour
2-hop, neighbour of neighbour
...

**Dropout event**
The molecule is **actually present**, but the measurement records a **zero or very low count**.

**Scanpy**
Python library for analyzing single-cell omics data.

**Leiden clusters**
Usually built by scanpy, uses nodes as cells, edges as similarity, and edge weights. Similarity usually formed with k-nearest neighbours in PCA space.
Not defined by distance.
Similarity calculated using proteins and expression counts
This information reduced using PCA

**Wilcoxon rank sum**
Statistical test. Compares distributions, not means, and does not assume normality.
"Do these two groups tend to have different values?"

**UMAP**
![[Pasted image 20260108170344.png]]

Uniform Manifold Approximation and Projection
Builds a neighbourhood graph with kNN.
Distances become probabilistic connections
Visualizes high dimension vectors into 2D space
One dot is a cell.
The position of the dot comes from UMAP.
Colours are Leiden clusters
