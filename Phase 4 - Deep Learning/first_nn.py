"""
 FIRST NEURAL NETWORK - MNIST Digit Recognition
==================================================

What is MNIST?
--------------
MNIST = Modified National Institute of Standards and Technology

It's the "Hello World" of deep learning:
- 70,000 images of handwritten digits (0-9)
- 28×28 pixels, grayscale
- 60,000 training images
- 10,000 test images

Why MNIST?
- Simple enough to train quickly
- Complex enough to need neural networks
- Perfect for learning!

The Task:
---------
Given a 28×28 image of a digit, classify it as 0, 1, 2, ..., or 9.

This is called "multi-class classification" (10 classes).

Our Approach:
-------------
1. Load and explore the data
2. Preprocess (normalize, reshape)
3. Build a neural network
4. Train and evaluate
5. Visualize predictions
6. Understand what the network learned

Let's build a real neural network!
"""

import numpy as np
import matplotlib.pyplot as plt

# Import TensorFlow and Keras
try:
    import tensorflow as tf
    from tensorflow import keras
    print("=" * 80)
    print("FIRST NEURAL NETWORK - MNIST Digit Recognition")
    print("=" * 80)
    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    print("Please install TensorFlow: pip install tensorflow")
    exit()

# ============================================================
# PART 1: Loading the Dataset
# ============================================================
print("\n PART 1: Loading MNIST Dataset")
print("-" * 80)

print("\nLoading MNIST data (this may take a moment)...")

# Keras includes MNIST dataset!
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

print(f"\n Data loaded successfully!")
print(f"\nDataset shapes:")
print(f"  Training images: {X_train.shape}")
print(f"  Training labels: {y_train.shape}")
print(f"  Test images: {X_test.shape}")
print(f"  Test labels: {y_test.shape}")

print(f"\nWhat this means:")
print(f"  - 60,000 training images")
print(f"  - Each image is 28×28 pixels")
print(f"  - Pixel values range from 0 (black) to 255 (white)")
print(f"  - Labels are digits 0-9")

# Check unique labels
print(f"\nUnique labels: {np.unique(y_train)}")
print(f"Number of classes: {len(np.unique(y_train))}")

# ============================================================
# PART 2: Exploring the Data
# ============================================================
print("\n\n PART 2: Exploring the Data")
print("-" * 80)

# Show first image
print(f"\nFirst training image:")
print(f"  Label: {y_train[0]}")
print(f"  Shape: {X_train[0].shape}")
print(f"  Min pixel value: {X_train[0].min()}")
print(f"  Max pixel value: {X_train[0].max()}")

# Visualize first 25 images
fig, axes = plt.subplots(5, 5, figsize=(10, 10))
fig.suptitle('First 25 MNIST Training Images', fontsize=16, fontweight='bold')

for i, ax in enumerate(axes.flat):
    ax.imshow(X_train[i], cmap='gray')
    ax.set_title(f'Label: {y_train[i]}', fontsize=12)
    ax.axis('off')

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/mnist_samples.png', dpi=150)
print("\n Saved visualization: mnist_samples.png")
print("  Look at the variety! Some digits are clear, others are tricky!")

# Class distribution
print("\n\n Class Distribution:")
unique, counts = np.unique(y_train, out=True)
for digit, count in zip(unique, counts):
    print(f"  Digit {digit}: {count:,} samples ({count/len(y_train)*100:.1f}%)")

plt.figure(figsize=(10, 6))
plt.bar(unique, counts, color='skyblue', edgecolor='black')
plt.xlabel('Digit', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Training Data Distribution', fontsize=14, fontweight='bold')
plt.xticks(unique)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/mnist_distribution.png', dpi=150)
print(" Saved visualization: mnist_distribution.png")
print("  Dataset is well-balanced! Each digit has roughly the same number of samples.")

# ============================================================
# PART 3: Data Preprocessing
# ============================================================
print("\n\n PART 3: Data Preprocessing")
print("-" * 80)

print("""
Why preprocess?
1. Normalization: Scale pixel values to [0, 1]
   - Helps neural networks learn faster
   - Prevents large gradients

2. Reshaping: Flatten 28×28 to 784
   - Dense layers expect 1D input
   - 28 × 28 = 784 features

3. One-hot encoding: Convert labels to vectors
   - Label 3 → [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
   - Needed for multi-class classification
""")

# Normalize pixel values to [0, 1]
print("\n Step 1: Normalizing pixel values")
X_train_normalized = X_train.astype('float32') / 255.0
X_test_normalized = X_test.astype('float32') / 255.0

print(f"  Original range: [{X_train[0].min()}, {X_train[0].max()}]")
print(f"  Normalized range: [{X_train_normalized[0].min():.1f}, {X_train_normalized[0].max():.1f}]")
print(f"   Pixels now in [0, 1] range")

# Flatten images
print("\n Step 2: Flattening images")
X_train_flat = X_train_normalized.reshape(-1, 28*28)
X_test_flat = X_test_normalized.reshape(-1, 28*28)

print(f"  Original shape: {X_train_normalized.shape}")
print(f"  Flattened shape: {X_train_flat.shape}")
print(f"   Each image is now a vector of 784 features")

# One-hot encode labels
print("\n Step 3: One-hot encoding labels")
y_train_onehot = keras.utils.to_categorical(y_train, 10)
y_test_onehot = keras.utils.to_categorical(y_test, 10)

print(f"  Original label: {y_train[0]}")
print(f"  One-hot encoded: {y_train_onehot[0]}")
print(f"   Labels now in one-hot format (shape: {y_train_onehot.shape})")

# ============================================================
# PART 4: Building the Neural Network
# ============================================================
print("\n\n PART 4: Building the Neural Network")
print("-" * 80)

print("""
Architecture Design:
  Input(784) → Dense(128, ReLU) → Dense(64, ReLU) → Dense(10, Softmax)

Layer breakdown:
- Input: 784 neurons (one per pixel)
- Hidden layer 1: 128 neurons with ReLU
  * Learns low-level features (edges, curves)
- Hidden layer 2: 64 neurons with ReLU
  * Learns higher-level features (digit parts)
- Output: 10 neurons with Softmax
  * One neuron per digit
  * Softmax converts to probabilities (sum = 1)

Why Softmax?
- For multi-class classification
- Outputs probabilities for each class
- Largest probability = predicted class
""")

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,), name='hidden1'),
    keras.layers.Dense(64, activation='relu', name='hidden2'),
    keras.layers.Dense(10, activation='softmax', name='output')
])

print("\n Model architecture:")
model.summary()

# Count parameters
print("\n Parameter breakdown:")
print(f"  Layer 1: 784×128 + 128 = {784*128 + 128:,} parameters")
print(f"  Layer 2: 128×64 + 64 = {128*64 + 64:,} parameters")
print(f"  Layer 3: 64×10 + 10 = {64*10 + 10:,} parameters")
print(f"  Total: {model.count_params():,} trainable parameters!")

print("\n Each parameter is a weight the network will learn!")

# ============================================================
# PART 5: Compiling the Model
# ============================================================
print("\n\n PART 5: Compiling the Model")
print("-" * 80)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print(" Model compiled!")
print("\nConfiguration:")
print("  Optimizer: Adam")
print("    - Adaptive learning rate")
print("    - Efficient and popular")
print("    - Works well for most problems")
print("\n  Loss: Categorical Cross-Entropy")
print("    - For multi-class classification")
print("    - Measures difference between predicted and actual probabilities")
print("\n  Metrics: Accuracy")
print("    - Percentage of correct predictions")

# ============================================================
# PART 6: Training the Model
# ============================================================
print("\n\n PART 6: Training the Model")
print("-" * 80)

print("\nTraining parameters:")
print("  Epochs: 10 (how many times to go through entire dataset)")
print("  Batch size: 128 (number of samples per gradient update)")
print("  Validation split: 0.1 (10% of training data for validation)")

print("\n️ Training started...\n")

history = model.fit(
    X_train_flat, y_train_onehot,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)

print("\n Training complete!")

# ============================================================
# PART 7: Evaluating the Model
# ============================================================
print("\n\n PART 7: Evaluating on Test Set")
print("-" * 80)

test_loss, test_accuracy = model.evaluate(X_test_flat, y_test_onehot, verbose=0)

print(f"\n Test Results:")
print(f"  Test Loss: {test_loss:.4f}")
print(f"  Test Accuracy: {test_accuracy*100:.2f}%")
print(f"\n The model correctly classifies {test_accuracy*100:.1f}% of unseen digits!")

if test_accuracy > 0.95:
    print("   Excellent performance! Above 95% accuracy!")
elif test_accuracy > 0.90:
    print("   Good performance! Above 90% accuracy!")
else:
    print("   Could be better. Try adding more layers or training longer!")

# ============================================================
# PART 8: Visualizing Training Progress
# ============================================================
print("\n\n PART 8: Visualizing Training Progress")
print("-" * 80)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Loss curves
ax1.plot(history.history['loss'], label='Training Loss', linewidth=2)
ax1.plot(history.history['val_loss'], label='Validation Loss', linewidth=2)
ax1.set_xlabel('Epoch', fontsize=12)
ax1.set_ylabel('Loss', fontsize=12)
ax1.set_title('Loss Over Time', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# Accuracy curves
ax2.plot(history.history['accuracy'], label='Training Accuracy', linewidth=2)
ax2.plot(history.history['val_accuracy'], label='Validation Accuracy', linewidth=2)
ax2.set_xlabel('Epoch', fontsize=12)
ax2.set_ylabel('Accuracy', fontsize=12)
ax2.set_title('Accuracy Over Time', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/mnist_training_history.png', dpi=150)
print(" Saved visualization: mnist_training_history.png")

print("\n What to look for:")
print("  - Loss should decrease over time")
print("  - Accuracy should increase over time")
print("  - Training and validation curves should be close")
print("  - If validation loss increases while training loss decreases → overfitting!")

# ============================================================
# PART 9: Making Predictions
# ============================================================
print("\n\n PART 9: Making Predictions on New Data")
print("-" * 80)

# Get predictions for test set
predictions = model.predict(X_test_flat[:100], verbose=0)

print("\n Example predictions:\n")
for i in range(5):
    predicted_class = np.argmax(predictions[i])
    confidence = predictions[i][predicted_class] * 100
    actual_class = y_test[i]

    print(f"  Image {i}:")
    print(f"    Predicted: {predicted_class} (confidence: {confidence:.1f}%)")
    print(f"    Actual: {actual_class}")
    print(f"    {' Correct!' if predicted_class == actual_class else ' Wrong!'}")
    print()

# Visualize predictions
fig, axes = plt.subplots(5, 5, figsize=(12, 12))
fig.suptitle('Predictions on Test Set', fontsize=16, fontweight='bold')

for i, ax in enumerate(axes.flat):
    # Get prediction
    pred_probs = predictions[i]
    pred_class = np.argmax(pred_probs)
    actual_class = y_test[i]
    confidence = pred_probs[pred_class] * 100

    # Plot image
    ax.imshow(X_test[i], cmap='gray')

    # Color based on correctness
    color = 'green' if pred_class == actual_class else 'red'

    ax.set_title(f'Pred: {pred_class} ({confidence:.0f}%)\nActual: {actual_class}',
                fontsize=10, color=color, fontweight='bold')
    ax.axis('off')

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/mnist_predictions.png', dpi=150)
print(" Saved visualization: mnist_predictions.png")
print("  Green = correct prediction, Red = wrong prediction")

# ============================================================
# PART 10: Analyzing Errors
# ============================================================
print("\n\n PART 10: Analyzing Errors - Where Did We Go Wrong?")
print("-" * 80)

# Get all predictions
all_predictions = model.predict(X_test_flat, verbose=0)
predicted_classes = np.argmax(all_predictions, axis=1)

# Find misclassified examples
misclassified_indices = np.where(predicted_classes != y_test)[0]
print(f"\n Number of errors: {len(misclassified_indices)} out of {len(y_test)}")
print(f"   Error rate: {len(misclassified_indices)/len(y_test)*100:.2f}%")

# Show some errors
if len(misclassified_indices) > 0:
    print("\n Examples of misclassifications:\n")

    fig, axes = plt.subplots(3, 5, figsize=(12, 8))
    fig.suptitle('Misclassified Examples - These Are Tricky!', fontsize=16, fontweight='bold')

    for i, ax in enumerate(axes.flat):
        if i < len(misclassified_indices) and i < 15:
            idx = misclassified_indices[i]
            pred = predicted_classes[idx]
            actual = y_test[idx]
            confidence = all_predictions[idx][pred] * 100

            ax.imshow(X_test[idx], cmap='gray')
            ax.set_title(f'Predicted: {pred} ({confidence:.0f}%)\nActual: {actual}',
                        fontsize=9, color='red')
            ax.axis('off')

            if i < 3:
                print(f"  Image {i+1}: Predicted {pred}, Actually {actual}")
                print(f"    Confidence: {confidence:.1f}%")
                print(f"     Even humans might struggle with this one!")
                print()
        else:
            ax.axis('off')

    plt.tight_layout()
    plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/mnist_errors.png', dpi=150)
    print(" Saved visualization: mnist_errors.png")
    print("  These are genuinely hard examples! The network did well overall.")

# ============================================================
# PART 11: Confusion Matrix
# ============================================================
print("\n\n PART 11: Confusion Matrix - Detailed Performance")
print("-" * 80)

from sklearn.metrics import confusion_matrix
import seaborn as sns

# Compute confusion matrix
cm = confusion_matrix(y_test, predicted_classes)

# Visualize
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True,
            xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Predicted Label', fontsize=12)
plt.ylabel('True Label', fontsize=12)
plt.title('Confusion Matrix - Where Does the Model Confuse?', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/mnist_confusion_matrix.png', dpi=150)
print(" Saved visualization: mnist_confusion_matrix.png")

print("\n Reading the confusion matrix:")
print("  - Diagonal: Correct predictions")
print("  - Off-diagonal: Confusions")
print("\n  Common confusions:")

# Find most confused pairs
for i in range(10):
    for j in range(10):
        if i != j and cm[i][j] > 20:  # Significant confusion
            print(f"    {i} confused with {j}: {cm[i][j]} times")

# ============================================================
# PART 12: Understanding What the Network Learned
# ============================================================
print("\n\n PART 12: Visualizing What the Network Learned")
print("-" * 80)

print("""
Let's visualize the weights of the first layer!
Each neuron in the first layer learns to detect specific patterns.
""")

# Get weights from first layer
first_layer_weights = model.layers[0].get_weights()[0]  # Shape: (784, 128)
print(f"\nFirst layer weights shape: {first_layer_weights.shape}")
print(f"  784 inputs × 128 neurons = {784*128:,} weights")

# Visualize first 25 neurons
fig, axes = plt.subplots(5, 5, figsize=(10, 10))
fig.suptitle('First Layer Neurons - What Patterns Do They Detect?', fontsize=14, fontweight='bold')

for i, ax in enumerate(axes.flat):
    if i < 25:
        # Reshape weights back to 28×28
        neuron_weights = first_layer_weights[:, i].reshape(28, 28)

        # Normalize for visualization
        neuron_weights = (neuron_weights - neuron_weights.min()) / (neuron_weights.max() - neuron_weights.min())

        ax.imshow(neuron_weights, cmap='viridis')
        ax.set_title(f'Neuron {i}', fontsize=9)
        ax.axis('off')

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/mnist_neuron_weights.png', dpi=150)
print(" Saved visualization: mnist_neuron_weights.png")
print("\n Each neuron learned to detect different patterns!")
print("  - Some detect edges")
print("  - Some detect curves")
print("  - Some detect specific digit features")
print("  - Together, they recognize all digits!")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY THIS MNIST PROJECT MATTERS")
print("=" * 80)
print("""
1. REAL-WORLD PROBLEM:
   - Image classification is everywhere!
   - MNIST is the foundation
   - Same principles apply to:
     * Medical image analysis
     * Facial recognition
     * Self-driving cars
     * Document processing

2. COMPLETE WORKFLOW LEARNED:
    Load data
    Explore and visualize
    Preprocess (normalize, reshape, encode)
    Build architecture
    Compile model
    Train with validation
    Evaluate on test set
    Analyze errors
    Visualize learned features

3. KEY CONCEPTS MASTERED:
    Multi-class classification
    One-hot encoding
    Softmax activation
    Categorical cross-entropy loss
    Train/validation/test split
    Confusion matrix
    Model evaluation

4. PERFORMANCE ACHIEVED:
   - ~97% accuracy with simple network!
   - Only 10 epochs of training
   - Room for improvement (CNNs can hit 99.7%!)

5. DEBUGGING SKILLS:
   - Visualize training curves
   - Analyze errors
   - Confusion matrix shows patterns
   - Understand model limitations

 Results Summary:
   Test Accuracy: ~{test_accuracy*100:.1f}%
   Training Time: ~1-2 minutes
   Parameters: {model.count_params():,}

   This is impressive! A simple network learned to recognize
   handwritten digits with near-human accuracy!

 What's Next?

   IMPROVEMENTS:
   - Add dropout (reduce overfitting)
   - Add batch normalization (faster training)
   - Try different architectures
   - Tune hyperparameters

   BETTER ARCHITECTURE:
   - Use CNNs (Convolutional Neural Networks)
   - CNNs are designed for images
   - Can achieve 99.5%+ accuracy!
   - See cnn_basics.py for details

   TRANSFER LEARNING:
   - Use pre-trained models
   - Fine-tune for your task
   - Save weeks of training time!

 Key Takeaways:

   1. More parameters ≠ Better performance
      - Our simple model works great!
      - Complexity adds training time
      - Start simple, add complexity if needed

   2. Preprocessing matters!
      - Normalization helps learning
      - Proper encoding is crucial
      - Clean data = better results

   3. Validation is essential
      - Detects overfitting early
      - Helps tune hyperparameters
      - Never evaluate on training data!

   4. Analyze errors
      - Shows model limitations
      - Guides improvements
      - Builds intuition

 You've built your first real neural network!
   This is the foundation of modern AI.
   Next: CNNs will take this to the next level!
""")

print("\n First Neural Network Complete!")
print("Next: cnn_basics.py - Convolutional Neural Networks for images")
