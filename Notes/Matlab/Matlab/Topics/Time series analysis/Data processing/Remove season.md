Deterministic approach:
```
N = length(data);
X = [ ones(N,1) (1:N)' ];
theV = inv( X'*X )*X'*data;             % This is the least-squares estimate of the trend. More on this later.
z = data - theV(1) - theV(2)*(1:N)';
```

Stochastic approach:
```
sweek = 168; 
sday  = 24;
dayPoly  = [1 zeros(1,sday-1) -1];
weekPoly = [1 zeros(1,sweek-1) -1];
powerload = filter(dayPoly,1,powerload);      powerload = powerload(sday+1:end);
powerload = filter(weekPoly,1,powerload);     powerload = powerload(sweek+1:end);
```
