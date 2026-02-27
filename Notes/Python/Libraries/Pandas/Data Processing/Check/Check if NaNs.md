All rows/columns
```
# To get mask for all rows
mask = df.isna().all(axis=1)
```
Outputs which indexes of rows that are filled with nans, for example
```
0: False
1: True
...
```

The below will result in a new pandas series, containing only those rows
```
mask = df[df.isna().all(axis=1)]
```
Just switch axis=0 for columns

Switch to indexes in the original dataframe
```
mask = df.iloc[:, col_indices].isna().all(axis=1)
idx = mask[mask].index
```