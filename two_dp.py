import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
g = 9.8  # Gravity (m/s^2)
L1 = 1.0  # Length of pendulum 1 (m)
L2 = 1.0  # Length of pendulum 2 (m)
m1 = 1.0  # Mass of pendulum 1 (kg)
m2 = 1.0  # Mass of pendulum 2 (kg)
angle1 = np.pi / 2  # Initial angle of pendulum 1
angle2 = np.pi / 2  # Initial angle of pendulum 2
angular_velocity1 = 0.0  # Initial angular velocity of pendulum 1
angular_velocity2 = 0.0  # Initial angular velocity of pendulum 2

# Function to compute the derivatives
def func(t, yin):
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

# Function to update the state using RK4
def rk4(yin, t, dt, func):
    k1 = func(t, yin)
    k2 = func(t + 0.5 * dt, yin + 0.5 * dt * k1)
    k3 = func(t + 0.5 * dt, yin + 0.5 * dt * k2)
    k4 = func(t + dt, yin + dt * k3)
    ynext = yin + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return ynext

# Function to update the state using RK45
def rk45(yin, t_span, dt, func):
    sol = solve_ivp(func, t_span, yin, method='RK45', t_eval=np.arange(t_span[0], t_span[1], dt))
    return sol.y.T

# Function to update the state using adaptive Runge-Kutta
def adaptive_rk(yin, t_span, dt, func):
    sol = solve_ivp(func, t_span, yin, method='DOP853', t_eval=np.arange(t_span[0], t_span[1], dt))
    return sol.y.T

# Example usage
if __name__ == "__main__":
    t = 0
    dt = 0.025
    t_max = 10
    t_span = (0, t_max)
    yin = [angle1, angle2, angular_velocity1, angular_velocity2]

    # Using RK4
    results_rk4 = []
    y = yin
    for _ in np.arange(t_span[0], t_span[1], dt):
        results_rk4.append(y)
        y = rk4(y, t, dt, func)
    results_rk4 = np.array(results_rk4)

    # Using RK45
    results_rk45 = rk45(yin, t_span, dt, func)

    # Using Adaptive Runge-Kutta
    results_adaptive_rk = adaptive_rk(yin, t_span, dt, func)

    # Plotting the results
    fig, ax = plt.subplots(2, 1, figsize=(10, 10))

    ax[0].plot(np.arange(t_span[0], t_span[1], dt), results_rk4[:, 0], label='Angle 1 (RK4)')
    ax[0].plot(np.arange(t_span[0], t_span[1], dt), results_rk4[:, 1], label='Angle 2 (RK4)')
    ax[0].plot(np.arange(t_span[0], t_span[1], dt), results_rk45[:, 0], label='Angle 1 (RK45)')
    ax[0].plot(np.arange(t_span[0], t_span[1], dt), results_rk45[:, 1], label='Angle 2 (RK45)')
    ax[0].plot(np.arange(t_span[0], t_span[1], dt), results_adaptive_rk[:, 0], label='Angle 1 (Adaptive RK)')
    ax[0].plot(np.arange(t_span[0], t_span[1], dt), results_adaptive_rk[:, 1], label='Angle 2 (Adaptive RK)')
    ax[0].set_title('Angles')
    ax[0].legend()

    ax[1].plot(np.arange(t_span[0], t_span[1], dt), results_rk4[:, 2], label='Angular Velocity 1 (RK4)')
    ax[1].plot(np.arange(t_span[0], t_span[1], dt), results_rk4[:, 3], label='Angular Velocity 2 (RK4)')
    ax[1].plot(np.arange(t_span[0], t_span[1], dt), results_rk45[:, 2], label='Angular Velocity 1 (RK45)')
    ax[1].plot(np.arange(t_span[0], t_span[1], dt), results_rk45[:, 3], label='Angular Velocity 2 (RK45)')
    ax[1].plot(np.arange(t_span[0], t_span[1], dt), results_adaptive_rk[:, 2], label='Angular Velocity 1 (Adaptive RK)')
    ax[1].plot(np.arange(t_span[0], t_span[1], dt), results_adaptive_rk[:, 3], label='Angular Velocity 2 (Adaptive RK)')
    ax[1].set_title('Angular Velocities')
    ax[1].legend()

    plt.tight_layout()
    plt.show()