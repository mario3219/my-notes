Get index of column of name
```
label_idx = df.columns.get_loc('column')
```
****
Get index of row in a column of value
```
row_mask = df['texts'].eq(text)
val = df.loc[row_mask,:]
```
This extracts an index mask for column texts for row that is equal to text.

Convert to indexes
```
row_idx = row_mask[row_mask].index
```
****
**Get indexes for elements corresponding to same elements in another container**

```
df
s_targets = pd.Series(["target2", "target4"]) #dtype strings
row_idx = 1
cols_to_update = df.columns.intersection(s_targets)
```
Gives `Index(['target2', 'target4'], dtype='object')`

```
df.loc[row_idx, cols_to_update] += 3
```

If you have a series that is indexed
```
s = pd.Series(vals, index=index_names)
cols_to_update = df.columns.intersection(s.index)
```

