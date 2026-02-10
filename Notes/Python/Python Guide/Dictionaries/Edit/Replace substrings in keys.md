```
old = "image_encoder.img_feature_extractor."

new_dict = {
    k.replace(old, ""): v
    for k, v in my_dict.items()
}
```