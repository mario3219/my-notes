```
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("My Figure Title")
plt.show()
```

```
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title("My Axis Title")
plt.show()
```

For whole figure
```
fig, ax = plt.subplots(2, 1)
fig.suptitle("Overall Figure Title")

ax[0].plot([1, 2, 3])
ax[1].plot([3, 2, 1])

plt.show()
```
