* UNI
[GitHub - mahmoodlab/UNI: Pathology Foundation Model - Nature Medicine](https://github.com/mahmoodlab/UNI)

H&E trained ViT model, requires HuggingFace access.

**Terms of service**
"May only be used for non-commercial, academic research purposes with proper attribution"
"By downloading this model, you agree not to distribute, publish or reproduce a copy of the model. If another user within your organization wishes to use the UNI 2 model, they must register as an individual user and agree to comply with the terms of use."

HuggingFace account matching institutional email, will have to wait until access to that email.

* CellViT
[CellViT: Vision Transformers for precise cell segmentation and classification - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1361841524000689)
[GitHub - TIO-IKIM/CellViT-plus-plus](https://github.com/TIO-IKIM/CellViT-Plus-Plus)

H&E trained ViT model
* Does require CUDA capable GPU
* 32GB RAM
* 30GB Disk space
* 16 core CPU

Requires conda, which still messes up my system

But the codebase includes a decoder block, not inherently only visual feature extraction

Have mostly been used in cell segmentation

Not pretrained

**Models from MIPHEI-ViT**
They benchmarked different visual encoders, which were "U-net" inspired architectures
****

* H-optimus-O
[releases/models/h-optimus/v0 at main · bioptimus/releases · GitHub](https://github.com/bioptimus/releases/tree/main/models/h-optimus/v0)

H&E trained

"to the best of our knowledge, the largest model backbone used in the context of computational pathology so far."

OUTPERFORMS ImageNet pretrained encoders

May be freely distributed if incorporated, however will have to include a copy of the Apache license

A model that states optimus was best
[1096 Hist2Cell: a vision transformer model for cell type prediction from histology images using pathology foundation models and spatial single-cell transcriptomics | Journal for ImmunoTherapy of Cancer](https://jitc.bmj.com/content/13/Suppl_2/A1248)


* CTransPath
[GitHub - Xiyue-Wang/TransPath](https://github.com/Xiyue-Wang/TransPath?tab=readme-ov-file

Good performance on unseen datasets
Uses frozen features, and then end-to-end fine tuning, H&E trained

.pth file for model states

****

Hibou-B
[GitHub - HistAI/hibou: Hibou: Foundational Models for Pathology](https://github.com/HistAI/hibou)
Trained on 1mill various histopathology images
Was however collaborated with CellViT, but is this meaningful?
Hibou-L also available, trained on 1Bil

* Virchow
[GitHub - Paige-AI/paige-ml-sdk: This package provides tools for training supervised machine learning models for computational pathology tasks using tile-level embeddings.](https://github.com/Paige-AI/paige-ml-sdk?tab=readme-ov-file)
[2309.07778](https://arxiv.org/pdf/2309.07778)

* ViTMatte
Cell segmentation focused
Proposed to have best trade-off between performance and training efficiency.
Not pretrained

* CONCH
[GitHub - mahmoodlab/CONCH: Vision-Language Pathology Foundation Model - Nature Medicine](https://github.com/mahmoodlab/CONCH)
Pretrained on several stains