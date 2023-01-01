import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(100)
y = x + np.random.normal(0, 0.1, size=100)

# Fit a linear regression to the data
m, b = np.polyfit(x, y, 1)

# Plot the data and the fitted line
plt.plot(x, y, 'o')
plt.plot(x, m*x + b, '-')
plt.show()