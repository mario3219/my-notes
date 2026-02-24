Through lists
```
def list = ["a", "b", "c"]

list.each { item ->
    println item
}
```

Through images in a project
```
def project = getProject()
if (project == null)
    throw new IllegalStateException("No project open")

project.getImageList().each { entry ->
    println entry.getImageName()
}
```

Continue is the same as in python in for/while loops

However, if using each
```
list.each {
    if (it == 5)
        return     // acts like continue
    println it
}
```