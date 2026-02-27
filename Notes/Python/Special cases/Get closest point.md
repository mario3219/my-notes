Imagine that you have coordinates in an image. The thing that those coordinates however points to something very small, so because of rounding the coordinates points outside of the object.

```
    _, nearest_idx = distance_transform_edt(
        mask == 0,
        return_indices=True
    )

```
Where mask consists of different values, and zero is background

You set the wanted values to false, and everything else to true. Scipy interprets zeros as targets.

Then you can call the nearest_idx variable.

```
idx = int(mask[
nearest_idx[0, yy, xx],
nearest_idx[1, yy, xx]
    ])
```