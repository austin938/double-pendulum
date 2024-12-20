import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle

# Load the pickle files
with open('double_pendulum_data.pickle', 'rb') as f:
    data1 = pickle.load(f)

with open('double_pendulum_data1.pickle', 'rb') as f:
    data2 = pickle.load(f)

# Extract the data for the first double pendulum
angles1_1 = data1['angle1']
angles2_1 = data1['angle2']
angular_velocity1_1 = data1['angular_velocity1']
angular_velocity2_1 = data1['angular_velocity2']
time1 = data1['t']
kinetic_energy1 = data1['kinetic_energy']
potential_energy1 = data1['potential_energy']
mechanical_energy1 = data1['mechanical_energy']

# Extract the data for the second double pendulum
angles1_2 = data2['angle1']
angles2_2 = data2['angle2']
angular_velocity1_2 = data2['angular_velocity1']
angular_velocity2_2 = data2['angular_velocity2']
time2 = data2['t']
kinetic_energy2 = data2['kinetic_energy']
potential_energy2 = data2['potential_energy']
mechanical_energy2 = data2['mechanical_energy']

# Calculate the positions of the pendulums
L1 = 1.0
L2 = 1.0
x1_1 = L1 * np.sin(angles1_1)
y1_1 = -L1 * np.cos(angles1_1)
x2_1 = x1_1 + L2 * np.sin(angles2_1)
y2_1 = y1_1 - L2 * np.cos(angles2_1)

x1_2 = L1 * np.sin(angles1_2)
y1_2 = -L1 * np.cos(angles1_2)
x2_2 = x1_2 + L2 * np.sin(angles2_2)
y2_2 = y1_2 - L2 * np.cos(angles2_2)

# Set up the figure and axes
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# Set up the double pendulum plot
ax1.set_xlim(-L1 - L2 - 0.5, L1 + L2 + 0.5)
ax1.set_ylim(-L1 - L2 - 0.5, L1 + L2 + 0.5)
ax1.set_aspect('equal')
ax1.grid()
line1, = ax1.plot([], [], 'o-', lw=2, label='Pendulum 1')
line2, = ax1.plot([], [], 'o-', lw=2, label='Pendulum 2')
ax1.legend()
ax1.set_title('Double Pendulum Simulation')

# Set up the energy plot
ax2.set_xlim(min(time1), max(time1))
ax2.set_ylim(min(min(kinetic_energy1), min(potential_energy1), min(mechanical_energy1),
                 min(kinetic_energy2), min(potential_energy2), min(mechanical_energy2)),
             max(max(kinetic_energy1), max(potential_energy1), max(mechanical_energy1),
                 max(kinetic_energy2), max(potential_energy2), max(mechanical_energy2)))
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Energy (J)')
ax2.set_title('Energy of Double Pendulum')
line_ke1, = ax2.plot([], [], 'r-', lw=2, label='Kinetic Energy 1')
line_pe1, = ax2.plot([], [], 'b-', lw=2, label='Potential Energy 1')
line_me1, = ax2.plot([], [], 'g-', lw=2, label='Mechanical Energy 1')
line_ke2, = ax2.plot([], [], 'r--', lw=2, label='Kinetic Energy 2')
line_pe2, = ax2.plot([], [], 'b--', lw=2, label='Potential Energy 2')
line_me2, = ax2.plot([], [], 'g--', lw=2, label='Mechanical Energy 2')
ax2.legend()

# Set up the phase space plot for pendulum 1
ax3.set_xlim(min(angles1_1), max(angles1_1))
ax3.set_ylim(min(min(angular_velocity1_1), min(angular_velocity1_2)), max(max(angular_velocity1_1), max(angular_velocity1_2)))
ax3.set_xlabel('Angle 1 (rad)')
ax3.set_ylabel('Angular Velocity 1 (rad/s)')
phase_space1_1, = ax3.plot([], [], 'r-', lw=1, label='Pendulum 1')
phase_space1_2, = ax3.plot([], [], 'b-', lw=1, label='Pendulum 2')
ax3.set_title('Phase Space: Pendulum 1')
ax3.legend()

# Set up the phase space plot for pendulum 2
ax4.set_xlim(min(angles2_1), max(angles2_1))
ax4.set_ylim(min(min(angular_velocity2_1), min(angular_velocity2_2)), max(max(angular_velocity2_1), max(angular_velocity2_2)))
ax4.set_xlabel('Angle 2 (rad)')
ax4.set_ylabel('Angular Velocity 2 (rad/s)')
phase_space2_1, = ax4.plot([], [], 'r-', lw=1, label='Pendulum 1')
phase_space2_2, = ax4.plot([], [], 'b-', lw=1, label='Pendulum 2')
ax4.set_title('Phase Space: Pendulum 2')
ax4.legend()

# Initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line_ke1.set_data([], [])
    line_pe1.set_data([], [])
    line_me1.set_data([], [])
    line_ke2.set_data([], [])
    line_pe2.set_data([], [])
    line_me2.set_data([], [])
    phase_space1_1.set_data([], [])
    phase_space1_2.set_data([], [])
    phase_space2_1.set_data([], [])
    phase_space2_2.set_data([], [])
    return line1, line2, line_ke1, line_pe1, line_me1, line_ke2, line_pe2, line_me2, phase_space1_1, phase_space1_2, phase_space2_1, phase_space2_2

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
    
    # Update energy plot
    line_ke1.set_data(time1[:i], kinetic_energy1[:i])
    line_pe1.set_data(time1[:i], potential_energy1[:i])
    line_me1.set_data(time1[:i], mechanical_energy1[:i])
    line_ke2.set_data(time2[:i], kinetic_energy2[:i])
    line_pe2.set_data(time2[:i], potential_energy2[:i])
    line_me2.set_data(time2[:i], mechanical_energy2[:i])
    
    # Update phase space plots
    phase_space1_1.set_data(angles1_1[:i], angular_velocity1_1[:i])
    phase_space1_2.set_data(angles1_2[:i], angular_velocity1_2[:i])
    phase_space2_1.set_data(angles2_1[:i], angular_velocity2_1[:i])
    phase_space2_2.set_data(angles2_2[:i], angular_velocity2_2[:i])
    
    return line1, line2, line_ke1, line_pe1, line_me1, line_ke2, line_pe2, line_me2, phase_space1_1, phase_space1_2, phase_space2_1, phase_space2_2

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(time1), init_func=init, blit=True, interval=10, repeat=True)

# Save the animation as an MP4 file
# writer = animation.FFMpegWriter(fps=60, metadata=dict(artist='Me'), bitrate=1800)
# ani.save('double_pendulum_simulation_verfication.mp4', writer=writer)

# Show the animation
plt.tight_layout()
plt.show()