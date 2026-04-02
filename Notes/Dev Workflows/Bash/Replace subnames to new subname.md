```
for f in *_mask.tif; do
    mv "$f" "${f/_mask.tif/.ome.tif}"
done
```

![[Pasted image 20260331233654.png]]