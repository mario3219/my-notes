```
from pathlib import Path

parts = ["data", "images", "file.tif"]

path = Path(*parts)
print(path)
```