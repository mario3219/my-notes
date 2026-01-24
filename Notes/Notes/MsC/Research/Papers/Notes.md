**ViT survey keywords**
* Masked image modelling
MAE, BEiT, SimMIM
* Self-distillation
DINO, iBOT

**Notes from H&E ViT survey**
[MIPHEI-vit: Multiplex Immunofluorescence Prediction from H&E Images using ViT Foundation Models](https://arxiv.org/html/2505.10294v1#bib.bib9)

Plain ViTs for image level tasks, struggle with capturing fine local details, CCNs excelled more.

Proposed hybrid structure, ex CellViT
"uses the UNETR architecture which integrates a ViT encoder into a U-Net-like design"

* Encoder finetuning method
Frozen encoder vs LoRA, lora was better, but what is lora?

"Low-Rank Adaptation (LoRA), adapts a pretrained ViT encoder by adding trainable low-rank matrices to the Query and Value projections of the attention layers"

[[2103.10504] UNETR: Transformers for 3D Medical Image Segmentation](https://arxiv.org/abs/2103.10504)
UNETR has been developed as powerful transformer based models, namely U-net Transformers. U-net because the encoder downsamples the image, relating spatial information, and is then upsampled using skip connections. The architecture resembles a U-shape.
****
**Read about vision transformers**
[Vision Transformer (ViT) Architecture - GeeksforGeeks](https://www.geeksforgeeks.org/deep-learning/vision-transformer-vit-architecture/)

[[2010.11929] An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929?utm_source=chatgpt.com)

****
**Evaluation methods**
* Integrated gradients
	Highlights regions with strong expressions

 "Additionally, there is a lack of critical evaluation regarding how different spatial characteristics of H&E images can affect the accuracy of SGE predictions, especially on their impact on downstream analysis as well as potential clinical translation."
 [Benchmarking the translational potential of spatial gene expression prediction from histology | Nature Communications](https://www.nature.com/articles/s41467-025-56618-y)

"To assess current methods of predicting gene expression from histology images, we have developed a benchmarking framework across five key categories (Fig. [1b](https://www.nature.com/articles/s41467-025-56618-y#Fig1)). We employed a hierarchy of evaluation categories: 
(1) within image SGE prediction performance for lower-resolution spatial transcriptomics (ST) data initially described by Stahl et al. and higher-resolution 10x Visium data; 
(2) cross-study model generalisability, evaluated by applying models trained on ST data to predict Visium tissues, as well as to predict TCGA images to identify whether models were useful for predicting existing H&E images; and
(3) clinical translational impact by predicting survival outcomes and canonical pathological regions via predicted SGE. In addition, we considered 
(4) the usability of the methods encompassing code, documentation and the manuscript;
(5) and the computational efficiency"

**How to train your transformer**
[2106.10270](https://arxiv.org/pdf/2106.10270)
