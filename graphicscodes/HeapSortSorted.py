import matplotlib.pyplot as plt
import numpy as np

# Данные для отсортированного массива (из таблицы Heap Sort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
sorted_times = [0.001519, 0.000439, 0.000698, 0.000885, 0.001219,
                0.000943, 0.001071, 0.001421, 0.001628, 0.001273,
                0.001563, 0.001267, 0.001366, 0.001480, 0.001625]

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
plt.title('Время выполнения Heap Sort (Отсортированный массив)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
