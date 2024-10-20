import matplotlib.pyplot as plt
import numpy as np

# Данные для массива в обратном порядке (из таблицы)
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
reverse_sorted_times = [
    0.000672, 0.000482, 0.000386, 0.000121, 0.000221,
    0.000264, 0.000300, 0.000296, 0.000324, 0.000364,
    0.000468, 0.000479, 0.000387, 0.000522, 0.000656
]

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
plt.title('Время выполнения сортировки Хиббарда (Массив в обратном порядке)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (с)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
