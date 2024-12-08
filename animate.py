import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle

# Load the pickle file
with open('double_pendulum_data.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract the angles, angular velocities, and energies from the data
angles1 = data['angle1']
angles2 = data['angle2']
angular_velocity1 = data['angular_velocity1']
angular_velocity2 = data['angular_velocity2']
kinetic_energies = data['kinetic_energy']
potential_energies = data['potential_energy']
mechanical_energies = data['mechanical_energy']
L1 = 1.0
L2 = 1.0

# Calculate the positions of the pendulums
x1 = L1 * np.sin(angles1)
y1 = -L1 * np.cos(angles1)
x2 = x1 + L2 * np.sin(angles2)
y2 = y1 - L2 * np.cos(angles2)

# Set up the figure and axis
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))

# Set up the animation plot
ax1.set_xlim(-L1 - L2 - 0.5, L1 + L2 + 0.5)
ax1.set_ylim(-L1 - L2 - 0.5, L1 + L2 + 0.5)
line, = ax1.plot([], [], 'o-', lw=2)
ax1.set_title('Double Pendulum Animation')

# Set up the phase space plots
ax2.set_xlim(min(angles1), max(angles1))
ax2.set_ylim(min(angular_velocity1), max(angular_velocity1))
ax2.set_xlabel('Angle 1 (rad)')
ax2.set_ylabel('Angular Velocity 1 (rad/s)')
phase_space1, = ax2.plot([], [], lw=1)
ax2.set_title('Phase Space: Pendulum 1')

ax3.set_xlim(min(angles2), max(angles2))
ax3.set_ylim(min(angular_velocity2), max(angular_velocity2))
ax3.set_xlabel('Angle 2 (rad)')
ax3.set_ylabel('Angular Velocity 2 (rad/s)')
phase_space2, = ax3.plot([], [], lw=1)
ax3.set_title('Phase Space: Pendulum 2')

# Set up the mechanical energy plot
ax4.set_xlim(0, len(angles1) * 0.025)  # Assuming dt = 0.025
ax4.set_ylim(min(mechanical_energies), max(mechanical_energies))
ax4.set_xlabel('Time (s)')
ax4.set_ylabel('Energy (J)')
kinetic_line, = ax4.plot([], [], label='Kinetic Energy', lw=1)
potential_line, = ax4.plot([], [], label='Potential Energy', lw=1)
mechanical_line, = ax4.plot([], [], label='Mechanical Energy', lw=1)
ax4.legend()
ax4.set_title('Energy vs Time')

# Initialization function
def init():
    line.set_data([], [])
    phase_space1.set_data([], [])
    phase_space2.set_data([], [])
    kinetic_line.set_data([], [])
    potential_line.set_data([], [])
    mechanical_line.set_data([], [])
    return line, phase_space1, phase_space2, kinetic_line, potential_line, mechanical_line

# Animation function
def animate(frame):
    # thisx = [0, x1[frame], x2[frame]]
    # thisy = [0, y1[frame], y2[frame]]
    line.set_data([0, x1[frame], x2[frame]], [0, y1[frame], y2[frame]])
    
    phase_space1.set_data(angles1[:frame], angular_velocity1[:frame])
    phase_space2.set_data(angles2[:frame], angular_velocity2[:frame])
    
    kinetic_line.set_data(np.arange(0, frame * 0.025, 0.025), kinetic_energies[:frame])
    potential_line.set_data(np.arange(0, frame * 0.025, 0.025), potential_energies[:frame])
    mechanical_line.set_data(np.arange(0, frame * 0.025, 0.025), mechanical_energies[:frame])
    
    return line, phase_space1, phase_space2, kinetic_line, potential_line, mechanical_line

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(angles1), init_func=init, blit=True, interval=10, repeat=True)

# Show the animation
plt.tight_layout()
plt.show()