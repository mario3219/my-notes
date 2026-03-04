 Git will insert conflict markers inside the file:
![[Pasted image 20260103230201.png]]
Simply open the file, and choose what to keep by deleting manually.

Then
```
git add
```
The resolved conflict file

****

If its a binary file, for example `.bashrc, .workspace.json`, there won't be added markers. Use `git diff` to manually edit those parts.

Or decide to keep yours or remote
```
git checkout --theirs -- path/to/file  
git add path/to/file
```

```
git checkout --ours -- path/to/file  
git add path/to/file
```

Then
```
git commit
```

This will finalize the merge
