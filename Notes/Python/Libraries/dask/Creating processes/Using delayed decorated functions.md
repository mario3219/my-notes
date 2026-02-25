Instead of
```
tasks = [dask.delayed(per_image_min_max)(p) for p in img_paths]
```

Add @delayed to the function
```
from dask import delayed

@delayed  
def per_image_min_max(path):  
	...  
return mn, mx
```

And instead called as
```
tasks = [per_image_min_max(p) for p in img_paths]
```