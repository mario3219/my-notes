```
C1 = [ 1 0.4 0 0.6 ];   // MA part
A1 = [ 1 -0.4 0.8 ];    // AR part

// Generate noise
N      = 1000;                                  % Try reducing the number of available samples to N=100. What happens? How many samples do you need to get a white residual even with the true model?
extraN = 100;                                   % Add some intial samples to avoid initiation effects.
e = randn(N+extraN, 1);
```

```
z = filter( C1, 1, e );     // MA process
x = filter( 1, A1, e );     // AR process
c = filter( C1, A1, e );    // ARMA process
```