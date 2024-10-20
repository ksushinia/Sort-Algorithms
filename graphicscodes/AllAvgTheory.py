import numpy as np
import matplotlib.pyplot as plt

# Размеры массива
sizes = np.linspace(100, 10000, 100)

# Временная сложность для среднего случая каждой сортировки
def selection_sort(n):
    return n ** 2

def insertion_sort(n):
    return n ** 2

def bubble_sort(n):
    return n ** 2

def merge_sort(n):
    return n * np.log2(n)

def shell_sort(n):
    return n ** 1.5

def hibbard_sort(n):
    return n ** 1.5

def pratt_sort(n):
    return n * np.log2(n)

def quick_sort(n):
    return n * np.log2(n)

def heap_sort(n):
    return n * np.log2(n)

# Подготовка данных для графика
selection_times = selection_sort(sizes)
insertion_times = insertion_sort(sizes)
bubble_times = bubble_sort(sizes)
merge_times = merge_sort(sizes)
shell_times = shell_sort(sizes)
hibbard_times = hibbard_sort(sizes)
pratt_times = pratt_sort(sizes)
quick_times = quick_sort(sizes)
heap_times = heap_sort(sizes)

# Построение графика
plt.figure(figsize=(12, 8))

# Каждая сортировка отображается на графике
plt.plot(sizes, selection_times, label='Сортировка выбором O(n^2)', linewidth=2)
plt.plot(sizes, insertion_times, label='Сортировка вставками O(n^2)', linewidth=2)
plt.plot(sizes, bubble_times, label='Сортировка пузырьком O(n^2)', linewidth=2)
plt.plot(sizes, merge_times, label='Сортировка слиянием O(n log n)', linewidth=2)
plt.plot(sizes, shell_times, label='Сортировка Шелла O(n^1.5)', linewidth=2)
plt.plot(sizes, hibbard_times, label='Последовательность Хиббарда O(n log^2 n)', linewidth=2)
plt.plot(sizes, pratt_times, label='Последовательность Пратта O(n log^2 n)', linewidth=2)
plt.plot(sizes, quick_times, label='Быстрая сортировка O(n log n)', linewidth=2)
plt.plot(sizes, heap_times, label='Пирамидальная сортировка O(n log n)', linewidth=2)

# Настройки графика
plt.title("Средние случаи различных сортировок", fontsize=16)
plt.xlabel("Размер массива", fontsize=14)
plt.ylabel("Время выполнения (условные единицы)", fontsize=14)
plt.yscale('log')  # Логарифмическая шкала по оси Y
plt.legend(loc="upper left", fontsize=10)
plt.grid(True)
plt.show()
