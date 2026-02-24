* Make transcripts extraction (label.csv) work for several tifs
* Make image processing more efficient
* The preprocessor handles all images at the same time, but some ROIs are gonna come from different original images. The global properties handling needs to be changed
	* Suggestion, in the image_preprocess function, find all unique image names, and iterate through them, extract relevant paths and pass that through the cell_seg function
****
* (DONE) Make preprocessing process for the whole image as a whole, not per ROI
	* Starts in cell_seg
	* Start to extract characteristics before the segmenting cells loop, by calling get_global_properties
	* What is needed in global properties:
		* min_vals, minima per channel
		(1,1,C)
		* ptp_vals, peak to peak
		(1,1,C)
		* img_max
* (DONE) Fix so data structures are initialized as empty, not zeros
* (DONE?) Fix binary mask exports from QuPath
[Exporting annotations — QuPath 0.6.0 documentation](https://qupath.readthedocs.io/en/stable/docs/advanced/exporting_annotations.html#binary-labeled-images)
* (SKIPPED) Instead of using regionprops, get cell positions using the csv files
* (DONE) Fix groovy script to save detections as labels for later in patch_generator

****

* Find out why marker_embeddings is always of shape 256
* Make preprocessing step
	* Take into account that ROIs can come from different images
	So, the normalization and such should be done per full image, not the cutouts
	How this should be done: Somehow associate cutouts to the same image
	(Currently on hold because im implementing the full dataloader from deepcell)
* (SKIPPED) Automatic channel names extraction from .xlsx
* ( SOLVED) Check if mpp is stored in .png masks metadata or if have to use .tif files instead, fix in qupath
* (DONE) Add batch implementation
* (DONE) I2C stores cells.npy per ROI, and creates embeddings pt per ROI
I2C cells.npy size:
	- (amount of cells, resolution width of ROI, cutout width, cutout width)

**Idea**
* (DONE) Create masks from qupath cell segments
* (DONE) implement save_embed_data
	* (SKIPPED) Create a child class to PatchDataset
	* (DONE) Rewrite PatchDataset to take image and mask paths instead of singular images and paths
	* (DONE) Add an outher for loop in iter function to pass on one image at a time to the patch_generator
	* (SKIPPED) In the child class, write the save_embed_data function that initializes the data loader and follows the same procedure as in predict.py