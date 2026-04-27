```
keys = ["Image", "Centroid.X.px", "Centroid.Y.px"]

df_reordered = df_ref[keys].merge(df, on=keys, how="left")
```

Good to check
```
merged = df_ref[keys].merge(df[keys], on=keys, how="outer", indicator=True)

print(merged["_merge"].value_counts())
```

- `"both"` → good ✅
- `"left_only"` → exists only in `df_ref`
- `"right_only"` → exists only in `df`