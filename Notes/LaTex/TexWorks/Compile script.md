Windows
```
taskkill /IM TeXworks /F
pdflatex main.tex
del main.aux main.log main.nav main.out main.snm
```

Bash
```
taskkill.exe /IM TeXworks.exe /F
pdflatex.exe main.tex
TeXworks.exe main.pdf
```