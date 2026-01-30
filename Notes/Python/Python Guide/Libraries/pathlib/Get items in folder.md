```
from pathlib import Path

folder = Path("data")

for item in folder.iterdir():
    print(item)
```