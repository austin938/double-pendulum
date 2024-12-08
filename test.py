# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import pickle

# # Load the pickle file
# with open('double_pendulum_data.pickle', 'rb') as f:
#     data = pickle.load(f)

# # Extract the angles and angular velocities from the data
# angles1 = data['angle1']
# angles2 = data['angle2']
# angular_velocity1 = data['angular_velocity1']
# angular_velocity2 = data['angular_velocity2']

# # Create the figure and axis for phase space plots
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))

# # Set up the phase space plot for pendulum 1
# ax1.set_xlim(min(angles1), max(angles1))
# ax1.set_ylim(min(angular_velocity1), max(angular_velocity1))
# ax1.set_xlabel('Angle 1 (rad)')
# ax1.set_ylabel('Angular Velocity 1 (rad/s)')
# phase_space1, = ax1.plot([], [], lw=1)
# ax1.set_title('Phase Space: Pendulum 1')

# # Set up the phase space plot for pendulum 2
# ax2.set_xlim(min(angles2), max(angles2))
# ax2.set_ylim(min(angular_velocity2), max(angular_velocity2))
# ax2.set_xlabel('Angle 2 (rad)')
# ax2.set_ylabel('Angular Velocity 2 (rad/s)')
# phase_space2, = ax2.plot([], [], lw=1)
# ax2.set_title('Phase Space: Pendulum 2')

# # Initialization function
# def init():
#     phase_space1.set_data([], [])
#     phase_space2.set_data([], [])
#     return phase_space1, phase_space2

# # Animation function
# def animate(frame):
#     phase_space1.set_data(angles1[:frame], angular_velocity1[:frame])
#     phase_space2.set_data(angles2[:frame], angular_velocity2[:frame])
#     return phase_space1, phase_space2

# # Create the animation
# ani = animation.FuncAnimation(fig, animate, frames=len(angles1), init_func=init, blit=True, interval=10, repeat=True)

# # Show the animation
# plt.tight_layout()
# plt.show()

a = [1, 2, 3, 4, 5]
for N in range(len(a)):
    print(a[N])
    print(a[:N+1])


