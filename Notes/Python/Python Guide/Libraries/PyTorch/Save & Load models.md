Save only weights
```
torch.save(model.state_dict(), "model_weights.pth")
```

Save complete model
```
torch.save(model, "complete_model.pth")
```

Load only weights
```
model.load_state_dict(torch.load("model_weights.pth"))
```

Load complete model
```
loaded_model = torch.load("complete_model.pth")
```