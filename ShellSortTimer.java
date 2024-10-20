import java.util.Arrays;
import java.util.Random;

public class ShellSortTimer {

    // Метод сортировки Шелла (Shell Sort)
    public static void shellSort(int[] array) {
        // Начинаем с большого значения шага, уменьшаем его с каждым циклом
        for (int gap = array.length / 2; gap > 0; gap /= 2) {
            // Проходим по элементам массива с шагом gap
            for (int i = gap; i < array.length; i++) {
                int temp = array[i]; // Запоминаем текущий элемент
                int j = i;
                // Выполняем вставку элементов на расстоянии gap друг от друга
                while (j >= gap && array[j - gap] > temp) {
                    array[j] = array[j - gap]; // Сдвигаем элементы вправо
                    j -= gap;
                }
                array[j] = temp; // Ставим запомненный элемент на нужное место
            }
        }
    }

    // Основной метод программы
    public static void main(String[] args) {
        // Запуск тестов для сортировки Шелла
        runSorts("Shell Sort", ShellSortTimer::shellSort);
    }

    // Метод для выполнения сортировок и замеров времени
    public static void runSorts(String sortName, SortAlgorithm algorithm) {
        // Печатаем заголовок таблицы
        System.out.printf("%-20s %-20s %-20s %-20s %-20s%n", "Size", "Sorted", "Nearly Sorted", "Reverse Sorted", "Random");

        // Выполняем тесты для различных размеров массива от 10,000 до 250,000 с шагом 10,000
        for (int size = 1000; size <= 15000; size += 1000) {
            // Создаем массив, уже отсортированный по возрастанию
            int[] sortedArray = new int[size];
            for (int i = 0; i < size; i++) sortedArray[i] = i;

            // 1. Измеряем время сортировки отсортированного массива
            long startTime = System.nanoTime(); // Запоминаем начальное время
            algorithm.sort(sortedArray); // Выполняем сортировку
            long endTime = System.nanoTime(); // Запоминаем конечное время
            double sortedTime = (endTime - startTime) / 1_000_000_000.0; // Рассчитываем время в секундах

            // 2. Генерируем почти отсортированный массив
            int[] nearlySortedArray = generateNearlySortedArray(size);
            startTime = System.nanoTime();
            algorithm.sort(nearlySortedArray);
            endTime = System.nanoTime();
            double nearlySortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 3. Генерируем массив, отсортированный в обратном порядке
            int[] reverseSortedArray = generateReverseSortedArray(size);
            startTime = System.nanoTime();
            algorithm.sort(reverseSortedArray);
            endTime = System.nanoTime();
            double reverseSortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 4. Генерируем случайный массив
            int[] randomArray = generateRandomArray(size);
            startTime = System.nanoTime();
            algorithm.sort(randomArray);
            endTime = System.nanoTime();
            double randomTime = (endTime - startTime) / 1_000_000_000.0;

            // Выводим результаты для текущего размера массива
            System.out.printf("%-20d %-20f %-20f %-20f %-20f%n", size, sortedTime, nearlySortedTime, reverseSortedTime, randomTime);
        }
    }

    // Метод для генерации почти отсортированного массива
    // 90% элементов будут отсортированы, а 10% - перемешаны случайным образом
    public static int[] generateNearlySortedArray(int size) {
        int[] array = new int[size];
        // Заполняем массив числами по порядку
        for (int i = 0; i < size; i++) {
            array[i] = i;
        }
        // Перемешиваем 10% элементов случайным образом
        for (int i = 0; i < size / 10; i++) {
            int index1 = new Random().nextInt(size); // Случайный индекс 1
            int index2 = new Random().nextInt(size); // Случайный индекс 2
            // Меняем местами элементы
            int temp = array[index1];
            array[index1] = array[index2];
            array[index2] = temp;
        }
        return array; // Возвращаем почти отсортированный массив
    }

    // Метод для генерации массива, отсортированного в обратном порядке
    public static int[] generateReverseSortedArray(int size) {
        int[] array = new int[size];
        // Заполняем массив числами в убывающем порядке
        for (int i = 0; i < size; i++) {
            array[i] = size - i;
        }
        return array; // Возвращаем массив
    }

    // Метод для генерации случайного массива
    public static int[] generateRandomArray(int size) {
        Random random = new Random(); // Создаем экземпляр класса Random для генерации случайных чисел
        int[] array = new int[size]; // Создаем массив заданного размера
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(100000); // Заполняем массив случайными числами от 0 до 100000
        }
        return array; // Возвращаем случайный массив
    }

    // Интерфейс для передачи алгоритма сортировки в метод runSorts
    interface SortAlgorithm {
        void sort(int[] array); // Метод для сортировки массива
    }
}
