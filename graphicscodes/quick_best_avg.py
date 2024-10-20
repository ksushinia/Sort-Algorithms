import matplotlib.pyplot as plt
import numpy as np

# Размеры массивов
sizes = np.arange(1000, 10001, 1000)  # от 1000 до 10000 с шагом 1000

# Оценка времени выполнения для лучшего и среднего случаев
best_case = sizes * np.log2(sizes)   # O(n log n)
average_case = sizes * np.log2(sizes)  # O(n log n)

# Построение графика
plt.figure()

# График для лучшего и среднего случаев
plt.plot(sizes, best_case, label='Лучший случай O(n log n)', color='green')
plt.plot(sizes, average_case, label='Средний случай O(n log n)', color='blue')

# Оформление графика
plt.title('Асимптотическая сложность QuickSort (Лучший и Средний случаи O(n log n))')
plt.xlabel('Размер массива (n)')
plt.ylabel('Оценка сложности')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
