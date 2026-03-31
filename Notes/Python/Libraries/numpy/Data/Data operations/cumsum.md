```
import numpy as np  
  
x = np.array([  
[1, 2, 3],  
[4, 5, 6]  
]) # shape (2, 3)

np.cumsum(x, axis=1)
```

Axis is 1, cumulative sum of *columns* in each row, so
```
[1, 1+2, 1+2+3]
[4, 4+5, 4+5+6]
```

Result
```
[[1 3 6]
[4 9 15]]
```