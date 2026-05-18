"""
📈 LINEAR REGRESSION FROM SCRATCH - Understanding the Math
===========================================================

What is Linear Regression?
--------------------------
Imagine you're trying to predict house prices based on size.
You notice: bigger houses cost more. That's a LINEAR relationship!

Linear Regression finds the "best fit line" through your data points.

The Math (Don't Worry, We'll Break It Down!):
y = mx + b
- y = what we're predicting (house price)
- x = what we know (house size)
- m = slope (how much price increases per square foot)
- b = intercept (base price when size = 0)

For multiple features: y = w₁x₁ + w₂x₂ + ... + b
- w = weights (importance of each feature)
- b = bias (starting point)

HOW does the computer find the best line?
1. Start with random m and b
2. Calculate predictions
3. Calculate error (how wrong we are)
4. Adjust m and b to reduce error
5. Repeat until error is minimized

This is called GRADIENT DESCENT - the heart of machine learning!
"""

import numpy as np
import matplotlib.pyplot as plt

print("=" * 70)
print("LINEAR REGRESSION FROM SCRATCH - Learning How ML Really Works")
print("=" * 70)

# ============================================================
# PART 1: Creating Sample Data
# ============================================================
print("\n📌 PART 1: Creating Sample Data")
print("-" * 70)

# Let's predict house prices based on size (square feet)
np.random.seed(42)  # So we get the same results every time

# True relationship: Price = 50 * Size + 100,000 (with some noise)
house_sizes = np.array([750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400,
                        1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400])
# Add some random noise to make it realistic
noise = np.random.randn(20) * 10000
house_prices = 50 * house_sizes + 100000 + noise

print(f"House Sizes (sq ft): {house_sizes[:5]}...")
print(f"House Prices ($): {house_prices[:5]}...")
print(f"\n💡 We have {len(house_sizes)} houses in our dataset")
print("   Goal: Learn the relationship between size and price!")

# ============================================================
# PART 2: Visualizing the Data
# ============================================================
print("\n\n📌 PART 2: Visualizing Our Data")
print("-" * 70)

plt.figure(figsize=(10, 6))
plt.scatter(house_sizes, house_prices, color='blue', alpha=0.6, s=100)
plt.xlabel('House Size (sq ft)', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('House Prices vs Size - Our Dataset', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/linear_regression_data.png', dpi=150)
print("✓ Saved plot: linear_regression_data.png")
print("  Look at the plot! You can see a clear LINEAR pattern!")

# ============================================================
# PART 3: The Math - Cost Function
# ============================================================
print("\n\n📌 PART 3: Understanding the COST FUNCTION")
print("-" * 70)

print("""
🎯 Cost Function (Mean Squared Error - MSE):

   Cost = (1/n) * Σ(predicted - actual)²

   Translation:
   1. For each house, calculate: (our prediction - real price)²
   2. Square it (so negative errors don't cancel positive ones)
   3. Average all the squared errors

   Lower cost = Better predictions!

   Example:
   - Real price: $200,000
   - Our prediction: $195,000
   - Error: $5,000
   - Squared error: $25,000,000

   We want to MINIMIZE this cost!
""")

def compute_cost(X, y, weights, bias):
    """
    Calculate how wrong our predictions are

    X: input features (house sizes)
    y: actual values (real prices)
    weights: slope (m)
    bias: intercept (b)
    """
    m = len(y)  # Number of houses

    # Make predictions: y_pred = weights * X + bias
    predictions = weights * X + bias

    # Calculate error: (prediction - actual)²
    squared_errors = (predictions - y) ** 2

    # Average the squared errors
    cost = np.sum(squared_errors) / (2 * m)

    return cost

# Test with random initial values
initial_weight = 0  # Start with weight = 0
initial_bias = 0    # Start with bias = 0

initial_cost = compute_cost(house_sizes, house_prices, initial_weight, initial_bias)
print(f"\n📊 With weight=0 and bias=0:")
print(f"   Cost (MSE): ${initial_cost:,.0f}")
print(f"   💡 This is HUGE! Our predictions are terrible!")
print(f"   We're predicting $0 for every house! 😱")

# ============================================================
# PART 4: Gradient Descent - The Learning Algorithm
# ============================================================
print("\n\n📌 PART 4: GRADIENT DESCENT - How the Model Learns")
print("-" * 70)

print("""
🎓 Gradient Descent Explained:

Imagine you're blindfolded on a mountain and want to reach the valley (minimum cost).
You take steps in the direction that goes DOWN the fastest.

Algorithm:
1. Calculate the gradient (which direction increases cost)
2. Move in the OPPOSITE direction (to decrease cost)
3. Take small steps (learning rate)
4. Repeat until you reach the bottom

Math:
   weight = weight - learning_rate * ∂Cost/∂weight
   bias = bias - learning_rate * ∂Cost/∂bias

   ∂Cost/∂weight means: "How much does cost change when weight changes?"
""")

def gradient_descent(X, y, learning_rate=0.0001, iterations=1000):
    """
    The learning algorithm that finds the best weight and bias

    learning_rate: how big our steps are (too big = overshoot, too small = slow)
    iterations: how many times to adjust our parameters
    """
    m = len(y)  # Number of training examples

    # Start with random guesses
    weight = 0
    bias = 0

    cost_history = []  # Track how cost decreases over time

    print(f"\n🏃 Starting Gradient Descent...")
    print(f"   Learning rate: {learning_rate}")
    print(f"   Iterations: {iterations}")
    print(f"\n   Initial: weight={weight:.2f}, bias={bias:.2f}")

    for i in range(iterations):
        # Make predictions with current weight and bias
        predictions = weight * X + bias

        # Calculate errors
        errors = predictions - y

        # Calculate gradients (derivatives)
        # These tell us which direction to move
        weight_gradient = (1/m) * np.sum(errors * X)
        bias_gradient = (1/m) * np.sum(errors)

        # Update parameters (move in opposite direction of gradient)
        weight = weight - learning_rate * weight_gradient
        bias = bias - learning_rate * bias_gradient

        # Calculate and store cost
        cost = compute_cost(X, y, weight, bias)
        cost_history.append(cost)

        # Print progress
        if i % 200 == 0 or i == iterations - 1:
            print(f"   Iteration {i:4d}: Cost = ${cost:,.0f}, weight={weight:.2f}, bias={bias:.2f}")

    print(f"\n✅ Training Complete!")
    print(f"   Final weight: {weight:.2f} (slope)")
    print(f"   Final bias: {bias:.2f} (intercept)")

    return weight, bias, cost_history

# Train the model!
final_weight, final_bias, cost_history = gradient_descent(house_sizes, house_prices,
                                                           learning_rate=0.0001,
                                                           iterations=1000)

# ============================================================
# PART 5: Visualizing the Learning Process
# ============================================================
print("\n\n📌 PART 5: Visualizing How the Model Learned")
print("-" * 70)

# Plot how cost decreased over time
plt.figure(figsize=(10, 6))
plt.plot(cost_history, linewidth=2, color='red')
plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Cost (MSE)', fontsize=12)
plt.title('Learning Curve - Cost Decreasing Over Time', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/linear_regression_learning_curve.png', dpi=150)
print("✓ Saved plot: linear_regression_learning_curve.png")
print("  The cost drops rapidly at first, then stabilizes!")
print("  This means our model is LEARNING! 🎉")

# ============================================================
# PART 6: Making Predictions with Our Trained Model
# ============================================================
print("\n\n📌 PART 6: Making Predictions")
print("-" * 70)

def predict(X, weight, bias):
    """Make predictions using our learned parameters"""
    return weight * X + bias

# Test on some house sizes
test_sizes = np.array([1000, 1500, 2000, 2500])
predictions = predict(test_sizes, final_weight, final_bias)

print("\n🏠 Predicting prices for new houses:")
for size, price in zip(test_sizes, predictions):
    print(f"   House size: {size:,} sq ft → Predicted price: ${price:,.2f}")

# Compare with actual data points
print("\n\n📊 Comparing Predictions vs Actual Prices:")
sample_indices = [0, 5, 10, 15, 19]
for idx in sample_indices:
    actual = house_prices[idx]
    predicted = predict(house_sizes[idx], final_weight, final_bias)
    error = abs(predicted - actual)
    print(f"   Size: {house_sizes[idx]:,} sq ft | Actual: ${actual:,.0f} | Predicted: ${predicted:,.0f} | Error: ${error:,.0f}")

# ============================================================
# PART 7: Visualizing the Best Fit Line
# ============================================================
print("\n\n📌 PART 7: The Best Fit Line")
print("-" * 70)

plt.figure(figsize=(12, 6))

# Original data points
plt.scatter(house_sizes, house_prices, color='blue', alpha=0.6, s=100, label='Actual Data')

# Best fit line
x_line = np.linspace(house_sizes.min(), house_sizes.max(), 100)
y_line = predict(x_line, final_weight, final_bias)
plt.plot(x_line, y_line, 'r-', linewidth=3, label='Best Fit Line')

plt.xlabel('House Size (sq ft)', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('Linear Regression - Best Fit Line', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/linear_regression_best_fit.png', dpi=150)
print("✓ Saved plot: linear_regression_best_fit.png")
print("  The red line shows our learned relationship!")
print(f"  Equation: Price = {final_weight:.2f} × Size + {final_bias:.2f}")

# ============================================================
# PART 8: Understanding What We Learned
# ============================================================
print("\n\n📌 PART 8: Interpreting the Results")
print("-" * 70)

print(f"""
🎯 Our Model's Equation:
   Price = {final_weight:.2f} × Size + {final_bias:.2f}

📊 What does this mean?

   Weight (Slope) = {final_weight:.2f}
   → For every additional square foot, price increases by ${final_weight:.2f}
   → Bigger weight = stronger relationship

   Bias (Intercept) = ${final_bias:.2f}
   → Base price (when size = 0)
   → Often doesn't make real-world sense, but mathematically necessary

💡 The True Relationship (we used to generate data):
   Price = 50 × Size + 100,000

   Our learned parameters are close! The difference is due to:
   - Random noise in the data (real world is never perfect)
   - Limited training data (only 20 houses)
   - Learning rate and iterations (could be tuned better)
""")

# ============================================================
# PART 9: Model Evaluation
# ============================================================
print("\n\n📌 PART 9: How Good is Our Model?")
print("-" * 70)

# Calculate R² score (coefficient of determination)
def r_squared(y_true, y_pred):
    """
    R² score: measures how well our model fits the data
    - R² = 1.0 → Perfect fit!
    - R² = 0.5 → Explains 50% of variance
    - R² = 0.0 → No better than predicting the mean
    """
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)  # Total variance
    ss_residual = np.sum((y_true - y_pred) ** 2)  # Unexplained variance
    return 1 - (ss_residual / ss_total)

predictions_all = predict(house_sizes, final_weight, final_bias)
r2 = r_squared(house_prices, predictions_all)

# Mean Absolute Error
mae = np.mean(np.abs(house_prices - predictions_all))

# Root Mean Squared Error
rmse = np.sqrt(np.mean((house_prices - predictions_all) ** 2))

print(f"\n📈 Model Performance Metrics:")
print(f"   R² Score: {r2:.4f}")
print(f"   → {r2*100:.2f}% of price variation is explained by house size!")
print(f"   → R² close to 1.0 means excellent fit! ✨")
print(f"\n   Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"   → On average, we're off by ${mae:,.2f}")
print(f"\n   Root Mean Squared Error (RMSE): ${rmse:,.2f}")
print(f"   → Similar to MAE but penalizes large errors more")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n🎯 WHY IMPLEMENTING FROM SCRATCH MATTERS")
print("=" * 70)
print("""
1. UNDERSTANDING: You now know what's happening inside scikit-learn!
   - Libraries are BLACK BOXES until you understand the math
   - Now you can debug, tune, and improve models effectively

2. GRADIENT DESCENT is EVERYWHERE:
   - Neural networks use it
   - Most ML algorithms use it
   - It's the foundation of deep learning

3. COST FUNCTIONS are KEY:
   - Different problems need different cost functions
   - Understanding MSE helps you choose the right one

4. LEARNING RATE matters:
   - Too high → model diverges (cost increases)
   - Too low → takes forever to train
   - Finding the sweet spot is crucial

5. You can now modify the algorithm:
   - Add regularization to prevent overfitting
   - Use different cost functions
   - Implement advanced optimizers (Adam, RMSprop)

🚀 What's Next?
   - Try with multiple features (multivariate regression)
   - Add polynomial features for non-linear relationships
   - Implement regularization (Ridge, Lasso)
   - Use scikit-learn (much faster, but now you understand it!)
""")

print("\n✅ Linear Regression from Scratch Complete!")
print("Next: linear_regression_sklearn.py - Using professional tools")
