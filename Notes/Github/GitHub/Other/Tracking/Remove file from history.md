<u>Backup all files</u>

```
git filter-repo --invert-paths --path path/to/large_file

git reflog expire --expire=now --all

git gc --prune=now --aggressive

git push --force
```

Head might be gone

Check:
`git remote -v`

