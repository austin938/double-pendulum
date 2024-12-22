import numpy as np
import pickle
from solver import solver
from Lagrangian import Lagrangian_dp
from Hamiltonian import Hamiltonian_dp

# Initial conditions and parameters
t_span = (0, 40)  # Time interval
t_eval = np.linspace(t_span[0], t_span[1], 4000)  # Time points at which to store the computed solution
method = 'DOP853'  # ODE solver to use
mechanics = 'Hamiltonian'  # Type of mechanics to use



# Solve the ODE 
if mechanics == 'Lagrangian':
    dp = Lagrangian_dp()
    y0 = [np.radians(45), np.radians(45), 1.0, 1.0]  # Initial state of Lagrangian
    delta_y0 = [1e-8, 0, 0, 0]
    y0_perturbed = np.add(y0, delta_y0)
    sol = solver(dp.L, y0, t_span, t_eval, method)
    sol_perturbed = solver(dp.L, y0_perturbed, t_span, t_eval, method)
    E = dp.mechanical_energy(sol.y)
    data = {
        't': sol.t,
        'theta1': sol.y[0],
        'theta2': sol.y[1],
        'omega1': sol.y[2],
        'omega2': sol.y[3],
        'mechanical_energy': E
    }
elif mechanics == 'Hamiltonian':
    dp = Hamiltonian_dp()
    y0 = [0.0, 0.0, 0.0, 5.0] # Initial state of Hamiltonian
    delta_y0 = [1e-8, 0, 0, 0]
    y0_perturbed = np.add(y0, delta_y0)
    sol = solver(dp.H, y0, t_span, t_eval, method)
    sol_perturbed = solver(dp.H, y0_perturbed, t_span, t_eval, method)
    E = dp.mechanical_energy(sol.y)
    data = {
        't': sol.t,
        'theta1': sol.y[0],
        'theta2': sol.y[1],
        'momentum1': sol.y[2],
        'momentum2': sol.y[3],
        'mechanical_energy': E
    }
else:
    raise SystemExit("Error: mechanics "+mechanics+" is not supported!")


# Save the solution data to a pickle file

with open(f'{mechanics}_dp.pickle', 'wb') as f:
    pickle.dump(data, f)

print(f"Mechanics: {mechanics} \nData saved to {mechanics}_dp.pickle")
