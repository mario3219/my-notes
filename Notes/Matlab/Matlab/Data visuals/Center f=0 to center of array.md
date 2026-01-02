```
Padd = 1024*4; %100;                                     % Try increasing the zero-padding to 1024.
X = fftshift( abs( fft(x, Padd) ).^2 / N );
```