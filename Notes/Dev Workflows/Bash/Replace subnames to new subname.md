```
for f in *_mask.tif; do
    mv "$f" "${f/_mask.tif/.ome.tif}"
done
```
Only targets `_mask.tif` and replaces it with `.ome.tif`.