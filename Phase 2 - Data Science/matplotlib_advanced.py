"""
📊 MATPLOTLIB ADVANCED - Subplots, Heatmaps, and Complex Visualizations
===========================================================================

What You'll Learn:
- Creating multiple plots in one figure (subplots)
- Heatmaps and correlation matrices
- 3D plots
-Advanced customization
- Interactive elements
- Statistical visualizations with Seaborn

This file takes your visualization skills to professional level!
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

print("=" * 60)
print("ADVANCED DATA VISUALIZATION")
print("=" * 60)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# ============================================================
# PART 1: Subplots - Multiple Plots in One Figure
# ============================================================
print("\n📌 PART 1: Subplots - Multiple Plots Together")
print("-" * 60)

# Create sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = x ** 2

# Method 1: plt.subplots()
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Four Different Plots in One Figure', fontsize=16, fontweight='bold')

axes[0, 0].plot(x, y1, 'r-', linewidth=2)
axes[0, 0].set_title('Sine Wave')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(x, y2, 'b-', linewidth=2)
axes[0, 1].set_title('Cosine Wave')
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].plot(x[:50], y3[:50], 'g-', linewidth=2)
axes[1, 0].set_title('Tangent (limited range)')
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].plot(x, y4, 'm-', linewidth=2)
axes[1, 1].set_title('Quadratic')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('subplots_2x2.png', dpi=300, bbox_inches='tight')
print("✓ Created: subplots_2x2.png")
plt.close()

# ============================================================
# PART 2: Heatmap - Correlation Matrix
# ============================================================
print("\n📌 PART 2: Heatmaps - Visualize Correlations")
print("-" * 60)

# Create sample dataset
np.random.seed(42)
data = pd.DataFrame({
    'Height': np.random.normal(170, 10, 100),
    'Weight': np.random.normal(70, 15, 100),
    'Age': np.random.randint(20, 60, 100),
    'Salary': np.random.normal(60000, 20000, 100),
    'Experience': np.random.randint(0, 30, 100)
})

# Add correlation
data['Weight'] = data['Height'] * 0.7 + np.random.normal(0, 5, 100)

# Calculate correlation matrix
corr_matrix = data.corr()

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix Heatmap', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('heatmap_correlation.png', dpi=300, bbox_inches='tight')
print("✓ Created: heatmap_correlation.png")
print("   💡 Red = positive correlation, Blue = negative, White = no correlation")
plt.close()

# ============================================================
# PART 3: Seaborn Advanced Plots
# ============================================================
print("\n📌 PART 3: Seaborn - Statistical Visualizations")
print("-" * 60)

# Violin plot - distribution with scatter
plt.figure(figsize=(12, 6))
tips = sns.load_dataset('tips')  # Built-in dataset
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True, palette='Set2')
plt.title('Restaurant Bills by Day and Gender', fontsize=16, fontweight='bold')
plt.savefig('violin_plot.png', dpi=300, bbox_inches='tight')
print("✓ Created: violin_plot.png")
plt.close()

# Pair plot - relationships between all variables
print("\n   Creating pair plot (this may take a moment)...")
iris = sns.load_dataset('iris')
pairplot = sns.pairplot(iris, hue='species', palette='husl', diag_kind='kde')
pairplot.fig.suptitle('Iris Dataset - All Pairwise Relationships', y=1.02, fontsize=16, fontweight='bold')
plt.savefig('pairplot.png', dpi=300, bbox_inches='tight')
print("✓ Created: pairplot.png")
plt.close()

# ============================================================
# PART 4: 3D Plots
# ============================================================
print("\n📌 PART 4: 3D Visualizations")
print("-" * 60)

# Create 3D surface plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Generate data
X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plot surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot - sin(√(x²+y²))', fontsize=14, fontweight='bold')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig('3d_surface.png', dpi=300, bbox_inches='tight')
print("✓ Created: 3d_surface.png")
plt.close()

# ============================================================
# PART 5: Complex Multi-Panel Dashboard
# ============================================================
print("\n📌 PART 5: Dashboard-Style Layout")
print("-" * 60)

# Create data
np.random.seed(42)
data = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=100),
    'Sales': np.cumsum(np.random.randn(100)) + 100,
    'Profit': np.cumsum(np.random.randn(100)) + 50,
    'Customers': np.random.randint(10, 100, 100)
})

# Create figure with custom layout
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Top row - main chart
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(data['Date'], data['Sales'], label='Sales', linewidth=2)
ax1.plot(data['Date'], data['Profit'], label='Profit', linewidth=2)
ax1.set_title('Sales and Profit Over Time', fontsize=14, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Middle left - histogram
ax2 = fig.add_subplot(gs[1, 0])
ax2.hist(data['Sales'], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
ax2.set_title('Sales Distribution')
ax2.set_xlabel('Sales')

# Middle center - scatter
ax3 = fig.add_subplot(gs[1, 1])
ax3.scatter(data['Sales'], data['Profit'], alpha=0.5, c=data['Customers'], cmap='viridis')
ax3.set_title('Sales vs Profit')
ax3.set_xlabel('Sales')
ax3.set_ylabel('Profit')

# Middle right - pie
ax4 = fig.add_subplot(gs[1, 2])
categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [data['Sales'][:25].sum(), data['Sales'][25:50].sum(),
          data['Sales'][50:75].sum(), data['Sales'][75:].sum()]
ax4.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
ax4.set_title('Quarterly Sales')

# Bottom row - statistics
ax5 = fig.add_subplot(gs[2, :])
ax5.axis('off')
stats_text = f"""
📊 KEY STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Sales:      ${data['Sales'].sum():,.2f}
Average Sales:    ${data['Sales'].mean():,.2f}
Total Profit:     ${data['Profit'].sum():,.2f}
Average Profit:   ${data['Profit'].mean():,.2f}
Total Customers:  {data['Customers'].sum():,}
Average Customers: {data['Customers'].mean():.0f}
"""
ax5.text(0.1, 0.5, stats_text, fontsize=12, family='monospace',
         verticalalignment='center')

plt.savefig('dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Created: dashboard.png")
plt.close()

# ============================================================
# PART 6: Annotation and Arrows
# ============================================================
print("\n📌 PART 6: Annotations - Highlight Important Points")
print("-" * 60)

# Stock price simulation
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100)
price = 100 + np.cumsum(np.random.randn(100))

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(dates, price, linewidth=2, color='darkblue')

# Find max and min
max_idx = price.argmax()
min_idx = price.argmin()

# Annotate maximum
ax.annotate('Peak\n${:.2f}'.format(price[max_idx]),
            xy=(dates[max_idx], price[max_idx]),
            xytext=(dates[max_idx+10], price[max_idx]+5),
            arrowprops=dict(arrowstyle='->', color='green', lw=2),
            fontsize=12, fontweight='bold', color='green',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', alpha=0.7))

# Annotate minimum
ax.annotate('Bottom\n${:.2f}'.format(price[min_idx]),
            xy=(dates[min_idx], price[min_idx]),
            xytext=(dates[min_idx+10], price[min_idx]-5),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12, fontweight='bold', color='red',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.7))

ax.set_title('Stock Price with Key Events Annotated', fontsize=16, fontweight='bold')
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Price ($)', fontsize=12)
ax.grid(True, alpha=0.3)

plt.savefig('annotated_plot.png', dpi=300, bbox_inches='tight')
print("✓ Created: annotated_plot.png")
plt.close()

# ============================================================
# PART 7: Custom Color Palettes and Styling
# ============================================================
print("\n📌 PART 7: Professional Styling")
print("-" * 60)

# Create styled plot with custom colors
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [85, 72, 95, 68, 90]

# Custom color palette
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(categories, values, color=colors, edgecolor='white', linewidth=2)

# Add gradient effect
for bar, color in zip(bars, colors):
    bar.set_alpha(0.8)

# Style the plot
ax.set_title('Professional Product Performance Report',
             fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Performance Score', fontsize=13)
ax.set_ylim(0, 105)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1,
            f'{int(height)}',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.savefig('professional_styled.png', dpi=300, bbox_inches='tight')
print("✓ Created: professional_styled.png")
plt.close()

# ============================================================
# SUMMARY
# ============================================================
print("\n\n🎯 ADVANCED VISUALIZATION SUMMARY")
print("=" * 60)
print("""
✅ Advanced Techniques You Learned:

1️⃣ SUBPLOTS - Multiple plots in one figure
   fig, axes = plt.subplots(rows, cols)
   Access: axes[row, col]

2️⃣ HEATMAPS - Correlation and patterns
   sns.heatmap(data, annot=True, cmap='coolwarm')

3️⃣ SEABORN - Statistical plots
   • Violin plots - distributions
   • Pair plots - all relationships
   • Box plots with hue

4️⃣ 3D PLOTS - Surface visualizations
   fig.add_subplot(111, projection='3d')

5️⃣ DASHBOARDS - Complex layouts
   fig.add_gridspec(rows, cols)

6️⃣ ANNOTATIONS - Highlight key points
   ax.annotate('text', xy=point, xytext=label_position)

7️⃣ STYLING - Professional appearance
   • Custom colors
   • Remove spines
   • Add gradients

🎨 Pro Tips for Publication-Quality Plots:
   • Use consistent color schemes
   • Remove unnecessary chart junk
   • Add clear titles and labels
   • Annotate important points
   • Save at high DPI (300+)
   • Use white space effectively

📊 Seaborn vs Matplotlib:
   Matplotlib: Full control, detailed customization
   Seaborn: Quick statistical plots, beautiful defaults
   → Use both! Seaborn is built on Matplotlib

🚀 Next Steps:
   - Open all the PNG files to see your visualizations
   - Try modifying colors and layouts
   - Apply these to your own datasets
   - Move to data_exploration.py for full EDA workflow
""")

print("\n✅ Matplotlib Advanced Complete!")
print("Next file: data_exploration.py - Full exploratory data analysis workflow")
