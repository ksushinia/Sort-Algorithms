import matplotlib.pyplot as plt

# Размеры массивов
sizes = range(1000, 10001, 1000)  # от 1000 до 10000 с шагом 1000

# Оценки времени выполнения для среднего и худшего случаев
average_case = [n**2 for n in sizes]  # O(n²)
worst_case = [n**2 for n in sizes]     # O(n²)

# Построение графика
plt.figure()

# График для среднего и худшего случаев
plt.plot(sizes, average_case, label='Средний случай O(n²)', color='orange')
plt.plot(sizes, worst_case, label='Худший случай O(n²)', color='red')

# Оформление графика
plt.title('Асимптотическая сложность сортировки вставками (Средний и Худший случаи)')
plt.xlabel('Размер массива (n)')
plt.ylabel('Оценка сложности')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
