# Import libraries
from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression

# Create Flask app
app = Flask(__name__)

# Train a simple model
X = np.array([[500], [1000], [1500], [2000], [2500]])
y = np.array([50, 100, 150, 200, 250])

model = LinearRegression()
model.fit(X, y)


# Home route
@app.route("/")
def home():
    return "ML Model is running!"


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Get input value
    size = data["size"]

    # Convert to numpy array
    prediction = model.predict(np.array([[size]]))

    # Return result
    return jsonify({"predicted_price": float(prediction[0])})


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
