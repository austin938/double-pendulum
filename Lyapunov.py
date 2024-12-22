import numpy as np
import matplotlib.pyplot as plt
import pickle

# Load the data from the pickle file
with open('Hamiltonian_dp.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract the data
time = data['t']
theta1 = data['theta1']
theta1_perturbed = data['theta1_perturbed']



# Calculate the separation between the original and perturbed trajectories
separations = np.abs(theta1_perturbed - theta1)

# Calculate the Lyapunov exponent
lyapunov_exponent = np.mean(np.log(separations / separations[0])) / (time[-1] - time[0])

print(f"Largest Lyapunov Exponent: {lyapunov_exponent}")

# Plot the separation of the trajectories
plt.figure(figsize=(10, 6))
plt.plot(time, separations, label='Separation')
plt.xlabel('Time (s)')
plt.ylabel('Separation')
plt.title('Separation of Trajectories Over Time')
plt.legend()
plt.grid(True)
plt.show()