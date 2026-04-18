Loop through genes
```
for gene in adata.var_names:  
	mean = adata.var.loc[gene, 'mean_expr']  
	var = adata.var.loc[gene, 'var_expr']  
	  
	# do something  
	print(gene, mean, var)
```