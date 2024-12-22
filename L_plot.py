import pickle
import numpy as np
import matplotlib.pyplot as plt


# Load the pickle file
with open(f'Lagrangian_dp.pickle', 'rb') as f:
    data = pickle.load(f)


# Extract the data
time = data['t']
theta1 = data['theta1']
theta2 = data['theta2']
omega1 = data['omega1']
omega2 = data['omega2']
mechanical_energy = data['mechanical_energy']


# Set up the figure and axis
fig, axs = plt.subplots(4, 1, figsize=(10, 12))
fig.suptitle('Double Pendulum Simulation')
axs[0].set_title('Angles vs Time')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Angle (radians)')
axs[1].set_title('Angular Velocities vs Time')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Angular Velocity (rad/s)')
axs[2].set_title('Energy vs Time')
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Energy (J)')
axs[2].set_ylim(min(mechanical_energy), max(mechanical_energy))
axs[3].set_title('Poincaré Section')
axs[3].set_xlabel('Theta1 (radians)')
axs[3].set_ylabel('Omega1 (rad/s)')
axs[3].set_xlim(-np.pi, np.pi)
axs[3].set_ylim(min(omega1)-1, max(omega1)+1)

# Plot the angles
axs[0].plot(time, theta1, label='theta1')
axs[0].plot(time, theta2, label='theta2')
axs[0].legend(loc='best')
axs[0].grid('True')

# Plot the angular velocities
axs[1].plot(time, omega1, label='omega1')
axs[1].plot(time, omega2, label='omega2')
axs[1].legend(loc='best')
axs[1].grid('True')

# Plot the energies
axs[2].plot(time, mechanical_energy, label='Mechanical Energy')
axs[2].legend(loc='best')
axs[2].grid('True')

# Extract Poincaré section data
poincare_theta1 = []
poincare_omega1 = []

for i in range(1, len(time) - 1):
    if theta1[i-1] < 0 and theta1[i] >= 0:
        poincare_theta1.append(theta1[i])
        poincare_omega1.append(omega1[i])

# Plot the Poincaré section
axs[3].plot(poincare_theta1, poincare_omega1, 'o', label='Poincaré Section')
axs[3].legend(loc='best')
axs[3].grid(True)

# Save the figure
fig.savefig(f'Lagrangian_dp_simulation.png')
print("Figure saved as double_pendulum_simulation.png")


# Show the figure
plt.tight_layout()
plt.show()