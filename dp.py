import numpy as np
import pickle

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

def rk4(yin: list, t: float, dt: float, func: callable) -> np.ndarray:
    k1 = func(yin, t)
    k2 = func(yin + k1 * dt * 0.5, t + 0.5 * dt)
    k3 = func(yin + k2 * dt * 0.5, t + dt * 0.5)
    k4 = func(yin + dt * k3, t + dt)
    ynext = yin + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return ynext

def func(yin: list, time: float) -> np.ndarray:
    angle1, angle2, angular_velocity1, angular_velocity2 = yin
    k = np.zeros(4)
    k[0] = angular_velocity1
    k[1] = angular_velocity2
    k[2] = (-0.5 * L1 * m2 * np.sin(2 * angle1 - 2 * angle2) * angular_velocity1**2
            - 1.0 * L2 * m2 * np.sin(angle1 - angle2) * angular_velocity2**2
            - 1.0 * g * m1 * np.sin(angle1)
            - 0.5 * g * m2 * np.sin(angle1 - 2 * angle2)
            - 0.5 * g * m2 * np.sin(angle1)) / (L1 * (m1 - m2 * np.cos(angle1 - angle2)**2 + m2))
    k[3] = (1.0 * L1 * m1 * np.sin(angle1 - angle2) * angular_velocity1**2
            + 1.0 * L1 * m2 * np.sin(angle1 - angle2) * angular_velocity1**2
            + 0.5 * L2 * m2 * np.sin(2 * angle1 - 2 * angle2) * angular_velocity2**2
            + 0.5 * g * m1 * np.sin(2 * angle1 - angle2)
            - 0.5 * g * m1 * np.sin(angle2)
            + 0.5 * g * m2 * np.sin(2 * angle1 - angle2)
            - 0.5 * g * m2 * np.sin(angle2)) / (L2 * (m1 - m2 * np.cos(angle1 - angle2)**2 + m2))
    return k

def update(t, dt, angle1, angular_velocity1, angle2, angular_velocity2):
    yin = [angle1, angle2, angular_velocity1, angular_velocity2]
    yout = rk4(yin, t, dt, func)
    return yout[0], yout[1], yout[2], yout[3]

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

# Example usage
if __name__ == "__main__":
    t = 0
    dt = 0.025
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
    try:
        while True:
            angle1, angle2, angular_velocity1, angular_velocity2 = update(t, dt, angle1, angular_velocity1, angle2, angular_velocity2)
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
    except KeyboardInterrupt:
        # Save the data to a pickle file when the loop is interrupted
        with open('double_pendulum_data.pickle', 'wb') as f:
            pickle.dump(data, f)
        print("Simulation stopped and data saved.")