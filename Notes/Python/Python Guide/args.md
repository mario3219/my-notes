**args is a dictionary passed as an argument.

```
def f(**args):
    print(args)
```

```
f(a=1, b=2, test=True)
```

Inside the function:
```
args == {
    "a": 1,
    "b": 2,
    "test": True
}
```