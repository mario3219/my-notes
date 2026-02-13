```
import argparse

def parse_args():
	parser = argparse.ArgumentParser(
		description="Describes the code"
	)
	parser.add_argument("--argint", type=int, default=10, help="help for int")
	parser.add_argument("--argstr", type=str, default="test", help="help for str")
	return parser.parse_args()

def main(**args):
	intvalue = args["argint"]
	stringvalue = args["argstr"]

if __name__ == '__main__':
	args = vars(parse_args())
	main(**args)
```

String list
```
    parser.add_argument("--channel_names",nargs='+',type=str, default="")
```

