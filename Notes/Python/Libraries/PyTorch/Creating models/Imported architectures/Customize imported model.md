**Output shape**

```
model = timm.create_model("MODEL_NAME_HERE", pretrained=True, num_classes=0)
model.eval()
```

num_classes=0 leads to the model outputting embeddings

**Input transform pipeline**

```
from timm.data import create_transform

model = timm.create_model("MODEL_NAME_HERE", pretrained=True)
cfg = timm.data.resolve_model_data_config(model)
transform = create_transform(**cfg, is_training=False)
x = transform(img).unsqueeze(0)

model.eval()
y = model(x)
```