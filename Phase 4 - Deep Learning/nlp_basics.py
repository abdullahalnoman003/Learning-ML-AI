"""
📝 NLP BASICS - Text Processing and Natural Language Processing
================================================================

What is NLP (Natural Language Processing)?
-------------------------------------------
NLP is teaching computers to understand human language!

Computers understand numbers, not words.
Our challenge: Convert text → numbers that preserve meaning!

Examples of NLP:
- Chatbots (ChatGPT, Siri)
- Translation (Google Translate)
- Sentiment analysis (Is this review positive?)
- Text summarization
- Question answering
- Autocomplete
- Spam detection

The NLP Pipeline:
-----------------
1. TEXT PREPROCESSING: Clean and normalize
2. TOKENIZATION: Split into words/tokens
3. VECTORIZATION: Convert to numbers
4. MODEL: Neural network processes numbers
5. OUTPUT: Classification, generation, etc.

Key Concepts:
-------------
- Tokens: Individual words or subwords
- Vocabulary: All unique tokens
- Embeddings: Dense vector representations of words
- Context: Meaning depends on surrounding words!

Let's learn how to process text for deep learning!
"""

import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter

try:
    import tensorflow as tf
    from tensorflow import keras
    print("=" * 80)
    print("NLP BASICS - Text Processing and Natural Language Processing")
    print("=" * 80)
    print(f"TensorFlow version: {tf.__version__}")
except ImportError:
    print("Please install TensorFlow: pip install tensorflow")
    exit()

# ============================================================
# PART 1: Text Preprocessing
# ============================================================
print("\n📌 PART 1: Text Preprocessing")
print("-" * 80)

print("""
Raw text is messy! We need to clean it:
- Convert to lowercase
- Remove punctuation
- Remove numbers
- Remove extra spaces
- Handle special characters

Let's see examples:
""")

# Sample texts
raw_texts = [
    "I LOVE this movie!!! It's absolutely amazing 😊",
    "This is terrible... Worst film ever!!!",
    "Not bad, could be better though.",
    "Best movie I've seen in 2024! 5/5 stars ⭐⭐⭐⭐⭐"
]

print("\n🔹 Original Texts:")
for i, text in enumerate(raw_texts, 1):
    print(f"  {i}. {text}")

def clean_text(text):
    """Basic text cleaning"""
    # Convert to lowercase
    text = text.lower()
    # Remove emojis and special characters (keep letters, numbers, spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Remove extra spaces
    text = ' '.join(text.split())
    return text

print("\n🔹 Cleaned Texts:")
cleaned_texts = [clean_text(text) for text in raw_texts]
for i, text in enumerate(cleaned_texts, 1):
    print(f"  {i}. {text}")

print("\n💡 Cleaning removes noise and standardizes text!")

# ============================================================
# PART 2: Tokenization
# ============================================================
print("\n\n📌 PART 2: Tokenization - Breaking Text into Pieces")
print("-" * 80)

print("""
Tokenization = Splitting text into tokens (words, subwords, characters)

Types:
1. Word tokenization: "I love NLP" → ["I", "love", "NLP"]
2. Character tokenization: "Hi" → ["H", "i"]
3. Subword tokenization: "unhappiness" → ["un", "happiness"]

We'll focus on word tokenization!
""")

def tokenize(text):
    """Simple word tokenization"""
    return text.split()

print("\n🔹 Tokenization Example:")
example_text = cleaned_texts[0]
tokens = tokenize(example_text)
print(f"  Text: {example_text}")
print(f"  Tokens: {tokens}")
print(f"  Number of tokens: {len(tokens)}")

# Tokenize all texts
all_tokens = [tokenize(text) for text in cleaned_texts]
print(f"\n🔹 All Tokenized:")
for i, tokens in enumerate(all_tokens, 1):
    print(f"  {i}. {tokens}")

# ============================================================
# PART 3: Building Vocabulary
# ============================================================
print("\n\n📌 PART 3: Building Vocabulary")
print("-" * 80)

print("""
Vocabulary = Set of all unique words in your corpus

Example:
  Texts: ["I love NLP", "I love coding"]
  Vocabulary: {"I", "love", "NLP", "coding"}
  Vocab size: 4 words
""")

# Build vocabulary
all_words = []
for tokens in all_tokens:
    all_words.extend(tokens)

word_counts = Counter(all_words)
vocab = sorted(word_counts.keys())

print(f"\n🔹 Vocabulary:")
print(f"  Total words (with repetition): {len(all_words)}")
print(f"  Unique words (vocabulary): {len(vocab)}")
print(f"\n  Vocabulary (sorted): {vocab}")

print(f"\n🔹 Word Frequencies:")
for word, count in word_counts.most_common(10):
    print(f"  '{word}': {count}")

# Visualize word frequencies
plt.figure(figsize=(12, 6))
words, counts = zip(*word_counts.most_common(15))
plt.bar(words, counts, color='skyblue', edgecolor='black')
plt.xlabel('Words', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Most Common Words', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/nlp_word_frequency.png', dpi=150)
print("\n✓ Saved visualization: nlp_word_frequency.png")

# ============================================================
# PART 4: Text Vectorization Methods
# ============================================================
print("\n\n📌 PART 4: Converting Text to Numbers")
print("-" * 80)

print("""
How to represent text as numbers?

1. ONE-HOT ENCODING:
   - Each word = binary vector
   - Vector length = vocabulary size
   - "love" → [0, 0, 1, 0, 0, ...]
   - Problem: High-dimensional, no semantics

2. BAG OF WORDS (BoW):
   - Count word occurrences
   - Ignores order!
   - "I love love NLP" → [1, 2, 1]
   - Problem: Loses word order

3. TF-IDF (Term Frequency-Inverse Document Frequency):
   - Weights words by importance
   - Rare words = higher weight
   - Common words (the, is) = lower weight

4. WORD EMBEDDINGS (Best!):
   - Dense vectors (50-300 dimensions)
   - Captures semantic meaning
   - Similar words → similar vectors
   - We'll use this!

Let's see each method!
""")

# Method 1: One-Hot Encoding
print("\n🔹 Method 1: One-Hot Encoding")

# Create word to index mapping
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

print(f"  Vocabulary size: {len(vocab)}")
print(f"  Word to Index mapping (first 10):")
for word, idx in list(word_to_idx.items())[:10]:
    print(f"    '{word}' → {idx}")

# One-hot encode a word
example_word = "love"
one_hot = np.zeros(len(vocab))
one_hot[word_to_idx[example_word]] = 1

print(f"\n  One-hot encoding of '{example_word}':")
print(f"  {one_hot[:15]}... (showing first 15)")
print(f"  Vector length: {len(one_hot)}")
print(f"  💡 Sparse! Only 1 position is 1, rest are 0")

# Method 2: Bag of Words
print("\n\n🔹 Method 2: Bag of Words (BoW)")

def text_to_bow(text, word_to_idx):
    """Convert text to bag of words vector"""
    bow = np.zeros(len(word_to_idx))
    tokens = tokenize(clean_text(text))
    for token in tokens:
        if token in word_to_idx:
            bow[word_to_idx[token]] += 1
    return bow

example_text = "I love this movie love"
bow_vector = text_to_bow(example_text, word_to_idx)

print(f"  Text: {example_text}")
print(f"  BoW vector: {bow_vector[:15]}... (showing first 15)")
print(f"  💡 Counts occurrences of each word")

# Show non-zero entries
nonzero_idx = np.nonzero(bow_vector)[0]
print(f"\n  Non-zero entries:")
for idx in nonzero_idx:
    word = idx_to_word[idx]
    count = int(bow_vector[idx])
    print(f"    '{word}': {count}")

# Method 3: TF-IDF
print("\n\n🔹 Method 3: TF-IDF (Term Frequency-Inverse Document Frequency)")

print("""
  TF-IDF = TF × IDF

  TF (Term Frequency): How often word appears in document
  IDF (Inverse Document Frequency): How rare the word is across all documents

  Formula:
    TF(t,d) = count of t in d / total words in d
    IDF(t) = log(total documents / documents containing t)
    TF-IDF(t,d) = TF(t,d) × IDF(t)

  Result: Common words (the, is) get low scores, rare meaningful words get high scores!
""")

from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "I love machine learning",
    "I love deep learning",
    "Machine learning is awesome",
    "Deep learning with neural networks"
]

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

print(f"\n  TF-IDF Matrix shape: {tfidf_matrix.shape}")
print(f"  ({len(documents)} documents, {len(tfidf.vocabulary_)} words)")

print(f"\n  Vocabulary: {list(tfidf.vocabulary_.keys())}")

print(f"\n  TF-IDF scores for first document:")
doc_vector = tfidf_matrix[0].toarray()[0]
feature_names = tfidf.get_feature_names_out()
word_scores = [(word, score) for word, score in zip(feature_names, doc_vector) if score > 0]
word_scores.sort(key=lambda x: x[1], reverse=True)
for word, score in word_scores:
    print(f"    '{word}': {score:.4f}")

# ============================================================
# PART 5: Word Embeddings
# ============================================================
print("\n\n📌 PART 5: Word Embeddings - The Modern Way")
print("-" * 80)

print("""
Word embeddings = Dense vector representations

Key properties:
1. Low-dimensional (50-300 vs vocabulary size ~10,000+)
2. Learned from data
3. Similar words → similar vectors
4. Captures semantic relationships!

Famous example:
  king - man + woman ≈ queen
  Paris - France + Italy ≈ Rome

Two approaches:
1. Pre-trained: Word2Vec, GloVe, FastText
2. Learned: Embedding layer in neural network
""")

print("\n🔹 Creating Embedding Layer in Keras:")

# Parameters
vocab_size = 1000  # Size of vocabulary
embedding_dim = 100  # Dimension of embedding vectors

# Create embedding layer
embedding_layer = keras.layers.Embedding(
    input_dim=vocab_size,
    output_dim=embedding_dim,
    input_length=10  # Max sequence length
)

print(f"  Vocabulary size: {vocab_size}")
print(f"  Embedding dimension: {embedding_dim}")
print(f"  Parameters: {vocab_size * embedding_dim:,}")
print(f"\n  💡 Each word → {embedding_dim}D vector (learned during training!)")

# Example: Convert sequence of word indices to embeddings
word_indices = np.array([[1, 5, 10, 3, 7, 2, 0, 0, 0, 0]])  # Padded sequence
embeddings = embedding_layer(word_indices)

print(f"\n  Input shape: {word_indices.shape}")
print(f"  Output shape: {embeddings.shape}")
print(f"  (batch_size, sequence_length, embedding_dim)")

# ============================================================
# PART 6: Text Classification with Embeddings
# ============================================================
print("\n\n📌 PART 6: Complete Text Classification Example")
print("-" * 80)

print("""
Task: Classify movie reviews as positive or negative

Pipeline:
1. Tokenize text
2. Convert to sequences of word indices
3. Pad sequences to same length
4. Embedding layer (text → vectors)
5. LSTM/GRU (capture context)
6. Dense layer (classification)

Let's build it!
""")

# Sample dataset
train_texts = [
    "this movie is great i love it",
    "amazing film best ever",
    "fantastic performance brilliant",
    "terrible movie waste of time",
    "awful boring horrible",
    "worst film i have ever seen",
    "excellent acting superb",
    "bad plot poor execution",
    "wonderful story masterpiece",
    "disappointing weak terrible"
]

train_labels = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]  # 1=positive, 0=negative

print(f"\n🔹 Training Data:")
print(f"  {len(train_texts)} samples")
for text, label in zip(train_texts[:3], train_labels[:3]):
    sentiment = "Positive" if label == 1 else "Negative"
    print(f"    '{text}' → {sentiment}")

# Use Keras Tokenizer
print("\n🔹 Tokenization with Keras:")
tokenizer = keras.preprocessing.text.Tokenizer(num_words=100, oov_token="<OOV>")
tokenizer.fit_on_texts(train_texts)

print(f"  Vocabulary size: {len(tokenizer.word_index)}")
print(f"  Word index (first 15):")
for word, idx in list(tokenizer.word_index.items())[:15]:
    print(f"    '{word}' → {idx}")

# Convert texts to sequences
sequences = tokenizer.texts_to_sequences(train_texts)
print(f"\n🔹 Text to Sequences:")
print(f"  Text: '{train_texts[0]}'")
print(f"  Sequence: {sequences[0]}")

# Pad sequences
max_length = 10
padded_sequences = keras.preprocessing.sequence.pad_sequences(
    sequences,
    maxlen=max_length,
    padding='post',
    truncating='post'
)

print(f"\n🔹 Padding:")
print(f"  Max length: {max_length}")
print(f"  Original: {sequences[0]}")
print(f"  Padded: {padded_sequences[0]}")
print(f"  Shape: {padded_sequences.shape}")

# Build model
print("\n🔹 Building Text Classification Model:")

model = keras.Sequential([
    keras.layers.Embedding(input_dim=100, output_dim=16, input_length=max_length),
    keras.layers.GlobalAveragePooling1D(),  # Average embeddings
    keras.layers.Dense(24, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

print("\n✅ Model Architecture:")
model.summary()

print("""
  Layer breakdown:
  1. Embedding: Words → 16D vectors
  2. GlobalAveragePooling: Average all word vectors → single vector
  3. Dense(24): Hidden layer
  4. Dense(1): Binary classification (positive/negative)
""")

# Compile and train
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("\n🏋️ Training...")
history = model.fit(
    padded_sequences,
    np.array(train_labels),
    epochs=50,
    verbose=0
)

print(f"✅ Training complete!")
print(f"  Final accuracy: {history.history['accuracy'][-1]*100:.1f}%")

# Test on new examples
print("\n\n🔹 Testing on New Reviews:")
test_texts = [
    "this is an amazing movie",
    "terrible film worst ever",
    "brilliant performance love it"
]

test_sequences = tokenizer.texts_to_sequences(test_texts)
test_padded = keras.preprocessing.sequence.pad_sequences(
    test_sequences,
    maxlen=max_length,
    padding='post'
)

predictions = model.predict(test_padded, verbose=0)

for text, pred in zip(test_texts, predictions):
    sentiment = "Positive" if pred[0] > 0.5 else "Negative"
    confidence = pred[0] if pred[0] > 0.5 else 1 - pred[0]
    print(f"  '{text}'")
    print(f"    → {sentiment} (confidence: {confidence*100:.1f}%)")

# ============================================================
# PART 7: Visualizing Word Embeddings
# ============================================================
print("\n\n📌 PART 7: Visualizing Word Embeddings")
print("-" * 80)

print("""
Word embeddings are high-dimensional vectors.
We can visualize them using dimensionality reduction!

Techniques:
- PCA (Principal Component Analysis): Linear
- t-SNE: Non-linear, preserves local structure
""")

# Get learned embeddings
embedding_weights = model.layers[0].get_weights()[0]
print(f"\n  Embedding matrix shape: {embedding_weights.shape}")
print(f"  ({embedding_weights.shape[0]} words, {embedding_weights.shape[1]} dimensions)")

# Get words we care about
words_to_plot = ['great', 'love', 'amazing', 'terrible', 'awful', 'worst', 'excellent', 'bad']
word_indices = [tokenizer.word_index.get(word, 0) for word in words_to_plot]
word_vectors = embedding_weights[word_indices]

# Use PCA to reduce to 2D
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
vectors_2d = pca.fit_transform(word_vectors)

# Visualize
plt.figure(figsize=(12, 8))
plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], s=200, alpha=0.6, c='blue', edgecolors='black', linewidth=2)

for i, word in enumerate(words_to_plot):
    plt.annotate(word, (vectors_2d[i, 0], vectors_2d[i, 1]),
                fontsize=14, fontweight='bold',
                xytext=(5, 5), textcoords='offset points')

plt.xlabel('PC1', fontsize=12)
plt.ylabel('PC2', fontsize=12)
plt.title('Word Embeddings Visualization (2D)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/nlp_embeddings.png', dpi=150)
print("\n✓ Saved visualization: nlp_embeddings.png")
print("  💡 Similar words cluster together!")
print("  Positive words on one side, negative on the other!")

# ============================================================
# PART 8: Common NLP Tasks
# ============================================================
print("\n\n📌 PART 8: Common NLP Tasks")
print("-" * 80)

print("""
📋 NLP Task Categories:

1. TEXT CLASSIFICATION:
   - Sentiment analysis
   - Spam detection
   - Topic classification
   - Intent detection

2. SEQUENCE LABELING:
   - Named Entity Recognition (NER)
   - Part-of-Speech (POS) tagging
   - Keyword extraction

3. TEXT GENERATION:
   - Machine translation
   - Text summarization
   - Question answering
   - Dialogue generation

4. TEXT SIMILARITY:
   - Semantic similarity
   - Duplicate detection
   - Document retrieval

5. INFORMATION EXTRACTION:
   - Relation extraction
   - Event extraction
   - Knowledge base population
""")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n🎯 WHY NLP BASICS MATTER")
print("=" * 80)
print("""
1. FOUNDATION OF MODERN AI:
   - ChatGPT, BERT, GPT-4 built on these principles
   - Understanding basics helps you use advanced models
   - Text is everywhere!

2. CORE CONCEPTS MASTERED:
   ✓ Text preprocessing
   ✓ Tokenization
   ✓ Vocabulary building
   ✓ Vectorization methods (BoW, TF-IDF)
   ✓ Word embeddings
   ✓ Text classification pipeline

3. REAL-WORLD APPLICATIONS:
   - Customer service: Chatbots
   - Social media: Sentiment analysis
   - Search engines: Document ranking
   - Healthcare: Clinical note analysis
   - Legal: Contract analysis
   - Finance: News sentiment trading

4. WHY EMBEDDINGS WIN:
   One-Hot Encoding:
   - Huge dimensions (vocab size)
   - No semantic meaning
   - Sparse (mostly zeros)

   Word Embeddings:
   - Small dimensions (50-300)
   - Captures semantics!
   - Dense (all values meaningful)

   Example:
   "king" - "man" + "woman" ≈ "queen"
   Vectors encode relationships!

5. EVOLUTION OF NLP:
   2013: Word2Vec (static embeddings)
   2014: GloVe (better static embeddings)
   2018: BERT (contextual embeddings!)
   2019: GPT-2 (large language models)
   2022: ChatGPT (instruction following)
   2023+: GPT-4, Claude (multimodal)

   But all build on these fundamentals!

📊 Key Insights:

   1. Text → Numbers
      - Computers need numbers
      - Preserve meaning!
      - Embeddings capture semantics

   2. Context Matters
      - "bank" (river) vs "bank" (money)
      - Word meaning depends on context
      - Modern models (BERT) handle this!

   3. Size vs Quality
      - More data = better embeddings
      - Transfer learning helps
      - Pre-trained embeddings save time

🔑 Best Practices:

   1. PREPROCESSING:
      ✓ Lowercase (usually)
      ✓ Remove punctuation (depends on task)
      ✓ Handle special cases
      × Don't over-clean (lose information)

   2. TOKENIZATION:
      ✓ Consider subword tokenization
      ✓ Handle out-of-vocabulary words
      ✓ Keep vocabulary manageable

   3. EMBEDDINGS:
      ✓ Use pre-trained when possible
      ✓ Fine-tune for your domain
      ✓ Dimension 50-300 usually sufficient

   4. MODELS:
      ✓ Start simple (embeddings + LSTM)
      ✓ Add complexity if needed
      ✓ Consider Transformers (next file!)

🚀 What's Next?

   IMPROVEMENTS:
   - Bidirectional LSTM
   - Attention mechanisms
   - Multi-layer models
   - Dropout for regularization

   ADVANCED TOPICS:
   - Transfer learning (BERT, GPT)
   - Transformers (revolutionary!)
   - Few-shot learning
   - Prompt engineering

   TOOLS:
   - Hugging Face Transformers
   - spaCy for preprocessing
   - NLTK for linguistic features
   - Sentence-BERT for similarity

💡 Remember:
   "The quality of your text preprocessing determines
    the quality of your model's understanding!"

   Garbage in = Garbage out
   Clean data = Better results

🎓 You've mastered NLP basics!
   This is your foundation for understanding modern NLP.
   Next: Transformers - the current state-of-the-art!
""")

print("\n✅ NLP Basics Complete!")
print("Next: transformers_intro.py - The revolution in NLP!")
