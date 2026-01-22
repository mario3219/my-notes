```
A  = [ 1 -0.6 0.8 ];
s = 24;
A = conv( A, [ 1 zeros(1,s-1) -1 ] );
y1 = filter( C, 1, e );     y1 = y1(extraN:end);
```