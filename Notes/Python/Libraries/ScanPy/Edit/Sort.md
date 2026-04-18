Sort by column
```
sorted_genes = adata.var.sort_values('SNR', ascending=False)
```
Where "SNR" is the column to sort all genes based on

If you want to reorder adata based on these results
```
adata = adata[:, sorted_genes.index]
```

Keep only top n
```
top_n = 500  
top_genes = adata.var.sort_values('SNR', ascending=False).head(top_n)
```