```
mif_patch = cell[i].transpose(1, 2, 0) # (H, W, C)
```

If the shape is ``B, C, H, W`
Then `transpose(0, 2, 3, 1)`
`-> B, H, W, C`
Meaning that (x,x,x,x) and place index where you want the dims to be placed