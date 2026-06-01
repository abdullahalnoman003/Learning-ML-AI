"""
🚀 TRANSFORMERS - The Revolution in Deep Learning
==================================================

What are Transformers?
----------------------
Transformers are THE breakthrough in AI (2017-present)!

Before Transformers: RNNs/LSTMs dominated NLP
- Sequential processing (slow!)
- Struggled with long sequences
- Vanishing gradients

Transformers changed everything:
- Parallel processing (fast!)
- Handle long sequences easily
- Attention mechanism (focus on relevant parts)
- State-of-the-art on almost all NLP tasks!

The Paper: "Attention Is All You Need" (2017)
- Google researchers
- Revolutionized NLP
- Foundation of modern AI

What Transformers Enabled:
---------------------------
- BERT (2018): Bidirectional understanding
- GPT-2/3/4 (2019-2023): Language generation
- ChatGPT (2022): Conversational AI
- Claude (2023): This conversation!
- T5: Text-to-text framework
- DALL-E, Stable Diffusion: Text-to-image
- AlphaFold: Protein structure prediction

Key Innovation: ATTENTION MECHANISM
------------------------------------
Instead of processing words sequentially, attend to ALL words simultaneously!

Example: "The animal didn't cross the street because IT was too tired"
- What does "IT" refer to?
- Humans: IT = animal (not street)
- Attention: Model learns to focus on "animal" when processing "IT"!

Core Components:
----------------
1. SELF-ATTENTION: How words relate to each other
2. MULTI-HEAD ATTENTION: Multiple attention patterns
3. POSITIONAL ENCODING: Where words are in sequence
4. FEED-FORWARD NETWORKS: Process each position
5. LAYER NORMALIZATION: Stabilize training
6. RESIDUAL CONNECTIONS: Help gradient flow

Let's understand transformers step by step!
"""

import numpy as np
import matplotlib.pyplot as plt

try:
    import tensorflow as tf
    from tensorflow import keras
    print("=" * 80)
    print("TRANSFORMERS - The Revolution in Deep Learning")
    print("=" * 80)
    print(f"TensorFlow version: {tf.__version__}")

    # Check if transformers library is available
    try:
        from transformers import pipeline, AutoTokenizer, TFAutoModel
        HAS_TRANSFORMERS = True
        print("✅ Hugging Face Transformers library available")
    except ImportError:
        HAS_TRANSFORMERS = False
        print("⚠️  Hugging Face Transformers not installed (optional)")
        print("   Install: pip install transformers")

except ImportError:
    print("Please install TensorFlow: pip install tensorflow")
    exit()

# ============================================================
# PART 1: Understanding Attention
# ============================================================
print("\n📌 PART 1: Understanding the Attention Mechanism")
print("-" * 80)

print("""
ATTENTION = "What should I focus on?"

Example sentence: "The cat sat on the mat"

When processing "sat":
- How much should we attend to "cat"? High! (subject)
- How much to "the"? Low (not important)
- How much to "mat"? Medium (object)

Attention computes these weights automatically!

Mathematical Intuition:
-----------------------
Attention(Q, K, V) = softmax(Q·Kᵀ / √d_k)·V

Where:
- Q = Query (what I'm looking for)
- K = Key (what I have)
- V = Value (actual content)

Think of it like a database:
- Query: Your search
- Keys: Index to search in
- Values: Content to retrieve
""")

# Simple attention example
print("\n🔹 Simple Attention Calculation:")

# Toy example: 3 words with 4-dim embeddings
word_embeddings = np.array([
    [1.0, 0.0, 0.5, 0.2],  # "the"
    [0.0, 1.0, 0.3, 0.8],  # "cat"
    [0.5, 0.5, 1.0, 0.1],  # "sat"
])

words = ["the", "cat", "sat"]
print(f"Words: {words}")
print(f"Embeddings shape: {word_embeddings.shape}")
print(f"\nWord vectors:")
for word, vec in zip(words, word_embeddings):
    print(f"  '{word}': {vec}")

# Compute attention for "sat" attending to all words
query = word_embeddings[2]  # "sat"
keys = word_embeddings
values = word_embeddings

print(f"\n🔹 Computing attention for 'sat':")
print(f"  Query (sat): {query}")

# Compute attention scores (dot product)
scores = np.dot(keys, query)
print(f"\n  Attention scores (before softmax):")
for word, score in zip(words, scores):
    print(f"    'sat' → '{word}': {score:.4f}")

# Apply softmax to get attention weights
attention_weights = np.exp(scores) / np.sum(np.exp(scores))
print(f"\n  Attention weights (after softmax):")
for word, weight in zip(words, attention_weights):
    print(f"    'sat' → '{word}': {weight:.4f} ({weight*100:.1f}%)")

# Compute weighted sum of values
context_vector = np.sum(attention_weights[:, np.newaxis] * values, axis=0)
print(f"\n  Context vector for 'sat': {context_vector}")
print(f"  💡 This captures relevant information from all words!")

# Visualize attention
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(attention_weights.reshape(1, -1), cmap='YlOrRd', aspect='auto')
ax.set_xticks(range(len(words)))
ax.set_xticklabels(words, fontsize=14, fontweight='bold')
ax.set_yticks([0])
ax.set_yticklabels(['sat'], fontsize=14, fontweight='bold')
ax.set_title('Attention Weights: "sat" attending to other words', fontsize=14, fontweight='bold')

# Add text annotations
for i, (word, weight) in enumerate(zip(words, attention_weights)):
    ax.text(i, 0, f'{weight:.2f}', ha='center', va='center',
            fontsize=16, fontweight='bold', color='black')

plt.colorbar(im, ax=ax, label='Attention Weight')
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/attention_weights.png', dpi=150)
print("\n✓ Saved visualization: attention_weights.png")

# ============================================================
# PART 2: Multi-Head Attention
# ============================================================
print("\n\n📌 PART 2: Multi-Head Attention")
print("-" * 80)

print("""
Why multiple attention heads?

Different heads learn different patterns:
- Head 1: Syntactic relationships (subject-verb)
- Head 2: Semantic relationships (synonyms)
- Head 3: Long-range dependencies
- Head 4: Local context

Example: "The bank is by the river"
- Head 1: "bank" → "is" (verb relationship)
- Head 2: "bank" → "river" (financial? or riverbank?)
- Multiple perspectives = better understanding!

Multi-Head Attention:
  MultiHead(Q,K,V) = Concat(head₁, head₂, ..., head_h)·W^O

  where head_i = Attention(Q·W^Q_i, K·W^K_i, V·W^V_i)
""")

# Demonstrate multi-head concept
num_heads = 4
print(f"\n🔹 Multi-Head Attention with {num_heads} heads:")

# Simulate different attention patterns for different heads
np.random.seed(42)
multi_head_patterns = []

for head in range(num_heads):
    # Each head has different attention pattern
    pattern = np.random.rand(len(words))
    pattern = pattern / pattern.sum()  # Normalize
    multi_head_patterns.append(pattern)

# Visualize
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for i, (ax, pattern) in enumerate(zip(axes, multi_head_patterns)):
    im = ax.imshow(pattern.reshape(1, -1), cmap='YlGnBu', aspect='auto')
    ax.set_xticks(range(len(words)))
    ax.set_xticklabels(words, fontsize=12, fontweight='bold')
    ax.set_yticks([0])
    ax.set_yticklabels(['sat'], fontsize=12, fontweight='bold')
    ax.set_title(f'Head {i+1} - Different Attention Pattern', fontsize=12, fontweight='bold')

    for j, (word, weight) in enumerate(zip(words, pattern)):
        ax.text(j, 0, f'{weight:.2f}', ha='center', va='center',
                fontsize=12, fontweight='bold')

    plt.colorbar(im, ax=ax)

plt.suptitle('Multi-Head Attention - Each Head Learns Different Patterns', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/multi_head_attention.png', dpi=150)
print("✓ Saved visualization: multi_head_attention.png")
print(f"  💡 {num_heads} different heads = {num_heads} different perspectives!")

# ============================================================
# PART 3: Transformer Architecture
# ============================================================
print("\n\n📌 PART 3: Complete Transformer Architecture")
print("-" * 80)

print("""
Full Transformer (Original):

ENCODER (understand input):
  Input → Embedding + Positional Encoding
  ↓
  Multi-Head Self-Attention
  ↓
  Add & Normalize
  ↓
  Feed-Forward Network
  ↓
  Add & Normalize
  ↓
  (Repeat N times)

DECODER (generate output):
  Output → Embedding + Positional Encoding
  ↓
  Masked Multi-Head Self-Attention
  ↓
  Add & Normalize
  ↓
  Multi-Head Cross-Attention (attend to encoder)
  ↓
  Add & Normalize
  ↓
  Feed-Forward Network
  ↓
  Add & Normalize
  ↓
  (Repeat N times)
  ↓
  Linear + Softmax → Prediction

Key Components:
1. Positional Encoding: Add position information
2. Layer Normalization: Stabilize training
3. Residual Connections: Help gradient flow
4. Feed-Forward: Process each position independently
""")

# Visualize architecture
print("\n🔹 Transformer Block Structure:")

fig, ax = plt.subplots(figsize=(10, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Draw components
components = [
    (5, 13, "Input Embeddings + Positional Encoding", 'lightblue'),
    (5, 11, "Multi-Head Self-Attention", 'lightgreen'),
    (5, 10, "Add & Normalize", 'lightyellow'),
    (5, 8.5, "Feed-Forward Network", 'lightcoral'),
    (5, 7.5, "Add & Normalize", 'lightyellow'),
    (5, 6, "Multi-Head Self-Attention", 'lightgreen'),
    (5, 5, "Add & Normalize", 'lightyellow'),
    (5, 3.5, "Feed-Forward Network", 'lightcoral'),
    (5, 2.5, "Add & Normalize", 'lightyellow'),
    (5, 1, "Output Layer", 'plum'),
]

for x, y, label, color in components:
    rect = plt.Rectangle((x-2, y-0.3), 4, 0.6, facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold')

# Draw arrows
arrow_positions = [(13, 11), (11, 10), (10, 8.5), (8.5, 7.5), (7.5, 6), (6, 5), (5, 3.5), (3.5, 2.5), (2.5, 1)]
for start, end in arrow_positions:
    ax.arrow(5, start, 0, -(start-end-0.3), head_width=0.3, head_length=0.2,
            fc='black', ec='black', linewidth=2)

# Add residual connections
ax.plot([7.5, 7.5, 2.5, 2.5], [11.3, 9.7, 9.7, 10.3], 'b--', linewidth=2, label='Residual Connection')
ax.plot([7.5, 7.5, 2.5, 2.5], [8.8, 7.2, 7.2, 7.8], 'b--', linewidth=2)

ax.set_title('Transformer Encoder Block', fontsize=16, fontweight='bold')
ax.legend(loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/transformer_architecture.png', dpi=150)
print("✓ Saved visualization: transformer_architecture.png")

# ============================================================
# PART 4: Positional Encoding
# ============================================================
print("\n\n📌 PART 4: Positional Encoding")
print("-" * 80)

print("""
Problem: Transformers process all words in parallel!
→ No inherent notion of word order

Solution: Add positional encoding!

PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

Where:
- pos = position in sequence
- i = dimension
- d_model = embedding dimension

Properties:
✓ Unique for each position
✓ Consistent across sequences
✓ Captures relative positions
✓ Smooth and continuous
""")

def get_positional_encoding(seq_len, d_model):
    """Generate positional encoding matrix"""
    position = np.arange(seq_len)[:, np.newaxis]
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))

    pos_encoding = np.zeros((seq_len, d_model))
    pos_encoding[:, 0::2] = np.sin(position * div_term)
    pos_encoding[:, 1::2] = np.cos(position * div_term)

    return pos_encoding

# Generate positional encoding
seq_length = 50
d_model = 128
pos_encoding = get_positional_encoding(seq_length, d_model)

print(f"\n  Positional encoding shape: {pos_encoding.shape}")
print(f"  (sequence_length, embedding_dimension)")

# Visualize
plt.figure(figsize=(12, 8))
plt.imshow(pos_encoding, cmap='RdBu', aspect='auto')
plt.xlabel('Embedding Dimension', fontsize=12)
plt.ylabel('Position in Sequence', fontsize=12)
plt.title('Positional Encoding Matrix', fontsize=14, fontweight='bold')
plt.colorbar(label='Value')
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/positional_encoding.png', dpi=150)
print("\n✓ Saved visualization: positional_encoding.png")
print("  💡 Each position has a unique pattern!")
print("  Sine/cosine waves at different frequencies")

# ============================================================
# PART 5: Using Pre-trained Transformers
# ============================================================
print("\n\n📌 PART 5: Using Pre-trained Transformers with Hugging Face")
print("-" * 80)

if HAS_TRANSFORMERS:
    print("""
Hugging Face 🤗 Transformers:
- Thousands of pre-trained models
- Easy to use API
- State-of-the-art performance
- Free and open-source!

Popular models:
- BERT: Bidirectional understanding
- GPT-2/3: Text generation
- T5: Text-to-text
- RoBERTa: Improved BERT
- DistilBERT: Faster, smaller BERT
""")

    print("\n🔹 Example 1: Sentiment Analysis")
    print("  Loading pre-trained sentiment analysis model...")

    try:
        # Sentiment analysis
        sentiment_pipeline = pipeline("sentiment-analysis")

        texts = [
            "I love this product! It's amazing!",
            "This is terrible. Waste of money.",
            "It's okay, nothing special."
        ]

        print("\n  Testing sentiment analysis:")
        for text in texts:
            result = sentiment_pipeline(text)[0]
            print(f"    '{text}'")
            print(f"      → {result['label']} (confidence: {result['score']*100:.1f}%)")

    except Exception as e:
        print(f"  ⚠️  Error: {e}")

    print("\n\n🔹 Example 2: Text Generation")
    print("  Loading GPT-2 for text generation...")

    try:
        # Text generation
        generator = pipeline("text-generation", model="gpt2")

        prompt = "Artificial intelligence is"
        print(f"\n  Prompt: '{prompt}'")
        print("  Generated text:")

        result = generator(prompt, max_length=50, num_return_sequences=1)[0]
        print(f"    {result['generated_text']}")

    except Exception as e:
        print(f"  ⚠️  Error: {e}")

    print("\n\n🔹 Example 3: Question Answering")
    print("  Loading BERT for question answering...")

    try:
        # Question answering
        qa_pipeline = pipeline("question-answering")

        context = """
        The Transformer is a deep learning model introduced in 2017.
        It is based primarily on the attention mechanism.
        Transformers have revolutionized natural language processing.
        """

        question = "When was the Transformer introduced?"

        print(f"\n  Context: {context.strip()}")
        print(f"\n  Question: {question}")

        result = qa_pipeline(question=question, context=context)
        print(f"  Answer: {result['answer']}")
        print(f"  Confidence: {result['score']*100:.1f}%")

    except Exception as e:
        print(f"  ⚠️  Error: {e}")

    print("\n\n🔹 Example 4: Named Entity Recognition")
    print("  Loading NER model...")

    try:
        # Named Entity Recognition
        ner_pipeline = pipeline("ner", aggregation_strategy="simple")

        text = "Elon Musk founded Tesla in California and later started SpaceX."
        print(f"\n  Text: {text}")
        print("  Entities found:")

        entities = ner_pipeline(text)
        for entity in entities:
            print(f"    {entity['word']}: {entity['entity_group']} (score: {entity['score']:.2f})")

    except Exception as e:
        print(f"  ⚠️  Error: {e}")

else:
    print("""
Install Hugging Face Transformers to use pre-trained models:

  pip install transformers

Then you can use thousands of pre-trained models:
- BERT, GPT-2, T5, RoBERTa, etc.
- Sentiment analysis, translation, QA, etc.
- State-of-the-art performance!
""")

# ============================================================
# PART 6: Building a Simple Transformer
# ============================================================
print("\n\n📌 PART 6: Building a Simple Transformer with Keras")
print("-" * 80)

print("""
Let's build a simplified transformer for text classification!

Components:
1. Token + Position Embedding
2. Multi-Head Attention
3. Feed-Forward Network
4. Classification Head
""")

class TransformerBlock(keras.layers.Layer):
    """A simple transformer block"""

    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):
        super(TransformerBlock, self).__init__()
        self.att = keras.layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=embed_dim
        )
        self.ffn = keras.Sequential([
            keras.layers.Dense(ff_dim, activation="relu"),
            keras.layers.Dense(embed_dim),
        ])
        self.layernorm1 = keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = keras.layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = keras.layers.Dropout(rate)
        self.dropout2 = keras.layers.Dropout(rate)

    def call(self, inputs, training=False):
        # Multi-head attention
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)  # Residual connection

        # Feed-forward network
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        return self.layernorm2(out1 + ffn_output)  # Residual connection

# Build model
vocab_size = 20000
max_length = 100
embed_dim = 32
num_heads = 2
ff_dim = 32

print(f"\n🔹 Building Transformer Model:")
print(f"  Vocabulary size: {vocab_size}")
print(f"  Max sequence length: {max_length}")
print(f"  Embedding dimension: {embed_dim}")
print(f"  Number of attention heads: {num_heads}")

inputs = keras.layers.Input(shape=(max_length,))
embedding_layer = keras.layers.Embedding(vocab_size, embed_dim)(inputs)
transformer_block = TransformerBlock(embed_dim, num_heads, ff_dim)(embedding_layer)
x = keras.layers.GlobalAveragePooling1D()(transformer_block)
x = keras.layers.Dropout(0.1)(x)
x = keras.layers.Dense(20, activation="relu")(x)
x = keras.layers.Dropout(0.1)(x)
outputs = keras.layers.Dense(2, activation="softmax")(x)

transformer_model = keras.Model(inputs=inputs, outputs=outputs)

print("\n✅ Transformer Model:")
transformer_model.summary()

print("""
  Key features:
  ✓ Multi-head attention (parallel attention patterns)
  ✓ Residual connections (help gradient flow)
  ✓ Layer normalization (stabilize training)
  ✓ Position-wise feed-forward (process each position)
""")

# ============================================================
# PART 7: Transformer Variants
# ============================================================
print("\n\n📌 PART 7: Famous Transformer Models")
print("-" * 80)

print("""
🏆 Transformer Family Tree:

2017: TRANSFORMER (Original)
  ↓
2018: BERT - Bidirectional Encoder
  - Masked language modeling
  - Bidirectional context
  - 110M-340M parameters
  - Use: Understanding tasks (classification, QA)

2018: GPT - Generative Pre-trained Transformer
  - Unidirectional (left-to-right)
  - Causal language modeling
  - 117M parameters
  - Use: Text generation

2019: GPT-2
  - Larger (1.5B parameters)
  - Better generation
  - "Text from the future"

2019: T5 - Text-to-Text Transfer Transformer
  - Everything is text-to-text
  - Translation, summarization, QA
  - 220M-11B parameters

2019: ALBERT - A Lite BERT
  - Parameter sharing
  - Smaller, faster
  - Similar performance

2019: RoBERTa - Robustly Optimized BERT
  - Better training
  - Improved performance
  - 125M-355M parameters

2019: DistilBERT
  - Distilled from BERT
  - 66M parameters (40% smaller)
  - 60% faster
  - 95% performance

2020: GPT-3
  - Massive (175B parameters!)
  - Few-shot learning
  - ChatGPT foundation

2021: CLIP - Contrastive Language-Image Pre-training
  - Text + Image understanding
  - Foundation for DALL-E

2022: ChatGPT
  - GPT-3.5 fine-tuned with RLHF
  - Conversational AI
  - Instruction following

2023: GPT-4
  - Multimodal (text + images)
  - Improved reasoning
  - Less hallucination

2023: Claude (Anthropic)
  - Constitutional AI
  - Long context (100K+ tokens)
  - Safety-focused

2023: LLaMA (Meta)
  - Open-source
  - Efficient
  - 7B-65B parameters

2023+: Many others
  - PaLM, Falcon, Mistral, Phi-2, etc.
""")

# Visualize timeline
fig, ax = plt.subplots(figsize=(14, 10))

models_timeline = [
    (2017, "Transformer\n(Original)", 1),
    (2018, "BERT", 2),
    (2018.3, "GPT", 2),
    (2019, "GPT-2", 3),
    (2019.3, "T5", 2.5),
    (2019.5, "RoBERTa", 2),
    (2020, "GPT-3", 4),
    (2021, "CLIP", 2.5),
    (2022, "ChatGPT", 4.5),
    (2023, "GPT-4", 5),
    (2023.3, "Claude", 4.5),
    (2023.5, "LLaMA", 3)
]

for year, name, importance in models_timeline:
    ax.scatter(year, importance, s=importance*200, alpha=0.6, c='blue', edgecolors='black', linewidth=2)
    ax.text(year, importance + 0.3, name, ha='center', fontsize=10, fontweight='bold')

ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Impact/Capabilities', fontsize=14, fontweight='bold')
ax.set_title('Transformer Models Timeline', fontsize=16, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xlim(2016.5, 2024)
ax.set_ylim(0, 6)
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/transformers_timeline.png', dpi=150)
print("\n✓ Saved visualization: transformers_timeline.png")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n🎯 WHY TRANSFORMERS MATTER")
print("=" * 80)
print("""
1. REVOLUTIONIZED AI:
   - State-of-the-art on almost ALL NLP tasks
   - Enabled ChatGPT, Claude, GPT-4
   - Scaled to 175B+ parameters
   - Multimodal (text, images, audio)

2. KEY INNOVATIONS:
   ✓ Attention mechanism (focus on relevant parts)
   ✓ Parallel processing (fast training!)
   ✓ Scalability (works with 100M-100B+ parameters)
   ✓ Transfer learning (pre-train once, fine-tune anywhere)
   ✓ Long-range dependencies (no vanishing gradients)

3. ADVANTAGES OVER RNNs:
   RNN/LSTM                    Transformer
   -----------                 -----------
   Sequential (slow)    →      Parallel (fast!)
   Vanishing gradients  →      Attention (no gradients issues)
   Limited context      →      Full context
   Hard to parallelize  →      GPU-friendly

4. REAL-WORLD IMPACT:
   - ChatGPT: 100M users in 2 months
   - Google Search: BERT improves results
   - Translation: Near human-level
   - Code generation: GitHub Copilot
   - Image generation: DALL-E, Midjourney
   - Protein folding: AlphaFold
   - Drug discovery: MolGPT

5. APPLICATIONS:
   📝 NLP:
   - Text classification
   - Sentiment analysis
   - Named entity recognition
   - Question answering
   - Text generation
   - Translation
   - Summarization

   🖼️  Vision:
   - Image classification (ViT)
   - Object detection (DETR)
   - Image generation (DALL-E)

   🎵 Audio:
   - Speech recognition
   - Music generation
   - Audio synthesis

   🧬 Science:
   - Protein structure (AlphaFold)
   - Molecule generation
   - Drug discovery

   🎮 Other:
   - Recommendation systems
   - Time series forecasting
   - Reinforcement learning (Decision Transformer)

📊 Performance Comparison:

Task: Text Classification
  Naive Bayes: ~75% accuracy
  SVM: ~80% accuracy
  CNN: ~85% accuracy
  LSTM: ~87% accuracy
  BERT: ~93% accuracy
  GPT-3: ~95% accuracy

Task: Machine Translation
  Statistical MT: BLEU ~30
  RNN: BLEU ~35
  LSTM: BLEU ~38
  Transformer: BLEU ~41+

🔑 Key Insights:

   1. Attention > Sequential Processing
      - See all tokens at once
      - Compute relationships in parallel
      - Scale to long sequences

   2. More data + More parameters = Better
      - GPT-3: 175B parameters, 45TB text
      - Scaling laws: performance improves predictably
      - "Bitter lesson": compute + data wins

   3. Transfer learning is key
      - Pre-train on massive data
      - Fine-tune on specific task
      - Few-shot learning possible!

   4. Multimodal future
      - CLIP: Text + Images
      - GPT-4: Text + Images
      - Future: Text + Image + Audio + Video

💡 Best Practices:

   1. START WITH PRE-TRAINED:
      ✓ Use Hugging Face models
      ✓ Fine-tune for your task
      ✓ Don't train from scratch!

   2. CHOOSE RIGHT MODEL:
      - Classification: BERT, RoBERTa
      - Generation: GPT-2, GPT-3
      - Everything: T5
      - Fast/small: DistilBERT, ALBERT

   3. OPTIMIZE:
      - Use smaller models when possible
      - Quantization (8-bit, 4-bit)
      - Distillation (teacher-student)
      - Pruning (remove weights)

   4. PROMPT ENGINEERING:
      - Clear instructions
      - Few-shot examples
      - Chain-of-thought prompting

🚀 What's Next?

   CURRENT TRENDS:
   - Larger models (GPT-4, PaLM-2)
   - Multimodal (text + image + audio)
   - Efficient transformers (Flash Attention)
   - Open-source (LLaMA, Falcon)

   FUTURE DIRECTIONS:
   - Sparse transformers (efficient)
   - Continual learning
   - Better reasoning
   - Longer context (100K+ tokens)
   - Alignment with human values

   LEARN MORE:
   - Hugging Face course (free!)
   - Fast.ai (practical deep learning)
   - OpenAI cookbook
   - Papers with Code
   - "Attention Is All You Need" paper

💡 Remember:
   "Transformers are not just for NLP anymore!"

   Originally for translation, now used for:
   - Vision (ViT)
   - Audio (Whisper)
   - Video (VideoGPT)
   - Protein folding (AlphaFold)
   - Reinforcement learning
   - Multi-modal tasks

   The attention mechanism is universal!

🎓 You've completed the Deep Learning Journey!
   From basic neural networks to transformers,
   you now understand the foundation of modern AI!

   The principles you learned:
   ✓ Forward pass & backpropagation
   ✓ CNNs for images
   ✓ RNNs for sequences
   ✓ Transfer learning
   ✓ Attention mechanism
   ✓ Transformers

   These power everything from ChatGPT to self-driving cars!

""")

print("\n" + "=" * 80)
print("🎉 CONGRATULATIONS! Phase 4 - Deep Learning Complete!")
print("=" * 80)
print("""
You've mastered:
  ✅ Neural networks from scratch
  ✅ Backpropagation mathematics
  ✅ TensorFlow & Keras
  ✅ CNNs for computer vision
  ✅ RNNs for sequences
  ✅ Transfer learning
  ✅ NLP fundamentals
  ✅ Transformers (state-of-the-art!)

Next steps:
  🚀 Build projects with real data
  🚀 Explore Hugging Face models
  🚀 Learn PyTorch (alternative to TensorFlow)
  🚀 Study research papers
  🚀 Contribute to open-source
  🚀 Build your own AI applications!

The future of AI is in your hands! 🌟
""")
