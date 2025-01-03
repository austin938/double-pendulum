import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load the pickle file
with open('Hamiltonian_dp.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract the data
time = data['t']
theta1 = data['theta1']
theta2 = data['theta2']
momentum1 = data['momentum1']
momentum2 = data['momentum2']
mechanical_energy = data['mechanical_energy']

# Set up the figure and axis
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Double Pendulum Simulation (Hamiltonian Mechanics)')
axs[0, 0].set_title('Angles vs Time')
axs[0, 0].set_xlabel('Time (s)')
axs[0, 0].set_ylabel('Angle (radians)')
axs[0, 1].set_title('Momenta vs Time')
axs[0, 1].set_xlabel('Time (s)')
axs[0, 1].set_ylabel('Momentum (kg m^2/s)')
axs[1, 0].set_title('Energy vs Time')
axs[1, 0].set_xlabel('Time (s)')
axs[1, 0].set_ylabel('Energy (J)')
axs[1, 0].set_ylim(min(mechanical_energy), max(mechanical_energy))
axs[1, 1].set_title('Poincaré Section')
axs[1, 1].set_xlabel('Theta1 (radians)')
axs[1, 1].set_ylabel('Momentum1 (kg m^2/s)')
axs[1, 1].set_xlim(-1, 1)
axs[1, 1].set_ylim(min(momentum1)-1, max(momentum1)+1)

# Plot the angles
axs[0, 0].plot(time, theta1, label=f'theta1')
axs[0, 0].plot(time, theta2, label=f'theta2')
axs[0, 0].legend(loc='best')
axs[0, 0].grid(True)

# Plot the momenta
axs[0, 1].plot(time, momentum1, label=f'momentum1')
axs[0, 1].plot(time, momentum2, label=f'momentum2')
axs[0, 1].legend(loc='best')
axs[0, 1].grid(True)

# Plot the energies
axs[1, 0].plot(time, mechanical_energy, label='Mechanical Energy')
axs[1, 0].legend(loc='best')
axs[1, 0].grid(True)

# Extract Poincaré section data at fixed time intervals
interval = 0.005  # Fixed time interval
poincare_theta1 = []
poincare_momentum1 = []

for i in range(1, len(time)):
    if np.isclose(time[i] % interval, 0, atol=1e-3):
        poincare_theta1.append(theta1[i])
        poincare_momentum1.append(momentum1[i])

# Plot the Poincaré section
axs[1, 1].plot(poincare_theta1, poincare_momentum1, 'o', label='Poincaré Section')
axs[1, 1].legend(loc='best')
axs[1, 1].grid(True)

# Save the figure
# fig.savefig('Hamiltonian_dp_simulation.png')
# print("Figure saved as Hamiltonian_dp_simulation.png")

# Show the figure
plt.tight_layout()
plt.show()