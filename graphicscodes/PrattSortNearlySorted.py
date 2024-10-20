import matplotlib.pyplot as plt
import numpy as np

# Данные для почти отсортированного массива (из таблицы Pratt Sort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
nearly_sorted_times = [0.002101, 0.000737, 0.000742, 0.001412, 0.001327, 0.001865,
                       0.002132, 0.002480, 0.003507, 0.003052, 0.003413, 0.003690,
                       0.005296, 0.004877, 0.005323]

# Построение графика в формате точек
plt.scatter(sizes, nearly_sorted_times, label="Данные", color='blue')

# Вычисление регрессионной кривой (полиномиальная регрессия 2-й степени)
coefs = np.polyfit(sizes, nearly_sorted_times, 2)
poly = np.poly1d(coefs)

# Построение регрессионной кривой
x = np.linspace(min(sizes), max(sizes), 500)
y = poly(x)
plt.plot(x, y, color='red', label='Регрессионная кривая')

# Оформление графика
plt.title('Время выполнения Pratt Sort (Почти отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
