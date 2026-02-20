```
from skimage import io
img = io.imread(path, plugin='tifffile', key=tuple(img_channels))
```
Or skip key img_channels if you dont have indexes for channels