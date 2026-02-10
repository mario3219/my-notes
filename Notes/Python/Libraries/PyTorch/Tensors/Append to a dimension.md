```
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32) 

# Number of zeros to append along dimension 1 
(columns) pad_size = 3 

# Create a zeros tensor with the same number of rows, # but extra columns
zeros_to_append = torch.zeros((x.size(0), pad_size), dtype=x.dtype)

# Concatenate along dimension 1
result = torch.cat((x, zeros_to_append), dim=1)
```