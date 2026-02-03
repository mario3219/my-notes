```
root = os.getcwd()
file = directory
path = os.path.join(root,file)
```

Other directories before root
```
new_path = os.path.join(os.getcwd(), "..", "other_directory")
new_path = os.path.abspath(new_path)
```