Iterates mask positions

![[Pasted image 20260420145145.png]]

Masks are two dimensional arrays where one region is associated with a certain value. In my MsC, every cell were associated with an ID corresponding to the value in the image (hence why darker regions in the image above are not very bright, because the ID is starting from 0)

Regionprops identifies these regions and extracts positions of centroids

```
from skimage.measure import regionprops

mask = np.load(path)
props = regionprops(mask, cache=False)
for prop in props:
	idx = prop.label
    if idx == 0: # skip background 
	    continue
	prop.centroid
```

Where `centroid = row, col`
So in an image
```
centroid[0] = y (row)
centroid[1] = x (column)
```