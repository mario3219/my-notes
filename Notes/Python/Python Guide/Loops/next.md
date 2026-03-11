Returns first occurrence
```
img_path = next(  
os.path.join(train_dir, p)  
for p in os.listdir(train_dir)  
if p.endswith(".tif")  
)
```