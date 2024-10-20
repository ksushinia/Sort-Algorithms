import matplotlib.pyplot as plt
import math

# Размеры массивов
sizes = list(range(10000, 110001, 10000))

# Оценки времени выполнения для лучшего, среднего и худшего случаев
best_case = [size * math.log(size) for size in sizes]   # O(n log n)
average_case = [size ** (3/2) for size in sizes]         # O(n^(3/2))
worst_case = [size ** (3/2) for size in sizes]           # O(n^(3/2))

# Построение графика
plt.figure()
plt.plot(sizes, best_case, label='Лучший случай O(n log n)')
plt.plot(sizes, average_case, label='Средний случай O(n^{3/2})')
plt.plot(sizes, worst_case, label='Худший случай O(n^{3/2})')

# Оформление графика
plt.title('Асимптотическая сложность сортировки Шелла с последовательностью Хиббарда')
plt.xlabel('Размер массива (n)')
plt.ylabel('Оценка сложности')
plt.legend()
plt.grid(True)

# Показать график
plt.show()

