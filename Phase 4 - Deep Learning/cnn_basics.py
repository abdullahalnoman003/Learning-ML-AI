"""
NOTE: IF YOU HAVE PYTHON VERSION GRETER THEN 3.12 THEN USE THIS METHOD BECAUSE TENSORFLOW DOSENT SUPPORT ON LATEST VERSION OF PYTHON

️ CONVOLUTIONAL NEURAL NETWORKS (CNN) - Deep Learning for Images

===================================================================

What is a CNN?
--------------
Convolutional Neural Networks are specifically designed for image data!

Regular neural networks treat images as flat vectors → lose spatial information
CNNs preserve spatial relationships → understand images better!

Why CNNs for Images?
--------------------
1. SPATIAL STRUCTURE: Images have local patterns
   - Edges, textures, shapes are nearby pixels
   - CNNs learn these local patterns

2. PARAMETER EFFICIENCY:
   - Regular NN on 28×28 image: 784 inputs
   - Regular NN on 224×224 color image: 150,528 inputs!
   - CNNs use shared weights → far fewer parameters

3. TRANSLATION INVARIANCE:
   - Cat in top-left corner = same as cat in bottom-right
   - CNNs learn this automatically

Key Concepts:
-------------
1. CONVOLUTION: Slide a filter over image to detect features
2. POOLING: Downsample to reduce size and capture important features
3. FILTERS/KERNELS: Small matrices that detect patterns
4. FEATURE MAPS: Output of convolution operations

CNN Architecture:
-----------------
Input Image → Conv → ReLU → Pool → Conv → ReLU → Pool → Flatten → Dense → Output

Let's build one and see how it works!
"""

import numpy as np
import matplotlib.pyplot as plt

try:
    import tensorflow as tf
    from tensorflow import keras
    print("=" * 80)
    print("CONVOLUTIONAL NEURAL NETWORKS (CNN) - Computer Vision")
    print("=" * 80)
    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    print("Please install TensorFlow: pip install tensorflow")
    exit()

# ============================================================
# PART 1: Understanding Convolution
# ============================================================
print("\n PART 1: Understanding Convolution Operation")
print("-" * 80)

print("""
Convolution = Sliding a filter over an image

Example: Edge Detection Filter

Filter (3×3):          Image (5×5):
 [-1  0  1]            [10 10 10 50 50]
 [-1  0  1]            [10 10 10 50 50]
 [-1  0  1]            [10 10 10 50 50]
                       [10 10 10 50 50]
                       [10 10 10 50 50]

The filter slides over the image, computing dot products.
This particular filter detects vertical edges!
""")

# Create a simple image with a vertical edge
simple_image = np.zeros((5, 5))
simple_image[:, :3] = 10  # Left side
simple_image[:, 3:] = 50  # Right side

print("\nSimple Image (with vertical edge):")
print(simple_image.astype(int))

# Define edge detection filter
edge_filter = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]])

print("\nEdge Detection Filter:")
print(edge_filter)

# Manual convolution (simplified - one position)
print("\n Manual Convolution Example:")
print("  Placing filter at position (1, 1):")

# Extract 3x3 patch
patch = simple_image[0:3, 0:3]
print(f"\n  Image patch:\n{patch.astype(int)}")

# Compute dot product
result = np.sum(patch * edge_filter)
print(f"\n  Filter:\n{edge_filter}")
print(f"\n  Element-wise multiply and sum: {result}")
print(f"   This value indicates edge strength!")

# Visualize
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].imshow(simple_image, cmap='gray')
axes[0].set_title('Original Image\n(Vertical Edge)', fontsize=12, fontweight='bold')
axes[0].axis('off')

axes[1].imshow(edge_filter, cmap='RdBu', vmin=-1, vmax=1)
axes[1].set_title('Edge Detection Filter\n(3×3 Kernel)', fontsize=12, fontweight='bold')
axes[1].axis('off')

# Apply convolution using TensorFlow
image_4d = simple_image.reshape(1, 5, 5, 1).astype(np.float32)
filter_4d = edge_filter.reshape(3, 3, 1, 1).astype(np.float32)
conv_result = tf.nn.conv2d(image_4d, filter_4d, strides=1, padding='VALID')
axes[2].imshow(conv_result[0, :, :, 0], cmap='gray')
axes[2].set_title('After Convolution\n(Edges Detected!)', fontsize=12, fontweight='bold')
axes[2].axis('off')

plt.tight_layout()
plt.savefig('convolution_example.png', dpi=150)
print("\n Saved visualization: convolution_example.png")
print("  The bright pixels show where edges were detected!")

# ============================================================
# PART 2: CNN Layer Types
# ============================================================
print("\n\n PART 2: CNN Layer Types")
print("-" * 80)

print("""
1. CONVOLUTIONAL LAYER (Conv2D):
   - Applies filters to detect features
   - Parameters: number of filters, kernel size
   - Example: Conv2D(32, (3,3))
     → 32 filters, each 3×3 pixels
   - Each filter learns a different pattern!

2. ACTIVATION (usually ReLU):
   - Add non-linearity
   - ReLU(x) = max(0, x)
   - Allows learning complex patterns

3. POOLING LAYER (MaxPooling2D):
   - Downsamples feature maps
   - Reduces spatial dimensions
   - Makes model translation-invariant
   - Example: MaxPooling2D((2,2))
     → Takes max value in each 2×2 region

4. FLATTEN:
   - Converts 2D feature maps to 1D vector
   - Connects CNN layers to Dense layers

5. DENSE (Fully Connected):
   - Regular neural network layer
   - Makes final classification decision
""")

# Demonstrate pooling
print("\n Max Pooling Example:")
example_map = np.array([[1, 3, 2, 4],
                        [5, 6, 7, 8],
                        [9, 2, 3, 1],
                        [4, 5, 6, 7]])
print("  Original 4×4 feature map:")
print(example_map)

print("\n  After 2×2 Max Pooling:")
print("  [Take maximum in each 2×2 block]")
pooled = tf.nn.max_pool2d(example_map.reshape(1, 4, 4, 1).astype(np.float32),
                          ksize=2, strides=2, padding='VALID')
print(pooled[0, :, :, 0].numpy().astype(int))
print("  Size reduced from 4×4 to 2×2!")
print("   Keeps important features, reduces computation")

# ============================================================
# PART 3: Loading MNIST Data
# ============================================================
print("\n\n PART 3: Loading and Preparing Data")
print("-" * 80)

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
print(f" MNIST data loaded")
print(f"   Training: {X_train.shape}")
print(f"   Test: {X_test.shape}")

# Preprocess for CNN
print("\n Preprocessing for CNN:")

# Reshape to add channel dimension
X_train_cnn = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
X_test_cnn = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

print(f"  Reshaped: {X_train_cnn.shape}")
print(f"  (samples, height, width, channels)")
print(f"  Channels = 1 (grayscale)")
print(f"  For RGB images, channels = 3!")

# One-hot encode labels
y_train_cnn = keras.utils.to_categorical(y_train, 10)
y_test_cnn = keras.utils.to_categorical(y_test, 10)
print(f"\n  Labels one-hot encoded: {y_train_cnn.shape}")

# ============================================================
# PART 4: Building a CNN
# ============================================================
print("\n\n PART 4: Building Our First CNN")
print("-" * 80)

print("""
Architecture:
  Input (28×28×1)
  ↓
  Conv2D(32 filters, 3×3) + ReLU
  ↓
  MaxPooling2D(2×2)
  ↓
  Conv2D(64 filters, 3×3) + ReLU
  ↓
  MaxPooling2D(2×2)
  ↓
  Flatten
  ↓
  Dense(128) + ReLU
  ↓
  Dropout(0.5)
  ↓
  Dense(10) + Softmax

Why this architecture?
- First Conv: Detects simple features (edges, curves)
- Second Conv: Detects complex features (digit parts)
- Pooling: Reduces size, captures important features
- Dense: Combines features for classification
- Dropout: Prevents overfitting
""")

cnn_model = keras.Sequential([
    # First Convolutional Block
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), name='conv1'),
    keras.layers.MaxPooling2D((2, 2), name='pool1'),

    # Second Convolutional Block
    keras.layers.Conv2D(64, (3, 3), activation='relu', name='conv2'),
    keras.layers.MaxPooling2D((2, 2), name='pool2'),

    # Dense Layers
    keras.layers.Flatten(name='flatten'),
    keras.layers.Dense(128, activation='relu', name='dense1'),
    keras.layers.Dropout(0.5, name='dropout'),
    keras.layers.Dense(10, activation='softmax', name='output')
])

print("\n CNN Model Architecture:")
cnn_model.summary()

print("\n Size transformations through network:")
print("  Input:        (28, 28, 1)")
print("  After Conv1:  (26, 26, 32)  [3×3 filter reduces size]")
print("  After Pool1:  (13, 13, 32)  [2×2 pooling halves size]")
print("  After Conv2:  (11, 11, 64)")
print("  After Pool2:  (5, 5, 64)")
print("  After Flatten: (1600,)      [5×5×64 = 1600]")
print("  After Dense:  (128,)")
print("  Output:       (10,)         [10 classes]")

print(f"\n Total parameters: {cnn_model.count_params():,}")
print("   Much more efficient than fully connected!")

# ============================================================
# PART 5: Training the CNN
# ============================================================
print("\n\n PART 5: Training the CNN")
print("-" * 80)

cnn_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print(" Model compiled")
print("\n️ Training CNN (this takes a bit longer than regular NN)...\n")

# Add callbacks
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True,
    verbose=1
)

history = cnn_model.fit(
    X_train_cnn, y_train_cnn,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    callbacks=[early_stop],
    verbose=1
)

print("\n Training complete!")

# ============================================================
# PART 6: Evaluating CNN Performance
# ============================================================
print("\n\n PART 6: Evaluating CNN Performance")
print("-" * 80)

test_loss, test_accuracy = cnn_model.evaluate(X_test_cnn, y_test_cnn, verbose=0)

print(f"\n Test Results:")
print(f"  Test Loss: {test_loss:.4f}")
print(f"  Test Accuracy: {test_accuracy*100:.2f}%")

print(f"\n CNN Performance:")
print(f"  Regular NN: ~97% accuracy")
print(f"  CNN: ~{test_accuracy*100:.1f}% accuracy")
print(f"  Improvement: ~{(test_accuracy - 0.97)*100:.1f}% better!")
print(f"\n CNNs are significantly better for image tasks!")

# Visualize training
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(history.history['loss'], label='Training Loss', linewidth=2)
ax1.plot(history.history['val_loss'], label='Validation Loss', linewidth=2)
ax1.set_xlabel('Epoch', fontsize=12)
ax1.set_ylabel('Loss', fontsize=12)
ax1.set_title('CNN Training Loss', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

ax2.plot(history.history['accuracy'], label='Training Accuracy', linewidth=2)
ax2.plot(history.history['val_accuracy'], label='Validation Accuracy', linewidth=2)
ax2.set_xlabel('Epoch', fontsize=12)
ax2.set_ylabel('Accuracy', fontsize=12)
ax2.set_title('CNN Training Accuracy', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('cnn_training_history.png', dpi=150)
print("\n Saved visualization: cnn_training_history.png")

# ============================================================
# PART 7: Visualizing Learned Filters
# ============================================================
print("\n\n PART 7: Visualizing What the CNN Learned")
print("-" * 80)

print("\n First Convolutional Layer Filters:")

# Get filters from first conv layer
filters, biases = cnn_model.layers[0].get_weights()
print(f"  Filter shape: {filters.shape}")
print(f"  (3×3 kernel, 1 input channel, 32 output filters)")

# Normalize filters for visualization
f_min, f_max = filters.min(), filters.max()
filters_normalized = (filters - f_min) / (f_max - f_min)

# Visualize first 32 filters
fig, axes = plt.subplots(4, 8, figsize=(12, 6))
fig.suptitle('First Layer Filters - What Patterns Do They Detect?', fontsize=14, fontweight='bold')

for i, ax in enumerate(axes.flat):
    if i < 32:
        # Get the i-th filter
        f = filters_normalized[:, :, 0, i]
        ax.imshow(f, cmap='viridis')
        ax.set_title(f'F{i}', fontsize=8)
        ax.axis('off')

plt.tight_layout()
plt.savefig('cnn_filters.png', dpi=150)
print(" Saved visualization: cnn_filters.png")
print("  Each filter learned to detect different patterns!")
print("  Edges, curves, orientations, etc.")

# ============================================================
# PART 8: Visualizing Feature Maps
# ============================================================
print("\n\n PART 8: Visualizing Feature Maps (Activations)")
print("-" * 80)

print("""
Feature maps = outputs of convolutional layers
They show what the CNN "sees" at each layer!
""")

# Create a model that outputs intermediate layers
layer_outputs = [layer.output for layer in cnn_model.layers[:4]]  # First 4 layers
activation_model = keras.models.Model(inputs=cnn_model.input, outputs=layer_outputs)

# Get activations for a test image
test_image = X_test_cnn[0:1]
print(f"\nTest digit: {y_test[0]}")

activations = activation_model.predict(test_image, verbose=0)

# Visualize
fig = plt.figure(figsize=(16, 10))

# Original image
ax = plt.subplot(4, 8, 1)
ax.imshow(test_image[0, :, :, 0], cmap='gray')
ax.set_title('Input\nImage', fontsize=10, fontweight='bold')
ax.axis('off')

# Conv1 feature maps (show first 7)
print("\n After first convolution (32 feature maps):")
for i in range(7):
    ax = plt.subplot(4, 8, i+2)
    ax.imshow(activations[0][0, :, :, i], cmap='viridis')
    ax.set_title(f'Conv1\nMap {i}', fontsize=8)
    ax.axis('off')

# After pooling
ax = plt.subplot(4, 8, 9)
ax.imshow(activations[1][0, :, :, 0], cmap='viridis')
ax.set_title('Pool1\nMap 0', fontsize=8)
ax.axis('off')

# Conv2 feature maps (show 7)
print(" After second convolution (64 feature maps):")
for i in range(7):
    ax = plt.subplot(4, 8, i+10)
    ax.imshow(activations[2][0, :, :, i], cmap='viridis')
    ax.set_title(f'Conv2\nMap {i}', fontsize=8)
    ax.axis('off')

# After pooling
ax = plt.subplot(4, 8, 17)
ax.imshow(activations[3][0, :, :, 0], cmap='viridis')
ax.set_title('Pool2\nMap 0', fontsize=8)
ax.axis('off')

plt.suptitle(f'Feature Maps Through CNN - Digit {y_test[0]}', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('cnn_feature_maps.png', dpi=150)
print(" Saved visualization: cnn_feature_maps.png")
print("\n Notice how:")
print("  - Early layers detect simple features (edges)")
print("  - Later layers detect complex features (digit parts)")
print("  - Feature maps get smaller but more numerous")

# ============================================================
# PART 9: Comparing CNN vs Regular NN
# ============================================================
print("\n\n PART 9: CNN vs Regular Neural Network")
print("-" * 80)

print("\n Comparison:")
print(f"\n  {'Aspect':<20} | {'Regular NN':<20} | {'CNN':<20}")
print(f"  {'-'*20}-+-{'-'*20}-+-{'-'*20}")
print(f"  {'Input':<20} | {'Flattened (784)':<20} | {'2D Image (28×28)':<20}")
print(f"  {'Spatial Info':<20} | {'Lost':<20} | {'Preserved':<20}")
print(f"  {'Parameters':<20} | {'~100,000':<20} | {'~100,000':<20}")
print(f"  {'Accuracy':<20} | {'~97%':<20} | {'~99%':<20}")
print(f"  {'Training Time':<20} | {'Faster':<20} | {'Slower':<20}")
print(f"  {'Works on Images':<20} | {'OK':<20} | {'Excellent':<20}")

print("\n Key Insights:")
print("   CNNs understand spatial relationships")
print("   CNNs are translation invariant")
print("   CNNs share weights → efficient")
print("   CNNs hierarchical features: simple → complex")

# ============================================================
# PART 10: Real-World CNN Architectures
# ============================================================
print("\n\n PART 10: Famous CNN Architectures")
print("-" * 80)

print("""
 Famous CNN Architectures:

1. LeNet-5 (1998) - Yann LeCun
   - First successful CNN
   - Used for digit recognition
   - 60,000 parameters

2. AlexNet (2012) - Won ImageNet
   - Popularized deep learning
   - 60 million parameters
   - Used ReLU, Dropout, GPU

3. VGGNet (2014)
   - Very deep (16-19 layers)
   - Simple architecture (3×3 conv only)
   - 138 million parameters

4. ResNet (2015) - Microsoft
   - Introduced skip connections
   - Can be 100+ layers deep!
   - Solved vanishing gradient problem

5. Inception/GoogLeNet (2014)
   - Multiple filter sizes in parallel
   - Very efficient

6. MobileNet (2017)
   - Designed for mobile devices
   - Fast and lightweight

7. EfficientNet (2019)
   - State-of-the-art efficiency
   - Scales all dimensions

All follow the same basic principles we learned!
""")

# ============================================================
# PART 11: Advanced CNN Techniques
# ============================================================
print("\n\n PART 11: Advanced CNN Techniques")
print("-" * 80)

print("""
 Advanced Techniques:

1. DATA AUGMENTATION:
   - Rotate, flip, zoom images during training
   - Creates more training data
   - Improves generalization

2. BATCH NORMALIZATION:
   - Normalizes activations
   - Faster training
   - Better performance

3. SKIP CONNECTIONS (ResNet):
   - Connect layers directly
   - Helps gradient flow
   - Enables very deep networks

4. DEPTHWISE SEPARABLE CONVOLUTIONS:
   - More efficient
   - Fewer parameters
   - Used in MobileNet

5. ATTENTION MECHANISMS:
   - Focus on important regions
   - Used in modern architectures
   - Bridge to Transformers

6. TRANSFER LEARNING:
   - Use pre-trained models
   - Fine-tune for your task
   - Saves massive amounts of time!
   - See transfer_learning.py for details
""")

# Demonstrate data augmentation
print("\n Data Augmentation Example:")

data_augmentation = keras.Sequential([
    keras.layers.RandomRotation(0.1),
    keras.layers.RandomZoom(0.1),
    keras.layers.RandomTranslation(0.1, 0.1)
])

# Show augmented images
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
fig.suptitle('Data Augmentation - Creating More Training Data', fontsize=14, fontweight='bold')

original = X_test_cnn[0:1]
for i in range(5):
    axes[0, i].imshow(original[0, :, :, 0], cmap='gray')
    axes[0, i].set_title('Original', fontsize=10)
    axes[0, i].axis('off')

    augmented = data_augmentation(original, training=True)
    axes[1, i].imshow(augmented[0, :, :, 0], cmap='gray')
    axes[1, i].set_title('Augmented', fontsize=10)
    axes[1, i].axis('off')

plt.tight_layout()
plt.savefig('cnn_augmentation.png', dpi=150)
print(" Saved visualization: cnn_augmentation.png")
print("  Same digit, different variations!")
print("  Helps model learn robust features")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY CNNs MATTER")
print("=" * 80)
print("""
1. REVOLUTIONIZED COMPUTER VISION:
   - Image classification
   - Object detection
   - Facial recognition
   - Medical image analysis
   - Self-driving cars
   - Image generation

2. CORE CONCEPTS MASTERED:
    Convolution: Local pattern detection
    Pooling: Spatial downsampling
    Filters: Learned feature detectors
    Feature maps: Hierarchical representations
    Translation invariance
    Parameter sharing

3. PRACTICAL APPLICATIONS:
   - Medical: Detect diseases from X-rays
   - Security: Face recognition
   - Autonomous vehicles: See the world
   - Agriculture: Crop disease detection
   - Manufacturing: Quality control
   - Entertainment: Filters, effects

4. WHY CNNs WORK SO WELL:
   - Preserve spatial structure
   - Learn hierarchical features
   - Translation invariant
   - Parameter efficient
   - Backpropagation works!

5. PERFORMANCE:
   - MNIST: 99%+ accuracy
   - ImageNet: Human-level performance
   - Face recognition: Superhuman accuracy
   - Medical imaging: Assists doctors

 Our Results:
   Regular NN: ~97% accuracy
   CNN: ~99% accuracy
   Same data, better architecture!

 Key Takeaways:

   1. Architecture matters!
      - Right tool for the right job
      - CNNs for images
      - RNNs for sequences
      - Transformers for everything!

   2. Convolution = Feature detection
      - Filters slide over image
      - Detect patterns automatically
      - Learned, not hand-crafted!

   3. Pooling = Dimensionality reduction
      - Keeps important features
      - Reduces computation
      - Makes model robust

   4. Deep = Hierarchical
      - Layer 1: Edges, colors
      - Layer 2: Textures, parts
      - Layer 3: Objects, concepts

 What's Next?

   IMPROVEMENTS:
   - Try deeper networks
   - Add batch normalization
   - Use data augmentation
   - Try different architectures

   ADVANCED:
   - Object detection (YOLO, R-CNN)
   - Image segmentation (U-Net)
   - Image generation (GANs, VAEs)
   - Style transfer
   - Super-resolution

   TRANSFER LEARNING:
   - Use pre-trained models (ResNet, VGG)
   - Fine-tune for your task
   - Achieve great results with little data!

 Remember:
   "CNNs are not just for images anymore!"
   - Used in audio processing (spectrograms are images!)
   - Used in NLP (text as 1D convolutions)
   - Foundation for modern deep learning

 You've mastered CNNs!
   This is the workhorse of computer vision.
   Billions of CNN predictions happen every second worldwide!
""")

print("\n CNN Basics Complete!")
print("Next: rnn_basics.py - Recurrent Neural Networks for sequences")
