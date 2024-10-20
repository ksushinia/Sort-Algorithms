import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
import numpy as np

# Данные для массива в обратном порядке
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
reverse_sorted_times = [0.003254, 0.002362, 0.008363, 0.010273, 0.014550, 0.020489, 0.028249, 0.043195,
                        0.053185, 0.065987, 0.082097, 0.083822, 0.103148, 0.107793, 0.133518]

# Построение графика в формате точек
plt.scatter(sizes, reverse_sorted_times, label="Данные", color='blue')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, reverse_sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения сортировки Selection Sort (Массив в обратном порядке)')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
