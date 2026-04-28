Several
```
df[df["Gene"].isin(["FGF17", "DKK1", "MMP7"])]
```

One value
```
df[df["Gene"].eq("FGF17")]
```

If any row contains it
```
(df["Gene"] == "FGF17").any()
```