# 🧠 Phase 4: Deep Learning — Detailed Guide

> Deep Learning is a subset of ML that uses **neural networks** with many layers.  
> It powers image recognition, language models, speech, game AI, and generative AI.

---

## 📋 Phase Overview

**Prerequisites:** Complete Phases 1–3 first. You must understand:
- Python, NumPy, Pandas, Matplotlib
- Supervised learning, gradient descent, model evaluation

| Topic | Files | Status |
|-------|-------|--------|
| Neural Networks from Scratch | `neural_network_scratch.py` | ⏳ |
| Backpropagation | `backpropagation.py` | ⏳ |
| TensorFlow / Keras | `tensorflow_basics.py`, `first_nn.py` | ⏳ |
| CNNs | `cnn_basics.py` | ⏳ |
| RNNs | `rnn_basics.py` | ⏳ |
| Transfer Learning | `transfer_learning.py` | ⏳ |
| NLP Basics | `nlp_basics.py` | ⏳ |
| Transformers | `transformers_intro.py` | ⏳ |

**Status: ⏳ Not Started**

---

## ⚙️ Setup

```bash
pip install tensorflow keras torch torchvision transformers
```

> **Note:** TensorFlow requires Python 3.8–3.11. Use GPU version if you have an NVIDIA GPU:
> ```bash
> pip install tensorflow-gpu
> ```

---

## 📘 Topic 1: Neural Networks from Scratch
📄 File to create: `neural_network_scratch.py`

Before using TensorFlow, understand what it's doing under the hood.

### What is a Neural Network?

```
Input Layer     Hidden Layer(s)    Output Layer
  [x1]  ─────────────●────────────── [y]
  [x2]  ─────────────●
  [x3]  ─────────────●
```

Each connection has a **weight**.  
Each neuron applies: `output = activation(weights × inputs + bias)`

### The Perceptron (Simplest Neural Network)

```python
import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, epochs=100):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def activation(self, x):
        return 1 if x >= 0 else 0   # Step function

    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        return self.activation(z)

    def fit(self, X, y):
        n_features = X.shape[1]
        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            for xi, yi in zip(X, y):
                prediction = self.predict(xi)
                error = yi - prediction
                # Update weights
                self.weights += self.lr * error * xi
                self.bias    += self.lr * error
```

### Activation Functions

| Function | Formula | When to Use |
|---------|---------|-------------|
| **Sigmoid** | $\frac{1}{1+e^{-x}}$ | Binary classification output |
| **ReLU** | $\max(0, x)$ | Hidden layers (most common) |
| **Softmax** | $\frac{e^{x_i}}{\sum e^{x_j}}$ | Multi-class output |
| **Tanh** | $\frac{e^x - e^{-x}}{e^x + e^{-x}}$ | RNNs |

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
```

---

## 📘 Topic 2: Backpropagation
📄 File to create: `backpropagation.py`

**How does a neural network actually learn?**

1. **Forward pass:** Input → compute prediction
2. **Compute loss:** How wrong was the prediction?
3. **Backward pass:** Use chain rule to compute gradient of loss w.r.t. every weight
4. **Update weights:** Gradient descent step

```
Loss function: L = (y_pred - y_true)²

dL/dw = dL/dy_pred × dy_pred/dz × dz/dw
      = 2(y_pred - y) × sigmoid'(z) × x

This is the "chain rule" = backpropagation
```

```python
# Forward pass
z = np.dot(X, weights) + bias
a = sigmoid(z)
loss = np.mean((a - y) ** 2)

# Backward pass
da = 2 * (a - y) / len(y)
dz = da * sigmoid_derivative(z)
dw = np.dot(X.T, dz)
db = np.sum(dz)

# Update
weights -= learning_rate * dw
bias    -= learning_rate * db
```

**Why understand this?**
> When your model doesn't learn, you need to know WHY.  
> Is it vanishing gradients? Bad learning rate? Wrong activation? You need to know the math to debug.

---

## 📘 Topic 3: TensorFlow & Keras Basics
📄 File to create: `tensorflow_basics.py`

```python
import tensorflow as tf
import numpy as np

# Tensors — multi-dimensional arrays
a = tf.constant([1, 2, 3, 4])
b = tf.constant([5, 6, 7, 8])

print(tf.add(a, b))
print(tf.multiply(a, b))

# Variables (learnable parameters)
w = tf.Variable([0.5, 0.5])
print(w)

# Automatic differentiation (the engine of backprop)
x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = x ** 2
dy_dx = tape.gradient(y, x)
print(dy_dx)   # 6.0  (derivative of x² at x=3)
```

---

## 📘 Topic 4: First Neural Network with Keras
📄 File to create: `first_nn.py`

**Task: Classify handwritten digits (MNIST)**

```python
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load MNIST dataset (built-in, downloads automatically)
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Normalize pixel values from 0-255 to 0-1
X_train = X_train / 255.0
X_test  = X_test  / 255.0

# Build the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),   # 28×28 image → 784 numbers
    keras.layers.Dense(128, activation="relu"),    # Hidden layer
    keras.layers.Dropout(0.2),                    # Prevent overfitting
    keras.layers.Dense(10, activation="softmax")  # Output: 10 digits (0-9)
])

# Compile — choose optimizer, loss function, metrics
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train
history = model.fit(X_train, y_train, epochs=10, validation_split=0.1)

# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.2%}")

# Plot training history
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Val Accuracy")
plt.legend()
plt.show()
```

**Common Keras layer types:**

| Layer | Use Case |
|-------|----------|
| `Dense` | Fully connected — general use |
| `Flatten` | Reshape (image → vector) |
| `Dropout` | Prevent overfitting |
| `Conv2D` | Image feature extraction |
| `MaxPooling2D` | Reduce spatial size |
| `LSTM` | Sequence data (text, time) |
| `Embedding` | Convert words to vectors |
| `BatchNormalization` | Stabilize training |

---

## 📘 Topic 5: Convolutional Neural Networks (CNN)
📄 File to create: `cnn_basics.py`

**Used for:** Images, video, any grid-like data.

Instead of flattening the image, CNNs **scan** it with filters to detect features:
- Layer 1: Detects edges
- Layer 2: Detects shapes
- Layer 3+: Detects objects

```python
model = keras.Sequential([
    # Convolutional block 1
    keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D((2, 2)),

    # Convolutional block 2
    keras.layers.Conv2D(64, (3, 3), activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),

    # Classifier head
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.summary()   # Shows architecture and parameter count
```

---

## 📘 Topic 6: Recurrent Neural Networks (RNN)
📄 File to create: `rnn_basics.py`

**Used for:** Text, time series, audio — anything where **order matters**.

```python
model = keras.Sequential([
    keras.layers.Embedding(input_dim=10000, output_dim=64),  # Word → vector
    keras.layers.LSTM(64),                                    # Process sequence
    keras.layers.Dense(1, activation="sigmoid")               # Binary output
])
```

**LSTM (Long Short-Term Memory):** The most popular RNN type.  
It has a "memory cell" that can remember context from many steps ago.

---

## 📘 Topic 7: Transfer Learning
📄 File to create: `transfer_learning.py`

**Don't train from scratch every time.**  
Use a model already trained on millions of images (ImageNet), and fine-tune it for your task.

```python
# Load pretrained MobileNetV2 (without top classification layer)
base_model = keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

# Freeze pretrained weights
base_model.trainable = False

# Add your own classification head
model = keras.Sequential([
    base_model,
    keras.layers.GlobalAveragePooling2D(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(2, activation="softmax")   # Your 2 classes
])
```

**Why transfer learning?** Train a great model with **very little data** and **much less time**.

---

## 📘 Topic 8: NLP Basics
📄 File to create: `nlp_basics.py`

**Natural Language Processing** = teaching computers to understand human language.

```python
# Text preprocessing pipeline
import re

def preprocess(text):
    text = text.lower()                          # Lowercase
    text = re.sub(r"[^a-z\s]", "", text)        # Remove punctuation
    words = text.split()                          # Tokenize
    return words

# Bag of Words
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

corpus = ["I love ML", "ML is amazing", "I love Python"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())
```

---

## 📘 Topic 9: Transformers Introduction
📄 File to create: `transformers_intro.py`

The architecture behind **GPT, BERT, ChatGPT, and all modern LLMs**.

**The key idea:** Self-Attention — each word looks at all other words to understand context.

```python
# Using Hugging Face Transformers library
from transformers import pipeline

# Sentiment analysis (pre-trained model, no training needed)
classifier = pipeline("sentiment-analysis")
result = classifier("I love learning machine learning!")
print(result)   # [{'label': 'POSITIVE', 'score': 0.99}]

# Text generation with GPT-2
generator = pipeline("text-generation", model="gpt2")
output = generator("Machine learning is", max_length=50)
print(output[0]["generated_text"])
```

---

## 🏁 Phase 4 Mini-Project (Choose One)

### Option A: Handwritten Digit Recognizer
- Dataset: MNIST (built into Keras)
- Model: CNN
- Extra: Build a small web UI where you draw a digit and it classifies it

### Option B: Image Classifier (Cats vs Dogs)
- Dataset: [Kaggle Cats vs Dogs](https://www.kaggle.com/c/dogs-vs-cats)
- Model: Custom CNN or Transfer Learning (MobileNetV2)

### Option C: Sentiment Analyzer
- Dataset: IMDB Movie Reviews
- Model: LSTM or pre-trained BERT
- Predict: Positive or Negative review

---

## 📈 Progress Tracker

```
[░░░░░░░░░░░░░░░░] 0% Complete

⏳ neural_network_scratch.py — Perceptron from scratch
⏳ backpropagation.py        — Manual backprop
⏳ tensorflow_basics.py      — Tensors & GradientTape
⏳ first_nn.py               — MNIST with Keras
⏳ cnn_basics.py             — Image classification
⏳ rnn_basics.py             — Sequence modeling
⏳ transfer_learning.py      — Pretrained models
⏳ nlp_basics.py             — Text processing
⏳ transformers_intro.py     — Transformers & HuggingFace
⏳ mini_project/             — Full deep learning project
```

---

*Go to [LEARNING_PATH.md](../LEARNING_PATH.md) for the complete AI/ML roadmap.*  
*Previous phase: [Machine Learning](../Phase%203%20-%20Machine%20Learning/GUIDE.md)*  
*Next phase: [Research & Projects](../Phase%205%20-%20Research/GUIDE.md)*
