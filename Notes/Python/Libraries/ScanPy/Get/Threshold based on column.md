Threshold genes based on values in a column
```
adata = adata[:, adata.var["SNR"] > threshold].copy()
```