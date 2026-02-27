Simple add
```
lst = []
lst.append(42)
```

Add several elements
```
a = [1, 2, 3]
b = [4, 5]

c = a+b
```
This creates a new list and allocates memory for it, copies all elements

If you want to add several elements to an existing list
```
a = [1, 2, 3]
b = [4, 5]

a.extend(b)
```