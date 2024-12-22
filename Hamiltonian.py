import numpy as np

class Hamiltonian_dp:
    def __init__(self, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81):
        self.m1 = m1  # mass of pendulum 1
        self.m2 = m2  # mass of pendulum 2
        self.L1 = L1  # length of pendulum 1
        self.L2 = L2  # length of pendulum 2
        self.g = g    # gravitational acceleration



    # Important to notice the order of the vaargument in the function, could cause error in solve_ivp
    def H(self, t: float, y: list) -> np.ndarray:
        '''
        Parameters:
        ------------
        Computes the derivatives of the state variables for a double pendulum system.

        t : float
            The current time (not used in this function but typically required for ODE solvers).
        y : list
            For Hamiltonian the state vector of the system. It contains:
                y[0] : float
                    Generalized coordinate of the first pendulum (theta1)
                y[1] : float
                    Generalized coordinate of the second pendulum (theta2)
                y[2] : float
                    Generalized momentum of the first pendulum (p1)
                y[3] : float
                    Generalized momentum of the second pendulum (p2)

        mechanics : str
            The type of mechanics to use. It can be 'Lagrangian' or 'Hamiltonian'.

        Returns:
        --------
        np.ndarray
            The derivatives of the state variables. It contains:
                k[0] : float
                    Derivative of theta1 (d(theta1)/dt), which is omega1.
                k[1] : float
                    Derivative of theta2 (d(theta2)/dt), which is omega2.
                k[2] : float
                    Derivative of momentum1 (d(p1)/dt).
                k[3] : float
                    Derivative of momentum2 (d(p2)/dt).
        '''
        m1 = self.m1
        m2 = self.m2
        L1 = self.L1
        L2 = self.L2
        g = self.g

        k = np.zeros_like(y)
        t1, t2, p1, p2 = y
        C0 = L1 * L2 * (m1 + m2 * np.sin(t1 - t2)**2)
        C1 = (p1 * p2 * np.sin(t1 - t2)) / C0
        C2 = (m2 * (L2 * p1)**2 + (m1 + m2) * (L1 * p2)**2 -
            2 * L1 * L2 * m2 * p1 * p2 * np.cos(t1 - t2)) * \
            np.sin(2 * (t1 - t2)) / (2 * C0**2)
        
        k[0] = (L2 * p1 - L1 * p2 * np.cos(t1 - t2)) / (L1 * C0)
        k[1] = (L1 * (m1 + m2) * p2 - L2 * m2 * p1 * np.cos(t1 - t2)) / (L2 * m2 * C0)
        k[2] = -(m1 + m2) * g * L1 * np.sin(t1) - C1 + C2
        k[3] = -m2 * g * L2 * np.sin(t2) + C1 - C2
        return k
    
    def angular_velocities(self, y: list):
        t1, t2, p1, p2 = y
        m1 = self.m1
        m2 = self.m2
        L1 = self.L1
        L2 = self.L2

        C0 = L1 * L2 * (m1 + m2 * np.sin(t1 - t2)**2)
        omega1 = (L2 * p1 - L1 * p2 * np.cos(t1 - t2)) / (L1 * C0)
        omega2 = (L1 * (m1 + m2) * p2 - L2 * m2 * p1 * np.cos(t1 - t2)) / (L2 * m2 * C0)
        return omega1, omega2
        

    def kinematic_energy(self, y: list) -> np.ndarray:
        m1 = self.m1
        m2 = self.m2
        L1 = self.L1
        L2 = self.L2

        omega1, omega2 = self.angular_velocities(y)
        T1 = 0.5 * m1 * (L1 * omega1)**2
        T2 = 0.5 * m2 * ((L1 * omega1)**2 + (L2 * omega2)**2 +
                 2 * L1 * L2 * omega1 * omega2 * np.cos(y[0] - y[1]))
        return T1 + T2

    def potential_energy(self, y: list) -> np.ndarray:
        m1 = self.m1
        m2 = self.m2
        L1 = self.L1
        L2 = self.L2
        g = self.g

        V1 = -m1 * g * L1 * np.cos(y[0])
        V2 = -m2 * g * (L1 * np.cos(y[0]) + L2 * np.cos(y[1]))
        return V1 + V2

    def mechanical_energy(self, y: list) -> np.ndarray:
        T = self.kinematic_energy(y)
        V = self.potential_energy(y)
        return T + V
