
[QuPath: script for exporting all annotations in a project + cropping - Usage & Issues - Image.sc Forum](https://forum.image.sc/t/qupath-script-for-exporting-all-annotations-in-a-project-cropping/49616)

```
import qupath.lib.images.writers.ome.OMEPyramidWriter

def server = getCurrentServer()

def baseImageName = getProjectEntry().getImageName()

path = buildFilePath(PROJECT_BASE_DIR, 'ROIsTif')
mkdirs(path)

getAnnotationObjects().eachWithIndex{it, x->
        println("Working on: "+it)
	def roi = it.getROI()
	def requestROI = RegionRequest.createInstance(server.getPath(), 1, roi)
	currentImagePath = buildFilePath(PROJECT_BASE_DIR, 'ROIsTif',baseImageName +it+'_'+ x + '.ome.tif')
	OMEPyramidWriter.writeImage(server, currentImagePath, OMEPyramidWriter.CompressionType.LZW, requestROI)
}
print 'Done!'
```