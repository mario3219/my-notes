```
def foo(p):
	...
	return x,y

def main():
	tasks = [foo(p) for p in ...]
	results = dask.compute(*tasks)
	xs = [x for (x,y) in results]
	ys = [y for (x,y) in results]
```