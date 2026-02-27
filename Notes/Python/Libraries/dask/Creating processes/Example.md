
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

****
<u>The code below doesn't work</u>

```
import dask
import dask.array as da
```

Define a function to run in process
```
def foo(x):
	mn = x.min(x)
	mx = x.max(x)
	return mn, mx
```

Define the processing function
```
def process(vals):
	tasks = [dask.delayed(foo)(p) for p in values]
```
This creates the tasks to run in parallel

```
mins = []
maxs = []
for t in tasks:
	mn, mx = t
	mins.append(mn)
	maxs.append(mx)
```
Create arrays to store the returned values from the parallel process. t is a delayed return from tasks, and is appended to the storage arrays.

Turn the delayed vectors into dask arrays
```
mins_arr = da.stack([da.from_delayed(
					m,
					shape=(np.nan,),
					dtype=np.float32
					)
					for m in mins],
					axis=0)
maxs_arr = da.stack([da.from_delayed(
					m,
					shape=(np.nan,),
					dtype=np.float32
					)
					for m in maxs],
					axis=0)
```
shape defines the dimensions of the array, but is set to an unknown length array of 1D in this example. The stack function stacks all the parallel process delayed returns into shape `(N_images, C)` where C is the amount of processes

```
global_min = mins_arr.min(axis=0)
global_max = maxs_arr.max(axis=0)
global_ptp = global_max - global_min
```
Gets the global from all processes

Up until now, nothing has been computed yet, but these final variables contain the pathways for the delayed returns. Executing the parallel processing will surmount to this final value.

```
min_vals, max_vals, ptp_vals = da.compute(
	global_min, global_max, global_ptp
)
```

All these wrapper processes can also be defined in its own function `parallelexample()` and passed into `da.compute`
```
import dask  
import dask.array as da 
import dask.delayed as delayed 
  
@delayed
def per_image_min_max(path):  
	... 
	return mn, mx  
	 
def parallelexample(img_paths):  
	...
	return global_min, global_max, global_ptp

def global_properties(img_paths)
	return da.compute(img_paths)  
```