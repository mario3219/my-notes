```
np.pad(array, pad_width, mode=...)
```
mode is what values to fill in

Usage
Pad width is shape dependent positioning, and padding left and right of that shape

For example
```
raw.shape = (C,3,H,W)
```
We want to pad H and W left and right and up and down

```
np.pad(raw,
	(
	(0,0),
	(0,0),
	(delta,delta),
	(delta,delta)
	),
	constant_values=0
)
```
So if you don't want to pad in one direction, add as zero