```
syms x y z
f = x+y+z;
solve(f,z)
```

Solve closest to point p:
```
f = @(x) 2*x-5;
fsolve(f,0.1)
```