```
git push --force origin HEAD:main
```

**OBS!** Will destroy commit history!

To keep history:
```
git checkout -b revert-and-edit
git add .
git commit -m "Changes based on earlier commit"

git checkout revert-and-edit
git rebase main
git checkout main
git merge revert-and-edit

git push origin main
```