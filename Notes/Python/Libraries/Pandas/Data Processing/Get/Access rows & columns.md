
<u>PREFERABLY USE ILOC</u>

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

Basic drop and get
```
X = df.drop(columns=['OVERALL_DIAGNOSIS'])
y = df['OVERALL_DIAGNOSIS']
```

If column contains substring
```
col_names = df[[col for col in col_names if slide_name in col]]
```