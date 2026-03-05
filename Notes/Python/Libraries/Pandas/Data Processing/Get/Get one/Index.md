Index of column
```
label_idx = df.columns.get_loc('column')
```
****
Get index of row where value is equal to x in a specific column
```
row_mask = df['texts'].eq(text)
val = df.loc[row_mask,:]
```
Creates a boolean mask of indexes

Convert to direct indexes:
```
row_idx = row_mask[row_mask].index
```
****
Index of last element
```
df.index[-1]
```