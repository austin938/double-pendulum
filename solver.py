from scipy.integrate import solve_ivp


def solver(func, y: list, t_span, t_eval, method):
    '''
    Parameters:
    ------------
    y : list
        The state vector of the system. It contains:
            y[0] : float
                Angle of the first pendulum (theta1).
            y[1] : float
                Angle of the second pendulum (theta2).
            y[2] : float
                Angular velocity or generalized momentum of the first pendulum (omega1 or p1).
            y[3] : float
                Angular velocity or generalized momentum of the second pendulum (omega2 or p2).    
    method : str
        The ODE solver to use. It can be 'RK45' or 'DOP853'.
    
    '''
    if method == 'RK45':
        sol = solve_ivp(func, t_span, y, method='RK45', t_eval=t_eval)
    elif method == 'DOP853':
        sol = solve_ivp(func, t_span, y, method='DOP853', t_eval=t_eval)
    else:
        raise SystemExit("Error: method "+method+" is not supported!")
    return sol
