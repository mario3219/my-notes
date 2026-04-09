The datatype used in ScanPy

Anndata has following variables
```
adata.X: Main matrix (cells x genes)
adata.obs: cell metadata
adata.var: gene metadata
adata.obsm: Multi-dimensional data (eg. spatial coords)
```
You can imagine that obs and var as their own pandas dataframes inside adata, so they can for example be accessed by
```
adata.var['CYTO13']
```

Example
```
counts = np.zeros((df.shape[0], 1))

coordinates = np.column_stack((
    df["Centroid.X.px"].to_numpy(),
    df["Centroid.Y.px"].to_numpy()
))

adata = AnnData(
    X=counts,
    obs=pd.DataFrame(index=[f"cell_{i}" for i in range(df.shape[0])]),
    var=pd.DataFrame(index=["dummy_gene"])
)

adata.obsm["spatial"] = coordinates
```