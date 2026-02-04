```
#!/usr/bin/env bash

for arg in "$@"; do
  case $arg in
    file=*)
      file="${arg#file=}"
      ;;
    mode=*)
      mode="${arg#mode=}"
      ;;
    epochs=*)
      epochs="${arg#epochs=}"
      ;;
    *)
      echo "Unknown argument: $arg"
      exit 1
      ;;
  esac
done

echo "file=$file"
echo "mode=$mode"
echo "epochs=$epochs"

```