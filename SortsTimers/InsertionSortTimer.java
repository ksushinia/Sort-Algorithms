import java.util.Arrays;
import java.util.Random;
public class InsertionSortTimer {

    // Метод сортировки вставками
    public static void insertionSort(int[] array) {
        for (int i = 1; i < array.length; i++) {
            int key = array[i];
            int j = i - 1;
            // Сдвигаем элементы массива, которые больше key
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = key;
        }
    }

    // Основной метод
    public static void main(String[] args) {
        runSorts("Insertion Sort", InsertionSortTimer::insertionSort);
    }

    // Запуск тестов
    public static void runSorts(String sortName, SortAlgorithm algorithm) {
        System.out.printf("%-20s %-20s %-20s %-20s %-20s%n", "Size", "Sorted", "Nearly Sorted", "Reverse Sorted", "Random");
        for (int size = 1000; size <= 15000; size += 1000) {
            int[] sortedArray = new int[size];
            for (int i = 0; i < size; i++) sortedArray[i] = i;

            // 1. Отсортированный массив
            long startTime = System.nanoTime();
            algorithm.sort(sortedArray);
            long endTime = System.nanoTime();
            double sortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 2. Почти отсортированный массив
            int[] nearlySortedArray = generateNearlySortedArray(size);
            startTime = System.nanoTime();
            algorithm.sort(nearlySortedArray);
            endTime = System.nanoTime();
            double nearlySortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 3. Массив, отсортированный в обратном порядке
            int[] reverseSortedArray = generateReverseSortedArray(size);
            startTime = System.nanoTime();
            algorithm.sort(reverseSortedArray);
            endTime = System.nanoTime();
            double reverseSortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 4. Случайный массив
            int[] randomArray = generateRandomArray(size);
            startTime = System.nanoTime();
            algorithm.sort(randomArray);
            endTime = System.nanoTime();
            double randomTime = (endTime - startTime) / 1_000_000_000.0;

            System.out.printf("%-20d %-20f %-20f %-20f %-20f%n", size, sortedTime, nearlySortedTime, reverseSortedTime, randomTime);
        }
    }

    // Генерация почти отсортированного массива
    public static int[] generateNearlySortedArray(int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = i;
        }
        for (int i = 0; i < size / 10; i++) {
            int index1 = new Random().nextInt(size);
            int index2 = new Random().nextInt(size);
            int temp = array[index1];
            array[index1] = array[index2];
            array[index2] = temp;
        }
        return array;
    }

    // Генерация массива, отсортированного в обратном порядке
    public static int[] generateReverseSortedArray(int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = size - i;
        }
        return array;
    }

    // Генерация случайного массива
    public static int[] generateRandomArray(int size) {
        Random random = new Random();
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(100000);
        }
        return array;
    }

    // Интерфейс для сортировки
    interface SortAlgorithm {
        void sort(int[] array);
    }
}
