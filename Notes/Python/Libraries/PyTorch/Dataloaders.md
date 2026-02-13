An efficient way of implementing generators

Consider a data structure class, and you want to make a generator from the data associated to it.

```
class dataset():
	def.__init__(data)
		self.data = data
```

You create an iterative function

```
def __iter__(self):
	for sample in data:
		yield sample
```

Now, outside of this class, if you want to generate the samples:

```
dataset = dataset(data)

from torch.utils.data import DataLoader
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)
```

Now you can loop using the dataloader

```
for sample in dataloader:
	print(sample)
```

And all the processing of the data will be called inside the iter function

The dataloader will generate data as batches. So if your batch_size is B large, it will generate a batch of B samples, which means it is calling the iter function B times.