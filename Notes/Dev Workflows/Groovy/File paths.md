Define new file path
```
def dir = new File(PROJECT_BASE_DIR)
```

Parent file: ```
```
def parent = dir.getParentFile().getAbsolutePath()
```

Relative style
```
def file = new File(PROJECT_BASE_DIR, '../data')
file = f.getCanonicalPath()
```