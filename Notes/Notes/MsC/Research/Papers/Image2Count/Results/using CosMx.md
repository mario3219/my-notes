CosMx cells had been stained for membrane, and counts had been assigned to detected cells. The counts was used to create 4 pseudo ROIs to train models.

**Performance**
Performance was generally higher when merging predictions over all cross-validation models.

Performance was higher with neighbourhood in mind.

Merged GAT Image2Count outperformed on:
* MI
* Spearman
* Pearson
Merged FFW Image2Count outperformed on:
* MSE
Merged ResNet outperformed on:
* Cosine Similarity

**Dropout events**
CosMx suffers from low detection accuracy of low abundant transcripts, so present molecules can be measured as low counts. Inputting these might give a better estimate on performance. DCA (deep count autoencoder) was used to estimate false dropout events. A separate model was trained using DCA compared to a model with raw counts, and performance was significantly improved.