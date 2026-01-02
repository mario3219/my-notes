```
syms x(t) b a u x0
dsolve(diff(x) == -a*x + b*u, x(0)==x0)
```