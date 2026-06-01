"""
🎯 TRANSFER LEARNING - Standing on the Shoulders of Giants
===========================================================

What is Transfer Learning?
---------------------------
Training neural networks from scratch is EXPENSIVE:
- Requires massive datasets (millions of images)
- Takes days/weeks on powerful GPUs
- Costs thousands of dollars

Transfer Learning: Use a pre-trained model!
- Someone already trained on millions of images
- We reuse their learned features
- Fine-tune for OUR specific task
- Train in minutes, not days!

The Analogy:
------------
Building from scratch = Learning to read from scratch
Transfer learning = Already know how to read, learn new vocabulary

A model trained on ImageNet (1.4M images, 1000 classes) already knows:
- Layer 1: Edges, colors, textures
- Layer 2: Shapes, patterns
- Layer 3: Parts (eyes, wheels, leaves)
- Layer 4: Objects (cats, dogs, cars)

We reuse layers 1-3 (general features) and retrain layer 4 (our specific task)!

When to use Transfer Learning:
-------------------------------
✅ Small dataset (< 10,000 images)
✅ Similar task (e.g., both are image classification)
✅ Limited compute resources
✅ Need quick results

Popular Pre-trained Models:
----------------------------
- VGG16/VGG19: Simple, powerful
- ResNet50/ResNet101: Very deep, skip connections
- InceptionV3/InceptionResNetV2: Multi-scale features
- MobileNet: Fast, for mobile devices
- EfficientNet: State-of-the-art efficiency

All trained on ImageNet dataset!
"""

import numpy as np
import matplotlib.pyplot as plt
import os

try:
    import tensorflow as tf
    from tensorflow import keras
    print("=" * 80)
    print("TRANSFER LEARNING - Using Pre-trained Models")
    print("=" * 80)
    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    print("Please install TensorFlow: pip install tensorflow")
    exit()

# ============================================================
# PART 1: Understanding Pre-trained Models
# ============================================================
print("\n📌 PART 1: Loading a Pre-trained Model")
print("-" * 80)

print("""
We'll use VGG16 - a classic CNN architecture:

VGG16 Architecture:
- 16 layers deep
- Trained on ImageNet (1.4M images, 1000 classes)
- Input: 224×224 RGB images
- Very good at feature extraction

Keras includes several pre-trained models!
""")

print("\n🔹 Loading VGG16 (this downloads ~500MB first time)...")

# Load VGG16 without top layer (we'll add our own)
base_model = keras.applications.VGG16(
    weights='imagenet',  # Use pre-trained ImageNet weights
    include_top=False,   # Exclude final classification layer
    input_shape=(224, 224, 3)  # Standard ImageNet size
)

print("\n✅ VGG16 loaded!")
print(f"  Model size: ~138M parameters")
print(f"  Trained on: ImageNet (1.4M images)")
print(f"  Original task: 1000-class classification")

print("\n📊 Base Model Architecture:")
base_model.summary()

print(f"\n💡 Notice:")
print(f"  - Input: (224, 224, 3) RGB image")
print(f"  - Output: (7, 7, 512) feature maps")
print(f"  - We'll use these features for our task!")

# ============================================================
# PART 2: Feature Extraction Strategy
# ============================================================
print("\n\n📌 PART 2: Transfer Learning Strategies")
print("-" * 80)

print("""
Two main strategies:

1. FEATURE EXTRACTION (Freeze base model):
   - Keep pre-trained weights frozen
   - Only train new top layers
   - Fast, works with small datasets
   - Good when datasets are similar

2. FINE-TUNING (Unfreeze some layers):
   - Freeze early layers (general features)
   - Unfreeze later layers (specific features)
   - Train with low learning rate
   - Better performance, needs more data

We'll demonstrate both!
""")

# Visualize freezing
print("\n🔹 Freezing Base Model Layers:")
base_model.trainable = False  # Freeze all layers

trainable_count = sum([1 for layer in base_model.layers if layer.trainable])
frozen_count = len(base_model.layers) - trainable_count

print(f"  Total layers: {len(base_model.layers)}")
print(f"  Trainable layers: {trainable_count}")
print(f"  Frozen layers: {frozen_count}")
print(f"  ✓ Base model weights won't change during training!")

# ============================================================
# PART 3: Building Transfer Learning Model
# ============================================================
print("\n\n📌 PART 3: Building Transfer Learning Model")
print("-" * 80)

print("""
Our Architecture:
  VGG16 (frozen) → Flatten → Dense(256) → Dropout(0.5) → Dense(10)

We'll classify CIFAR-10:
- 10 classes: airplane, car, bird, cat, deer, dog, frog, horse, ship, truck
- 60,000 images (32×32 color)
- Much smaller than ImageNet!
""")

# Load CIFAR-10 dataset
print("\n🔹 Loading CIFAR-10 dataset...")
(X_train_cifar, y_train_cifar), (X_test_cifar, y_test_cifar) = keras.datasets.cifar10.load_data()

print(f"  Training: {X_train_cifar.shape}")
print(f"  Test: {X_test_cifar.shape}")

# Class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Visualize samples
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
fig.suptitle('CIFAR-10 Sample Images', fontsize=14, fontweight='bold')

for i, ax in enumerate(axes.flat):
    ax.imshow(X_train_cifar[i])
    ax.set_title(class_names[y_train_cifar[i][0]], fontsize=10)
    ax.axis('off')

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/cifar10_samples.png', dpi=150)
print("\n✓ Saved visualization: cifar10_samples.png")

# Preprocess for VGG16
print("\n🔹 Preprocessing for VGG16:")
print("  1. Resize 32×32 → 224×224 (VGG16 input size)")
print("  2. Normalize using ImageNet statistics")

def preprocess_for_vgg(images):
    """Resize and preprocess images for VGG16"""
    # Resize to 224x224
    resized = tf.image.resize(images, (224, 224))
    # Preprocess for VGG16 (ImageNet normalization)
    return keras.applications.vgg16.preprocess_input(resized)

# Use subset for faster demo (use full dataset for real projects!)
X_train_subset = X_train_cifar[:5000]  # 5000 samples
y_train_subset = y_train_cifar[:5000]
X_test_subset = X_test_cifar[:1000]  # 1000 samples
y_test_subset = y_test_cifar[:1000]

print(f"\n  Using subset for demo:")
print(f"    Training: {X_train_subset.shape}")
print(f"    Test: {X_test_subset.shape}")

# Preprocess
X_train_processed = preprocess_for_vgg(X_train_subset.astype('float32'))
X_test_processed = preprocess_for_vgg(X_test_subset.astype('float32'))

# One-hot encode
y_train_onehot = keras.utils.to_categorical(y_train_subset, 10)
y_test_onehot = keras.utils.to_categorical(y_test_subset, 10)

print(f"  ✓ Preprocessed!")

# Build model
print("\n🔹 Building Transfer Learning Model:")

model = keras.Sequential([
    base_model,
    keras.layers.Flatten(),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation='softmax')
])

print("\n✅ Transfer Learning Model:")
model.summary()

# Count parameters
total_params = model.count_params()
trainable_params = sum([tf.reduce_prod(var.shape).numpy() for var in model.trainable_variables])
frozen_params = total_params - trainable_params

print(f"\n📊 Parameter Analysis:")
print(f"  Total parameters: {total_params:,}")
print(f"  Trainable parameters: {trainable_params:,} ({trainable_params/total_params*100:.1f}%)")
print(f"  Frozen parameters: {frozen_params:,} ({frozen_params/total_params*100:.1f}%)")
print(f"\n💡 We only train {trainable_params/total_params*100:.1f}% of parameters!")
print(f"   This is why transfer learning is so fast!")

# ============================================================
# PART 4: Training with Transfer Learning
# ============================================================
print("\n\n📌 PART 4: Training the Model")
print("-" * 80)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("✅ Model compiled")
print("\n🏋️ Training with frozen base model...\n")

# Callbacks
early_stop = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True,
    verbose=1
)

history = model.fit(
    X_train_processed, y_train_onehot,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

print("\n✅ Training complete!")

# Evaluate
test_loss, test_acc = model.evaluate(X_test_processed, y_test_onehot, verbose=0)
print(f"\n📊 Test Results (Feature Extraction):")
print(f"  Test Accuracy: {test_acc*100:.2f}%")
print(f"\n💡 Not bad for training only {trainable_params:,} parameters!")

# ============================================================
# PART 5: Fine-Tuning
# ============================================================
print("\n\n📌 PART 5: Fine-Tuning for Better Performance")
print("-" * 80)

print("""
Fine-tuning strategy:
1. Freeze early layers (general features)
2. Unfreeze later layers (more specific features)
3. Train with LOWER learning rate
4. Prevent overfitting on small dataset
""")

print("\n🔹 Unfreezing last 4 layers of VGG16:")

# Unfreeze the last 4 layers
base_model.trainable = True
for layer in base_model.layers[:-4]:
    layer.trainable = False

trainable_count = sum([1 for layer in base_model.layers if layer.trainable])
frozen_count = len(base_model.layers) - trainable_count

print(f"  Total layers: {len(base_model.layers)}")
print(f"  Frozen layers: {frozen_count}")
print(f"  Trainable layers: {trainable_count}")

# Recompile with lower learning rate
print("\n🔹 Recompiling with lower learning rate:")
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),  # Much lower!
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("  Learning rate: 1e-5 (vs 1e-3 default)")
print("  ✓ Lower learning rate prevents destroying pre-trained weights")

print("\n🏋️ Fine-tuning...\n")

history_finetune = model.fit(
    X_train_processed, y_train_onehot,
    epochs=5,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

print("\n✅ Fine-tuning complete!")

# Evaluate again
test_loss_ft, test_acc_ft = model.evaluate(X_test_processed, y_test_onehot, verbose=0)
print(f"\n📊 Test Results After Fine-Tuning:")
print(f"  Test Accuracy: {test_acc_ft*100:.2f}%")
print(f"  Improvement: +{(test_acc_ft - test_acc)*100:.2f}%")

# Visualize training
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Combine histories
all_loss = history.history['loss'] + history_finetune.history['loss']
all_val_loss = history.history['val_loss'] + history_finetune.history['val_loss']
all_acc = history.history['accuracy'] + history_finetune.history['accuracy']
all_val_acc = history.history['val_accuracy'] + history_finetune.history['val_accuracy']

ax1.plot(all_loss, label='Training Loss', linewidth=2)
ax1.plot(all_val_loss, label='Validation Loss', linewidth=2)
ax1.axvline(x=len(history.history['loss']), color='red', linestyle='--', linewidth=2, label='Fine-tuning starts')
ax1.set_xlabel('Epoch', fontsize=12)
ax1.set_ylabel('Loss', fontsize=12)
ax1.set_title('Transfer Learning: Loss', fontsize=14, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

ax2.plot(all_acc, label='Training Accuracy', linewidth=2)
ax2.plot(all_val_acc, label='Validation Accuracy', linewidth=2)
ax2.axvline(x=len(history.history['accuracy']), color='red', linestyle='--', linewidth=2, label='Fine-tuning starts')
ax2.set_xlabel('Epoch', fontsize=12)
ax2.set_ylabel('Accuracy', fontsize=12)
ax2.set_title('Transfer Learning: Accuracy', fontsize=14, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/transfer_learning_history.png', dpi=150)
print("\n✓ Saved visualization: transfer_learning_history.png")

# ============================================================
# PART 6: Making Predictions
# ============================================================
print("\n\n📌 PART 6: Testing the Transfer Learning Model")
print("-" * 80)

# Make predictions
predictions = model.predict(X_test_processed[:25], verbose=0)
predicted_classes = np.argmax(predictions, axis=1)

# Visualize predictions
fig, axes = plt.subplots(5, 5, figsize=(12, 12))
fig.suptitle('Transfer Learning Predictions', fontsize=16, fontweight='bold')

for i, ax in enumerate(axes.flat):
    ax.imshow(X_test_subset[i])

    pred_class = predicted_classes[i]
    actual_class = y_test_subset[i][0]
    confidence = predictions[i][pred_class] * 100

    color = 'green' if pred_class == actual_class else 'red'
    ax.set_title(f'Pred: {class_names[pred_class]}\n({confidence:.0f}%)\nActual: {class_names[actual_class]}',
                fontsize=9, color=color)
    ax.axis('off')

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/transfer_learning_predictions.png', dpi=150)
print("\n✓ Saved visualization: transfer_learning_predictions.png")

print("\n🧪 Sample Predictions:")
for i in range(5):
    pred = predicted_classes[i]
    actual = y_test_subset[i][0]
    conf = predictions[i][pred] * 100
    status = '✓' if pred == actual else '✗'
    print(f"  {status} Predicted: {class_names[pred]:12s} ({conf:5.1f}%) | Actual: {class_names[actual]}")

# ============================================================
# PART 7: Comparing Approaches
# ============================================================
print("\n\n📌 PART 7: Comparing Different Approaches")
print("-" * 80)

print("""
Let's compare three approaches:

1. TRAIN FROM SCRATCH:
   - Initialize random weights
   - Train all layers
   - Needs LOTS of data

2. FEATURE EXTRACTION:
   - Freeze base model
   - Train only top layers
   - Fast, works with small data

3. FINE-TUNING:
   - Unfreeze some layers
   - Train with low learning rate
   - Best performance
""")

print("\n📊 Comparison (on CIFAR-10 subset):\n")
print(f"  {'Approach':<20} | {'Training Time':<15} | {'Parameters':<15} | {'Accuracy':<10}")
print(f"  {'-'*20}+{'-'*16}+{'-'*16}+{'-'*10}")
print(f"  {'From Scratch':<20} | {'Hours (slow)':<15} | {'~15M (all)':<15} | {'~65%':<10}")
print(f"  {'Feature Extract':<20} | {'Minutes (fast)':<15} | {f'~{trainable_params:,} (few)':<15} | {f'{test_acc*100:.1f}%':<10}")
print(f"  {'Fine-Tuning':<20} | {'~30 min':<15} | {f'~{trainable_params:,}+':<15} | {f'{test_acc_ft*100:.1f}%':<10}")

print("\n💡 Key Insights:")
print("  ✓ Transfer learning is MUCH faster")
print("  ✓ Works great with small datasets")
print("  ✓ Fine-tuning gives best results")
print("  ✓ Pre-trained models are incredibly valuable!")

# ============================================================
# PART 8: Other Pre-trained Models
# ============================================================
print("\n\n📌 PART 8: Other Pre-trained Models Available")
print("-" * 80)

print("""
Keras provides many pre-trained models:

📦 Available Models:

1. VGG16 / VGG19
   - Simple, powerful
   - Large model size
   - Good baseline

2. ResNet50 / ResNet101 / ResNet152
   - Very deep (50-152 layers!)
   - Skip connections
   - Great performance

3. InceptionV3 / InceptionResNetV2
   - Multi-scale features
   - Efficient
   - Good accuracy/speed trade-off

4. MobileNet / MobileNetV2
   - Lightweight
   - Fast inference
   - Perfect for mobile/edge devices

5. EfficientNet B0-B7
   - State-of-the-art efficiency
   - Scalable
   - Best accuracy/parameters ratio

6. DenseNet121 / DenseNet169
   - Dense connections
   - Parameter efficient
   - Strong performance

7. Xception
   - Depthwise separable convolutions
   - Very efficient
   - High accuracy

All available via: keras.applications.<ModelName>
All trained on ImageNet!
""")

print("\n🔹 Quick comparison:")
models_info = [
    ("VGG16", "138M", "71.3%", "Slow"),
    ("ResNet50", "25M", "74.9%", "Medium"),
    ("InceptionV3", "24M", "77.9%", "Medium"),
    ("MobileNetV2", "3.5M", "71.3%", "Fast"),
    ("EfficientNetB0", "5.3M", "77.1%", "Fast"),
]

print(f"\n  {'Model':<15} | {'Parameters':<12} | {'Top-1 Acc':<10} | {'Speed':<8}")
print(f"  {'-'*15}+{'-'*13}+{'-'*11}+{'-'*8}")
for name, params, acc, speed in models_info:
    print(f"  {name:<15} | {params:<12} | {acc:<10} | {speed:<8}")

# ============================================================
# PART 9: Best Practices
# ============================================================
print("\n\n📌 PART 9: Transfer Learning Best Practices")
print("-" * 80)

print("""
🎯 When to Use Transfer Learning:
  ✅ Small dataset (< 10,000 samples)
  ✅ Similar domain (both images, both text, etc.)
  ✅ Limited compute resources
  ✅ Need quick results
  ✅ Prototyping

⚠️  When NOT to Use:
  ❌ Very different domain (ImageNet → medical scans may not help)
  ❌ Extremely large dataset (train from scratch might be better)
  ❌ Very different task (ImageNet → audio)

📋 Step-by-Step Guide:

1. CHOOSE BASE MODEL:
   - Similar task? Use related model
   - Mobile device? Use MobileNet
   - Best accuracy? Use EfficientNet
   - Good baseline? Use ResNet50

2. FREEZE BASE MODEL:
   base_model.trainable = False
   - Train only top layers first
   - Fast convergence

3. ADD CUSTOM LAYERS:
   - Flatten or GlobalAveragePooling
   - Dense layers for your classes
   - Dropout to prevent overfitting

4. TRAIN (FEATURE EXTRACTION):
   - Train with normal learning rate
   - Monitor validation loss
   - Save best model

5. FINE-TUNE:
   - Unfreeze last few layers
   - Use LOW learning rate (1e-5)
   - Train few more epochs
   - Watch for overfitting!

6. EVALUATE:
   - Test on held-out set
   - Compare to baseline
   - Analyze errors

🔧 Tips:

1. DATA AUGMENTATION:
   - Flip, rotate, zoom images
   - Prevents overfitting
   - Creates more training data

2. LEARNING RATE:
   - Feature extraction: 1e-3 (normal)
   - Fine-tuning: 1e-5 (much lower!)
   - Too high → destroy pre-trained weights

3. BATCH SIZE:
   - Smaller: Better generalization, slower
   - Larger: Faster training, more memory
   - Try 16-64

4. EARLY STOPPING:
   - Monitor validation loss
   - Stop when not improving
   - Prevent overfitting

5. CALLBACKS:
   - EarlyStopping
   - ModelCheckpoint
   - ReduceLROnPlateau

💡 Common Mistakes:

❌ Fine-tuning too early (do feature extraction first!)
❌ High learning rate when fine-tuning (destroys weights!)
❌ Unfreezing too many layers (overfits on small data!)
❌ Not using data augmentation
❌ Wrong preprocessing (each model has specific preprocessing!)

✅ Do This:

1. Start simple (freeze everything)
2. Add data augmentation
3. Train with callbacks
4. Fine-tune carefully
5. Compare multiple models
6. Save best models
""")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n🎯 WHY TRANSFER LEARNING MATTERS")
print("=" * 80)
print("""
1. DEMOCRATIZES DEEP LEARNING:
   - Don't need massive datasets
   - Don't need weeks of training
   - Don't need expensive GPUs
   - Anyone can build state-of-the-art models!

2. PRACTICAL APPLICATIONS:
   - Medical: Disease detection (few examples per disease)
   - Agriculture: Crop disease (limited labeled data)
   - Manufacturing: Quality control (rare defects)
   - Wildlife: Animal classification (few photos)
   - Art: Style classification

3. REAL-WORLD SUCCESS:
   - Google Photos: Transfer learning for face recognition
   - Healthcare: X-ray analysis with limited data
   - Startups: Build MVPs quickly
   - Research: Rapid prototyping

4. COST SAVINGS:
   Training from scratch:
   - Dataset: Millions of images
   - Compute: $10,000+ in cloud costs
   - Time: Weeks
   - Expertise: PhD-level

   Transfer learning:
   - Dataset: Hundreds of images
   - Compute: $10 or free GPU
   - Time: Hours
   - Expertise: This tutorial!

5. SCIENTIFIC INSIGHT:
   - Pre-trained models learn universal features
   - Early layers: Edges, textures (universal!)
   - Later layers: Specific objects (task-specific)
   - We leverage universal features!

📊 Our Achievement:
   - Used 5,000 images (vs 1.4M for ImageNet)
   - Trained in minutes (vs weeks)
   - Achieved ~{test_acc_ft*100:.1f}% accuracy
   - Only trained {trainable_params:,} parameters!

🔑 Key Takeaways:

   1. Transfer learning = Reusing learned features
      - Pre-trained on large dataset
      - Fine-tune for your task
      - Save time, money, data

   2. Two strategies:
      - Feature extraction: Freeze base
      - Fine-tuning: Unfreeze some layers

   3. Works best:
      - Small datasets
      - Similar domains
      - Limited resources

   4. Choose right model:
      - Accuracy: EfficientNet
      - Speed: MobileNet
      - Baseline: ResNet50

🚀 What's Next?

   PRACTICE:
   - Try different models (ResNet, EfficientNet)
   - Use your own dataset
   - Experiment with fine-tuning strategies
   - Add data augmentation

   ADVANCED:
   - Multi-task learning
   - Domain adaptation
   - Few-shot learning
   - Self-supervised learning

   REAL PROJECTS:
   - Plant disease classification
   - Wildlife species identification
   - Product defect detection
   - Custom image search

💡 Remember:
   "Transfer learning is not cheating, it's smart engineering!"

   Just like we don't reinvent programming languages,
   we don't retrain from scratch when great models exist!

🎓 You've mastered transfer learning!
   This is THE practical way to use deep learning today.
   Most real-world applications use transfer learning!
""")

print("\n✅ Transfer Learning Complete!")
print("Next: nlp_basics.py - Text processing and NLP fundamentals")
