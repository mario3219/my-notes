
**Vertical**
```
command! -nargs=1 VResize execute 'vertical resize ' . float2nr(&columns * <args>)
```

Usage:
```
:VResize 0.8
:VResize 0.7
:VResize 0.5
```


**Horizontal**
```
command! -nargs=1 HResize execute 'resize ' . float2nr(&lines * <args>)
```

Usage:
```
:HResize 0.8
:HResize 0.5   
:HResize 0.3   
```