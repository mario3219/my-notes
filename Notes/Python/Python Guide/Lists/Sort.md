If the list contains strings with indexing, for example
```
img_1
img_2
...
```

```
def extract_idx(path):
    stem = path.split(os.sep)[-1]
    if '.ome.tif' in stem:
        stem = stem.split('.ome.tif')[0]
    elif '_mask.tif' in stem:
        stem = stem.split('_mask.tif')[0]
    return int(stem.rsplit('_', 1)[1])
    
main():
        img_paths = sorted(
                        ([os.path.join(train_dir,p) for p in os.listdir(train_dir) 
                              if p.startswith(img_name)]
                         +([os.path.join(test_dir,p) for p in os.listdir(test_dir) 
                              if p.startswith(img_name)])
                         )
                    ,key=extract_idx
                    )
```

The key part is extract_idx function, before it is just list comprehensions to form the list of strings. Each string in the list gets passed through extract_idx function, and gets processed in some way. You customize extract_idx in however way you want to get the indexing value.