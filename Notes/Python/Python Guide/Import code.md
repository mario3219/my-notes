Import specific functions
```
from src.utils import per_gene_corr, get_bulk_expression
```
Where utils is utils.py

Import all functions
```
from src.utils import *
```

Change script 'current directory'
```
import sys
import os

sys.path.append(<path>)

from src.utils import *
```
This changes the current directory for the script