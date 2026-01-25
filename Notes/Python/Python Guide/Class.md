```
class myClass(args):
	def __init__(self):
```
def __init__ is the function that runs when myClass is called somewhere else, it is the constructor function that is called

```
class Child(Parent):
	def __init__(self):
		super().__init__()
```

Here inheritance is used. The child class inherits the constructor of the parent class.