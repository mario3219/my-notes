```
from huggingface_hub import login
import torch
import timm

login()
model = timm.create_model(
    model_name, pretrained=True)
```