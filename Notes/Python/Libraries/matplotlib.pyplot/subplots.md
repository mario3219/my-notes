```
plt.subplot(2,1,1)
plt.plot(x,y1)
plt.title()

plt.subplot(2,1,2)
plt.plot(x,y2)
plt.title()

plt.tight_layout()
plt.show()
```

****

```
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)
axs[1,1].set_title("Example")
plt.close(fig)
```

Only two
```
fig, axs = plt.subplots(1,2) # 1 row 2 columns
axs[0]...
axs[1]...
```

Layout
```
ax[0,0] ax[0,1]  
ax[1,0] ax[1,1]
```