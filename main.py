import numpy as np
import dichotomy
import golden_ratio
import matplotlib.pyplot as plt
from grid import grid

a_0, b_0 = 0.5, 3.5
eps = 0.1
n = 100
n_acc = 10

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

x_axis, y_axis = grid(a_0, b_0, n, func)

accuracy = []
gr_func_calls = []
dich_func_calls = []

for i in range(0, n_acc):
    acc = 10 ** (-i - 1)
    accuracy.append(acc)

for acc in accuracy:
    x_min, y_min, iters = find_minimum_with_accuracy(a_0, b_0, func, acc, golden_ratio.golden_ratio_iteration)
    gr_func_calls.append(golden_ratio.golden_ratio_func_calls(iters))

    x_min, y_min, iters = find_minimum_with_accuracy(a_0, b_0, func, acc, dichotomy.dichotomy_iteration)
    dich_func_calls.append(dichotomy.dichotomy_func_calls(iters))

# plt.plot(x_axis, y_axis)
figure, axis = plt.subplots(3, 1)
axis[0].plot(x_axis, y_axis)
axis[0].set_title('График функции')

axis[1].semilogx(accuracy, gr_func_calls)
axis[1].set_title('Метод золотого сечения')
axis[1].set_xlabel('Точность')
axis[1].set_ylabel('Число вызовов функции')

axis[2].semilogx(accuracy, dich_func_calls)
axis[2].set_title('Метод дихотомии')
axis[2].set_xlabel('Точность')
axis[2].set_ylabel('Число вызовов функции')

plt.subplots_adjust(hspace=0.5)
plt.show()
