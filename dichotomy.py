delta_coef = 0.001


def delta_calc(a, b):
    return delta_coef * (b - a)


def dichotomy_iteration(a, b, func, delta=0):
    # delta = delta_calc(a, b)
    x1 = (b + a) / 2 - delta
    x2 = (b + a) / 2 + delta
    if func(x1) < func(x2):
        return a, x2
    else:
        return x1, b


def dichotomy_func_calls(iter):
    return 2 * iter
