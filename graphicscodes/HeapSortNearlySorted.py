import matplotlib.pyplot as plt
import numpy as np

# Данные для почти отсортированного массива (из таблицы Heap Sort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
nearly_sorted_times = [0.000390, 0.000458, 0.000855, 0.001189, 0.000809,
                       0.000781, 0.001150, 0.001570, 0.001710, 0.001407,
                       0.001561, 0.001444, 0.001587, 0.002139, 0.001877]

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
plt.title('Время выполнения Heap Sort (Почти отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
