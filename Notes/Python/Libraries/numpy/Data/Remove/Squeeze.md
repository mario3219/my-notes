Removes dimensions with length 1

```
a = np.zeros((1, 374, 374, 1))
b = np.squeeze(a)  
b.shape  
# (374, 374)
```