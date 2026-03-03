```
#!/bin/bash  
  
for i in {1..5}  
do  
echo "Number: $i"  
done
```

```
Number: 1  
Number: 2  
...  
Number: 5
```
****

```
num_cfolds=10
for ((i=0; i<num_cfolds; i++))
do
    echo "$i"
done
```

****

```
for m in '0' '1' '2';
do
echo "Numer: $i"
done
```

```
fruits = ("apple","banana","mango")
for fruit in "${fruits[@]}"
do
echo "$fruit"
done
```