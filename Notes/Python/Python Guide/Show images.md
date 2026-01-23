Preferably don't use this in WSL, requires proper GNU image tool

```
from PIL import Image
```

Example generating random RGB image with torch
```
input = torch.rand(3, 224, 224)
pil_img = transforms.ToPILImage()(input)
pil_img.show()
```
