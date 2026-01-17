**DCA and dropout events**
Finding dropout events using DCA improved performance

CosMx suffers from low detection accuracy of low abundant transcripts, so present molecules can be measured as low counts. Inputting these might give a better estimate on performance. DCA (deep count autoencoder) was used to estimate false dropout events. A separate model was trained using DCA compared to a model with raw counts, and performance was significantly improved.

**Higher L1 loss leads to more average expressions across tissue**

**Future work will benefit from considering penalizing models for creating sc predictions far from observed sc expressions**

**Selecting more diverse areas for GeoMx ROIs might increase performance**
Performance was worse with GeoMx (from 0.90 to 0.20 compared to t-CyCIF) due to variance in the dataset. Many more patients were included and few ROIs per patient, and not perfect cut-outs.

**Single-cell segmentation quality was not investigated**
Expected to be a limiting factor as well.

**Oversampling low abundance phenotypes improves performance.**

**Inclusion of more markers increased predictions overall**

**Foundation models struggle when other markers are included**