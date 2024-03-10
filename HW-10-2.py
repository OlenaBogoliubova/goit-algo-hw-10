import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    try:
        return np.sqrt(x)
    except (ValueError, RuntimeWarning):
        return np.nan


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(0, 3, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

max_y = np.nanmax(y)
ax.set_ylim([0, max_y + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(
    'Графік інтегрування f(x) = $\sqrt{x}$ від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Генерація випадкових точок в межах інтегрування
num_points = 100000
random_x = np.random.uniform(a, b, num_points)
random_y = np.random.uniform(0, f(b), num_points)

# Підрахунок кількості точок, які знаходяться під кривою
points_under_curve = sum(random_y <= f(random_x))

# Обчислення площі сірої зони (інтеграл за допомогою методу Монте-Карло)
monte_carlo_result = (points_under_curve / num_points) * \
    (b - a) * max(f(a), f(b))

print("Інтеграл методом Монте-Карло: ", monte_carlo_result)

# Порівняння з результатом використання функції quad
quad_result = spi.quad(f, a, b)
print("Інтеграл за допомогою функції quad: ", quad_result)
