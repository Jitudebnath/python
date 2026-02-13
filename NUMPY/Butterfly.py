import numpy as np
import matplotlib.pyplot as plt

# Create theta values
theta = np.linspace(0, 2 * np.pi, 1000)

# Butterfly curve equation
r = (
    np.exp(np.sin(theta))
    - 2 * np.cos(4 * theta)
    + (np.sin((2 * theta - np.pi) / 24)) ** 5
)

# Convert polar to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot butterfly wings
plt.figure(figsize=(8, 8))
plt.plot(x, y, color="orange", linewidth=2)

# Fill wings with gradient-like effect
plt.fill_between(x, y, color="gold", alpha=0.7)

# Add body (vertical line)
plt.plot([0, 0], [-2, 2], color="black", linewidth=4)

# Add antennae
plt.plot([0, 0.5], [2, 3], color="black", linewidth=2)
plt.plot([0, -0.5], [2, 3], color="black", linewidth=2)

# Title
plt.title("Butterfly Curve 🦋", fontsize=16)

# Remove axes for cleaner look
plt.axis("off")
plt.show()
