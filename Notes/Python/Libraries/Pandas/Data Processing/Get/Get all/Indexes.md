Index translation mask, imagine you have two data frames where columns in one frame appears in the other, and you want to connect their indexes as pairs

This example has a series containing string values, and their names should appear in the data frame column names.
```
s_targets = pd.Series(["target2", "target4"]) #dtype strings
cols_to_update = df.columns.intersection(s_targets)
```
`cols_to_update` gives an object that connects indexes in your data frame to the series, the object can be used to access corresponding values.
```
df.loc[row_idx, cols_to_update] += 3
```

If the series has index names, these can be used instead
```
s = pd.Series(vals, index=index_names)
cols_to_update = df.columns.intersection(s.index)
```