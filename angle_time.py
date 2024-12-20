import pickle
import matplotlib.pyplot as plt

# Load the data from the pickle file
with open('dp.pickle', 'rb') as f:
    data = pickle.load(f)

# Extract the data
time = data['t']
angle1 = data['theta1']
angle2 = data['theta2']

# Create the plot with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot theta1 vs time
ax1.plot(time, angle1, label='Theta 1')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Angle 1 (rad)')
ax1.set_title('Theta 1 vs Time')
ax1.legend()

# Plot theta2 vs time
ax2.plot(time, angle2, label='Theta 2')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Angle 2 (rad)')
ax2.set_title('Theta 2 vs Time')
ax2.legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()