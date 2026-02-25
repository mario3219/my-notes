Adds manual control on threads and cores

Example
```
from dask import delayed
from dask.distributed import Client
import dask.array as da
import numpy as np

client = Client(n_workers=8, threads_per_worker=1)

@delayed
def per_image_min_max(path):
    x = np.load(path).astype(np.float32)
    return x.min(axis=(0,1)), x.max(axis=(0,1))

global_min, global_max, global_ptp = build_global_min_max_ptp(
    img_paths, per_image_min_max
)

min_vals, max_vals, ptp_vals = da.compute(
    global_min, global_max, global_ptp
)
```

If skipped, dask will handle core and threads automatically to what is readily available