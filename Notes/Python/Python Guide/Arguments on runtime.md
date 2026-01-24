```
import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--argint", type=int, default=10)
	parser.add_argument("--argstr", type=str, default="test")
	return parser.parse_args()

def main(**args):
	value = args["argint"]

if __name__ == '__main__':
	args = vars(parse_args())
	main(**args)
```

