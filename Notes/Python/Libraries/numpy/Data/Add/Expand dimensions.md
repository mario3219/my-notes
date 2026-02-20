Add a new dimension
```
c = np.zeros((374, 374))
c.shape
# (374, 374)

d = np.expand_dims(c, axis=0)
d.shape
# (1, 374, 374)
```