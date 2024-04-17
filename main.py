import numpy as np
import dichotomy
import golden_ratio
import matplotlib.pyplot as plt
from grid import grid
import math as m
import mpld3

a_0, b_0 = 0.5, 3.5
eps = 0.1
n = 100
n_acc = 10

golden_ratio.left_inner, golden_ratio.right_inner, golden_ratio.last_func_value = 0, 0, 0


def func(x):
    return 2 * x + 1 / (x ** 2)


def given_func(x):
    return m.tan(x) - 2 * m.sin(x)


a_1, b_1 = 0, m.pi


def find_minimum_with_accuracy(a, b, f, acc, method):
    iter_number = 0
    # a, b = a_0, b_0
    delta = 0.4 * acc
    coef = 0.1
    iter = 1
    while coef > acc:
        coef=coef/10
        iter+=1
    while b - a > acc:
        iter_number += 1
        a, b = method(a, b, f, delta)
        a = round(a, iter + 1)
        b = round(b, iter + 1)

    if method == golden_ratio.golden_ratio_iteration:
        golden_ratio.clear_vars()
    min_point = (b + a) / 2
    # min_point = round(min_point, iter+1)
    min_value = f(min_point)
    return min_point, min_value, iter_number


# print(find_minimum_with_accuracy(a_0, b_0, func, eps, golden_ratio.golden_ratio_iteration))
# print(find_minimum_with_accuracy(a_0, b_0, func, eps, dichotomy.dichotomy_iteration))

x_axis, y_axis = grid(a_0, b_0, n, func)
# x_axis, y_axis = grid(a_1, b_1, n, given_func)

accuracy = []
gr_func_calls = []
dich_func_calls = []

gr_min = []
dich_min = []

for i in range(0, n_acc):
    acc = 10 ** (-i - 1)
    accuracy.append(acc)

for acc in accuracy:
    x_min, y_min, iters = find_minimum_with_accuracy(a_0, b_0, func, acc, golden_ratio.golden_ratio_iteration)
    gr_func_calls.append(golden_ratio.golden_ratio_func_calls(iters))
    gr_min.append([x_min, y_min])

    x_min, y_min, iters = find_minimum_with_accuracy(a_0, b_0, func, acc, dichotomy.dichotomy_iteration)
    dich_func_calls.append(dichotomy.dichotomy_func_calls(iters))
    dich_min.append([x_min, y_min])

# for acc in accuracy:
#     x_min, y_min, iters = find_minimum_with_accuracy(a_1, b_1, given_func, acc, golden_ratio.golden_ratio_iteration)
#     gr_func_calls.append(golden_ratio.golden_ratio_func_calls(iters))
#
#     x_min, y_min, iters = find_minimum_with_accuracy(a_1, b_1, given_func, acc, dichotomy.dichotomy_iteration)
#     dich_func_calls.append(dichotomy.dichotomy_func_calls(iters))

# plt.plot(x_axis, y_axis)
for i in range(3):
    print('Для точности ' + str(accuracy[i]) + ' методом золотого сечения получено решение: ' + str(gr_min[i][0])+'\n Значение функции: ' + str(gr_min[i][1]))
for i in range(3):
    print('Для точности ' + str(accuracy[i]) + ' методом дихотомии получено решение: ' + str(dich_min[i][0])+'\n Значение функции: ' + str(dich_min[i][1]))



figure, axis = plt.subplots(2, 1)

fig, ax = plt.subplots()

ax.set_ylim(-3, 10)
ax.plot(x_axis, y_axis)
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('y')

axis[0].semilogx(accuracy, gr_func_calls)
axis[0].set_title('Метод золотого сечения')
axis[0].set_xlabel('Точность')
axis[0].set_ylabel('Число вызовов функции')

axis[1].semilogx(accuracy, dich_func_calls)
axis[1].set_title('Метод дихотомии')
axis[1].set_xlabel('Точность')
axis[1].set_ylabel('Число вызовов функции')

ff, ax = plt.subplots()
ax.semilogx(accuracy, dich_func_calls, label='Метод дихотомии')
ax.semilogx(accuracy, gr_func_calls, label='Метод золотого сечения')
ax.set_xlabel('Точность')
ax.set_ylabel('Число вызовов функции')
ax.legend()

# figure.subplots_adjust(hspace=1)
figure.tight_layout()
plt.show()

