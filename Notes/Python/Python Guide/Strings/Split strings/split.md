```
test = 'test_string'
strings = test.split('_')
```
Will return `[test, string]`

Split from a direction
```
test = 'test_string_example'
strings = test.rsplit('_',1)
```
Will return `[test_string, example]`
The number 1 decides how many splits, so 2 would lead to
`[test, string, example]`

Remove by trailing numbers
```
import re
re.sub(r'_\d+$', '', name)
```

Meaning that if
```
img_12
img_32
...
```
Will extract only `img`
`_` literal underscore
`\d+` one or more digits
`$` end of string