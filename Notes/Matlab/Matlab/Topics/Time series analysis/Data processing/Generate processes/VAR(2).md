```
rng(1)                                          % Set the seed (just done for the lecture!)
N      = 1000;                                  % Try using a shorter realization.
m      = 2;                                     % Dimension of the VAR-process.
noLags = 10;

% Simulate a VAR(2) process.
A1 = [.5 .4 ; .1 .8];                           % Try changing the AR-polynomials (remember to check for stability!)
A2 = [-.2 -.1 ; .3 .6 ];
e = randn(m, N);
Y = zeros(m, N);
for k=3:N
    Y(:,k) = -A1*Y(:,k-1) -A2*Y(:,k-2) + e(:,k);
end
```