```
num_epochs = 20

for epoch in range(num_epochs):
    model.train()   # 🔴 training mode
    running_loss = 0.0

    for x, y in train_loader:
        x = x.to(device)
        y = y.to(device)

        optimizer.zero_grad()      # 1️⃣ clear gradients
        outputs = model(x)         # 2️⃣ forward pass
        loss = criterion(outputs, y)
        loss.backward()            # 3️⃣ backward pass
        optimizer.step()           # 4️⃣ update weights

        running_loss += loss.item()

    scheduler.step()  # optional

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss:.4f}")

```