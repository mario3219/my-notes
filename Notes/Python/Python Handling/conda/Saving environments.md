Using conda-forge and conda-pack
```
conda install -c conda-forge conda-pack
```

Activate environment
```
conda activate myenv
```

Pack
```
conda-pack -o myenv.tar.gz
```

Transfer tar to new PC and unpack
```
tar -xzf myenv.tar.gz
./myenv/bin/conda-unpack
```

 ****

Using yml
```
conda env export -n myenv > env.yml
```

```
conda env create -f env.yml
```

```
conda activate myenv
```