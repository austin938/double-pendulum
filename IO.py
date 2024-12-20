import numpy as np
import pickle
from solver import rk45
from initialization import func

# Initial conditions and parameters
y0 = [np.radians(5), 0.0, 0.0, 0.0]  # Initial state
t_span = (0, 10)  # Time interval
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Time points at which to store the computed solution

# Solve the ODE using RK45
sol = rk45(func, y0, t_span, t_eval)

# Save the solution data to a pickle file
data = {
    't': sol.t,
    'theta1': sol.y[0],
    'theta2': sol.y[1],
    'omega1': sol.y[2],
    'omega2': sol.y[3]
}

with open('dp.pickle', 'wb') as f:
    pickle.dump(data, f)

print("Data saved to dp.pickle")
