Instead of having a nested for loop, use generators that uses yield instead

```
def generator(data):
	for sample in data:
		out = process(sample)
		yield out

if __name__=='__main__':
	for sample in generator(data):
		print(sample)
```

Now you can do processing for each sample outside of the for loop, increasing readability

To return which run the generator is on
```
def generator(data):
	for run,sample in enumerate(data, start=1):
		out = process(sample)
		yield run, sample

if __name__=='__main__':
	for run, sample in generator(data):
		print(sample)
		print(run)
```