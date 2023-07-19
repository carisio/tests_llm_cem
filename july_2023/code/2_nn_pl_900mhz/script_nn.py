import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

# Create sample input data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([3, 5, 7, 9])

# Normalize the input data
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Train the MLP regressor
mlp = MLPRegressor(hidden_layer_sizes=(10, 10))  # Two hidden layers with 10 neurons each
mlp.fit(X_normalized, y)

# Create a new sample for prediction
X_new = np.array([[2, 3]])

# Normalize the new input sample
X_new_normalized = scaler.transform(X_new)

# Make predictions using the trained MLP regressor
prediction = mlp.predict(X_new_normalized)
print("Prediction:", prediction)
