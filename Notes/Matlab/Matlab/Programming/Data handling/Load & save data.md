Load data:
```
load 'file'
```

Save data:
```
% Saves data y, u, t to file mydata.mat
save('mydata.mat', 'y', 'u', 't');

% Save to a directory relative to your current folder
save(fullfile(pwd, 'mydata.mat'), 'y', 'u');
```