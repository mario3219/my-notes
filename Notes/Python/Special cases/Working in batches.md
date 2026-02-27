```
num_batches = (size+batch_size-1) // batch_size
for batch_idx in range(num_batches):
	if batch_idx < num_batches - 1:
		start = batch_idx*batch_size
		end = batch_idx*batch_size+batch_size
	else:
		start = batch_idx*batch_size
		end = size
	y = vals[start:end]
```