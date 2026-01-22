Every layer receives all previous layer feature maps, the total amount of channels increase with the amount of layers.

**Feature reuse**
- Early, low-level features remain accessible
- Later layers don’t need to relearn edges or textures
**Strong gradient flow**
- Short paths from loss to shallow layers
- Less vanishing gradient trouble
**Parameter efficiency**
- Often fewer parameters than ResNet with similar accuracy

**Trade-offs**
- High memory usage (due to concatenation)
- Slower inference
- Less GPU-friendly than ResNet