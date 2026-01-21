<u>Abstract</u>

Tumour immune microenvironment (TIME) has been shown from studies to contain information that is prognostic for treatment outcome. Goal is to predict cell expressions using AI to enhance individual patient treatment by quantifying the TIME.

In-house model, Image2Count deconvolutes molecular expression from low-plex immunofluorescence imaging. Utilizes graph neural networks to predict expressions from cell graphs.

The trained model then enables high-plex predictions from images.

Measures performance using GeoMx dataset with larger 78-plex ROI, Cyclic IF 39-plex, 960-plex RNA single cell CosMx.

The difference from past research is that instead of using H&F (nuclei and cytoplasm) the in-house model predicts using low-plex images.

<u>Introduction</u>
Instead of predicting expressions for image patches or ROI's, the in-house model predicts expression counts (how many of what protein) that are present in individual cells, which is used downstream for further analysis.

This architecture choice benefits from training on bulk-count ROI data (how?)