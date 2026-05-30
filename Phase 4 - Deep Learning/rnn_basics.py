"""
🔄 RECURRENT NEURAL NETWORKS (RNN) - Deep Learning for Sequences
==================================================================

What is a Recurrent Neural Network?
------------------------------------
RNNs are designed for SEQUENTIAL data:
- Time series (stock prices, weather)
- Text (sentences, documents)
- Audio (speech, music)
- Video (frames over time)

The key idea: MEMORY!

Regular NN: Each input is independent
RNN: Each input depends on previous inputs!

Think of it like reading:
- You remember previous words to understand current word
- Context matters!
- Order matters!

How RNNs Work:
--------------
At each time step:
1. Take current input
2. Combine with previous hidden state (memory!)
3. Produce output
4. Pass hidden state to next time step

Formula: h_t = tanh(W_h · h_{t-1} + W_x · x_t + b)

The same weights are used at EVERY time step!
This is called "parameter sharing"

Problems with Vanilla RNNs:
----------------------------
1. Vanishing Gradients: Can't remember long-term dependencies
2. Exploding Gradients: Gradients become too large

Solutions:
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)

These have "gates" that control information flow!

Let's build and understand them!
"""

import numpy as np
import matplotlib.pyplot as plt

try:
    import tensorflow as tf
    from tensorflow import keras
    print("=" * 80)
    print("RECURRENT NEURAL NETWORKS (RNN) - Sequences and Time Series")
    print("=" * 80)
    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    print("Please install TensorFlow: pip install tensorflow")
    exit()

# ============================================================
# PART 1: Understanding Sequential Data
# ============================================================
print("\n📌 PART 1: Understanding Sequential Data")
print("-" * 80)

print("""
Examples of sequential data:

1. TEXT: "The cat sat on the mat"
   - Words depend on previous words
   - Order matters!
   - "mat the on sat cat The" makes no sense

2. TIME SERIES: [10, 12, 15, 14, 16, ...]
   - Stock prices over time
   - Temperature over days
   - Past values predict future

3. AUDIO: Waveform samples
   - Speech recognition
   - Music generation

4. VIDEO: Sequence of frames
   - Action recognition
   - Video prediction

Key characteristic: ORDER MATTERS!
""")

# Create simple sequence data
print("\n🔹 Example: Predicting Next Number in Sequence")
print("\nSequence pattern: Each number = sum of previous two (like Fibonacci)")

# Generate sequence
sequence = [1, 1]
for i in range(18):
    next_val = sequence[-1] + sequence[-2]
    sequence.append(next_val)

print(f"\nSequence: {sequence[:10]}...")
print("\nPattern:")
for i in range(5):
    print(f"  {sequence[i]}, {sequence[i+1]} → {sequence[i+2]}")

# Visualize
plt.figure(figsize=(12, 5))
plt.plot(sequence, 'o-', linewidth=2, markersize=8, color='blue')
plt.xlabel('Time Step', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.title('Sequential Data - Order Matters!', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/rnn_sequence_data.png', dpi=150)
print("\n✓ Saved visualization: rnn_sequence_data.png")

# ============================================================
# PART 2: Vanilla RNN from Scratch
# ============================================================
print("\n\n📌 PART 2: Understanding Vanilla RNN")
print("-" * 80)

print("""
Simple RNN Architecture:

At each time step t:
  1. Input: x_t
  2. Previous hidden state: h_{t-1}
  3. Calculate: h_t = tanh(W_h·h_{t-1} + W_x·x_t + b)
  4. Output: y_t = W_y·h_t + b_y

The hidden state h_t is the "memory"!
It carries information from previous time steps.
""")

# Simple RNN example
print("\n🔹 Manual RNN Calculation Example:")

# Parameters (small example)
W_h = np.array([[0.5]])  # Hidden to hidden
W_x = np.array([[0.3]])  # Input to hidden
W_y = np.array([[1.0]])  # Hidden to output
b = np.array([0.1])
b_y = np.array([0.0])

# Input sequence
x_sequence = np.array([1.0, 2.0, 3.0])
print(f"Input sequence: {x_sequence}")

# Initialize hidden state
h = np.array([0.0])
outputs = []

print("\n⏱️ Processing sequence step-by-step:\n")
for t, x in enumerate(x_sequence):
    # RNN cell computation
    h = np.tanh(W_h * h + W_x * x + b)
    y = W_y * h + b_y

    outputs.append(y[0])
    print(f"  Step {t}: x={x:.1f}, h={h[0]:.4f}, y={y[0]:.4f}")

print(f"\n💡 Notice how hidden state h changes and carries information!")
print(f"   The hidden state h is the RNN's \"memory\"")

# ============================================================
# PART 3: Preparing Sequential Data
# ============================================================
print("\n\n📌 PART 3: Preparing Data for RNN")
print("-" * 80)

print("""
Creating sequences for training:

Original series: [1, 1, 2, 3, 5, 8, 13, 21, ...]

Create input-output pairs:
  Input: [1, 1, 2] → Output: 3
  Input: [1, 2, 3] → Output: 5
  Input: [2, 3, 5] → Output: 8
  ...

This is called a "sliding window" approach!
""")

def create_sequences(data, seq_length):
    """Create input-output pairs for sequence prediction"""
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

# Create training data
seq_length = 3  # Use 3 previous values to predict next
X_seq, y_seq = create_sequences(sequence[:-5], seq_length)  # Hold out last 5 for testing

print(f"\n🔹 Training Data:")
print(f"  Input shape: {X_seq.shape}")
print(f"  Output shape: {y_seq.shape}")
print(f"  Number of samples: {len(X_seq)}")

print(f"\n  First 3 training examples:")
for i in range(3):
    print(f"    {X_seq[i]} → {y_seq[i]}")

# Reshape for RNN (samples, time steps, features)
X_seq = X_seq.reshape(-1, seq_length, 1)
print(f"\n  Reshaped for RNN: {X_seq.shape}")
print(f"  (samples, time_steps, features)")

# Normalize
X_seq_normalized = X_seq / np.max(X_seq)
y_seq_normalized = y_seq / np.max(y_seq)
print(f"\n  ✓ Normalized to [0, 1] range")

# ============================================================
# PART 4: Building a Simple RNN
# ============================================================
print("\n\n📌 PART 4: Building RNN with Keras")
print("-" * 80)

print("""
Simple RNN Architecture:
  Input (3 time steps) → SimpleRNN(32 units) → Dense(16) → Dense(1)

SimpleRNN layer:
- Takes sequence input
- Processes each time step
- Maintains hidden state
- Returns final output (or all outputs)
""")

simple_rnn_model = keras.Sequential([
    keras.layers.SimpleRNN(32, activation='tanh', input_shape=(seq_length, 1), name='rnn'),
    keras.layers.Dense(16, activation='relu', name='dense1'),
    keras.layers.Dense(1, name='output')
])

print("\n✅ Simple RNN Model:")
simple_rnn_model.summary()

simple_rnn_model.compile(optimizer='adam', loss='mse', metrics=['mae'])

print("\n🏋️ Training Simple RNN...")
history_simple = simple_rnn_model.fit(
    X_seq_normalized, y_seq_normalized,
    epochs=100,
    batch_size=8,
    validation_split=0.2,
    verbose=0
)

print(f"✅ Training complete!")
print(f"  Final loss: {history_simple.history['loss'][-1]:.6f}")

# ============================================================
# PART 5: LSTM - The Better RNN
# ============================================================
print("\n\n📌 PART 5: LSTM - Long Short-Term Memory")
print("-" * 80)

print("""
Why LSTM?
---------
Vanilla RNN has problems:
- Can't remember long-term dependencies
- Vanishing gradient problem

LSTM solves this with GATES:

1. FORGET GATE: What to forget from memory
   f_t = σ(W_f · [h_{t-1}, x_t] + b_f)

2. INPUT GATE: What new information to add
   i_t = σ(W_i · [h_{t-1}, x_t] + b_i)

3. OUTPUT GATE: What to output
   o_t = σ(W_o · [h_{t-1}, x_t] + b_o)

4. CELL STATE: The "memory" that flows through time
   C_t = f_t * C_{t-1} + i_t * tanh(W_C · [h_{t-1}, x_t] + b_C)

Think of it like a conveyor belt with valves:
- Forget gate: Remove old information
- Input gate: Add new information
- Output gate: What to expose

LSTM can remember for 100s or 1000s of time steps!
""")

lstm_model = keras.Sequential([
    keras.layers.LSTM(32, input_shape=(seq_length, 1), name='lstm'),
    keras.layers.Dense(16, activation='relu', name='dense1'),
    keras.layers.Dense(1, name='output')
])

print("\n✅ LSTM Model:")
lstm_model.summary()

print(f"\n📊 Parameter comparison:")
print(f"  SimpleRNN(32): {32*32 + 32*1 + 32:,} parameters")
print(f"  LSTM(32): {32*32*4 + 32*1*4 + 32*4:,} parameters")
print(f"  LSTM has 4× more parameters (4 gates!)")

lstm_model.compile(optimizer='adam', loss='mse', metrics=['mae'])

print("\n🏋️ Training LSTM...")
history_lstm = lstm_model.fit(
    X_seq_normalized, y_seq_normalized,
    epochs=100,
    batch_size=8,
    validation_split=0.2,
    verbose=0
)

print(f"✅ Training complete!")
print(f"  Final loss: {history_lstm.history['loss'][-1]:.6f}")

# Compare performance
plt.figure(figsize=(12, 5))
plt.plot(history_simple.history['loss'], label='Simple RNN', linewidth=2)
plt.plot(history_lstm.history['loss'], label='LSTM', linewidth=2)
plt.xlabel('Epoch', fontsize=12)
plt.ylabel('Loss (MSE)', fontsize=12)
plt.title('Training Loss: Simple RNN vs LSTM', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.yscale('log')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/rnn_vs_lstm_training.png', dpi=150)
print("\n✓ Saved visualization: rnn_vs_lstm_training.png")

# ============================================================
# PART 6: Making Predictions
# ============================================================
print("\n\n📌 PART 6: Making Sequence Predictions")
print("-" * 80)

# Test on held-out data
test_sequence = sequence[-8:-5]  # Last values
X_test = np.array([test_sequence]).reshape(1, seq_length, 1) / np.max(X_seq)
y_test_actual = sequence[-5]

# Predictions
pred_simple = simple_rnn_model.predict(X_test, verbose=0)[0][0] * np.max(y_seq)
pred_lstm = lstm_model.predict(X_test, verbose=0)[0][0] * np.max(y_seq)

print(f"\n🧪 Test Prediction:")
print(f"  Input sequence: {test_sequence}")
print(f"  Actual next value: {y_test_actual}")
print(f"  Simple RNN prediction: {pred_simple:.2f}")
print(f"  LSTM prediction: {pred_lstm:.2f}")
print(f"\n  Simple RNN error: {abs(y_test_actual - pred_simple):.2f}")
print(f"  LSTM error: {abs(y_test_actual - pred_lstm):.2f}")

# ============================================================
# PART 7: Sentiment Analysis with IMDB
# ============================================================
print("\n\n📌 PART 7: Text Sequence - IMDB Sentiment Analysis")
print("-" * 80)

print("""
Real-world RNN application: Sentiment Analysis!

Task: Given a movie review, predict if it's positive or negative.

IMDB Dataset:
- 50,000 movie reviews
- Labeled as positive (1) or negative (0)
- Text is sequential data!
""")

print("\nLoading IMDB dataset...")
max_features = 10000  # Consider only top 10,000 words
maxlen = 200  # Cut reviews after 200 words

(X_train_imdb, y_train_imdb), (X_test_imdb, y_test_imdb) = keras.datasets.imdb.load_data(num_words=max_features)

print(f"\n✅ Data loaded:")
print(f"  Training samples: {len(X_train_imdb)}")
print(f"  Test samples: {len(X_test_imdb)}")

print(f"\n🔹 Example review (as word indices):")
print(f"  {X_train_imdb[0][:20]}...")
print(f"  Label: {'Positive' if y_train_imdb[0] == 1 else 'Negative'}")

# Pad sequences to same length
print(f"\n🔹 Padding sequences to length {maxlen}...")
X_train_imdb = keras.preprocessing.sequence.pad_sequences(X_train_imdb, maxlen=maxlen)
X_test_imdb = keras.preprocessing.sequence.pad_sequences(X_test_imdb, maxlen=maxlen)

print(f"  Padded shape: {X_train_imdb.shape}")
print(f"  (samples, time_steps)")

# Build LSTM model for sentiment
print("\n\n📌 PART 8: LSTM for Sentiment Analysis")
print("-" * 80)

print("""
Architecture:
  Embedding(10000, 128) → LSTM(64) → Dropout(0.5) → Dense(1, sigmoid)

New layer: EMBEDDING
- Converts word indices to dense vectors
- Example: word 42 → [0.2, -0.5, 0.1, ..., 0.3] (128 dimensions)
- Learns word meanings!
- Similar words get similar vectors
""")

sentiment_model = keras.Sequential([
    keras.layers.Embedding(max_features, 128, input_length=maxlen, name='embedding'),
    keras.layers.LSTM(64, dropout=0.2, recurrent_dropout=0.2, name='lstm'),
    keras.layers.Dense(1, activation='sigmoid', name='output')
])

print("\n✅ Sentiment Model:")
sentiment_model.summary()

sentiment_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("\n🏋️ Training sentiment model (this takes a few minutes)...")
print("  Training on 25,000 reviews...")

history_sentiment = sentiment_model.fit(
    X_train_imdb, y_train_imdb,
    epochs=5,
    batch_size=128,
    validation_split=0.2,
    verbose=1
)

print("\n✅ Training complete!")

# Evaluate
test_loss, test_acc = sentiment_model.evaluate(X_test_imdb, y_test_imdb, verbose=0)
print(f"\n📊 Test Results:")
print(f"  Test Accuracy: {test_acc*100:.2f}%")
print(f"  The model correctly classifies {test_acc*100:.1f}% of reviews!")

# Visualize training
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(history_sentiment.history['loss'], label='Training', linewidth=2)
ax1.plot(history_sentiment.history['val_loss'], label='Validation', linewidth=2)
ax1.set_xlabel('Epoch', fontsize=12)
ax1.set_ylabel('Loss', fontsize=12)
ax1.set_title('LSTM Sentiment Analysis - Loss', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

ax2.plot(history_sentiment.history['accuracy'], label='Training', linewidth=2)
ax2.plot(history_sentiment.history['val_accuracy'], label='Validation', linewidth=2)
ax2.set_xlabel('Epoch', fontsize=12)
ax2.set_ylabel('Accuracy', fontsize=12)
ax2.set_title('LSTM Sentiment Analysis - Accuracy', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/rnn_sentiment_training.png', dpi=150)
print("\n✓ Saved visualization: rnn_sentiment_training.png")

# Test on example
print("\n\n🔹 Testing on examples:")
word_index = keras.datasets.imdb.get_word_index()
reverse_word_index = {v: k for k, v in word_index.items()}

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review if i >= 3])

for i in range(3):
    review = decode_review(X_test_imdb[i])
    prediction = sentiment_model.predict(X_test_imdb[i:i+1], verbose=0)[0][0]
    actual = y_test_imdb[i]

    print(f"\n  Review {i+1} (truncated):")
    print(f"    {review[:200]}...")
    print(f"    Prediction: {'Positive' if prediction > 0.5 else 'Negative'} (score: {prediction:.3f})")
    print(f"    Actual: {'Positive' if actual == 1 else 'Negative'}")
    print(f"    {'✓ Correct!' if (prediction > 0.5) == actual else '✗ Wrong'}")

# ============================================================
# PART 9: GRU - Alternative to LSTM
# ============================================================
print("\n\n📌 PART 9: GRU - Gated Recurrent Unit")
print("-" * 80)

print("""
GRU is a simpler alternative to LSTM:

Differences:
- Fewer gates (2 instead of 3)
- Fewer parameters
- Faster to train
- Often similar performance

Gates:
1. Reset gate: What to forget
2. Update gate: What to remember

When to use GRU vs LSTM?
- Try both!
- GRU: Faster, less data
- LSTM: More complex patterns, more data
""")

gru_model = keras.Sequential([
    keras.layers.Embedding(max_features, 128, input_length=maxlen),
    keras.layers.GRU(64, dropout=0.2, recurrent_dropout=0.2),
    keras.layers.Dense(1, activation='sigmoid')
])

print("\n✅ GRU Model:")
gru_model.summary()

print(f"\n📊 Parameter comparison (for 64 units):")
print(f"  LSTM: {lstm_model.layers[0].count_params():,} parameters")
print(f"  GRU: {64*64*3 + 64*1*3 + 64*3:,} parameters (estimate)")
print(f"  GRU is simpler and faster!")

# ============================================================
# PART 10: Bidirectional RNN
# ============================================================
print("\n\n📌 PART 10: Bidirectional RNN")
print("-" * 80)

print("""
Bidirectional RNN processes sequence in BOTH directions!

Forward:  The → cat → sat → on → mat
Backward: mat → on → sat → cat → The

Why?
- Context from both past AND future
- Better understanding
- Used in NLP (BERT uses this idea!)

Example: "I am ___"
- Forward: Knows "I am"
- Backward: Knows what comes after
- Both: Better prediction!
""")

bidirectional_model = keras.Sequential([
    keras.layers.Embedding(max_features, 128, input_length=maxlen),
    keras.layers.Bidirectional(keras.layers.LSTM(64, dropout=0.2, recurrent_dropout=0.2)),
    keras.layers.Dense(1, activation='sigmoid')
])

print("\n✅ Bidirectional LSTM Model:")
bidirectional_model.summary()

print("\n💡 Notice: Parameters doubled!")
print("   Two LSTMs: one forward, one backward")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n🎯 WHY RNNs MATTER")
print("=" * 80)
print("""
1. REVOLUTIONIZED SEQUENCE MODELING:
   - Natural Language Processing
   - Speech recognition
   - Time series forecasting
   - Music generation
   - Video analysis

2. CORE CONCEPTS MASTERED:
   ✓ Sequential data
   ✓ Hidden state (memory)
   ✓ Parameter sharing across time
   ✓ Backpropagation through time (BPTT)
   ✓ Vanishing gradient problem
   ✓ LSTM gates (forget, input, output)
   ✓ GRU (simpler alternative)
   ✓ Bidirectional processing

3. REAL-WORLD APPLICATIONS:
   - Language translation: Google Translate
   - Speech recognition: Siri, Alexa
   - Text generation: Autocomplete
   - Sentiment analysis: Review classification
   - Stock prediction: Financial forecasting
   - Music generation: AI composers
   - Video captioning: Describe videos

4. WHY RNNs WORK:
   - Handle variable-length sequences
   - Share parameters across time
   - Maintain memory/context
   - Learn temporal patterns
   - Process sequential dependencies

5. WHEN TO USE RNN/LSTM/GRU:
   - Text: Sentiment, translation, generation
   - Time series: Stock prices, weather
   - Audio: Speech recognition, music
   - Video: Action recognition, captioning

   Choose:
   - SimpleRNN: Short sequences, prototyping
   - LSTM: Long sequences, complex patterns
   - GRU: Faster, similar performance
   - Bidirectional: Need future context (NLP)

📊 Our Results:
   Sentiment Analysis: ~85% accuracy
   5 epochs, 25,000 reviews
   Understands positive vs negative!

🔑 Key Takeaways:

   1. Sequences need special handling
      - Order matters!
      - Context matters!
      - RNNs maintain memory

   2. LSTM solves vanishing gradient
      - Gates control information flow
      - Can remember long-term dependencies
      - The workhorse for sequences

   3. Embeddings learn word meanings
      - Convert words to vectors
      - Similar words → similar vectors
      - Learned from data!

   4. Architecture choices matter
      - SimpleRNN: Fast, short sequences
      - LSTM: Complex, long sequences
      - GRU: Balance of both
      - Bidirectional: Best for NLP

🚀 What's Next?

   LIMITATIONS:
   - RNNs are SLOW (sequential, can't parallelize)
   - Transformers solve this!
   - Attention mechanism > RNN memory

   IMPROVEMENTS:
   - Stack multiple LSTM layers
   - Use attention mechanisms
   - Try Transformers (see transformers_intro.py)

   ADVANCED:
   - Seq2Seq models (translation)
   - Encoder-Decoder architecture
   - Attention mechanisms
   - BERT, GPT (transformer-based)

💡 Historical Context:
   2010-2017: RNN/LSTM golden age
   2017+: Transformers took over
   "Attention is All You Need" paper changed everything!

   But RNNs are still used:
   - On-device processing (smaller models)
   - Streaming data (online learning)
   - Time-series forecasting
   - When you need true sequential processing

🎓 You've mastered RNNs!
   This was the foundation of modern NLP.
   Now, Transformers build on these ideas!
""")

print("\n✅ RNN Basics Complete!")
print("Next: transfer_learning.py - Using pre-trained models")
