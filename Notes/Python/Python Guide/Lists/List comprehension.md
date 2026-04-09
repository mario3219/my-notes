```
file_paths = [file+'.xlsx' for file in files]
```

Several statements
```
for col in sheet:
	for row in col:
		row
```
Equal to
```
[row for col in sheet for row in col]
```
Meaning that the order is the same in list comprehension and for loop, same goes for if statements

```
for col in sheet:
	if col.endswith('X')
		for row in col
			row
```

```
[row for col in sheet if col.endswith('X') for row in col]
```