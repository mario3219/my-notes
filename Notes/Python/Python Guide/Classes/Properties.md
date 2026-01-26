Defined using:
```
@property
def myattribute(self):
	return self.attribute
```

myattribute is an attribute belonging to the class. Class attributes are public and can be freely changed. By using the @property decorator, users who make attribute changes will pass through the function instead, thus allowing the developer more control on valid data flow.