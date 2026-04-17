import matplotlib.pyplot as plt
import numpy as np

# Import your shiny new package!
from statsplotlib.plotting import create_branded_subplot, add_branded_title

print("Generating STATSports Branded Subplot Demo...")

# 1. Create the canvas with subplots
fig, axes = create_branded_subplot(nrows=3, ncols=1, figsize=(6, 9), transparent=False, watermark=True)
axes = axes.flatten()

# 2. Generate some dummy data
# Top plot (line chart)
innings = np.arange(1, 10)
player1_velocity = [95.2, 95.0, 94.8, 95.5, 94.1, 93.8, 93.0, 92.5, 92.0]
player2_velocity = [86.1, 85.8, 86.0, 85.5, 85.1, 84.9, 84.5, 84.0, 83.8]

# Middle plot (scatter)
np.random.seed(42)
scatter_x = np.random.randn(50)
scatter_y = np.random.randn(50)

# Bottom plot (bar)
teams = ["Team A", "Team B", "Team C", "Team D"]
win_counts = [12, 10, 9, 11]

# 3. Populate the plots
axes[0].plot(innings, player1_velocity, marker='o', label='Player 1')
axes[0].plot(innings, player2_velocity, marker='o', label='Player 2')
axes[0].set_xlabel("Inning")
axes[0].set_ylabel("Pitch Velocity (mph)")
axes[0].legend(loc='upper right', fontsize=8)

axes[1].scatter(scatter_x, scatter_y, alpha=1)
axes[1].set_xlabel("Metric X")
axes[1].set_ylabel("Metric Y")

axes[2].bar(teams, win_counts)
axes[2].set_xlabel("Team")
axes[2].set_ylabel("Wins")

# Add overall branded title
add_branded_title(fig, axes[0], 
                  title_text="Performance Dashboard", 
                  subtitle_text="Example of a 3-row subplot with STATSports branding")

# 8. Adjust layout and save
plt.subplots_adjust(hspace=0.3)
plt.savefig("demo_subplot.png")
plt.show()

print("Demo complete!")