To be used with for example:
```
for x in object:
```

Formed by for example
```
class CountTo:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(1, self.n + 1):
            yield i
```

Used inside its own class
```
class MyClass:
    def __iter__(self):
        return iter([1, 2, 3])

    def do_something(self):
        it = self.__iter__()
        return list(it)
```