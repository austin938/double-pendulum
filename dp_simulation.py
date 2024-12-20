import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle

# Load the pickle file
with open('double_pendulum_data.pickle', 'rb') as f:
    data1 = pickle.load(f)
with open('double_pendulum_data1.pickle', 'rb') as f:
    data2 = pickle.load(f)

# Extract the angles from the data
angles1_1 = data1['angle1']
angles2_1 = data1['angle2']
angles1_2 = data2['angle1']
angles2_2 = data2['angle2']
L1 = 1.0
L2 = 1.0

# Calculate the positions of the first double pendulum
x1_1 = L1 * np.sin(angles1_1)
y1_1 = -L1 * np.cos(angles1_1)
x2_1 = x1_1 + L2 * np.sin(angles2_1)
y2_1 = y1_1 - L2 * np.cos(angles2_1)

# Calculate the positions of the second double pendulum
x1_2 = L1 * np.sin(angles1_2)
y1_2 = -L1 * np.cos(angles1_2)
x2_2 = x1_2 + L2 * np.sin(angles2_2)
y2_2 = y1_2 - L2 * np.cos(angles2_2)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-L1 - L2 - 0.5, L1 + L2 + 0.5)
ax.set_ylim(-L1 - L2 - 0.5, L1 + L2 + 0.5)
ax.set_aspect('equal')
ax.grid()

# Initialize the lines for the pendulums
line1, = ax.plot([], [], 'o-', lw=2, label='Pendulum 1')
line2, = ax.plot([], [], 'o-', lw=2, label='Pendulum 2')
ax.legend()

# Initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Animation function
def animate(i):
    # Update first double pendulum
    thisx1_1 = [0, x1_1[i], x2_1[i]]
    thisy1_1 = [0, y1_1[i], y2_1[i]]
    line1.set_data(thisx1_1, thisy1_1)
    
    # Update second double pendulum
    thisx1_2 = [0, x1_2[i], x2_2[i]]
    thisy1_2 = [0, y1_2[i], y2_2[i]]
    line2.set_data(thisx1_2, thisy1_2)
    
    return line1, line2

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(angles1_1), init_func=init, blit=True, interval=5, repeat=True)

# Save the animation as an MP4 file
# writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)
# ani.save('double_pendulum_simulation.mp4', writer=writer)

# Show the animation
plt.tight_layout()
plt.show()
