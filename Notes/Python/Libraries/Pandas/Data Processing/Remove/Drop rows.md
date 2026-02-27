```
df = df.drop(index=5)
```

If a column contains a value from a list
```
df_filtered = df[~df['Name'].isin(remove_list)].reset_index(drop=True)
```