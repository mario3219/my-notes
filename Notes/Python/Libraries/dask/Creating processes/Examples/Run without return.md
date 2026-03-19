
Run processes in parallel that are uncorrelated
```
from dask import delayed
from dask.diagnostics import ProgressBar
import dask

@delayed
def foo(x):
	...
	return y

def process(vals):
	tasks = [foo(p) for p in vals]
	with ProgressBar():
		results = dask.compute(*tasks)
		
```