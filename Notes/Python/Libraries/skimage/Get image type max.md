```
import numpy as np  
  
img = io.imread(path)  
  
dtype_max = np.iinfo(img.dtype).max  
print(dtype_max)
```