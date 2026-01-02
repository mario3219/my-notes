```
C  = [ 1 0.6 0 0 0.4 ];
X = abs( polyval(C,w) ).^2;
w  = exp( 1i* linspace(-.5,.5,Padd)*2*pi )';
```