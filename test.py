import numpy as np
import matplotlib.pyplot as plt
from Hamiltonian import Hamiltonian_dp
from solver import solver

# Initialize parameters
dp = Hamiltonian_dp(m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81)
y0 = [np.radians(45), np.radians(45), 0.0, 0.0]  # initial conditions

# Perturbation for the second trajectory
delta_y0 = [1e-8, 0, 0, 0]
y0_perturbed = np.add(y0, delta_y0)

# Time span
t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

# Solve for both trajectories using the solver function
sol1 = solver(dp.H, y0, t_span, t_eval, method='DOP853')
sol2 = solver(dp.H, y0_perturbed, t_span, t_eval, method='DOP853')

# Calculate separation and Lyapunov exponent
separations = np.linalg.norm(sol2.y - sol1.y, axis=0)
lyapunov_exponent = np.mean(np.log(separations / separations[0])) / (t_span[1] - t_span[0])

print(f"Largest Lyapunov Exponent: {lyapunov_exponent}")

# Plot the separation of the trajectories
plt.figure(figsize=(10, 6))
plt.plot(t_eval, separations, label='Separation')
plt.xlabel('Time (s)')
plt.ylabel('Separation')
plt.title('Separation of Trajectories Over Time')
plt.legend()
plt.grid(True)
plt.show()