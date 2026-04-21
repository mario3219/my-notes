```
genes_to_keep = [...]  # your list of gene names

adata = adata[:, adata.var_names.isin(genes_to_keep)].copy()
```