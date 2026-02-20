Example
```
import qupath.lib.objects.PathObject
import qupath.lib.roi.interfaces.ROI

def exportCircularROI(imageData, roi, outPath) {
    println "Exporting ROI to ${outPath}"
    // ... implementation ...
}

def roiArea(ROI roi) {
    return roi.getArea()
}
```

Import
```
def utils_path = new File(PROJECT_DIR, 'Image2Count/src/utils/qupath_utils/')

def shell = new GroovyShell(this.class.classLoader, this.binding)

def maskUtils = shell.parse(new File(utils_path, "mask.groovy"))

def positionsUtils = shell.parse(new File(utils_path, "positions.groovy"))

maskUtils.run()
positionsUtils.run()

```