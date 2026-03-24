```
import torch
import torch.nn as nn

class ConvAutoencoder(nn.Module):
    def __init__(self, latent_dim=128):
        super().__init__()
        self.encoder_cnn = nn.Sequential(
            nn.Conv2d(4, 16, kernel_size=3, stride=2, padding=1),  # (16, 32, 32)
            nn.ReLU(),

            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1), # (32, 16, 16)
            nn.ReLU(),

            nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1), # (64, 8, 8)
            nn.ReLU(),
        )
        self.flatten = nn.Flatten()
        self.encoder_fc = nn.Linear(64 * 8 * 8, latent_dim)

        self.decoder_fc = nn.Linear(latent_dim, 64 * 8 * 8)
        self.decoder_cnn = nn.Sequential(
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2,
                               padding=1, output_padding=1),  # (32, 16, 16)
            nn.ReLU(),

            nn.ConvTranspose2d(32, 16, kernel_size=3, stride=2,
                               padding=1, output_padding=1),  # (16, 32, 32)
            nn.ReLU(),

            nn.ConvTranspose2d(16, 4, kernel_size=3, stride=2,
                               padding=1, output_padding=1),  # (4, 64, 64)
            nn.Sigmoid()  # or remove depending on your normalization
        )

    def encode(self, x):
        x = self.encoder_cnn(x)
        x = self.flatten(x)
        z = self.encoder_fc(x)
        return z

    def decode(self, z):
        x = self.decoder_fc(z)
        x = x.view(-1, 64, 8, 8)
        x = self.decoder_cnn(x)
        return x

    def forward(self, x):
        z = self.encode(x)
        x_recon = self.decode(z)
        return x_recon, z
```