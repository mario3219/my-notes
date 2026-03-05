```
my_list = ["apple", "banana", "cherry"]  
  
with open("output.txt", "w") as f:  
for item in my_list:  
f.write(str(item) + "\n")
```

Will write to a new file, change w to a to append