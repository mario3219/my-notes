```
from dask.diagnostics import ProgressBar

with ProgressBar():
    results = dask.compute(*tasks)
```