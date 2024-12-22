import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle
from func import DoublePendulum

# Load the pickle file
with open('dp.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract the angles from the data
theta1 = data['theta1']
theta2 = data['theta2']

# Create an instance of the DoublePendulum class
dp = DoublePendulum()

# Calculate the positions of the double pendulum
x1 = dp.L1 * np.sin(theta1)
y1 = -dp.L1 * np.cos(theta1)
x2 = x1 + dp.L2 * np.sin(theta2)
y2 = y1 - dp.L2 * np.cos(theta2)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-dp.L1 - dp.L2 - 0.5, dp.L1 + dp.L2 + 0.5)
ax.set_ylim(-dp.L1 - dp.L2 - 0.5, dp.L1 + dp.L2 + 0.5)
ax.set_aspect('equal')
ax.grid()

# Initialize the lines for the pendulums
line, = ax.plot([], [], 'o-', lw=2, label='Double Pendulum')
ax.legend()

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function
def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(theta1), init_func=init, blit=True, interval=3, repeat=True)

# Save the animation as an MP4 file
# Uncomment the following lines to save the animation
# writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)
# ani.save('double_pendulum_simulation.mp4', writer=writer)

# Show the animation
plt.tight_layout()
plt.show()