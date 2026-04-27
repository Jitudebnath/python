# Import libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Training data (house size in sq ft)
X = np.array([[500], [1000], [1500], [2000], [2500]])

# Target values (price in thousands)
y = np.array([50, 100, 150, 200, 250])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict for new house (1800 sq ft)
new_size = np.array([[1800]])
predicted_price = model.predict(new_size)

# Output
print("Predicted price:", predicted_price[0], "thousand")
