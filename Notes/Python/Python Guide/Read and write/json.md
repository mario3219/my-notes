Load
```
import json

with open("file.json", "r") as f:
    data = json.load(f)

print(type(data))
```

Save
```
import json

data = {
    "CD3": 0,
    "CD20": 1,
    "PanCK": 2
}

with open("marker2idx.json", "w") as f:
    json.dump(data, f)
```