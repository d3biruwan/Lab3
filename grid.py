def grid(a, b, n, f):
    x_grid, y_grid = [], []
    h = (b - a) / n
    for i in range(0, n + 1):
        x_grid.append(a + h * i)
        y_grid.append(f(x_grid[i]))
    return x_grid, y_grid
