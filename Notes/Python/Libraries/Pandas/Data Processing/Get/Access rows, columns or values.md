
By index
```
df.iloc[:, i]
```

By name
```
df.loc[:,'column']
df['column']
```

Get only specific columns
```
data = data[['ROICoordinateY','AOINucleiCount']]
```

By row index and column name vice versa
```
label_idx = df.columns.get_loc('column')
counts.iloc[idx,label_idx]
```

Last element
```
df["col"].iloc[-1]
```

Get column names
```
names = df.columns
```