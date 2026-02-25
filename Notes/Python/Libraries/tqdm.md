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

If you're looping through a generator
```
for path in tqdm(generator(vals), total=total, desc='Converting tiff to npy'):
	pass
```