**Iterate rows**

```
for row in df.itertuples(index=False):
    print(row[0], row[1])
```

Loop selected columns:
```
for row in df[["slide", "roi_id", "count"]].itertuples(index=False):
    process(row.slide, row.roi_id, row.count)
```

****
**Iterate columns**
```
for col in df.columns
```

Iterate column and rows
```
for col in df.columns:
    for idx, val in df[col].items():
        print(f"column={col}, row={idx}, value={val}")
```