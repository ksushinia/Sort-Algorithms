import matplotlib.pyplot as plt
import numpy as np

# Размеры массивов
sizes = np.arange(1000, 10001, 1000)  # от 1000 до 10000 с шагом 1000

# Оценка времени выполнения для всех случаев
best_case = sizes * (np.log2(sizes) ** 2)   # O(n log^2 n)
average_case = sizes * (np.log2(sizes) ** 2)  # O(n log^2 n)
worst_case = sizes * (np.log2(sizes) ** 2)   # O(n log^2 n)

# Построение графика
plt.figure()

# График для всех случаев
plt.plot(sizes, best_case, label='Лучший случай O(n log² n)', color='green')
plt.plot(sizes, average_case, label='Средний случай O(n log² n)', color='blue')
plt.plot(sizes, worst_case, label='Худший случай O(n log² n)', color='red')

# Оформление графика
plt.title('Асимптотическая сложность сортировки Пратта (Все случаи O(n log² n))')
plt.xlabel('Размер массива (n)')
plt.ylabel('Оценка сложности')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
