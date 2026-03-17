Can be needed if following error occurs
```
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Run
```
git remote -v
```
Can be empty, then run
```
git remote add origin https://github.com/mario3219/<repo>.git
```

```
git push -u origin main --force
```