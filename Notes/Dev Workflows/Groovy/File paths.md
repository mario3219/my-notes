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

List of paths to files ending with
```
def dir = new File("/path/to/roi_directory")

List<String> roiPaths = dir
        .listFiles { file -> file.name.toLowerCase().endsWith(".roi") }
        .collect { it.absolutePath }
```