Remove the large file from being tracked
```
git rm --cached <file_path>
git commit --amend
git push
```

****
Old and more forceful fix

Check status of local commits
```
git status
```

Reset N amount of local commits to the past
```
git reset --soft HEAD~<change this>
```

```
git restore --staged .
git add .
git commit -m "<message>"
git push --force-with-lease origin main
```