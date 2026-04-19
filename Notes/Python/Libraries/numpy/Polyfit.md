```
import numpy as np  
import matplotlib.pyplot as plt  
  
# Sample data  
x = np.array([1, 2, 3, 4, 5])  
y = np.array([2, 4, 5, 4, 5])  
  
# Fit line: y = mx + b  
coeffs = np.polyfit(x, y, deg=1)  
m, b = coeffs  
  
# Generate smooth line  
x_fit = np.linspace(x.min(), x.max(), 100)  
y_fit = np.polyval(coeffs, x_fit)  
  
# Plot  
plt.scatter(x, y, label="Data")  
plt.plot(x_fit, y_fit, label=f"Fit: y={m:.2f}x+{b:.2f}")  
plt.legend()  
plt.show()
```