import matplotlib.pyplot as plt
import numpy as np

# Данные для массива в обратном порядке (из таблицы Pratt Sort)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
reverse_sorted_times = [0.001319, 0.000594, 0.000580, 0.000897, 0.000830, 0.001368,
                        0.001251, 0.001496, 0.002072, 0.001872, 0.002147, 0.002308,
                        0.003295, 0.002802, 0.004262]

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
plt.title('Время выполнения Pratt Sort (Массив в обратном порядке)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
