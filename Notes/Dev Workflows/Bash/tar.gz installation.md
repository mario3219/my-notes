```
tar -xvzf something.tar.gz
cd something
ls
```

Case A: configure, Makefile
```
./configure
make
sudo make install
```

Or if it fails,
```
cmake .
make
sudo make install
```

Case B: install.sh
```
chmod +x install.sh
./install.sh
```

Case C: Binary file

Example contents
```
mytool
README
```

Then
```
chmod +x mytool
./mytool
```

Case D: Python package
```
pip install .
```