"""
📊 MATPLOTLIB BASICS - Data Visualization Fundamentals
=======================================================

Why Visualize Data?
-------------------
"A picture is worth a thousand numbers"
- Spot patterns instantly
- Find outliers visually
- Communicate insights clearly
- Understand data distribution

Matplotlib is Python's main plotting library.
Think of it as Python's version of Excel charts, but way more powerful!
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("=" * 60)
print("MATPLOTLIB - MAKING DATA VISUAL")
print("=" * 60)

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')  # Makes plots prettier

# ============================================================
#  PART 1: Line Plot (Trends Over Time)
# ============================================================
print("\n📌 PART 1: Line Plots - Show Trends")
print("-" * 60)

# Data: Monthly sales
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [15000, 18000, 16000, 22000, 25000, 27000]

# Create the plot
plt.figure(figsize=(10, 6))  # Width=10 inches, Height=6 inches
plt.plot(months, sales, marker='o', linewidth=2, markersize=8, color='blue')

# Add labels and title
plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)

# Add grid for easier reading
plt.grid(True, alpha=0.3)

# Save the plot
plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
print("✓ Created: line_plot.png")
print("   💡 Use line plots for: Time series, trends, continuous data")
plt.close()  # Close to save memory

# ============================================================
# PART 2: Bar Chart (Compare Categories)
# ============================================================
print("\n📌 PART 2: Bar Charts - Compare Categories")
print("-" * 60)

# Data: Department employee counts
departments = ['Sales', 'IT', 'HR', 'Marketing', 'Finance']
employees = [45, 32, 18, 25, 20]

# Vertical bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(departments, employees, color='steelblue', edgecolor='black', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.title('Employees by Department', fontsize=16, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)
plt.ylim(0, max(employees) * 1.1)  # Add space on top

plt.savefig('bar_chart.png', dpi=300, bbox_inches='tight')
print("✓ Created: bar_chart.png")
print("   💡 Use bar charts for: Comparing categories, counts, rankings")
plt.close()

# Horizontal bar chart (better for long labels)
plt.figure(figsize=(10, 6))
plt.barh(departments, employees, color='coral', edgecolor='black', alpha=0.7)
plt.title('Employees by Department (Horizontal)', fontsize=16, fontweight='bold')
plt.xlabel('Number of Employees', fontsize=12)
plt.ylabel('Department', fontsize=12)
plt.savefig('bar_chart_horizontal.png', dpi=300, bbox_inches='tight')
print("✓ Created: bar_chart_horizontal.png")
plt.close()

# ============================================================
# PART 3: Histogram (Distribution of Data)
# ============================================================
print("\n📌 PART 3: Histograms - Show Distribution")
print("-" * 60)

# Generate random age data
np.random.seed(42)
ages = np.random.normal(35, 10, 1000)  # Mean=35, Std=10, 1000 samples

plt.figure(figsize=(10, 6))
plt.hist(ages, bins=30, color='green', edgecolor='black', alpha=0.7)

# Add mean line
mean_age = np.mean(ages)
plt.axvline(mean_age, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_age:.1f}')

plt.title('Age Distribution of Employees', fontsize=16, fontweight='bold')
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency (Count)', fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.3)

plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
print("✓ Created: histogram.png")
print("   💡 Use histograms for: Understanding distribution, checking normality")
plt.close()

# ============================================================
# PART 4: Scatter Plot (Relationships)
# ============================================================
print("\n📌 PART 4: Scatter Plots - Find Relationships")
print("-" * 60)

# Data: Study hours vs exam scores
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [45, 51, 58, 62, 68, 74, 78, 84, 88, 92]

plt.figure(figsize=(10, 6))
plt.scatter(study_hours, exam_scores, s=100, alpha=0.6, c='purple', edgecolors='black')

# Add trend line
z = np.polyfit(study_hours, exam_scores, 1)  # Linear fit
p = np.poly1d(z)
plt.plot(study_hours, p(study_hours), "r--", linewidth=2, label='Trend Line')

plt.title('Study Hours vs Exam Score', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Exam Score', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
print("✓ Created: scatter_plot.png")
print("   💡 Use scatter plots for: Correlations, relationships between 2 variables")
plt.close()

# ============================================================
# PART 5: Pie Chart (Part-to-Whole)
# ============================================================
print("\n📌 PART 5: Pie Charts - Show Proportions")
print("-" * 60)

# Data: Market share
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Others']
market_share = [35, 25, 20, 15, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    market_share,
    labels=companies,
    colors=colors,
    autopct='%1.1f%%',  # Show percentages
    startangle=90,
    explode=(0.1, 0, 0, 0, 0),  # Explode first slice
    shadow=True
)

# Make percentage text bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)

plt.title('Market Share Distribution', fontsize=16, fontweight='bold')
plt.axis('equal')  # Equal aspect ratio ensures circular pie

plt.savefig('pie_chart.png', dpi=300, bbox_inches='tight')
print("✓ Created: pie_chart.png")
print("   💡 Use pie charts for: Proportions, market share (max 5-6 categories)")
print("   ⚠️  Avoid pie charts if you have >6 categories - use bar chart instead!")
plt.close()

# ============================================================
# PART 6: Box Plot (Statistical Summary)
# ============================================================
print("\n📌 PART 6: Box Plots - Show Statistical Distribution")
print("-" * 60)

# Generate salary data for different departments
np.random.seed(42)
sales_salaries = np.random.normal(70000, 15000, 100)
it_salaries = np.random.normal(85000, 12000, 100)
hr_salaries = np.random.normal(60000, 10000, 100)

data_to_plot = [sales_salaries, it_salaries, hr_salaries]

plt.figure(figsize=(10, 6))
box = plt.boxplot(data_to_plot, labels=['Sales', 'IT', 'HR'], patch_artist=True)

# Color the boxes
colors = ['lightblue', 'lightgreen', 'lightcoral']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Salary Distribution by Department', fontsize=16, fontweight='bold')
plt.ylabel('Salary ($)', fontsize=12)
plt.xlabel('Department', fontsize=12)
plt.grid(axis='y', alpha=0.3)

plt.savefig('box_plot.png', dpi=300, bbox_inches='tight')
print("✓ Created: box_plot.png")
print("   💡 Box plot shows: Min, Q1 (25%), Median (50%), Q3 (75%), Max, Outliers")
print("   💡 Use for: Comparing distributions, finding outliers")
plt.close()

# ============================================================
# PART 7: Multiple Lines
# ============================================================
print("\n📌 PART 7: Multiple Lines - Compare Multiple Trends")
print("-" * 60)

# Data: Sales for 3 products over months
months = range(1, 13)
product_a = [100 + i*10 + np.random.randint(-10, 10) for i in range(12)]
product_b = [80 + i*8 + np.random.randint(-10, 10) for i in range(12)]
product_c = [120 + i*12 + np.random.randint(-10, 10) for i in range(12)]

plt.figure(figsize=(12, 6))
plt.plot(months, product_a, marker='o', linewidth=2, label='Product A')
plt.plot(months, product_b, marker='s', linewidth=2, label='Product B')
plt.plot(months, product_c, marker='^', linewidth=2, label='Product C')

plt.title('Product Sales Comparison (Monthly)', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales (Units)', fontsize=12)
plt.legend(fontsize=11, loc='upper left')
plt.grid(True, alpha=0.3)
plt.xticks(months)

plt.savefig('multiple_lines.png', dpi=300, bbox_inches='tight')
print("✓ Created: multiple_lines.png")
print("   💡 Use for: Comparing multiple trends over time")
plt.close()

# ============================================================
# PART 8: Customization Examples
# ============================================================
print("\n📌 PART 8: Customization - Making Plots Publication-Ready")
print("-" * 60)

# Create an impressive customized plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(x, y1, color='#FF6B6B', linewidth=3, label='sin(x)', linestyle='-')
ax.plot(x, y2, color='#4ECDC4', linewidth=3, label='cos(x)', linestyle='--')

# Fill area between curves
ax.fill_between(x, y1, y2, where=(y1 >= y2), interpolate=True, alpha=0.3, color='#FF6B6B', label='sin > cos')
ax.fill_between(x, y1, y2, where=(y1 < y2), interpolate=True, alpha=0.3, color='#4ECDC4', label='cos > sin')

# Customize everything
ax.set_title('Sine and Cosine Functions', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('x (radians)', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.legend(fontsize=11, loc='upper right', framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=1)
ax.axhline(y=0, color='k', linewidth=0.8)
ax.axvline(x=0, color='k', linewidth=0.8)

plt.savefig('customized_plot.png', dpi=300, bbox_inches='tight')
print("✓ Created: customized_plot.png")
print("   💡 Professional plots have: titles, labels, legends, grids, colors")
plt.close()

# ============================================================
# SUMMARY AND CHEAT SHEET
# ============================================================
print("\n\n🎯 MATPLOTLIB BASICS SUMMARY")
print("=" * 60)
print("""
✅ Plot Types You Learned:
   1. Line Plot - plt.plot() → Trends over time
   2. Bar Chart - plt.bar() / plt.barh() → Compare categories
   3. Histogram - plt.hist() → Distribution of continuous data
   4. Scatter Plot - plt.scatter() → Relationships between variables
   5. Pie Chart - plt.pie() → Proportions (use sparingly!)
   6. Box Plot - plt.boxplot() → Statistical distribution + outliers
   7. Multiple Lines - Multiple plt.plot() → Compare trends

🎨 Common Customizations:
   • plt.figure(figsize=(width, height)) - Set plot size
   • plt.title() - Add title
   • plt.xlabel() / plt.ylabel() - Add axis labels
   • plt.legend() - Add legend
   • plt.grid() - Add grid lines
   • plt.savefig() - Save to file
   • plt.close() - Close plot to free memory

🔑 Quick Reference:
   • color='blue' or color='#FF6B6B' - Set color
   • linewidth=2 - Line thickness
   • marker='o' - Add markers
   • alpha=0.7 - Transparency (0=transparent, 1=opaque)
   • linestyle='--' - Dash style
   • s=100 - Marker size (scatter)

📊 When to Use Each Plot:
   • Line → Time series, trends
   • Bar → Comparing categories
   • Histogram → Distribution of numbers
   • Scatter → Correlation, relationships
   • Pie → Parts of a whole (max 6 slices)
   • Box → Statistical summary, outliers

💡 Pro Tips:
   1. Always label your axes!
   2. Add a title
   3. Use appropriate colors (not too many!)
   4. Save as PNG with dpi=300 for presentations
   5. Close plots after saving (plt.close())

🚀 Next Steps:
   - Open the PNG files to see your plots!
   - Experiment with colors and styles
   - Learn matplotlib_advanced.py for subplots and complex visualizations
""")

print("\n✅ Matplotlib Basics Complete!")
print("Next file: matplotlib_advanced.py - Multiple plots, heatmaps, and more")
