import numpy as np

golden_ratio = (3 - np.sqrt(5)) / 2

left_inner = 0
right_inner = 0
last_func_value = 0


def sub_iteration(a, b, func, f_left=None, f_right=None):
    global left_inner
    global right_inner
    global last_func_value
    if f_left is None:
        f_left = func(left_inner)
    if f_right is None:
        f_right = func(right_inner)
    if f_left < f_right:
        new_b = right_inner
        right_inner = left_inner
        left_inner = None
        last_func_value = f_left
        return a, new_b
    else:
        new_a = left_inner
        left_inner = right_inner
        right_inner = None
        last_func_value = f_right
        return new_a, b


def golden_ratio_iteration(a, b, func):
    global left_inner
    global right_inner
    if left_inner == right_inner:
        left_inner = a + golden_ratio * (b - a)
        right_inner = a + (1 - golden_ratio) * (b - a)
        return sub_iteration(a, b, func)
    elif left_inner is None:
        left_inner = a + golden_ratio * (b - a)
        return sub_iteration(a, b, func, f_right=last_func_value)
    else:
        right_inner = a + (1 - golden_ratio) * (b - a)
        return sub_iteration(a, b, func, f_left=last_func_value)
