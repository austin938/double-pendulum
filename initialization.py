import numpy as np

class DoublePendulum:
    def __init__(self, m1=1.0, m2=1.0, L1=1.0, L2=1.0, theta1=1, theta2=1, omega1=0.0, omega2=0.0, g=9.81):
        self.m1 = m1  # mass of pendulum 1
        self.m2 = m2  # mass of pendulum 2
        self.L1 = L1  # length of pendulum 1
        self.L2 = L2  # length of pendulum 2
        self.theta1 = theta1 # angle of pendulum 1
        self.theta2 = theta2 # angle of pendulum 2
        self.omega1 = omega1 # angular velocity of pendulum 1
        self.omega2 = omega2 # angular velocity of pendulum 2
        self.g = g    # gravitational acceleration


# Important to notice the order of the vaargument in the function, could cause error in solve_ivp
def func(t: float, y: list) -> np.ndarray:
    '''
    Parameters:
    ------------
    y: state | y[0] = theta1, y[1] = theta2, y[2] = omega1, y[3] = omega2
    '''
    dp = DoublePendulum()
    k = np.zeros_like(y)
    k[0] = y[2]
    k[1] = y[3]
    k[2] = (-0.5 * dp.L1 * dp.m2 * np.sin(2 * y[0] - 2 * y[1]) * y[2]**2
            - 1.0 * dp.L2 * dp.m2 * np.sin(y[0] - y[1]) * y[3]**2
            - 1.0 * dp.g * dp.m1 * np.sin(y[0])
            - 0.5 * dp.g * dp.m2 * np.sin(y[0] - 2 * y[1])
            - 0.5 * dp.g * dp.m2 * np.sin(y[0])) / (dp.L1 * (dp.m1 - dp.m2 * np.cos(y[0] - y[1])**2 + dp.m2))
    k[3] = (1.0 * dp.L1 * dp.m1 * np.sin(y[0] - y[1]) * y[2]**2
            + 1.0 * dp.L1 * dp.m2 * np.sin(y[0] - y[1]) * y[2]**2
            + 0.5 * dp.L2 * dp.m2 * np.sin(2 * y[0] - 2 * y[1]) * y[3]**2
            + 0.5 * dp.g * dp.m1 * np.sin(2 * y[0] - y[1])
            - 0.5 * dp.g * dp.m1 * np.sin(y[1])
            + 0.5 * dp.g * dp.m2 * np.sin(2 * y[0] - y[1])
            - 0.5 * dp.g * dp.m2 * np.sin(y[1])) / (dp.L2 * (dp.m1 - dp.m2 * np.cos(y[0] - y[1])**2 + dp.m2))
    return k