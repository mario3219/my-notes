Create mask if indexes are known
```
remove = [1,3,5]
mask = [i in set(remove) for i in range(len(data))]
```

```
lst = ['a', 'b', 'c', 'd', 'e']
mask = [False, True, False, True, False]

result = [x for x, m in zip(lst, mask) if m]

# ['b', 'd']
```