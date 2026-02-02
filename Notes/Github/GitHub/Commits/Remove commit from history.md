Make sure you're clean

```
git status
```

```
git rebase -i 5e5bf3c^
```

Editor will open, pick which commits to keep or drop using **pick** or **drop**

```
drop 5e5bf3c qupath scripts
```

Probably will hit conflicts, run

```
git add -A
git rebase --continue
```

Want to cancel? Run

```
git rebase --abort
```

Otherwise, force push

```
git push --force-with-lease origin main
```