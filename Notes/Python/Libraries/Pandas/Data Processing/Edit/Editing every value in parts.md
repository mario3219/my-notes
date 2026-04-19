```
parts = df_meas["Image"].str.rsplit("_", n=1, expand=True)  
  
df_meas["Image"] = (  
parts[0] + "_ROI_" +  
parts[1].str.split("F").str[-1]  
)
```

Parts is a series of lists, so `parts[0]` gives the first split for every value in that column