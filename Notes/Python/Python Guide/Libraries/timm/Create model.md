```
from huggingface_hub import login
import torch
import timm

login()
model = timm.create_model(
    model_name, pretrained=True)
```

If imported in a class:
```
import torch
import torch.nn as nn
import timm

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.backbone = timm.create_model(
            "vit_small_patch16_224",
            pretrained=True
        )

        self.head = nn.Linear(self.backbone.num_features, 10)

    def forward(self, x):
        x = self.backbone(x)
        x = self.head(x)
        return x
```

create_model imports a pytorch model. If the class inherits from nn.module, operations such as MyModel.to(device) moves all self attributes to the device.