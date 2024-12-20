import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle

# Load the pickle files
with open('double_pendulum_data.pickle', 'rb') as f:
    data1 = pickle.load(f)

with open('double_pendulum_data1.pickle', 'rb') as f:
    data2 = pickle.load(f)

# Extract the angles and angular velocities from the data
angles1_1 = data1['angle1']
angles2_1 = data1['angle2']
angular_velocity1_1 = data1['angular_velocity1']
angular_velocity2_1 = data1['angular_velocity2']

angles1_2 = data2['angle1']
angles2_2 = data2['angle2']
angular_velocity1_2 = data2['angular_velocity1']
angular_velocity2_2 = data2['angular_velocity2']

# Set up the figure and axis for phase space plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Set up the phase space plot for pendulum 1
ax1.set_xlim(min(min(angles1_1), min(angles1_2)), max(max(angles1_1), max(angles1_2)))
ax1.set_ylim(min(min(angular_velocity1_1), min(angular_velocity1_2)), max(max(angular_velocity1_1), max(angular_velocity1_2)))
ax1.set_xlabel('Angle 1 (rad)')
ax1.set_ylabel('Angular Velocity 1 (rad/s)')
phase_space1_1, = ax1.plot([], [], 'r-', lw=1, label='Pendulum 1')
phase_space1_2, = ax1.plot([], [], 'b-', lw=1, label='Pendulum 2')
ax1.set_title('Phase Space: Pendulum 1')
ax1.legend()

# Set up the phase space plot for pendulum 2
ax2.set_xlim(min(min(angles2_1), min(angles2_2)), max(max(angles2_1), max(angles2_2)))
ax2.set_ylim(min(min(angular_velocity2_1), min(angular_velocity2_2)), max(max(angular_velocity2_1), max(angular_velocity2_2)))
ax2.set_xlabel('Angle 2 (rad)')
ax2.set_ylabel('Angular Velocity 2 (rad/s)')
phase_space2_1, = ax2.plot([], [], 'r-', lw=1, label='Pendulum 1')
phase_space2_2, = ax2.plot([], [], 'b-', lw=1, label='Pendulum 2')
ax2.set_title('Phase Space: Pendulum 2')
ax2.legend()

# Initialization function
def init():
    phase_space1_1.set_data([], [])
    phase_space1_2.set_data([], [])
    phase_space2_1.set_data([], [])
    phase_space2_2.set_data([], [])
    return phase_space1_1, phase_space1_2, phase_space2_1, phase_space2_2

# Animation function
def animate(frame):
    phase_space1_1.set_data(angles1_1[:frame], angular_velocity1_1[:frame])
    phase_space1_2.set_data(angles1_2[:frame], angular_velocity1_2[:frame])
    phase_space2_1.set_data(angles2_1[:frame], angular_velocity2_1[:frame])
    phase_space2_2.set_data(angles2_2[:frame], angular_velocity2_2[:frame])
    return phase_space1_1, phase_space1_2, phase_space2_1, phase_space2_2

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(angles1_1), init_func=init, blit=True, interval=10, repeat=True)

# Show the animation
plt.tight_layout()
plt.show()