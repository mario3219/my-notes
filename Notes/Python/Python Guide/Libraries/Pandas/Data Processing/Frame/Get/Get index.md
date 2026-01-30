Get index of column of name
```
label_idx = df.columns.get_loc('column')
```

Get index of row in a column of value
```
row = df.iloc[:,column]
row_index = row[row==value].index[0]
```