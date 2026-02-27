
```
mask = (df.iloc[:, col_indices] == 0).all(axis=1)
```

Indexes
```
idx = df.index[mask]
```