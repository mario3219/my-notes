```
plt.xlabel("X-label")
plt.ylabel("Y-label")

axs[...].set_xlabel("X-label")
```

Plot against strings in x-axis
```
genes = ["CXCL10","KRT14"]
values = [1,2,3]
x = np.arange(len(genes))

plt.scatter(x,values)
plt.xticks(x,genes)
```

But when using subplots
```
    fig, axs = plt.subplots(1,2)
    axs[0].scatter(x_axis, top_genes["SNR"].values)
    
    axs[0].set_xticks(x_axis)
    axs[0].set_xticklabels(top_genes.index, rotation=90)
```