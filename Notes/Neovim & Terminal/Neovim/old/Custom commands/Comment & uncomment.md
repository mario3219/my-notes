```
command! -range -nargs=1 CommentRange <line1>,<line2>s/^/<args>/
command! -range -nargs=1 UnCommentRange <line1>,<line2>s/^<args>//
```