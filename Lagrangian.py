import numpy as np

class Lagrangian_dp:
    def __init__(self, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81):
        self.m1 = m1  # mass of pendulum 1
        self.m2 = m2  # mass of pendulum 2
        self.L1 = L1  # length of pendulum 1
        self.L2 = L2  # length of pendulum 2
        self.g = g    # gravitational acceleration



# Important to notice the order of the vaargument in the function, could cause error in solve_ivp
    def L(self, t: float, y: list) -> np.ndarray:
        '''
        Parameters:
        ------------
        Computes the derivatives of the state variables for a double pendulum system.

        t : float
            The current time (not used in this function but typically required for ODE solvers).
        y : list
            For Lagrangian the state vector of the system. It contains:
                y[0] : float
                    Angle of the first pendulum (theta1).
                y[1] : float
                    Angle of the second pendulum (theta2).
                y[2] : float
                    Angular velocity of the first pendulum (omega1).
                y[3] : float
                    Angular velocity of the second pendulum (omega2).

        Returns:
        --------
        np.ndarray
            The derivatives of the state variables. It contains:
                k[0] : float
                    Derivative of theta1 (d(theta1)/dt), which is omega1.
                k[1] : float
                    Derivative of theta2 (d(theta2)/dt), which is omega2.
                k[2] : float
                    Derivative of omega1 (d(omega1)/dt).
                k[3] : float
                    Derivative of omega2 (d(omega2)/dt).
        '''
        m1 = self.m1
        m2 = self.m2
        L1 = self.L1
        L2 = self.L2
        g = self.g

        k = np.zeros_like(y)
        k[0] = y[2]
        k[1] = y[3]
        k[2] = (-0.5 * L1 * m2 * np.sin(2 * y[0] - 2 * y[1]) * y[2]**2
            - L2 * m2 * np.sin(y[0] - y[1]) * y[3]**2
            - g * m1 * np.sin(y[0])
            - 0.5 * g * m2 * np.sin(y[0] - 2 * y[1])
            - 0.5 * g * m2 * np.sin(y[0])) / (L1 * (m1 - m2 * np.cos(y[0] - y[1])**2 + m2))
        k[3] = (L1 * m1 * np.sin(y[0] - y[1]) * y[2]**2
            + L1 * m2 * np.sin(y[0] - y[1]) * y[2]**2
            + 0.5 * L2 * m2 * np.sin(2 * y[0] - 2 * y[1]) * y[3]**2
            + 0.5 * g * m1 * np.sin(2 * y[0] - y[1])
            - 0.5 * g * m1 * np.sin(y[1])
            + 0.5 * g * m2 * np.sin(2 * y[0] - y[1])
            - 0.5 * g * m2 * np.sin(y[1])) / (L2 * (m1 - m2 * np.cos(y[0] - y[1])**2 + m2))
        return k
    
    def kinematic_energy(self, y: list) -> np.ndarray:
        m1 = self.m1
        m2 = self.m2
        L1 = self.L1
        L2 = self.L2

        T1 = 0.5 * m1 * (L1 * y[2])**2
        T2 = 0.5 * m2 * ((L1 * y[2] * np.cos(y[0] - y[1]) - L2 * y[3])**2 + (L1 * y[2] * np.sin(y[0] - y[1]))**2)
        T = T1 + T2
        return T
    
    def potential_energy(self, y: list) -> np.ndarray:
        m1 = self.m1
        m2 = self.m2
        L1 = self.L1
        L2 = self.L2
        g = self.g

        V1 = -m1 * g * L1 * np.cos(y[0])
        V2 = -m2 * g * (L1 * np.cos(y[0]) + L2 * np.cos(y[1]))
        V = V1 + V2
        return V
    
    def mechanical_energy(self, y: list) -> np.ndarray:
        T = self.kinematic_energy(y)
        V = self.potential_energy(y)
        return T + V
