import java.util.Random;

public class QuickSortTimer {

    // Метод быстрой сортировки (Quick Sort) с медианой из трёх
    public static void quickSort(int[] array, int left, int right) {
        if (left < right) {
            // Выбираем опорный элемент с помощью медианы из трёх
            int pivotIndex = medianOfThree(array, left, right);
            int pivot = array[pivotIndex];

            // Разделяем массив на две части
            int partitionIndex = partition(array, left, right, pivot);

            // Рекурсивно сортируем левую и правую части массива
            quickSort(array, left, partitionIndex - 1);
            quickSort(array, partitionIndex + 1, right);
        }
    }

    // Метод для разделения массива на две части
    private static int partition(int[] array, int left, int right, int pivot) {
        while (left <= right) {
            // Ищем элемент слева, который больше или равен pivot
            while (array[left] < pivot) {
                left++;
            }
            // Ищем элемент справа, который меньше или равен pivot
            while (array[right] > pivot) {
                right--;
            }
            // Если нашли пару элементов, которые нужно поменять местами
            if (left <= right) {
                swap(array, left, right); // Меняем местами
                left++;
                right--;
            }
        }
        return left; // Возвращаем индекс разделения
    }

    // Метод для выбора медианы из трёх элементов
    private static int medianOfThree(int[] array, int left, int right) {
        int mid = (left + right) / 2;

        // Сравниваем и переставляем элементы так, чтобы array[left] <= array[mid] <= array[right]
        if (array[left] > array[mid]) swap(array, left, mid);
        if (array[left] > array[right]) swap(array, left, right);
        if (array[mid] > array[right]) swap(array, mid, right);

        // Возвращаем индекс медианного элемента
        return mid;
    }

    // Метод для обмена элементов массива
    private static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    // Основной метод программы
    public static void main(String[] args) {
        runSorts("Quick Sort", (array) -> quickSort(array, 0, array.length - 1));
    }

    // Метод для выполнения сортировок и замеров времени
    public static void runSorts(String sortName, SortAlgorithm algorithm) {
        System.out.printf("%-20s %-20s %-20s %-20s %-20s%n", "Size", "Sorted", "Nearly Sorted", "Reverse Sorted", "Random");

        // Выполняем тесты для различных размеров массива от 10,000 до 250,000 с шагом 10,000
        for (int size = 1000; size <= 15000; size += 1000) {
            int[] sortedArray = new int[size];
            for (int i = 0; i < size; i++) sortedArray[i] = i;

            // 1. Измеряем время сортировки отсортированного массива
            long startTime = System.nanoTime();
            algorithm.sort(sortedArray);
            long endTime = System.nanoTime();
            double sortedTime = (endTime - startTime) / 1_000_000_000.0;

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
