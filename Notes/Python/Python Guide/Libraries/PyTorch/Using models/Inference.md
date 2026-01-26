```
model.eval()

with torch.no_grad():
    x = x.to(device)
    outputs = model(x)

    predictions = torch.argmax(outputs, dim=1)
```

Or to get probabilities:
```
probs = torch.softmax(outputs, dim=1)
```