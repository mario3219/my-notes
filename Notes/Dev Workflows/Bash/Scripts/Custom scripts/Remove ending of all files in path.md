```
#!/usr/bin/env bash

for arg in "$@"; do
  case $arg in
    path=*)
      path="${arg#path=}"
      ;;
    subname=*)
      subname="${arg#subname=}"
      ;;
    newsub=*)
      newsub="${arg#newsub=}"
      ;;
  esac
done

for f in "${path}"/*${subname}; do
    mv "$f" "${f/${subname}/${newsub}}"
done
```

```
path: Absolute path, example "/mnt/d/git-repositories/MsC-project/Code/Image2Count/figures", with NO '/' at the end

subname: Trailing substring, so can only catch end of files
newsub: What to replace subname with
```