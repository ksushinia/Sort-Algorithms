import matplotlib.pyplot as plt
import numpy as np

# Данные для массива в обратном порядке (из таблицы Heap Sort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
reverse_sorted_times = [0.000367, 0.000436, 0.000715, 0.001039, 0.000583,
                        0.000683, 0.001261, 0.001295, 0.001243, 0.001291,
                        0.001261, 0.001754, 0.001450, 0.001560, 0.002153]

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
plt.title('Время выполнения Heap Sort (Массив в обратном порядке)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
