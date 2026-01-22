A **standard Python library** for handling **command-line arguments**

```
import argparse
```

Example:

```
parser = argparse.ArgumentParser(description="Train a model")
parser.add_argument("--epochs", type=int, default=10)
parser.add_argument("--lr", type=float, default=0.001)

args = parser.parse_args()
```

In command prompt:

```
python train.py --epochs 50 --lr 0.01
```

Assigns:

```
args.epochs == 50
args.lr == 0.01
```