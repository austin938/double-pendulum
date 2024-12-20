from scipy.integrate import solve_ivp

def rk4(func, y: list, t, dt):
    '''
    Parameters:
    ------------
    y: initial state
    '''
    k1 = func(y, t)
    k2 = func(y + k1 * dt * 0.5, t + 0.5 * dt)
    k3 = func(y + k2 * dt * 0.5, t + dt * 0.5)
    k4 = func(y + dt * k3, t + dt)
    ynext = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return ynext


def rk45(func, y: list, t_span, t_eval):
    '''
    Parameters:
    ------------
    y: initial state
    '''
    sol = solve_ivp(func, t_span, y, method='RK45', t_eval=t_eval)
    return sol

