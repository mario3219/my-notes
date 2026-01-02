```
x_0 = 1;
timespan = [0 6];
f = @(t,x) -2*x;
[T,Y] = ode45(f,timespan,x_0);
plot(T,Y)
```

```
f = @(t,x) [x(2); 3*x(1)-7*x(2)];
x0 = [0 1];
timespan = [0 5];
[T,Y] = ode45(f,timespan,x0);
plot(T,Y)
```