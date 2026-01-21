**Replace**
```
function! ReplaceLiteralPrompt(line1, line2)
  let l:from = input('Replace what: ')
  let l:to   = input('Replace with: ')

  if empty(l:from)
    echoerr 'Replace: "from" cannot be empty'
    return
  endif

  " Escape for literal search + safe replacement
  let l:pat = escape(l:from, '\\/.*$^~[]')
  let l:rep = escape(l:to,   '\\/&')

  execute printf('%d,%ds/\V%s/%s/g', a:line1, a:line2, l:pat, l:rep)
endfunction

command! -range Replace call ReplaceLiteralPrompt(<line1>, <line2>)
```

**Usage**

Whole file:
```
:%Replace
```

Specific lines:
```
:10,20 Replace
```