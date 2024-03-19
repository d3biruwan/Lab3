import numpy as np
import dichotomy
import golden_ratio

a_0, b_0 = 0.5, 3.5
eps = 0.01

golden_ratio.left_inner, golden_ratio.right_inner, golden_ratio.last_func_value = 0, 0, 0


def func(x):
    return 2 * x + 1 / (x ** 2)


def find_minimum_with_accuracy(a, b, f, acc, method):
    iter_number = 0
    # a, b = a_0, b_0
    while b - a > acc:
        iter_number += 1
        a, b = method(a, b, f)
    min_point = (b + a) / 2
    min_value = f(min_point)
    return min_point, min_value, iter_number


print(find_minimum_with_accuracy(a_0, b_0, func, eps, golden_ratio.golden_ratio_iteration))
print(find_minimum_with_accuracy(a_0, b_0, func, eps, dichotomy.dichotomy_iteration))

