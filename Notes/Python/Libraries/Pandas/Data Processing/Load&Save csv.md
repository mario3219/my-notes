Load
```
import pandas as pd

outcome_labels = pd.read_csv('outcome_labels.csv', header=None)
```

Save
```
df.to_csv("out.csv", index=False)
```