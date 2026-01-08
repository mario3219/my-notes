Data was split into test and training sets. For each dataset, a feature backbone was trained via SimCLR.

SimCLR sampled equally using KMeans, to achieve a more equal cell class distribution.

**How does KMeans lead to more equal cell class distribution?**
For each cell image, clustering pixels, then equal amount of sampling from each cluster. No dominant visual representation overfloods the visual feature sampling.

Features of each cell were embedded into spatial cell graphs, with edges being the Euclidian distance between cells.

Pseudo bulk-counts were constructed, by making local ROI's using the distances, to create datasets similar to the GeoMx data.

K-cross-validation was then used.