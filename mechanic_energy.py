import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pickle

# Load the pickle file
with open('double_pendulum_data.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract the time and energies from the data
time = data['t']
kinetic_energy = data['kinetic_energy']
potential_energy = data['potential_energy']
mechanical_energy = data['mechanical_energy']

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(min(time), max(time))
ax.set_ylim(min(min(kinetic_energy), min(potential_energy), min(mechanical_energy)),
            max(max(kinetic_energy), max(potential_energy), max(mechanical_energy)))
ax.set_xlabel('Time (s)')
ax.set_ylabel('Energy (J)')
ax.set_title('Energy of Double Pendulum')

# Initialize the lines for the energies
line_ke, = ax.plot([], [], 'r-', lw=2, label='Kinetic Energy')
line_pe, = ax.plot([], [], 'b-', lw=2, label='Potential Energy')
line_me, = ax.plot([], [], 'g-', lw=2, label='Mechanical Energy')
ax.legend()

# Initialization function
def init():
    line_ke.set_data([], [])
    line_pe.set_data([], [])
    line_me.set_data([], [])
    return line_ke, line_pe, line_me

# Animation function
def animate(i):
    line_ke.set_data(time[:i], kinetic_energy[:i])
    line_pe.set_data(time[:i], potential_energy[:i])
    line_me.set_data(time[:i], mechanical_energy[:i])
    return line_ke, line_pe, line_me

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(time), init_func=init, blit=True, interval=25, repeat=True)

# Show the animation
plt.show()