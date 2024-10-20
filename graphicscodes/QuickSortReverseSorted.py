import matplotlib.pyplot as plt
import numpy as np

# Данные для массива в обратном порядке (из таблицы QuickSort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
reverse_sorted_times = [0.000184, 0.000171, 0.000157, 0.000211, 0.000242, 0.000306,
                        0.000354, 0.000295, 0.000230, 0.000378, 0.000285, 0.000457,
                        0.000404, 0.000565, 0.000379]

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
plt.title('Время выполнения QuickSort (Массив в обратном порядке)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
