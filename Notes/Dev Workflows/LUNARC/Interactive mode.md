```
interactive -N 1 --ntasks-per-node=4 -t 60 -A <proj>
```
lu-test in our case is:
```
lu2025-2-104
```

More memory
```
interactive -N 1 --ntasks-per-node=4 -t 60 --mem-per-cpu=10600 -A lu2025-2-104
```