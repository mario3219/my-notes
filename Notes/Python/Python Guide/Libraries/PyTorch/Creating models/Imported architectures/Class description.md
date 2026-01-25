```
import torch
import torch.nn as nn

class myNN(torch.nn.Module):

	def __init__(self):
		super().__init__()
		self.mode = <mode>
		self.embed_size = <embed>
		self.contrast_size = <contrast>
		self.resnet_model = <resnet>
		self.res = resnet101() #example
		
	def forward(self, data):
		return self.res.forward()
```