```
git stash list
```
Example output
```
stash@{0}: WIP on main: abc123 something
stash@{1}: WIP on feature-x: def456 something else
```

Apply
```
git stash apply stash@{1}
```