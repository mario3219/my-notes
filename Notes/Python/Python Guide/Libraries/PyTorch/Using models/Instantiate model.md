```
model = MyModel(
    input_dim=100,
    hidden_dim=256,
    output_dim=10
).to(device)

criterion = nn.CrossEntropyLoss()        # or MSELoss, BCEWithLogitsLoss, etc.
optimizer = optim.Adam(model.parameters(), lr=1e-3)
```

Or alternatively SGD:
```
optimizer = torch.optim.SGD(filter(lambda p: p.requires_grad, model.parameters()),      # Stochastic gradient descent with momentum
                                lr=lr,                                                      # weight_decay = regularization (?)
                                weight_decay=weight_decay,
                                momentum=0.9)
```

You can optimize the optimizer through different scheduler

```
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
```