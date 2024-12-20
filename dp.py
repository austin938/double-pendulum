import numpy as np
from scipy.integrate import solve_ivp
import pickle

method = 'rk4'
# Parameters
g = 9.8  # Gravity (m/s^2)
L1 = 1.0  # Length of pendulum 1 (m)
L2 = 1.0  # Length of pendulum 2 (m)
m1 = 1.0  # Mass of pendulum 1 (kg)
m2 = 1.0  # Mass of pendulum 2 (kg)
angle1 = np.pi / 2  # Initial angle of pendulum 1
angle2 = 1.00001  # Initial angle of pendulum 2
angular_velocity1 = 0.0  # Initial angular velocity of pendulum 1
angular_velocity2 = 0.0  # Initial angular velocity of pendulum 2

def rk4(yin: list, t: float, dt: float, func: callable) -> np.ndarray:
    k1 = func(yin, t)
    k2 = func(yin + k1 * dt * 0.5, t + 0.5 * dt)
    k3 = func(yin + k2 * dt * 0.5, t + dt * 0.5)
    k4 = func(yin + dt * k3, t + dt)
    ynext = yin + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return ynext

# Function to update the state using RK45
def rk45(yin, t_span, dt, func):
    sol = solve_ivp(func, t_span, yin, method='RK45', t_eval=np.arange(t_span[0], t_span[1], dt))
    return sol.y.T

# Function to compute the derivatives
def func(time: float, yin: list) -> np.ndarray:
    angle1, angle2, angular_velocity1, angular_velocity2 = yin
    dydt = np.zeros(4)
    dydt[0] = angular_velocity1
    dydt[1] = angular_velocity2
    dydt[2] = (-0.5 * L1 * m2 * np.sin(2 * angle1 - 2 * angle2) * angular_velocity1**2
               - 1.0 * L2 * m2 * np.sin(angle1 - angle2) * angular_velocity2**2
               - 1.0 * g * m1 * np.sin(angle1)
               - 0.5 * g * m2 * np.sin(angle1 - 2 * angle2)
               - 0.5 * g * m2 * np.sin(angle1)) / (L1 * (m1 - m2 * np.cos(angle1 - angle2)**2 + m2))
    dydt[3] = (1.0 * L1 * m1 * np.sin(angle1 - angle2) * angular_velocity1**2
               + 1.0 * L1 * m2 * np.sin(angle1 - angle2) * angular_velocity1**2
               + 0.5 * L2 * m2 * np.sin(2 * angle1 - 2 * angle2) * angular_velocity2**2
               + 0.5 * g * m1 * np.sin(2 * angle1 - angle2)
               - 0.5 * g * m1 * np.sin(angle2)
               + 0.5 * g * m2 * np.sin(2 * angle1 - angle2)
               - 0.5 * g * m2 * np.sin(angle2)) / (L2 * (m1 - m2 * np.cos(angle1 - angle2)**2 + m2))
    return dydt

def kinetic_energy(angular_velocity1, angular_velocity2, m1, m2):
    k1 = 0.5 * m1 * (L1 * angular_velocity1)**2
    k2 = 0.5 * m2 * ((L1 * angular_velocity1)**2 + (L2 * angular_velocity2)**2
                      + 2 * L1 * L2 * angular_velocity1 * angular_velocity2 * np.cos(angle1 - angle2))
    return k1 + k2

def potential_energy(angle1, angle2, m1, m2):
    y1 = -L1 * np.cos(angle1)
    y2 = y1 - L2 * np.cos(angle2)
    p1 = m1 * g * y1
    p2 = m2 * g * y2
    return p1 + p2

def mechanical_energy(angle1, angle2, angular_velocity1, angular_velocity2, m1, m2):
    return kinetic_energy(angular_velocity1, angular_velocity2, m1, m2) + potential_energy(angle1, angle2, m1, m2)

# Function to update the state using adaptive Runge-Kutta
# def adaptive_rk(yin, t_span, dt, func, tol=1e-6):
#     t = t_span[0]
#     y = np.array(yin)
#     results = [y]
#     times = [t]
    
#     while t < t_span[1]:
#         k1 = func(y, t)
#         k2 = func(y + k1 * dt * 0.5, t + 0.5 * dt)
#         k3 = func(y + k2 * dt * 0.5, t + 0.5 * dt)
#         k4 = func(y + k3 * dt, t + dt)
        
#         y4 = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        
#         k1 = func(y4, t + dt)
#         k2 = func(y4 + k1 * dt * 0.5, t + 1.5 * dt)
#         k3 = func(y4 + k2 * dt * 0.5, t + 1.5 * dt)
#         k4 = func(y4 + k3 * dt, t + 2 * dt)
        
#         y5 = y4 + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        
#         error = np.linalg.norm(y5 - y4)
        
#         if error < tol:
#             t += dt
#             y = y4
#             results.append(y)
#             times.append(t)
        
#         dt *= min(max_factor, max(min_factor, safety * (tol / error)**0.25))
    
#     return np.array(results), np.array(times)

# Function to update the state
def update(t, dt, angle1, angular_velocity1, angle2, angular_velocity2, method):
    yin = [angle1, angle2, angular_velocity1, angular_velocity2]
    if method == 'rk4':
        yout = rk4(yin, t, dt, func)
    elif method == 'rk45':
        yout = rk45(yin, (t, t + dt), dt, func)
    # elif method == 'adaptive_rk':
    #     yout, times = adaptive_rk(yin, (t, t + dt), dt, func)
    return yout[0], yout[1], yout[2], yout[3]

# Example usage
if __name__ == "__main__":
    t = 0
    dt = 0.025
    duration = 10  # Set the duration of the simulation in seconds
    data = {
        't': [],
        'angle1': [],
        'angle2': [],
        'angular_velocity1': [],
        'angular_velocity2': [],
        'kinetic_energy': [],
        'potential_energy': [],
        'mechanical_energy': []
    }
    
    while t < duration:
        angle1, angle2, angular_velocity1, angular_velocity2 = update(t, dt, angle1, angular_velocity1, angle2, angular_velocity2, method)
        t += dt
        data['t'].append(t)
        data['angle1'].append(angle1)
        data['angle2'].append(angle2)
        data['angular_velocity1'].append(angular_velocity1)
        data['angular_velocity2'].append(angular_velocity2)
        ke = kinetic_energy(angular_velocity1, angular_velocity2, m1, m2)
        pe = potential_energy(angle1, angle2, m1, m2)
        me = ke + pe
        data['kinetic_energy'].append(ke)
        data['potential_energy'].append(pe)
        data['mechanical_energy'].append(me)
        print(f"t={t:.2f}, angle1={angle1:.2f}, angle2={angle2:.2f}, angular_velocity1={angular_velocity1:.2f}, angular_velocity2={angular_velocity2:.2f}, KE={ke:.2f}, PE={pe:.2f}, ME={me:.2f}")
    
    # Save the data to a pickle file
    with open('double_pendulum_data1.pickle', 'wb') as f:
        pickle.dump(data, f)
    print("Simulation completed and data saved.")