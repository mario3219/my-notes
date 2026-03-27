```
import re

patterns = [re.compile(p) for p in list]

new_list = [col for col in lib if any(p.search(col) for p in patterns)]
```