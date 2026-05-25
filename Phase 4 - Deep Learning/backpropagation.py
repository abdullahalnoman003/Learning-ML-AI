"""
🔄 BACKPROPAGATION EXPLAINED - The Heart of Deep Learning
==========================================================

What is Backpropagation?
------------------------
Backpropagation = "Backward Propagation of Errors"

It's the algorithm that teaches neural networks by:
1. Calculating how much each weight contributed to the error
2. Adjusting weights to reduce that error

Think of it like this:
- You make a mistake on a test
- You trace back to find WHERE you went wrong
- You learn from that specific mistake
- You adjust your understanding

Why is it called "back"propagation?
- Forward pass: Input → Output (make predictions)
- Backward pass: Output → Input (calculate gradients)
- We propagate errors BACKWARD through the network!

The Math (Don't Panic!):
------------------------
It's all based on the CHAIN RULE from calculus:

If y = f(g(x)), then dy/dx = (df/dg) × (dg/dx)

For neural networks:
- We have nested functions (layers)
- Chain rule lets us calculate gradients through all layers
- Each layer's gradient depends on the next layer's gradient

We'll visualize this step-by-step!
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

print("=" * 80)
print("BACKPROPAGATION EXPLAINED - Understanding the Math Visually")
print("=" * 80)

# ============================================================
# PART 1: Simple Example - One Neuron
# ============================================================
print("\n📌 PART 1: Backpropagation with ONE Neuron")
print("-" * 80)

print("""
Let's start SIMPLE - just one neuron!

Network:
  x → [w, b] → z = w*x + b → a = σ(z) → Loss

Where:
  x = input
  w = weight
  b = bias
  z = linear output
  σ = sigmoid activation
  a = activated output
  Loss = (a - y)²  (Mean Squared Error)

Goal: Calculate dLoss/dw and dLoss/db
(How does changing w or b affect the loss?)
""")

# Example values
x = 1.5
w = 0.5
b = 0.2
y_true = 1.0  # Target output

# Forward pass
z = w * x + b
print(f"Forward Pass:")
print(f"  x = {x}")
print(f"  w = {w}, b = {b}")
print(f"  z = w*x + b = {w}*{x} + {b} = {z}")

# Sigmoid activation
a = 1 / (1 + np.exp(-z))
print(f"  a = sigmoid(z) = {a:.4f}")

# Loss
loss = (a - y_true) ** 2
print(f"  Loss = (a - y_true)² = ({a:.4f} - {y_true})² = {loss:.6f}")

print(f"\n\nBackward Pass (Chain Rule):")
print(f"-" * 80)

# Backward pass - Chain rule!
# dLoss/dw = dLoss/da × da/dz × dz/dw

# Step 1: dLoss/da
dLoss_da = 2 * (a - y_true)
print(f"Step 1: dLoss/da = 2(a - y_true) = 2({a:.4f} - {y_true}) = {dLoss_da:.4f}")
print(f"        → This tells us: 'How does loss change when activation changes?'")

# Step 2: da/dz (sigmoid derivative)
da_dz = a * (1 - a)
print(f"\nStep 2: da/dz = a(1-a) = {a:.4f}(1-{a:.4f}) = {da_dz:.4f}")
print(f"        → This tells us: 'How does activation change when z changes?'")

# Step 3: dz/dw
dz_dw = x
print(f"\nStep 3: dz/dw = x = {x}")
print(f"        → This tells us: 'How does z change when weight changes?'")

# Chain them together!
dLoss_dw = dLoss_da * da_dz * dz_dw
print(f"\n🎯 Final: dLoss/dw = dLoss/da × da/dz × dz/dw")
print(f"                    = {dLoss_da:.4f} × {da_dz:.4f} × {dz_dw}")
print(f"                    = {dLoss_dw:.4f}")

# Similarly for bias
dz_db = 1
dLoss_db = dLoss_da * da_dz * dz_db
print(f"\n         dLoss/db = {dLoss_da:.4f} × {da_dz:.4f} × {dz_db}")
print(f"                    = {dLoss_db:.4f}")

# Update weights
learning_rate = 0.1
w_new = w - learning_rate * dLoss_dw
b_new = b - learning_rate * dLoss_db

print(f"\n\n📊 Gradient Descent Update:")
print(f"  Old weight: w = {w}")
print(f"  Gradient: dLoss/dw = {dLoss_dw:.4f}")
print(f"  New weight: w = {w} - {learning_rate} × {dLoss_dw:.4f} = {w_new:.4f}")
print(f"\n  Old bias: b = {b}")
print(f"  Gradient: dLoss/db = {dLoss_db:.4f}")
print(f"  New bias: b = {b} - {learning_rate} × {dLoss_db:.4f} = {b_new:.4f}")

# Verify loss decreased
z_new = w_new * x + b_new
a_new = 1 / (1 + np.exp(-z_new))
loss_new = (a_new - y_true) ** 2

print(f"\n✅ Verification:")
print(f"  Old loss: {loss:.6f}")
print(f"  New loss: {loss_new:.6f}")
print(f"  Improvement: {loss - loss_new:.6f}")
print(f"  Loss decreased! We moved in the right direction! 🎉")

# ============================================================
# PART 2: Two-Layer Network
# ============================================================
print("\n\n📌 PART 2: Backpropagation with TWO Layers")
print("-" * 80)

print("""
Now let's add complexity - two layers!

Network Architecture:
  Input → Hidden Layer → Output Layer → Loss

Mathematical Flow:
  x → [w1,b1] → z1 = w1*x + b1 → a1 = σ(z1)
    → [w2,b2] → z2 = w2*a1 + b2 → a2 = σ(z2)
    → Loss = (a2 - y)²

Challenge: How do we update w1 and b1?
They're hidden deep in the network!

Answer: CHAIN RULE! We backpropagate the error!
""")

# Network with 2 layers
x_input = np.array([[2.0], [3.0]])  # 2 inputs
y_target = np.array([[1.0]])  # 1 output

# Layer 1: Input (2) → Hidden (3)
np.random.seed(42)
W1 = np.random.randn(2, 3) * 0.5  # 2 inputs, 3 hidden neurons
b1 = np.zeros((1, 3))

# Layer 2: Hidden (3) → Output (1)
W2 = np.random.randn(3, 1) * 0.5  # 3 hidden, 1 output
b2 = np.zeros((1, 1))

print(f"Network Architecture:")
print(f"  Input layer: 2 neurons")
print(f"  Hidden layer: 3 neurons")
print(f"  Output layer: 1 neuron")
print(f"\nParameter shapes:")
print(f"  W1: {W1.shape}, b1: {b1.shape}")
print(f"  W2: {W2.shape}, b2: {b2.shape}")

# Forward pass
print(f"\n\n🎯 FORWARD PASS:")
print(f"-" * 80)

z1 = np.dot(x_input.T, W1) + b1
a1 = 1 / (1 + np.exp(-z1))  # Sigmoid
print(f"Hidden layer:")
print(f"  z1 = x·W1 + b1")
print(f"  a1 = sigmoid(z1) = {a1}")

z2 = np.dot(a1, W2) + b2
a2 = 1 / (1 + np.exp(-z2))  # Sigmoid
print(f"\nOutput layer:")
print(f"  z2 = a1·W2 + b2")
print(f"  a2 = sigmoid(z2) = {a2[0][0]:.4f}")

loss = (a2 - y_target) ** 2
print(f"\nLoss = (a2 - y_target)² = {loss[0][0]:.6f}")

# Backward pass
print(f"\n\n🔄 BACKWARD PASS (Backpropagation):")
print(f"-" * 80)

print(f"\nStep 1: Output Layer Gradients")
print(f"  We start from the loss and work backward!")

# Output layer gradients
dLoss_da2 = 2 * (a2 - y_target)
print(f"  dLoss/da2 = {dLoss_da2[0][0]:.4f}")

da2_dz2 = a2 * (1 - a2)
print(f"  da2/dz2 = {da2_dz2[0][0]:.4f}")

dLoss_dz2 = dLoss_da2 * da2_dz2
print(f"  dLoss/dz2 = dLoss/da2 × da2/dz2 = {dLoss_dz2[0][0]:.4f}")

# Gradients for W2 and b2
dLoss_dW2 = np.dot(a1.T, dLoss_dz2)
dLoss_db2 = np.sum(dLoss_dz2, axis=0, keepdims=True)

print(f"\n  dLoss/dW2 = a1ᵀ · dLoss/dz2")
print(f"  dLoss/db2 = sum(dLoss/dz2)")

print(f"\nStep 2: Hidden Layer Gradients")
print(f"  Now we BACKPROPAGATE the error to the hidden layer!")

# Backpropagate to hidden layer
dLoss_da1 = np.dot(dLoss_dz2, W2.T)
print(f"  dLoss/da1 = dLoss/dz2 · W2ᵀ (backpropagating error!)")

da1_dz1 = a1 * (1 - a1)
print(f"  da1/dz1 = a1(1-a1) (sigmoid derivative)")

dLoss_dz1 = dLoss_da1 * da1_dz1
print(f"  dLoss/dz1 = dLoss/da1 × da1/dz1")

# Gradients for W1 and b1
dLoss_dW1 = np.dot(x_input, dLoss_dz1)
dLoss_db1 = np.sum(dLoss_dz1, axis=0, keepdims=True)

print(f"\n  dLoss/dW1 = xᵀ · dLoss/dz1")
print(f"  dLoss/db1 = sum(dLoss/dz1)")

print(f"\n✅ All gradients calculated!")
print(f"   We can now update ALL weights using gradient descent!")

# ============================================================
# PART 3: Visual Representation
# ============================================================
print("\n\n📌 PART 3: Visualizing Backpropagation")
print("-" * 80)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# Forward pass visualization
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 6)
ax1.axis('off')
ax1.set_title('FORWARD PASS - Data flows forward', fontsize=16, fontweight='bold', pad=20)

# Draw nodes
input_y = 3
hidden_y = 3
output_y = 3

# Input layer
ax1.add_patch(FancyBboxPatch((0.5, input_y-0.3), 1, 0.6, boxstyle="round,pad=0.1",
                             edgecolor='blue', facecolor='lightblue', linewidth=3))
ax1.text(1, input_y, 'Input\nx', ha='center', va='center', fontsize=12, fontweight='bold')

# Hidden layer
for i in range(3):
    y_pos = input_y + (i-1)*1.2
    ax1.add_patch(FancyBboxPatch((3, y_pos-0.3), 1, 0.6, boxstyle="round,pad=0.1",
                                 edgecolor='green', facecolor='lightgreen', linewidth=3))
    ax1.text(3.5, y_pos, f'h{i+1}', ha='center', va='center', fontsize=11, fontweight='bold')

# Output layer
ax1.add_patch(FancyBboxPatch((6, output_y-0.3), 1, 0.6, boxstyle="round,pad=0.1",
                             edgecolor='red', facecolor='lightcoral', linewidth=3))
ax1.text(6.5, output_y, 'Output\na', ha='center', va='center', fontsize=12, fontweight='bold')

# Loss
ax1.add_patch(FancyBboxPatch((8.5, output_y-0.3), 1, 0.6, boxstyle="round,pad=0.1",
                             edgecolor='purple', facecolor='plum', linewidth=3))
ax1.text(9, output_y, 'Loss', ha='center', va='center', fontsize=12, fontweight='bold')

# Forward arrows
arrow_style = dict(arrowstyle='->', lw=3, color='black')
ax1.annotate('', xy=(3, 3), xytext=(1.5, 3), arrowprops=arrow_style)
ax1.annotate('', xy=(6, 3), xytext=(4, 3), arrowprops=arrow_style)
ax1.annotate('', xy=(8.5, 3), xytext=(7, 3), arrowprops=arrow_style)

# Labels
ax1.text(2.25, 3.5, 'W1, b1', ha='center', fontsize=10, style='italic')
ax1.text(5, 3.5, 'W2, b2', ha='center', fontsize=10, style='italic')
ax1.text(1, 5, '1. Calculate predictions', fontsize=12, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Backward pass visualization
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 6)
ax2.axis('off')
ax2.set_title('BACKWARD PASS - Gradients flow backward', fontsize=16, fontweight='bold', pad=20)

# Draw nodes (same positions)
ax2.add_patch(FancyBboxPatch((0.5, input_y-0.3), 1, 0.6, boxstyle="round,pad=0.1",
                             edgecolor='blue', facecolor='lightblue', linewidth=3))
ax2.text(1, input_y, 'Input\nx', ha='center', va='center', fontsize=12, fontweight='bold')

for i in range(3):
    y_pos = input_y + (i-1)*1.2
    ax2.add_patch(FancyBboxPatch((3, y_pos-0.3), 1, 0.6, boxstyle="round,pad=0.1",
                                 edgecolor='green', facecolor='lightgreen', linewidth=3))
    ax2.text(3.5, y_pos, f'h{i+1}', ha='center', va='center', fontsize=11, fontweight='bold')

ax2.add_patch(FancyBboxPatch((6, output_y-0.3), 1, 0.6, boxstyle="round,pad=0.1",
                             edgecolor='red', facecolor='lightcoral', linewidth=3))
ax2.text(6.5, output_y, 'Output\na', ha='center', va='center', fontsize=12, fontweight='bold')

ax2.add_patch(FancyBboxPatch((8.5, output_y-0.3), 1, 0.6, boxstyle="round,pad=0.1",
                             edgecolor='purple', facecolor='plum', linewidth=3))
ax2.text(9, output_y, 'Loss', ha='center', va='center', fontsize=12, fontweight='bold')

# Backward arrows (opposite direction!)
backward_arrow_style = dict(arrowstyle='->', lw=3, color='red')
ax2.annotate('', xy=(7, 2.7), xytext=(8.5, 2.7), arrowprops=backward_arrow_style)
ax2.annotate('', xy=(4, 2.7), xytext=(6, 2.7), arrowprops=backward_arrow_style)
ax2.annotate('', xy=(1.5, 2.7), xytext=(3, 2.7), arrowprops=backward_arrow_style)

# Gradient labels
ax2.text(7.75, 2.3, '∂L/∂a', ha='center', fontsize=10, color='red', fontweight='bold')
ax2.text(5, 2.3, '∂L/∂W2', ha='center', fontsize=10, color='red', fontweight='bold')
ax2.text(2.25, 2.3, '∂L/∂W1', ha='center', fontsize=10, color='red', fontweight='bold')

ax2.text(1, 5, '2. Calculate gradients (chain rule!)', fontsize=12,
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
ax2.text(1, 0.5, '3. Update weights: W = W - α·∂L/∂W', fontsize=12,
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/backprop_visualization.png', dpi=150)
print("✓ Saved visualization: backprop_visualization.png")
print("  Shows how data flows forward and gradients flow backward!")

# ============================================================
# PART 4: Computational Graph
# ============================================================
print("\n\n📌 PART 4: Computational Graph")
print("-" * 80)

print("""
A computational graph shows the flow of calculations!

Example: Loss = (σ(w*x + b) - y)²

Graph:
  x, w, b → multiply/add → z → sigmoid → a → subtract → square → Loss

Each node is an operation.
Each edge passes a value forward (and gradient backward!)

Forward pass: Calculate left to right
Backward pass: Calculate right to left (chain rule!)
""")

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')
ax.set_title('Computational Graph - Forward and Backward Pass', fontsize=16, fontweight='bold')

# Nodes
nodes = [
    (1, 4, 'x'),
    (1, 5.5, 'w'),
    (1, 2.5, 'b'),
    (2.5, 4, 'w·x'),
    (4, 4, 'z=w·x+b'),
    (5.5, 4, 'σ(z)'),
    (5.5, 2, 'y'),
    (7, 4, 'a-y'),
    (8.5, 4, '(a-y)²\nLoss')
]

for x, y, label in nodes:
    color = 'lightblue' if 'x' in label or 'w' in label or 'b' in label or 'y' == label else 'lightgreen'
    if 'Loss' in label:
        color = 'lightcoral'
    ax.add_patch(plt.Circle((x, y), 0.4, color=color, ec='black', linewidth=2))
    ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold')

# Forward edges
forward_edges = [
    ((1, 5.5), (2.3, 4.3)),
    ((1, 4), (2.3, 4)),
    ((2.7, 4), (3.6, 4)),
    ((1, 2.5), (3.6, 3.8)),
    ((4.4, 4), (5.1, 4)),
    ((5.9, 4), (6.6, 4)),
    ((5.5, 2.4), (6.7, 3.7)),
    ((7.4, 4), (8.1, 4))
]

for start, end in forward_edges:
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=2, color='blue'))

# Backward edges (gradients)
backward_edges = [
    ((8.1, 3.7), (7.4, 3.7)),
    ((6.6, 3.7), (5.9, 3.7)),
    ((5.1, 3.7), (4.4, 3.7))
]

for start, end in backward_edges:
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=2, color='red', linestyle='dashed'))

# Labels
ax.text(5, 7, 'Forward Pass (blue arrows): Calculate outputs', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
ax.text(5, 0.5, 'Backward Pass (red arrows): Calculate gradients', fontsize=12,
        bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/computational_graph.png', dpi=150)
print("✓ Saved visualization: computational_graph.png")
print("  Blue arrows = forward pass, Red arrows = backward pass!")

# ============================================================
# PART 5: Gradient Flow Animation (Simulated)
# ============================================================
print("\n\n📌 PART 5: Understanding Gradient Magnitudes")
print("-" * 80)

print("""
Important concept: Vanishing and Exploding Gradients!

As we backpropagate through many layers:
- Gradients can become VERY SMALL (vanishing) → learning stops
- Gradients can become VERY LARGE (exploding) → weights diverge

This is why:
- ReLU activation is popular (helps with vanishing gradients)
- Batch normalization is used
- Gradient clipping prevents explosions
""")

# Simulate gradient flow through multiple layers
n_layers = 10
gradients = [1.0]  # Start with gradient = 1 at output

# Sigmoid derivative is small (max 0.25)
sigmoid_derivative_max = 0.25

for layer in range(n_layers):
    # Each layer multiplies gradient by sigmoid derivative
    gradient = gradients[-1] * sigmoid_derivative_max
    gradients.append(gradient)

plt.figure(figsize=(12, 6))
layers = list(range(n_layers + 1))
plt.plot(layers[::-1], gradients, 'o-', linewidth=3, markersize=10, color='red')
plt.xlabel('Layer (from output to input)', fontsize=12)
plt.ylabel('Gradient Magnitude', fontsize=12)
plt.title('Vanishing Gradient Problem - Gradients shrink as we go deeper!', fontsize=14, fontweight='bold')
plt.yscale('log')
plt.grid(True, alpha=0.3)
plt.axhline(y=0.001, color='orange', linestyle='--', linewidth=2, label='Too small to learn!')
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/vanishing_gradients.png', dpi=150)
print("✓ Saved visualization: vanishing_gradients.png")
print("  Shows why deep networks with sigmoid are hard to train!")
print("  Gradients shrink exponentially as we go deeper!")

# ============================================================
# PART 6: Practical Example - Training Loop
# ============================================================
print("\n\n📌 PART 6: Complete Training Loop with Backpropagation")
print("-" * 80)

# Simple dataset
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])  # XOR

# Initialize network
np.random.seed(42)
W1 = np.random.randn(2, 4) * 0.5
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 1) * 0.5
b2 = np.zeros((1, 1))

learning_rate = 0.5
epochs = 5000
loss_history = []

print(f"Training XOR with backpropagation...")
print(f"  Architecture: 2 → 4 → 1")
print(f"  Learning rate: {learning_rate}")
print(f"  Epochs: {epochs}\n")

for epoch in range(epochs):
    # Forward pass
    z1 = np.dot(X_train, W1) + b1
    a1 = 1 / (1 + np.exp(-z1))
    z2 = np.dot(a1, W2) + b2
    a2 = 1 / (1 + np.exp(-z2))

    # Loss
    loss = np.mean((a2 - y_train) ** 2)
    loss_history.append(loss)

    # Backward pass
    # Output layer
    dLoss_da2 = 2 * (a2 - y_train) / len(X_train)
    da2_dz2 = a2 * (1 - a2)
    dLoss_dz2 = dLoss_da2 * da2_dz2

    dLoss_dW2 = np.dot(a1.T, dLoss_dz2)
    dLoss_db2 = np.sum(dLoss_dz2, axis=0, keepdims=True)

    # Hidden layer (backpropagation!)
    dLoss_da1 = np.dot(dLoss_dz2, W2.T)
    da1_dz1 = a1 * (1 - a1)
    dLoss_dz1 = dLoss_da1 * da1_dz1

    dLoss_dW1 = np.dot(X_train.T, dLoss_dz1)
    dLoss_db1 = np.sum(dLoss_dz1, axis=0, keepdims=True)

    # Update weights
    W2 -= learning_rate * dLoss_dW2
    b2 -= learning_rate * dLoss_db2
    W1 -= learning_rate * dLoss_dW1
    b1 -= learning_rate * dLoss_db1

    if epoch % 1000 == 0 or epoch == epochs - 1:
        predictions = (a2 > 0.5).astype(int)
        accuracy = np.mean(predictions == y_train) * 100
        print(f"  Epoch {epoch:5d}: Loss = {loss:.6f}, Accuracy = {accuracy:.0f}%")

print("\n✅ Training complete!")
print("\n🧪 Final predictions:")
for i in range(len(X_train)):
    print(f"  Input: {X_train[i]} → Predicted: {(a2[i][0] > 0.5)*1} (prob: {a2[i][0]:.4f}) | Actual: {y_train[i][0]}")

# Plot learning
plt.figure(figsize=(10, 6))
plt.plot(loss_history, linewidth=2)
plt.xlabel('Epoch', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.title('Learning Curve - Backpropagation in Action!', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.yscale('log')
plt.tight_layout()
plt.savefig('/d/Language Learning/AI ML/Learning-ML-AI/Phase 4 - Deep Learning/backprop_training.png', dpi=150)
print("\n✓ Saved visualization: backprop_training.png")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n🎯 WHY UNDERSTANDING BACKPROPAGATION MATTERS")
print("=" * 80)
print("""
1. THE CORE OF ALL DEEP LEARNING:
   - Every neural network uses backpropagation
   - CNN, RNN, Transformer - all use the same principle
   - Forward pass → Calculate loss → Backward pass → Update weights

2. IT'S JUST CHAIN RULE:
   - Not magic, just calculus!
   - Each layer's gradient depends on next layer
   - Multiply derivatives as we go backward

3. DEBUGGING NETWORKS:
   - Understand vanishing/exploding gradients
   - Know why deep networks are hard to train
   - Choose right activations (ReLU vs Sigmoid)

4. OPTIMIZATION:
   - Gradients tell us the direction
   - Learning rate controls step size
   - Modern optimizers (Adam) modify gradients smartly

5. WHAT PYTORCH/TENSORFLOW DO:
   - Autograd: Automatic differentiation
   - They calculate gradients for you!
   - But now you understand HOW they do it

🔍 Key Insights:

   ∂Loss/∂w = How much does loss change when weight changes?

   Backpropagation answers this for EVERY weight!

   Chain rule lets us efficiently calculate all gradients
   in one backward pass through the network.

💡 The Algorithm (Simplified):

   1. Forward pass: Calculate outputs
   2. Calculate loss
   3. Backward pass (starting from loss):
      - Calculate gradient at current layer
      - Pass gradient to previous layer
      - Repeat until we reach the input
   4. Update all weights using gradients
   5. Repeat!

🚀 What's Next?
   - Use automatic differentiation (PyTorch/TensorFlow)
   - Understand different optimizers (SGD, Adam, RMSprop)
   - Learn about batch normalization
   - Study advanced architectures (ResNet, attention)

🎓 Remember:
   "Backpropagation is not a panacea, but it's the best hammer we have,
    and everything looks like a nail once you have it."

   Understanding it deeply makes you a better deep learning engineer!
""")

print("\n✅ Backpropagation Deep Dive Complete!")
print("Next: tensorflow_basics.py - Using professional deep learning frameworks")
