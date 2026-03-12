* Rows where column value is equal to
String
```
cell_positions = df[df['Image'].str.startswith(img_name)]
df_filtered = df[df["label"].str.contains("cell")]
counts = counts[counts['ROI'].isin(roi_labels)].reset_index(drop=True)
```

Indexes are preserved from the old
```
cell_positions.index
```

Absolute equals, specific column
```
df_filtered = df[df.iloc[:, 2] == some_value]
```
Any column
```
df[df.eq(some_value).any(axis=1)]
```