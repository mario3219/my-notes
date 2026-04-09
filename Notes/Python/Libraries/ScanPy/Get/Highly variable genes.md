```
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)
```

Will add
```
adata.var['highly_variable']
```
Which is a boolean mask for highly variable rows

Only keep top n genes
`n_top_genes=n`

Threshold
```
min_mean  (remove barely expressed)
max_mean  (remove dominant)
min_disp  (keep over this variability)
```

More parameters
[scanpy.pp.highly_variable_genes — scanpy](https://scanpy.readthedocs.io/en/stable/generated/scanpy.pp.highly_variable_genes.html)

Plot highly variable
```
sc.pl.highly_variable_genes(adata, save=name+'.png', show=False)
```

Example
![[Pasted image 20260409152742.png]]
You use the resulting image to adjust filtering parameters, to keep the genes you want.

Example above:
* Most genes clustered around mean 1.5-2.5
* A tail of dispersion above 1-2
* Outliers with dispersion 8-9

Intuition guideline
```
Low expression + low variance
❌|noise|

High expression + low variance
❌|constant|

Low expression + high variance
⚠️|often noisy|

Moderate expression + high variance
✅|informative|
```