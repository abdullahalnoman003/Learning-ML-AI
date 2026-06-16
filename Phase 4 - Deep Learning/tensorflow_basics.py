"""
 TENSORFLOW & KERAS BASICS - Professional Deep Learning Tools
================================================================

What is TensorFlow?
-------------------
TensorFlow is Google's open-source deep learning framework.
Think of it as a powerful calculator specifically designed for neural networks!

Why use TensorFlow?
- Handles all the complex math (no manual backpropagation!)
- Runs on GPU/TPU (100x faster than CPU)
- Production-ready (deploy to mobile, web, servers)
- Industry standard (used by Google, Uber, Airbnb, etc.)

What is Keras?
--------------
Keras is a high-level API built into TensorFlow.
- Simple, user-friendly interface
- Write less code, get more done
- Perfect for beginners and experts alike

Think of it this way:
  TensorFlow = The engine (powerful but complex)
  Keras = The steering wheel (easy to use)

What are Tensors?
-----------------
Tensors are multi-dimensional arrays (generalization of matrices):
- 0D tensor = Scalar (just a number)
- 1D tensor = Vector [1, 2, 3]
- 2D tensor = Matrix [[1,2], [3,4]]
- 3D tensor = Cube of numbers (e.g., RGB image)
- 4D tensor = Multiple cubes (e.g., batch of images)

Deep learning is all about transforming tensors!
"""

import numpy as np
import matplotlib.pyplot as plt

# Check TensorFlow installation
try:
    import tensorflow as tf
    from tensorflow import keras
    print("=" * 80)
    print("TENSORFLOW & KERAS BASICS - Your Deep Learning Toolkit")
    print("=" * 80)
    print(f"\n TensorFlow version: {tf.__version__}")
    print(f" Keras version: {keras.__version__}")
    print(f" GPU available: {len(tf.config.list_physical_devices('GPU')) > 0}")
    if len(tf.config.list_physical_devices('GPU')) > 0:
        print(f"   GPU devices: {tf.config.list_physical_devices('GPU')}")
    else:
        print(f"   Running on CPU (slower but works fine for learning!)")
except ImportError:
    print("️  TensorFlow not installed!")
    print("   Install with: pip install tensorflow")
    print("\n   For GPU support: pip install tensorflow-gpu")
    exit()

# ============================================================
# PART 1: Understanding Tensors
# ============================================================
print("\n\n PART 1: Understanding Tensors")
print("-" * 80)

print("""
Tensors are the fundamental data structure in TensorFlow!
Everything is a tensor: inputs, outputs, weights, gradients.
""")

# Creating tensors
print("\n Creating Tensors:")

# Scalar (0D tensor)
scalar = tf.constant(42)
print(f"\nScalar (0D): {scalar}")
print(f"  Shape: {scalar.shape}")
print(f"  Rank: {tf.rank(scalar).numpy()}D")
print(f"  Value: {scalar.numpy()}")

# Vector (1D tensor)
vector = tf.constant([1, 2, 3, 4, 5])
print(f"\nVector (1D): {vector}")
print(f"  Shape: {vector.shape}")
print(f"  Rank: {tf.rank(vector).numpy()}D")

# Matrix (2D tensor)
matrix = tf.constant([[1, 2, 3],
                     [4, 5, 6]])
print(f"\nMatrix (2D):\n{matrix}")
print(f"  Shape: {matrix.shape}  (2 rows, 3 columns)")
print(f"  Rank: {tf.rank(matrix).numpy()}D")

# 3D tensor (like an RGB image!)
tensor_3d = tf.constant([[[1, 2], [3, 4]],
                         [[5, 6], [7, 8]]])
print(f"\n3D Tensor:\n{tensor_3d}")
print(f"  Shape: {tensor_3d.shape}")
print(f"  Rank: {tf.rank(tensor_3d).numpy()}D")

# Random tensors (how we initialize weights!)
print(f"\n\n Random Tensors (for weight initialization):")
random_normal = tf.random.normal(shape=(3, 4), mean=0.0, stddev=1.0)
print(f"\nRandom Normal (3×4):\n{random_normal.numpy()}")
print(f"  Mean: {tf.reduce_mean(random_normal).numpy():.4f}")
print(f"  Std: {tf.math.reduce_std(random_normal).numpy():.4f}")

random_uniform = tf.random.uniform(shape=(2, 3), minval=0, maxval=1)
print(f"\nRandom Uniform (2×3):\n{random_uniform.numpy()}")

# Special tensors
print(f"\n\n Special Tensors:")
zeros = tf.zeros(shape=(2, 3))
print(f"\nZeros:\n{zeros.numpy()}")

ones = tf.ones(shape=(2, 3))
print(f"\nOnes:\n{ones.numpy()}")

identity = tf.eye(3)
print(f"\nIdentity Matrix:\n{identity.numpy()}")

# ============================================================
# PART 2: Tensor Operations
# ============================================================
print("\n\n PART 2: Tensor Operations")
print("-" * 80)

print("""
Neural networks are just sequences of tensor operations!
Let's learn the basic operations.
""")

a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])

print(f"\nTensor a:\n{a.numpy()}")
print(f"\nTensor b:\n{b.numpy()}")

# Element-wise operations
print(f"\n\n Element-wise Operations:")
print(f"\nAddition (a + b):\n{tf.add(a, b).numpy()}")
print(f"\nSubtraction (a - b):\n{tf.subtract(a, b).numpy()}")
print(f"\nMultiplication (a * b) [element-wise]:\n{tf.multiply(a, b).numpy()}")
print(f"\nDivision (a / b):\n{tf.divide(a, b).numpy()}")

# Matrix operations
print(f"\n\n Matrix Operations:")
print(f"\nMatrix Multiplication (a @ b):\n{tf.matmul(a, b).numpy()}")
print(f"  This is THE operation in neural networks!")

print(f"\nTranspose (aᵀ):\n{tf.transpose(a).numpy()}")

# Reduction operations
print(f"\n\n Reduction Operations:")
x = tf.constant([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0]])
print(f"\nTensor x:\n{x.numpy()}")
print(f"\nSum (all elements): {tf.reduce_sum(x).numpy()}")
print(f"Mean (all elements): {tf.reduce_mean(x).numpy():.2f}")
print(f"Max: {tf.reduce_max(x).numpy()}")
print(f"Min: {tf.reduce_min(x).numpy()}")

print(f"\nSum along axis 0 (columns): {tf.reduce_sum(x, axis=0).numpy()}")
print(f"Sum along axis 1 (rows): {tf.reduce_sum(x, axis=1).numpy()}")

# Reshaping
print(f"\n\n Reshaping Tensors:")
original = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"\nOriginal shape {original.shape}:\n{original.numpy()}")

reshaped = tf.reshape(original, shape=(4, 2))
print(f"\nReshaped to (4, 2):\n{reshaped.numpy()}")

flattened = tf.reshape(original, shape=(-1,))
print(f"\nFlattened to 1D: {flattened.numpy()}")
print(f"  Shape: {flattened.shape}")

# ============================================================
# PART 3: Automatic Differentiation (Autograd)
# ============================================================
print("\n\n PART 3: Automatic Differentiation - The Magic of TensorFlow!")
print("-" * 80)

print("""
 This is what makes deep learning frameworks powerful!

In the previous files, we manually calculated gradients.
Now, TensorFlow does it AUTOMATICALLY using GradientTape!

GradientTape "records" operations so it can calculate gradients.
""")

print("\n Example 1: Simple Gradient")
print("  Calculate: f(x) = x², find df/dx at x=3")

x = tf.Variable(3.0)  # Variables are trainable!
print(f"  x = {x.numpy()}")

# Record operations
with tf.GradientTape() as tape:
    y = x ** 2
    print(f"  y = x² = {y.numpy()}")

# Calculate gradient
dy_dx = tape.gradient(y, x)
print(f"  dy/dx = {dy_dx.numpy()}")
print(f"   Correct! The derivative of x² is 2x = 2×3 = 6")

print("\n\n Example 2: Complex Function")
print("  f(x) = 3x² + 2x + 1, find df/dx at x=2")

x = tf.Variable(2.0)
with tf.GradientTape() as tape:
    y = 3*x**2 + 2*x + 1
    print(f"  y = {y.numpy()}")

dy_dx = tape.gradient(y, x)
print(f"  dy/dx = {dy_dx.numpy()}")
print(f"   Correct! df/dx = 6x + 2 = 6×2 + 2 = 14")

print("\n\n Example 3: Multiple Variables (Neural Network!)")
print("  Simulating: Loss = (w₁x₁ + w₂x₂ + b - target)²")

w1 = tf.Variable(0.5)
w2 = tf.Variable(0.3)
b = tf.Variable(0.1)
x1, x2 = 2.0, 3.0
target = 5.0

with tf.GradientTape() as tape:
    prediction = w1*x1 + w2*x2 + b
    loss = (prediction - target) ** 2
    print(f"  Prediction: {prediction.numpy():.2f}")
    print(f"  Loss: {loss.numpy():.4f}")

# Calculate gradients for ALL variables!
gradients = tape.gradient(loss, [w1, w2, b])
print(f"\n  Gradients:")
print(f"    dLoss/dw1 = {gradients[0].numpy():.4f}")
print(f"    dLoss/dw2 = {gradients[1].numpy():.4f}")
print(f"    dLoss/db = {gradients[2].numpy():.4f}")
print(f"   TensorFlow calculated all gradients automatically!")

# ============================================================
# PART 4: Building a Simple Neural Network
# ============================================================
print("\n\n PART 4: Building Your First Neural Network with Keras")
print("-" * 80)

print("""
Keras makes building neural networks incredibly easy!
Three ways to build models:
1. Sequential API (simplest - linear stack of layers)
2. Functional API (flexible - complex architectures)
3. Subclassing (advanced - full control)

Let's start with Sequential!
""")

print("\n Method 1: Sequential API")

# Build the model
model = keras.Sequential([
    keras.layers.Dense(4, activation='relu', input_shape=(2,), name='hidden'),
    keras.layers.Dense(1, activation='sigmoid', name='output')
])

print("\n Model created!")
model.summary()

print("""
Let's break down what we just created:

1. Sequential: Stack layers linearly
2. Dense layer: Fully connected layer (every neuron connects to all previous)
3. input_shape=(2,): Expecting 2 input features
4. Dense(4): Hidden layer with 4 neurons
5. activation='relu': ReLU activation function
6. Dense(1): Output layer with 1 neuron
7. activation='sigmoid': Sigmoid for binary classification (0-1 probability)

Architecture: Input(2) → Dense(4, ReLU) → Dense(1, Sigmoid)
""")

# Visualize architecture
print("\n Model Architecture Visualization:")
print("""
    Input Layer         Hidden Layer        Output Layer
        (2)                 (4)                 (1)
         ●                   ●                   ●
         ●              ●    ●    ●         (sigmoid)
                        ●    ●
                             ●

    [x1, x2]  →  [ReLU activations]  →  [probability]
""")

# Count parameters
total_params = sum([tf.reduce_prod(var.shape).numpy() for var in model.trainable_variables])
print(f"\n Total trainable parameters: {total_params}")
print(f"  Hidden layer: 2×4 weights + 4 biases = 12 parameters")
print(f"  Output layer: 4×1 weights + 1 bias = 5 parameters")
print(f"  Total: 12 + 5 = 17 parameters")

# ============================================================
# PART 5: Compiling and Training
# ============================================================
print("\n\n PART 5: Compiling and Training the Model")
print("-" * 80)

print("""
Before training, we must COMPILE the model:
- Optimizer: How to update weights (e.g., Adam, SGD)
- Loss: What to minimize (e.g., MSE, cross-entropy)
- Metrics: What to track (e.g., accuracy)
""")

# Compile the model
model.compile(
    optimizer='adam',  # Adaptive learning rate optimizer
    loss='binary_crossentropy',  # For binary classification
    metrics=['accuracy']  # Track accuracy
)

print(" Model compiled!")
print("  Optimizer: Adam (smart gradient descent)")
print("  Loss: Binary Cross-Entropy (for 0/1 classification)")
print("  Metrics: Accuracy")

# Create training data (XOR problem!)
print("\n\n Training Data (XOR Problem):")
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_train = np.array([[0], [1], [1], [0]], dtype=np.float32)

print("Inputs → Outputs:")
for i in range(len(X_train)):
    print(f"  {X_train[i]} → {y_train[i][0]}")

# Train the model
print("\n\n️ Training the model...")
history = model.fit(
    X_train, y_train,
    epochs=1000,
    verbose=0,  # Don't print every epoch
    batch_size=4
)

print(f" Training complete!")
print(f"  Final loss: {history.history['loss'][-1]:.6f}")
print(f"  Final accuracy: {history.history['accuracy'][-1]*100:.2f}%")

# Test predictions
print("\n\n Testing Predictions:")
predictions = model.predict(X_train, verbose=0)
for i in range(len(X_train)):
    pred_class = 1 if predictions[i][0] > 0.5 else 0
    print(f"  Input: {X_train[i]} → Predicted: {pred_class} (prob: {predictions[i][0]:.4f}) | Actual: {int(y_train[i][0])}")

# ============================================================
# PART 6: Visualizing Training
# ============================================================
print("\n\n PART 6: Visualizing Training Progress")
print("-" * 80)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Loss curve
ax1.plot(history.history['loss'], linewidth=2, color='blue')
ax1.set_xlabel('Epoch', fontsize=12)
ax1.set_ylabel('Loss', fontsize=12)
ax1.set_title('Training Loss Over Time', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_yscale('log')

# Accuracy curve
ax2.plot(history.history['accuracy'], linewidth=2, color='green')
ax2.set_xlabel('Epoch', fontsize=12)
ax2.set_ylabel('Accuracy', fontsize=12)
ax2.set_title('Training Accuracy Over Time', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_ylim([0, 1.1])

plt.tight_layout()
plt.savefig('keras_training.png', dpi=150)
print(" Saved visualization: keras_training.png")

# ============================================================
# PART 7: Different Layer Types
# ============================================================
print("\n\n PART 7: Common Keras Layers")
print("-" * 80)

print("""
Keras provides many types of layers:

1. DENSE (Fully Connected):
   keras.layers.Dense(units, activation)
   - Every neuron connects to all previous neurons
   - Use for: Most tasks

2. DROPOUT:
   keras.layers.Dropout(rate)
   - Randomly drops neurons during training
   - Use for: Preventing overfitting

3. BATCH NORMALIZATION:
   keras.layers.BatchNormalization()
   - Normalizes activations
   - Use for: Faster training, better performance

4. CONV2D:
   keras.layers.Conv2D(filters, kernel_size)
   - Convolutional layer for images
   - Use for: Image processing (CNNs)

5. LSTM/GRU:
   keras.layers.LSTM(units)
   - Recurrent layers for sequences
   - Use for: Time series, text (RNNs)

6. FLATTEN:
   keras.layers.Flatten()
   - Converts multi-dimensional to 1D
   - Use for: After Conv layers, before Dense

7. EMBEDDING:
   keras.layers.Embedding(vocab_size, embedding_dim)
   - Converts tokens to dense vectors
   - Use for: NLP tasks
""")

# Example with more layers
print("\n Example: Model with Dropout and Batch Normalization")

advanced_model = keras.Sequential([
    keras.layers.Dense(8, activation='relu', input_shape=(4,)),
    keras.layers.BatchNormalization(),  # Normalize activations
    keras.layers.Dropout(0.3),  # Drop 30% of neurons during training
    keras.layers.Dense(4, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(1, activation='sigmoid')
])

advanced_model.summary()
print("\n This model is more robust against overfitting!")

# ============================================================
# PART 8: Saving and Loading Models
# ============================================================
print("\n\n PART 8: Saving and Loading Models")
print("-" * 80)

# Save the model
model_path = '/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/my_first_model.h5'
model.save(model_path)
print(f" Model saved to: {model_path}")
print("  This saves:")
print("  - Architecture (layer structure)")
print("  - Weights (learned parameters)")
print("  - Optimizer state (for resuming training)")

# Load the model
loaded_model = keras.models.load_model(model_path)
print(f"\n Model loaded!")

# Verify it works
test_predictions = loaded_model.predict(X_train, verbose=0)
print(f"\n Testing loaded model:")
for i in range(len(X_train)):
    pred_class = 1 if test_predictions[i][0] > 0.5 else 0
    print(f"  {X_train[i]} → {pred_class}")

# ============================================================
# PART 9: Callbacks
# ============================================================
print("\n\n PART 9: Callbacks - Control Training Process")
print("-" * 80)

print("""
Callbacks let you do things during training:
- Save best model
- Stop early if not improving
- Reduce learning rate when stuck
- Log to TensorBoard
- Custom actions
""")

# Create new model for demonstration
callback_model = keras.Sequential([
    keras.layers.Dense(4, activation='relu', input_shape=(2,)),
    keras.layers.Dense(1, activation='sigmoid')
])
callback_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Define callbacks
early_stop = keras.callbacks.EarlyStopping(
    monitor='loss',
    patience=50,
    restore_best_weights=True,
    verbose=0
)

reduce_lr = keras.callbacks.ReduceLROnPlateau(
    monitor='loss',
    factor=0.5,
    patience=20,
    verbose=0
)

print("Training with callbacks...")
history_callbacks = callback_model.fit(
    X_train, y_train,
    epochs=1000,
    callbacks=[early_stop, reduce_lr],
    verbose=0
)

print(f" Training stopped at epoch {len(history_callbacks.history['loss'])}")
print(f"  Early stopping saved time!")
print(f"  Final accuracy: {history_callbacks.history['accuracy'][-1]*100:.2f}%")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY TENSORFLOW/KERAS MATTERS")
print("=" * 80)
print("""
1. NO MANUAL BACKPROPAGATION:
   - GradientTape calculates ALL gradients automatically
   - You focus on architecture, not calculus
   - Scales to any network depth!

2. PRODUCTION-READY:
   - Deploy to mobile (TensorFlow Lite)
   - Deploy to web (TensorFlow.js)
   - Deploy to servers
   - Used by Google, Uber, Airbnb

3. GPU ACCELERATION:
   - 100x faster training
   - Essential for large models
   - Automatic parallelization

4. KERAS SIMPLICITY:
   - Build models in few lines
   - Clear, readable code
   - Rapid prototyping

5. ECOSYSTEM:
   - TensorBoard: Visualization
   - TF Serving: Production deployment
   - TF Hub: Pre-trained models
   - Huge community

 Key Concepts Mastered:

    Tensors: Multi-dimensional arrays
    Operations: Add, multiply, matmul
    Automatic Differentiation: GradientTape
    Sequential API: Build models easily
    Compile: Optimizer + Loss + Metrics
    Fit: Train the model
    Predict: Make predictions
    Save/Load: Persist models

 The Keras Workflow:

   1. Build: Define architecture
      model = keras.Sequential([...])

   2. Compile: Choose optimizer & loss
      model.compile(optimizer='adam', loss='...')

   3. Train: Fit the model
      model.fit(X_train, y_train, epochs=100)

   4. Evaluate: Test performance
      model.evaluate(X_test, y_test)

   5. Predict: Use the model
      predictions = model.predict(X_new)

 What's Next?
   - Real datasets (MNIST, CIFAR-10)
   - Convolutional Neural Networks (images)
   - Recurrent Neural Networks (sequences)
   - Transfer Learning (use pre-trained models)
   - Advanced architectures (ResNet, BERT)

 Compare to NumPy Implementation:
   NumPy: 200+ lines, manual gradients
   Keras: 10 lines, automatic gradients
   Same result! But Keras is:
   - Faster (GPU support)
   - Easier (less code)
   - Scalable (works for huge networks)

 Best Practices:
    Start simple (Sequential API)
    Use callbacks (early stopping, learning rate scheduling)
    Normalize inputs (mean=0, std=1)
    Use appropriate activation (ReLU for hidden, sigmoid/softmax for output)
    Monitor training (loss & accuracy curves)
    Save best model (ModelCheckpoint callback)
""")

print("\n TensorFlow & Keras Basics Complete!")
print("Next: first_nn.py - Build a real neural network on MNIST!")
