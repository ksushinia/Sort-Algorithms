import java.util.Arrays;
import java.util.Random;

public class SelectionSortTimer {

    // Метод для сортировки выбором
    public static void selectionSort(int[] array) {
        int n = array.length; // Получаем длину массива
        for (int i = 0; i < n - 1; i++) { // Проходим по всем элементам массива
            int minIndex = i; // Предполагаем, что текущий элемент - минимальный
            for (int j = i + 1; j < n; j++) { // Сравниваем с оставшимися элементами
                if (array[j] < array[minIndex]) { // Если найден меньший элемент
                    minIndex = j; // Обновляем индекс минимального элемента
                }
            }
            // Меняем местами найденный минимальный элемент с текущим
            int temp = array[minIndex];
            array[minIndex] = array[i];
            array[i] = temp;
        }
    }

    // Метод для генерации случайного массива
    public static int[] generateRandomArray(int size) {
        Random random = new Random(); // Создаем генератор случайных чисел
        int[] array = new int[size]; // Инициализируем массив
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(100000); // Заполняем массив случайными числами
        }
        return array;
    }

    // Метод для создания почти отсортированного массива
    public static int[] generateNearlySortedArray(int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = i; // Заполняем массив отсортированными числами
        }
        // Перемешиваем 10% элементов
        for (int i = 0; i < size / 10; i++) {
            int index1 = new Random().nextInt(size); // Случайный индекс
            int index2 = new Random().nextInt(size); // Еще один случайный индекс
            // Меняем местами два случайных элемента
            int temp = array[index1];
            array[index1] = array[index2];
            array[index2] = temp;
        }
        return array;
    }

    // Метод для создания массива, отсортированного в обратном порядке
    public static int[] generateReverseSortedArray(int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = size - i; // Заполняем массив убывающими числами
        }
        return array;
    }

    // Метод для запуска тестов
    public static void main(String[] args) {
        int startSize = 1000; // Начальный размер массива
        int endSize = 15000; // Конечный размер массива
        int step = 1000; // Шаг увеличения размера массива

        System.out.printf("%-20s %-20s %-20s %-20s %-20s%n", "Size", "Sorted", "Nearly Sorted", "Reverse Sorted", "Random");
        for (int size = startSize; size <= endSize; size += step) {
            // 1. Отсортированный массив
            int[] sortedArray = new int[size];
            for (int i = 0; i < size; i++) {
                sortedArray[i] = i; // Заполняем массив отсортированными числами
            }
            long startTime = System.nanoTime(); // Начало отсчета времени
            selectionSort(sortedArray); // Сортируем
            long endTime = System.nanoTime(); // Конец отсчета времени
            double sortedTime = (endTime - startTime) / 1_000_000_000.0; // Время в секундах

            // 2. Почти отсортированный массив
            int[] nearlySortedArray = generateNearlySortedArray(size);
            startTime = System.nanoTime();
            selectionSort(nearlySortedArray);
            endTime = System.nanoTime();
            double nearlySortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 3. Массив, отсортированный в обратном порядке
            int[] reverseSortedArray = generateReverseSortedArray(size);
            startTime = System.nanoTime();
            selectionSort(reverseSortedArray);
            endTime = System.nanoTime();
            double reverseSortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 4. Случайный массив
            int[] randomArray = generateRandomArray(size);
            startTime = System.nanoTime();
            selectionSort(randomArray);
            endTime = System.nanoTime();
            double randomTime = (endTime - startTime) / 1_000_000_000.0;

            // Вывод результатов
            System.out.printf("%-20d %-20f %-20f %-20f %-20f%n", size, sortedTime, nearlySortedTime, reverseSortedTime, randomTime);
        }
    }
}
