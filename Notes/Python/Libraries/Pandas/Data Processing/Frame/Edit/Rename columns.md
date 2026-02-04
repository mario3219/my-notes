
Specific
```
df = df.rename(columns={
    "old_name": "new_name",
    "Centroid.X.px": "x_px",
})
```

All
```
df.columns = ["Image", "x_px", "y_px"]
```