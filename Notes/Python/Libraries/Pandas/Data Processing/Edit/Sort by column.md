```
data = data.sort_values(by='ROILabel')
```

Sort by column if it contains strings that are indexed, for example image_1, image_4, image_16

****

```
import pandas as pd

df = pd.read_csv("data.csv")
df["img_idx"] = df["Image"].str.extract(r"_(\d+)$").astype(int)
```
This will extract numeric indexes based on digits **after the last underscore**

Sort by the numeric column
```
df = df.sort_values("img_idx")
```

Drop helper columns
```
df = df.drop(columns="img_idx")
```

If you want to do operations on the strings first:
```
stem = df["Image"].str.split(".ome.tif").str[0]
idx = stem.str.extract(r"_(\d+)$").astype(int)
df["img_idx"] = idx
df = df.sort_values("img_idx").drop(columns="img_idx")
```