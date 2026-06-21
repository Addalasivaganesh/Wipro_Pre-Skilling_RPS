import numpy as np

# Step 1: Define class labels
classes = ["Cat", "Dog", "Horse"]

# Step 2: Simulated model output (logits)
# These are raw scores (not probabilities)
logits = np.array([2.5, 1.2, 0.8])

# Step 3: Define Softmax function
def softmax(x):
    # Subtract max(x) for numerical stability
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)

# Step 4: Convert logits → probabilities
probabilities = softmax(logits)

# Step 5: Print results
for i in range(len(classes)):
    print(f"{classes[i]}: {probabilities[i]*100:.2f}%")

# Step 6: Prediction (highest probability)
predicted_class = classes[np.argmax(probabilities)]
print("\nPrediction:", predicted_class)
