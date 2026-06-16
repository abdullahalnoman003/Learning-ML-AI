"""
 BUILDING A NEURAL NETWORK FROM SCRATCH - Understanding Deep Learning
========================================================================

What is a Neural Network?
--------------------------
Think of your brain: billions of neurons connected together, learning patterns.
A neural network mimics this! It's multiple layers of simple units (neurons)
that work together to learn complex patterns.

Why "Deep" Learning?
- "Deep" = Multiple layers
- Each layer learns different levels of features
- Layer 1: Simple patterns (edges, colors)
- Layer 2: Combinations (shapes, textures)
- Layer 3: Complex concepts (faces, objects)

The Architecture:
-----------------
Input Layer → Hidden Layer(s) → Output Layer

Example: Predicting if someone will buy a product
- Input: [age, income, browsing_time]
- Hidden: Learns complex patterns
- Output: [probability of purchase]

Key Concepts We'll Learn:
1. FORWARD PASS: Data flows forward through the network
2. ACTIVATION FUNCTIONS: Add non-linearity (helps learn complex patterns)
3. LOSS: How wrong our predictions are
4. BACKPROPAGATION: Calculate gradients (how to adjust weights)
5. GRADIENT DESCENT: Update weights to improve predictions

The Math (Simplified):
----------------------
For each layer:
  z = weights @ inputs + bias    (linear transformation)
  a = activation(z)               (add non-linearity)

Don't worry if this seems complex! We'll build it step by step.
"""

import numpy as np
import matplotlib.pyplot as plt

print("=" * 80)
print("BUILDING A NEURAL NETWORK FROM SCRATCH - Understanding Deep Learning")
print("=" * 80)

# ============================================================
# PART 1: Activation Functions
# ============================================================
print("\n PART 1: Understanding Activation Functions")
print("-" * 80)

print("""
 Why do we need activation functions?

Without them, our neural network is just multiple linear transformations.
Multiple linear transformations = One big linear transformation!
This means the network can only learn LINEAR patterns.

Activation functions add NON-LINEARITY, allowing networks to learn complex patterns!

Common Activation Functions:
""")

def sigmoid(z):
    """
    Sigmoid: Squashes values between 0 and 1
    Used for: Binary classification, output probabilities
    Range: (0, 1)
    """
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    """Derivative of sigmoid for backpropagation"""
    return sigmoid(z) * (1 - sigmoid(z))

def relu(z):
    """
    ReLU (Rectified Linear Unit): If positive, keep it; if negative, make it 0
    Used for: Hidden layers (most popular!)
    Range: [0, ∞)
    Fast and effective!
    """
    return np.maximum(0, z)

def relu_derivative(z):
    """Derivative of ReLU for backpropagation"""
    return (z > 0).astype(float)

def tanh(z):
    """
    Tanh: Squashes values between -1 and 1
    Used for: Hidden layers (centered around 0)
    Range: (-1, 1)
    """
    return np.tanh(z)

def tanh_derivative(z):
    """Derivative of tanh for backpropagation"""
    return 1 - np.tanh(z) ** 2

# Visualize activation functions
x = np.linspace(-5, 5, 100)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(x, sigmoid(x), 'b-', linewidth=2, label='Sigmoid')
plt.grid(True, alpha=0.3)
plt.title('Sigmoid Activation', fontweight='bold')
plt.xlabel('Input')
plt.ylabel('Output')
plt.legend()
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)

plt.subplot(1, 3, 2)
plt.plot(x, relu(x), 'r-', linewidth=2, label='ReLU')
plt.grid(True, alpha=0.3)
plt.title('ReLU Activation', fontweight='bold')
plt.xlabel('Input')
plt.ylabel('Output')
plt.legend()
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)

plt.subplot(1, 3, 3)
plt.plot(x, tanh(x), 'g-', linewidth=2, label='Tanh')
plt.grid(True, alpha=0.3)
plt.title('Tanh Activation', fontweight='bold')
plt.xlabel('Input')
plt.ylabel('Output')
plt.legend()
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/activation_functions.png', dpi=150)
print(" Saved visualization: activation_functions.png")

print("\nKey differences:")
print("  • Sigmoid: Good for output layer (probabilities)")
print("  • ReLU: Most popular for hidden layers (fast, effective)")
print("  • Tanh: Like sigmoid but centered at 0")

# ============================================================
# PART 2: Creating Training Data
# ============================================================
print("\n\n PART 2: Creating Training Data - XOR Problem")
print("-" * 80)

print("""
The XOR (Exclusive OR) Problem:
- A classic problem that CANNOT be solved by linear models
- Perfect for demonstrating neural network power!

XOR Truth Table:
  Input 1  |  Input 2  |  Output
  ---------|-----------|--------
     0     |     0     |    0
     0     |     1     |    1
     1     |     0     |    1
     1     |     1     |    0

Notice: Output is 1 only when inputs are DIFFERENT
This is NOT linearly separable! (Try drawing a line to separate them!)
""")

# XOR dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

print(f"Training data shape: {X.shape}")
print(f"Labels shape: {y.shape}")
print(f"\nDataset:")
for i in range(len(X)):
    print(f"  Input: {X[i]} → Output: {y[i][0]}")

# Visualize XOR problem
plt.figure(figsize=(8, 8))
colors = ['red' if label == 0 else 'blue' for label in y.flatten()]
plt.scatter(X[:, 0], X[:, 1], c=colors, s=500, alpha=0.6, edgecolors='black', linewidth=2)
for i, (x_val, y_val) in enumerate(X):
    plt.annotate(f'({x_val},{y_val}) → {y[i][0]}',
                xy=(x_val, y_val),
                xytext=(10, 10),
                textcoords='offset points',
                fontsize=12,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.5))
plt.xlabel('Input 1', fontsize=14, fontweight='bold')
plt.ylabel('Input 2', fontsize=14, fontweight='bold')
plt.title('XOR Problem - Not Linearly Separable!', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)
plt.legend(['Output = 0', 'Output = 1'], loc='upper right')
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/xor_problem.png', dpi=150)
print("\n Saved visualization: xor_problem.png")
print("  Red points (0) and blue points (1) cannot be separated by a single line!")

# ============================================================
# PART 3: Neural Network Class
# ============================================================
print("\n\n PART 3: Building the Neural Network Class")
print("-" * 80)

class NeuralNetwork:
    """
    A simple 2-layer neural network (1 hidden layer)

    Architecture:
      Input (2 neurons) → Hidden (n neurons) → Output (1 neuron)
    """

    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.5):
        """
        Initialize the network with random weights

        Parameters:
        -----------
        input_size: Number of input features
        hidden_size: Number of neurons in hidden layer
        output_size: Number of output neurons
        learning_rate: How fast the network learns
        """
        self.learning_rate = learning_rate

        # Initialize weights randomly (small values near 0)
        # Why random? So each neuron learns different patterns!
        np.random.seed(42)

        # Weights between input and hidden layer
        self.weights_input_hidden = np.random.randn(input_size, hidden_size) * 0.5
        self.bias_hidden = np.zeros((1, hidden_size))

        # Weights between hidden and output layer
        self.weights_hidden_output = np.random.randn(hidden_size, output_size) * 0.5
        self.bias_output = np.zeros((1, output_size))

        print(f"\n Neural Network Initialized!")
        print(f"   Architecture: {input_size} → {hidden_size} → {output_size}")
        print(f"   Learning rate: {learning_rate}")
        print(f"   Total parameters: {self.count_parameters()}")

    def count_parameters(self):
        """Count total trainable parameters"""
        return (self.weights_input_hidden.size + self.bias_hidden.size +
                self.weights_hidden_output.size + self.bias_output.size)

    def forward(self, X):
        """
        FORWARD PASS: Data flows through the network

        Steps:
        1. Input → Hidden Layer (with activation)
        2. Hidden → Output Layer (with activation)

        Returns predictions and intermediate values (needed for backprop)
        """
        # Input to Hidden Layer
        # z = W·X + b (linear transformation)
        self.z_hidden = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        # a = activation(z) (add non-linearity)
        self.a_hidden = sigmoid(self.z_hidden)

        # Hidden to Output Layer
        self.z_output = np.dot(self.a_hidden, self.weights_hidden_output) + self.bias_output
        self.a_output = sigmoid(self.z_output)

        return self.a_output

    def compute_loss(self, y_true, y_pred):
        """
        Binary Cross-Entropy Loss (better than MSE for classification)

        Loss = -[y·log(pred) + (1-y)·log(1-pred)]

        Why this loss?
        - Heavily penalizes confident wrong predictions
        - Works great with sigmoid output
        """
        # Clip predictions to avoid log(0)
        y_pred = np.clip(y_pred, 1e-7, 1 - 1e-7)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss

    def backward(self, X, y):
        """
        BACKPROPAGATION: Calculate gradients

        This is the MAGIC of neural networks!
        We calculate how much each weight contributed to the error,
        then adjust weights in the opposite direction.

        Uses the CHAIN RULE from calculus:
        - Start from output
        - Work backward through each layer
        - Calculate gradient at each step
        """
        m = X.shape[0]  # Number of examples

        # Output layer gradients
        # How much did output layer contribute to error?
        d_output = self.a_output - y  # Derivative of loss w.r.t output

        # Gradients for output layer weights
        d_weights_hidden_output = np.dot(self.a_hidden.T, d_output) / m
        d_bias_output = np.sum(d_output, axis=0, keepdims=True) / m

        # Hidden layer gradients (backpropagate error)
        # How much did hidden layer contribute to error?
        d_hidden = np.dot(d_output, self.weights_hidden_output.T) * sigmoid_derivative(self.z_hidden)

        # Gradients for hidden layer weights
        d_weights_input_hidden = np.dot(X.T, d_hidden) / m
        d_bias_hidden = np.sum(d_hidden, axis=0, keepdims=True) / m

        # Update weights (Gradient Descent)
        # Move in opposite direction of gradient to minimize loss
        self.weights_hidden_output -= self.learning_rate * d_weights_hidden_output
        self.bias_output -= self.learning_rate * d_bias_output
        self.weights_input_hidden -= self.learning_rate * d_weights_input_hidden
        self.bias_hidden -= self.learning_rate * d_bias_hidden

    def train(self, X, y, epochs=10000, print_every=1000):
        """
        Train the network!

        epochs: How many times to go through the entire dataset
        """
        loss_history = []

        print(f"\n️ Training Neural Network...")
        print(f"   Epochs: {epochs}")
        print(f"   Dataset size: {len(X)}")

        for epoch in range(epochs):
            # Forward pass
            predictions = self.forward(X)

            # Calculate loss
            loss = self.compute_loss(y, predictions)
            loss_history.append(loss)

            # Backward pass (update weights)
            self.backward(X, y)

            # Print progress
            if epoch % print_every == 0 or epoch == epochs - 1:
                accuracy = np.mean((predictions > 0.5) == y) * 100
                print(f"   Epoch {epoch:5d}: Loss = {loss:.6f}, Accuracy = {accuracy:.2f}%")

        print("\n Training Complete!")
        return loss_history

    def predict(self, X):
        """Make predictions on new data"""
        predictions = self.forward(X)
        return (predictions > 0.5).astype(int)

print("""
Key Components Explained:

1. FORWARD PASS:
   - Data flows through layers
   - Each layer: linear transformation → activation
   - Produces predictions

2. LOSS FUNCTION:
   - Measures how wrong predictions are
   - Lower loss = better predictions

3. BACKPROPAGATION:
   - Calculate gradients (derivatives)
   - Uses chain rule from calculus
   - Tells us how to adjust each weight

4. GRADIENT DESCENT:
   - Update weights based on gradients
   - Move in direction that reduces loss
   - Learning rate controls step size
""")

# ============================================================
# PART 4: Training the Network
# ============================================================
print("\n\n PART 4: Training on XOR Problem")
print("-" * 80)

# Create and train network
nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1, learning_rate=0.5)
loss_history = nn.train(X, y, epochs=10000, print_every=2000)

# ============================================================
# PART 5: Testing the Network
# ============================================================
print("\n\n PART 5: Testing the Trained Network")
print("-" * 80)

print("\n Testing on training data:")
predictions = nn.predict(X)
for i in range(len(X)):
    pred_prob = nn.forward(X[i:i+1])[0][0]
    print(f"   Input: {X[i]} → Predicted: {predictions[i][0]} (prob: {pred_prob:.4f}) | Actual: {y[i][0]}")

accuracy = np.mean(predictions == y) * 100
print(f"\n Final Accuracy: {accuracy:.2f}%")
print("   The network learned XOR perfectly! ")

# ============================================================
# PART 6: Visualizing Learning Process
# ============================================================
print("\n\n PART 6: Visualizing the Learning Process")
print("-" * 80)

# Plot learning curve
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(loss_history, linewidth=2, color='blue')
plt.xlabel('Epoch', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.title('Learning Curve - Loss Over Time', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Plot log scale to see details
plt.subplot(1, 2, 2)
plt.plot(loss_history, linewidth=2, color='red')
plt.xlabel('Epoch', fontsize=12)
plt.ylabel('Loss (log scale)', fontsize=12)
plt.title('Learning Curve - Log Scale', fontsize=14, fontweight='bold')
plt.yscale('log')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/nn_learning_curve.png', dpi=150)
print(" Saved visualization: nn_learning_curve.png")
print("  Notice how loss decreases rapidly, then stabilizes!")

# ============================================================
# PART 7: Visualizing Decision Boundary
# ============================================================
print("\n\n PART 7: Visualizing Decision Boundary")
print("-" * 80)

# Create a mesh of points
xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 200),
                     np.linspace(-0.5, 1.5, 200))
mesh_input = np.c_[xx.ravel(), yy.ravel()]

# Get predictions for all points
mesh_predictions = nn.forward(mesh_input).reshape(xx.shape)

# Plot decision boundary
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, mesh_predictions, levels=20, cmap='RdYlBu', alpha=0.7)
plt.colorbar(label='Predicted Probability')

# Plot training points
colors = ['red' if label == 0 else 'blue' for label in y.flatten()]
plt.scatter(X[:, 0], X[:, 1], c=colors, s=300, alpha=0.9, edgecolors='black', linewidth=3)

# Add labels
for i, (x_val, y_val) in enumerate(X):
    plt.annotate(f'{y[i][0]}',
                xy=(x_val, y_val),
                ha='center', va='center',
                fontsize=16, fontweight='bold', color='white')

plt.xlabel('Input 1', fontsize=14, fontweight='bold')
plt.ylabel('Input 2', fontsize=14, fontweight='bold')
plt.title('Neural Network Decision Boundary - XOR Problem Solved!', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/nn_decision_boundary.png', dpi=150)
print(" Saved visualization: nn_decision_boundary.png")
print("  The network learned a NON-LINEAR decision boundary!")
print("  Red regions predict 0, blue regions predict 1")

# ============================================================
# PART 8: Understanding What the Network Learned
# ============================================================
print("\n\n PART 8: Understanding What the Hidden Layer Learned")
print("-" * 80)

print("\nHidden layer weights (Input → Hidden):")
print(nn.weights_input_hidden)
print("\nThese weights determine what patterns each hidden neuron detects!")

print("\nOutput layer weights (Hidden → Output):")
print(nn.weights_hidden_output)
print("\nThese weights combine hidden neuron outputs to make final prediction!")

# Analyze hidden layer activations
print("\n Hidden layer activations for each input:")
for i in range(len(X)):
    hidden_activation = nn.forward(X[i:i+1])
    print(f"   Input: {X[i]} → Hidden activations: {nn.a_hidden[0]}")
    print(f"                    → Output: {hidden_activation[0][0]:.4f}")

print("""
 What's happening?
Each hidden neuron learns a different feature!
- Some neurons activate for certain input patterns
- The output layer combines these features
- This allows learning complex, non-linear patterns!
""")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY BUILDING FROM SCRATCH MATTERS")
print("=" * 80)
print("""
1. UNDERSTANDING THE MAGIC:
   - Neural networks are NOT magic - just math!
   - Forward pass: Simple matrix multiplications
   - Backpropagation: Chain rule from calculus
   - Now you know what happens inside PyTorch/TensorFlow!

2. CORE CONCEPTS MASTERED:
    Activation functions add non-linearity
    Forward pass makes predictions
    Loss function measures error
    Backpropagation calculates gradients
    Gradient descent updates weights

3. THE XOR PROBLEM:
   - Proves neural networks can learn non-linear patterns
   - Single layer cannot solve it (try it!)
   - Hidden layer creates new feature space

4. FOUNDATION FOR DEEP LEARNING:
   - Same principles apply to deep networks
   - Just more layers!
   - Modern networks: same forward/backward pattern

5. YOU CAN NOW:
   - Debug neural networks effectively
   - Understand hyperparameters (learning rate, architecture)
   - Know when/why networks fail
   - Appreciate what libraries do for you!

 What's Next?
   - Add more layers (go deeper!)
   - Try different activation functions
   - Implement different optimizers (Adam, RMSprop)
   - Add regularization (dropout, L2)
   - Use real datasets (MNIST, CIFAR-10)
   - Learn TensorFlow/PyTorch (much easier now!)

 Key Takeaway:
   Deep learning is just:
   1. Forward pass (make predictions)
   2. Calculate loss (measure error)
   3. Backward pass (calculate gradients)
   4. Update weights (gradient descent)
   5. Repeat!

   Everything else is optimization and engineering!
""")

print("\n Neural Network from Scratch Complete!")
print("Next: backpropagation.py - Deep dive into the math")
