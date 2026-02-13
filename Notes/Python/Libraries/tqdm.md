A nice progress bar

Instead of
```
for path in img_paths:
	pass
```

Do
```
from tqdm import tqdm

for path in tqdm(img_paths, desc='Converting tiff to npy'):
	pass
```