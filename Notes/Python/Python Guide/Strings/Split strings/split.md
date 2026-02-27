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