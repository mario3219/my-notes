Save
```
import pickle  
  
my_list = [1, 2, 3, "cat", "gene"]  
  
with open(save_path, "wb") as f:  
	pickle.dump(my_list, f)
```

Load
```
import pickle 
with open(load_path, "rb") as f:  
	my_list = pickle.load(f)
```

Save as .txt