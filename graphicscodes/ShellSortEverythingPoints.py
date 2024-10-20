import numpy as np
import matplotlib.pyplot as plt

# Данные
sortedSize = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.000283, 0.0001405, 0.000190, 0.000216, 0.000252, 0.000245, 0.000180, 0.000293, 0.000341, 0.000297, 0.000327, 0.000376, 0.000358, 0.000379, 0.000448])
nearly_sorted_times = np.array([0.001089, 0.000526, 0.000607, 0.000593, 0.000948, 0.000859, 0.001214, 0.001198, 0.001411, 0.001645, 0.001989, 0.002029, 0.002215, 0.002560, 0.002765])
reverse_sorted_times = np.array([0.000735, 0.000325, 0.000252, 0.000211, 0.000144, 0.000243, 0.000408, 0.000317, 0.000484, 0.000329, 0.000464, 0.000610, 0.000521, 0.000785, 0.000756])
random_times = np.array([0.001220, 0.000506, 0.000537, 0.000575, 0.000762, 0.000948, 0.001313, 0.001711, 0.001609, 0.001704, 0.001851, 0.002366, 0.002735, 0.003408, 0.003068])

# Параметры для графика
plt.figure(figsize=(12, 8))

# Функция для построения регрессионной кривой
def plot_regression(x, y, label):
    # Подгонка полинома второго порядка
    coeffs = np.polyfit(x, y, 2)
    poly = np.poly1d(coeffs)
    # Получение значений для регрессионной кривой
    x_line = np.linspace(min(x), max(x), 100)
    y_line = poly(x_line)
    # Построение точек и регрессионной кривой
    plt.scatter(x, y, label=f"{label} (данные)", s=100)  # Точки
    plt.plot(x_line, y_line, label=f"{label} (кривая)", linewidth=2)  # Регрессия

# Построение для каждого типа массива
plot_regression(sortedSize, sorted_times, "Отсортированный")
plot_regression(sortedSize, nearly_sorted_times, "Почти отсортированный")
plot_regression(sortedSize, reverse_sorted_times, "Обратный отсортированный")
plot_regression(sortedSize, random_times, "Случайный")

# Настройки графика
plt.title("Все случаи Shell Sort с точками")
plt.xlabel("Размер массива")
plt.ylabel("Время (в секундах)")
plt.legend()
plt.grid()
plt.show()
