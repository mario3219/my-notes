Visual representation learning on data was based on images from DNA, Keratin, CD35 and CD8a only (the database had up to 35 protein biomarkers)
Visual representation learning was also conducted using two markers only (DNA and keratin) to investigate performance when immune markers CD45 and CD8 was used downstream instead.
Data was processed to resemble GeoMx data which was based on ROIs selected from 4-plex IF.

**Neighbourhood tests**
The 4-channel models (learning from DNA, CD45, keratin and CD8) outperformed all models consistently, compared to only using 2-channel models.

* Merged GAT Image2Count > Merged FFW Image2Count
Implies that immediate neighbours is most impactful for prediction
However, the most relevant information was contained in the first cut-out, as neighbouring cells usually take space in the cut-out as well, meaning that neighbouring nodes representing other cut-outs minimally improves performance.
Merged GAT displayed higher standard deviation, which shows that neighbouring cells in data affect predictions, requiring more data during training.
Certain markers also benefit from spatial context.
Oversampling low abundance phenotypes helped performance.
Consensus predictions over all cross-validation runs improved prediction.
Window size benefited some markers, some worse.

**Spatial patterns and specific cell clusters**
Data was separated into two large clusters, difference being varying mean intensities for markers.

Predicted cell counts was lower than true counts, but showed a more "average" prediction across tissue.

Comparing visually shows that some expressions in structure was correctly learned. A lot of biomarkers were failed to be detected, some a lot more than others, around boundaries and or high density areas.
An implication was that the model struggles to discriminate between different lymphocytes as they share similar morphology.
Reducing window size allowed the model to more easily detect some cell expressions.

TLS, one of the biomarkers, were uncommon and likely underrepresented in the training data.




