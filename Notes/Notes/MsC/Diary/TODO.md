* Find out why marker_embeddings is always of shape 256
* (ON-HOLD) Make preprocessing step
	* Take into account that ROIs can come from different images
	So, the normalization and such should be done per full image, not the cutouts
	How this should be done: Somehow associate cutouts to the same image
	(Currently on hold because im implementing the full dataloader from deepcell)
* Automatic channel names extraction from .xlsx
* Check if mpp is stored in .png masks metadata or if have to use .tif files instead, fix in qupath
* Add batch implementation
* I2C stores cells.npy per ROI, and creates embeddings pt per ROI

**Idea**
* (DONE) Create masks from qupath cell segments
* implement save_embed_data
	* Create a child class to PatchDataset
	* Rewrite PatchDataset to take image and mask paths instead of singular images and paths
	* Add an outher for loop in iter function to pass on one image at a time to the patch_generator
	* In the child class, write the save_embed_data function that initializes the data loader and follows the same procedure as in predict.py