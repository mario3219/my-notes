```
extraN = 100;
N  = 100;
e  = randn( N+extraN, 1 );
```

```
rng(0);
sigma2 = 1;
e = sqrt(sigma2) * randn(N,1);
```