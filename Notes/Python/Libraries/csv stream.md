Good if resizing is expensive in memory

```
import csv

with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["a", "b", "c"])
    writer.writeheader()
    for item in items:
        writer.writerow({"a": a, "b": b, "c": c})
```

If you want to initialize, and append data over time
```
    import csv
    f = open(os.path.join(os.path.dirname(df_path),'test.csv'), 'w',newline="")
    writer = csv.writer(f)
    writer.writerow(df.columns)

        for row in positions.itertuples(index=False):
            writer.writerow(row._asdict())

```

Explicit add row
```
writer.writerow([1, 2, 3])
```

If file doesnt exist
```
open(path, 'w', newline="")
```
If file exists
```
open(path, 'a', newline="")
```