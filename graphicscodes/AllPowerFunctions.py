import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Данные для случайно отсортированных массивов для разных сортировок
sizes = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000])

# Время выполнения для различных сортировок
random_times_bubble = np.array([0.001794, 0.005107, 0.004717, 0.009298, 0.013376, 0.022216, 0.028064, 0.048378, 0.060630, 0.082880, 0.110587, 0.128625, 0.175136, 0.205286, 0.231990])
random_times_insertion = np.array([0.001581, 0.002297, 0.002996, 0.003242, 0.004782, 0.006893, 0.009093, 0.009871, 0.012591, 0.015686, 0.017060, 0.022549, 0.028010, 0.029843, 0.040771])
random_times_shell = np.array([0.001220, 0.000506, 0.000537, 0.000575, 0.000762, 0.000948, 0.001313, 0.001711, 0.001609, 0.001704, 0.001851, 0.002366, 0.002735, 0.003408, 0.003068])
random_times_hibbard = np.array([0.001167, 0.000618, 0.000601, 0.000612, 0.000947, 0.001131, 0.001268, 0.001625, 0.001607, 0.001699, 0.002050, 0.002344, 0.002489, 0.002992, 0.003020])
random_times_selection = np.array([0.010060, 0.001824, 0.005714, 0.008467, 0.011079, 0.017326, 0.024610, 0.032152, 0.047880, 0.053028, 0.059921, 0.066272, 0.075475, 0.086703, 0.099986])

# Функции для регрессионных кривых (полиномы степени 2)
p_bubble = Polynomial.fit(sizes, random_times_bubble, deg=2)
p_insertion = Polynomial.fit(sizes, random_times_insertion, deg=2)
p_shell = Polynomial.fit(sizes, random_times_shell, deg=2)
p_hibbard = Polynomial.fit(sizes, random_times_hibbard, deg=2)
p_selection = Polynomial.fit(sizes, random_times_selection, deg=2)

# Для плавных кривых
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 500)
bubble_times_smooth = p_bubble(sizes_smooth)
insertion_times_smooth = p_insertion(sizes_smooth)
shell_times_smooth = p_shell(sizes_smooth)
hibbard_times_smooth = p_hibbard(sizes_smooth)
selection_times_smooth = p_selection(sizes_smooth)

# Построение графика
plt.figure(figsize=(10, 6))

# Построение кривых для каждой сортировки
plt.plot(sizes_smooth, bubble_times_smooth, color='blue', label='Bubble Sort')
plt.plot(sizes_smooth, insertion_times_smooth, color='green', label='Insertion Sort')
plt.plot(sizes_smooth, shell_times_smooth, color='red', linestyle='--', linewidth=3, label='Shell Sort')  # Линия толще и пунктиром
plt.plot(sizes_smooth, hibbard_times_smooth, color='purple', label='Hibbard Sort')
plt.plot(sizes_smooth, selection_times_smooth, color='orange', label='Selection Sort')

# Настройка графика
plt.title('Сравнение времени выполнения для сортировок со степенной сложностью')
plt.xlabel('Размер массива (n)')
plt.ylabel('Время выполнения (секунды)')
plt.grid(True)
plt.legend()

# Показать график
plt.show()
