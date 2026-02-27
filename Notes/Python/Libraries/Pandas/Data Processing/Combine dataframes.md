Stack vertically
```
combined = pd.concat(dfs, axis=0, ignore_index=True)
```

Stack horizontally
```
combined = pd.concat(dfs, axis=1)
```

If all dataframes share the same shape and column names
```
combined = sum(dfs)
```
Or selected columns
```
# dfs = list of DataFrames
base = dfs[0][[dfs[0].columns[0]]].copy()   # keep first column

data = sum(df.iloc[:, 1:] for df in dfs)    # sum everything except col 0

combined = pd.concat([base, data], axis=1)
```