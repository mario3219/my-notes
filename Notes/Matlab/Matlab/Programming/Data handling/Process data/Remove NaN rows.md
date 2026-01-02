```
q = data(:,2); % y axeln i data
t = data(:,1)./10^6; % x axeln i data
dat = [t q];
dat(any(isnan(dat), 2), :) = [];
t = dat(:,1);
q = dat(:,2);
```