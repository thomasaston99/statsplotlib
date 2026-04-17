# demo.py
import matplotlib.pyplot as plt
import numpy as np

# Import your shiny new package!
from statsplotlib.plotting import create_branded_plot, add_branded_title

print("Generating STATSports Branded Demo Plot...")

# 1. Create the canvas (using the default transparent background)
fig, ax = create_branded_plot(watermark=True, transparent=False) 

# 2. Generate some dummy data
innings = np.arange(1, 10)
player1 = [95.2, 95.0, 94.8, 95.5, 94.1, 93.8, 93.0, 92.5, 92.0]
player2 = [86.1, 85.8, 86.0, 85.5, 85.1, 84.9, 84.5, 84.0, 83.8]

# 3. Plot the data
ax.plot(innings, player1, marker='o', label="Player 1", linewidth=3)
ax.plot(innings, player2, marker='s', label="Player 2", linewidth=3)

# 4. Add the branded titles and labels
add_branded_title(fig, ax, 
                  title_text="Pitcher Velocity Drop-off", 
                  subtitle_text="Simulated Data: Player 1 vs Player 2 over 9 Innings")
                  
ax.set_xlabel("Inning")
ax.set_ylabel("Velocity (mph)")
ax.set_xticks(innings)
ax.legend(loc='upper right')
plt.savefig("demo_plot.png")
plt.show()

print("Demo complete! If you see the Oswald titles, the STATSports logo, and the clean background, your package is perfect.")