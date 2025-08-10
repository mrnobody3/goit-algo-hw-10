import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Функція для інтегрування


def f(x):
    return x ** 2


a, b = 0, 2  # Межі інтегрування

# Метод Монте-Карло
N = 1_000_000  # кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

under_curve = y_random <= f(x_random)
monte_carlo_result = (b - a) * f(b) * np.sum(under_curve) / N

# Перевірка через quad
quad_result, error = spi.quad(f, a, b)

print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Метод quad: {quad_result}, похибка {error}")
print(f"Різниця: {abs(monte_carlo_result - quad_result)}")

# Побудова графіка
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

plt.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
plt.fill_between(ix, iy, color='gray', alpha=0.3)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.axvline(x=a, color='gray', linestyle='--')
plt.axvline(x=b, color='gray', linestyle='--')
plt.title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()
