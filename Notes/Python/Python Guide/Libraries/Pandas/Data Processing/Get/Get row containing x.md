```
% Rows where a column contains a value
df_filtered = df[df.iloc[:, 2] == some_value]

% Rows where any column contains a value
df[df.eq(some_value).any(axis=1)]
```