![[Pasted image 20260102080713.png]]
```
% A(z) y(t) = [B(z)/A2(z)] u(t) + [C1(z)/A1(z)] e(t)

C1 = [ 1 0.4 0 0.6 ];
A1 = [ 1 -0.4 0.8 ];
C3 = [ 1 0 0 0.8 ]; 
A3 = [ 1 .9 ];
B  = [ 0 0 2 0 -0.8 ];
A2 = 1;
noLags = 30;    

% Generate the noise and the input signals.
N      = 1000;                                  % Try reducing the number of available samples to N=100. What happens? How many samples do you need to get a white residual even with the true model?
extraN = 100;                                   % Add some intial samples to avoid initiation effects.
z = filter( C1, A1, randn(N+extraN, 1) );       % This is the noise model.
x = filter( C3, A3, randn(N+extraN, 1) );       % This is the input signal.

% Form the output using the filtered input. Remove the initial samples.
u = filter( B, A2, x );                         % This is the influence of the input on the output.
y = u + z;                                      % Form the observed signal.

% Remove the extra samples added to avoid initiation effects.
y = y(extraN:end);                              
x = x(extraN:end);
u = u(extraN:end);
```