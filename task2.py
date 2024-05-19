from scipy.integrate import quad
import numpy as np
from graphics import f, a, b

# Кількість випадкових точок
N = 1000000

# Генерація випадкових точок у області інтегрування
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, b**2, N)

# Обчислення кількості точок, що знаходяться під кривою
points_under_curve = y_random < f(x_random)
area_under_curve = (points_under_curve.sum() / N) * (b * b**2)

# Обчислення інтегралу функцією quad
result, error = quad(f, a, b)

print(f"Значення інтегралу за допомогою методу Монте Карло: {
      area_under_curve:10.6f}")
print(f"Значення інтегралу за допомогою функції quad:     {result:12.6f}")
print(f"Похибка: {abs(area_under_curve - result):53.6f}")
