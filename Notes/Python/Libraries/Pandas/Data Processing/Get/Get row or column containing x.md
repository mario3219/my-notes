```
% Rows where a column contains a value
df_filtered = df[df.iloc[:, 2] == some_value]

% Rows where any column contains a value
df[df.eq(some_value).any(axis=1)]
```

Where a column contains a substring
```
df_filtered = df[df["label"].str.contains("cell")]
```

```
counts = counts[counts['ROI'].isin(roi_labels)].reset_index(drop=True)
```

If strings are indexed:
```
image_1
image_4
image_2
```

Then
```
subset = df[df["Image"].str.startswith("image_")]
```