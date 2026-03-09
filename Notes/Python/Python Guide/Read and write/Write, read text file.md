```
my_list = ["apple", "banana", "cherry"]  
  
with open("output.txt", "w") as f:  
for item in my_list:  
f.write(str(item) + "\n")
```

Will write to a new file, change w to a to append

****

**Read**
```
with open("file.txt", "r") as f:
    text = f.read()

print(text)
```

Line by line
```
with open("markers.txt", "r") as f:
    lines = f.readlines()

print(lines)
```