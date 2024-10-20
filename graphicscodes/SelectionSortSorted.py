import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
import numpy as np

# Данные для отсортированного массива
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
sorted_times = [0.005574, 0.001740, 0.003732, 0.007686, 0.010974, 0.015535, 0.020217, 0.029127, 0.039143,
                0.058127, 0.053653, 0.067040, 0.078331, 0.080945, 0.098994]

# Построение графика в формате точек
plt.scatter(sizes, sorted_times, label="Данные", color='blue')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения сортировки Selection Sort (Отсортированный массив)')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()