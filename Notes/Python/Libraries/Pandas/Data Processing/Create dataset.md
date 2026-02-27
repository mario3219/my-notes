```
import pandas as pd

data = pd.DataFrame({
        'zone': ['A','B','C','A','C','B','A','D','A','B','C','A'],
        'price': [3,6,12,4,10,5,2,14,3,7,11,4]
    })

# Empty dataset
df = pd.DataFrame(columns=["col1", "col2", "col3"])

# numpy to pandas
df = pd.DataFrame(my_array)
```

Zero filled dataset
```
df = pd.DataFrame(0, index=range(n_rows), columns=cols)
```

Empty filled dataset
```
df = pd.DataFrame(  
np.empty((n_rows, len(cols))),
columns=cols  
)
```

If you already know all the values in a column
```
import pandas as pd

values = ["ROI_1", "ROI_2", "ROI_3"]

df = pd.DataFrame({
    "roi_name": values
})
```