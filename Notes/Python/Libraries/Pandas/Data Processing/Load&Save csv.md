Load
```
import pandas as pd

outcome_labels = pd.read_csv('outcome_labels.csv', header=None)
```

Load specific columns
```
df = pd.read_csv("data.csv", usecols=["gene", "expression", "ROI"])
```

Save
```
df.to_csv("out.csv", index=False)
```