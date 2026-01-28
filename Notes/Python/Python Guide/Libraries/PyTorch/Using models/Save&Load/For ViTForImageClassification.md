Load first time
```
model = ViTForImageClassification.from_pretrained(
    "google/vit-base-patch16-224",
    )
```

Save
```
torch.save(model.state_dict(), "vit_model.pt")
```

Load later
```
model = ViTForImageClassification.from_pretrained(
    "google/vit-base-patch16-224",
    pretrained=False
)
model.load_state_dict(torch.load("vit_model.pt", map_location="cpu"))
model.to(device)
```