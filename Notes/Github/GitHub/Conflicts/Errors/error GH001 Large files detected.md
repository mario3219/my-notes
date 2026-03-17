Remove the large file from being tracked in recent commit
```
git rm --cached <file_path>
git commit --amend
git push
```

If it is present in past commit history
```
git filter-repo --path <file_path>
git push origin main --force
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