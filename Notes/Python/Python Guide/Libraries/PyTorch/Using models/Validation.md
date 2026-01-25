```
model.eval()    # 🧊 evaluation mode
val_loss = 0.0

with torch.no_grad():   # 🚫 no gradients
    for x, y in val_loader:
        x = x.to(device)
        y = y.to(device)

        outputs = model(x)
        loss = criterion(outputs, y)
        val_loss += loss.item()

print(f"Validation loss: {val_loss:.4f}")
```