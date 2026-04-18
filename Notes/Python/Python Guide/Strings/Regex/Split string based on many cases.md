```
parts = re.split(r'ome\.tif|\.tif', filename)
```
Add more cases using
```
...|\.png
```
So for example
```
parts = re.split(r'ome\.tif|\.tif|\.png|\.jpg', filename)
```