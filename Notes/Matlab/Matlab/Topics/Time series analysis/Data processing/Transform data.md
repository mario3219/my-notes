```
figure; 
lambda_max = bcNormPlot(y,1);   % See also table 4.6
fprintf('The Box-Cox curve is maximized at %4.2f. This suggests that a sqrt or log-transform might be helpful.\n', lambda_max)
```

```
original  = powerload;
powerload = log( powerload );
```