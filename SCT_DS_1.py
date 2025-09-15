import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ["0-20 Years", "21-44 Years", "45+ Years"]
population = [512, 807, 101]  # in millions
percentages = [36.1, 57.0, 6.9]

# Colors (modern palette)
colors = ["#FFD700", "#1E90FF", "#FF69B4"]

# Plot
plt.figure(figsize=(9,6))
bars = plt.bar(age_groups, population, color=colors, edgecolor="black", linewidth=1.2)

# Add labels on bars
for bar, pop, pct in zip(bars, population, percentages):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 15, 
             f"{pop}M\n({pct}%)", 
             ha="center", va="bottom", fontsize=10, fontweight="bold", color="black")

# Titles & Labels
plt.title("India's Population Distribution by Age (2022)", fontsize=15, fontweight="bold")
plt.xlabel("Age Groups", fontsize=12)
plt.ylabel("Population (in Millions)", fontsize=12)

# Styling
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(fontsize=11, fontweight="bold")
plt.yticks(fontsize=11)
plt.box(False)

# Show
plt.tight_layout()
plt.show()
