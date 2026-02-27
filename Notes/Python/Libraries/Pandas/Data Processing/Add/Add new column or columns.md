```
df["cell_count"] = pd.NA
```

```
df = pd.concat(  
	[df, pd.DataFrame(0, index=df.index, columns=missing, dtype=float)],  
	axis=1  
)
```