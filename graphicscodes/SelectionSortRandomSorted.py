import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
import numpy as np

# Данные для случайно отсортированного массива
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
random_sorted_times = [0.010060, 0.001824, 0.005714, 0.008467, 0.011079, 0.017326, 0.024610, 0.032152,
                       0.047880, 0.053028, 0.059921, 0.066272, 0.075475, 0.086703, 0.099986]

# Построение графика в формате точек
plt.scatter(sizes, random_sorted_times, label="Данные", color='green')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, random_sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения Selection Sort (Случайно отсортированный массив)')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
