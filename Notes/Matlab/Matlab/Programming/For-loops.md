```
sum = 0;
for t = 1:1:8
    sum = sum + 1
end
```

For string arrays:
```
for data = {'afdb_1.mat','afdb_2.mat','afdb_3.mat','afdb_4.mat','afdb_5.mat','afdb_6.mat','afdb_7.mat'}
    funcs.plotdata(data{1});
end
```

If passed as argument to a function:
```
% Outside the class file
trainingdata = {'afdb_1.mat','afdb_2.mat','afdb_3.mat','afdb_4.mat','afdb_5.mat','afdb_6.mat','afdb_7.mat'}
func(trainingdata)

% inside class file
for i = 1:length(trainingdata)
    load(trainingdata{i})
end
```
