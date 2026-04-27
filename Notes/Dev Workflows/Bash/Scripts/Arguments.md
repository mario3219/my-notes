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

Usage
```
./script.sh file=data.csv mode=train epochs=50
```

****

List argument
```
./myscript.sh hops 1 2 3 4
```

```
#!/bin/bash

if [[ "$1" == "hops" ]]; then
    shift  # remove "hops"
    hops=("$@")
fi

for h in "${hops[@]}"; do
    echo "Hop: $h"
done
```

```
#!/bin/bash

thres=()

for arg in "$@"; do
  case $arg in
    name=*)
      name="${arg#name=}"
      ;;
    pred_label=*)
      pred_label="${arg#pred_label=}"
      ;;
    train_on=*)
      train_on="${arg#train_on=}"
      ;;
    pred_on=*)
      pred_on="${arg#pred_on=}"
      ;;
    subset_pred_dir=*)
      subset_pred_dir="${arg#subset_pred_dir=}"
      ;;
    gene_filter=*)
      gene_filter="${arg#gene_filter=}"
      ;;
    thres=*)
      IFS=',' read -ra thres <<< "${arg#thres=}"
      ;;
    *)
      echo "Unknown argument: $arg"
      exit 1
      ;;
  esac
done
```

```
./yourscript.sh \
  name=myrun \
  pred_label=labels.csv \
  train_on=cta \
  pred_on=wta \
  subset_pred_dir=wta/raw \
  gene_filter=wta \
  thres=6,8,10,12
```