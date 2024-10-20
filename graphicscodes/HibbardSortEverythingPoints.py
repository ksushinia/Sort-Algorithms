import numpy as np
import matplotlib.pyplot as plt

# Данные
sortedSize = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])
sorted_times = np.array([0.000507, 0.000889, 0.000360, 0.000104, 0.000151, 0.000201, 0.000152, 0.000222, 0.000244, 0.000285, 0.000242, 0.000244, 0.000408, 0.000402, 0.000496])
nearly_sorted_times = np.array([0.001103, 0.000623, 0.000585, 0.000539, 0.000797, 0.000984, 0.001204, 0.001291, 0.001427, 0.001782, 0.001699, 0.002104, 0.002288, 0.002720, 0.002634])
reverse_sorted_times = np.array([0.000672, 0.000482, 0.000386, 0.000121, 0.000221, 0.000264, 0.000300, 0.000296, 0.000324, 0.000364, 0.000468, 0.000479, 0.000387, 0.000522, 0.000656])
random_times = np.array([0.001167, 0.000618, 0.000601, 0.000612, 0.000947, 0.001131, 0.001268, 0.001625, 0.001607, 0.001699, 0.002050, 0.002344, 0.002489, 0.002992, 0.003020])

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
plt.title("Все случаи Hibbard Sort с точками")
plt.xlabel("Размер массива")
plt.ylabel("Время (в секундах)")
plt.legend()
plt.grid()
plt.show()
