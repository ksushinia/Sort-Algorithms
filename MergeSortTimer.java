import java.util.Arrays;
import java.util.Random;

public class MergeSortTimer {

    // Метод сортировки слиянием (Merge Sort)
    public static void mergeSort(int[] array, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;  // Находим середину массива
            // Рекурсивно сортируем левую половину
            mergeSort(array, left, mid);
            // Рекурсивно сортируем правую половину
            mergeSort(array, mid + 1, right);
            // Сливаем две отсортированные половины
            merge(array, left, mid, right);
        }
    }

    // Метод для слияния двух отсортированных частей массива
    public static void merge(int[] array, int left, int mid, int right) {
        // Определяем размеры двух подмассивов
        int n1 = mid - left + 1;
        int n2 = right - mid;

        // Создаем временные массивы для левой и правой части
        int[] leftArray = new int[n1];
        int[] rightArray = new int[n2];

        // Копируем данные во временные массивы
        System.arraycopy(array, left, leftArray, 0, n1);
        System.arraycopy(array, mid + 1, rightArray, 0, n2);

        // Индексы для левой части, правой части и основного массива
        int i = 0, j = 0, k = left;

        // Сливаем два временных массива обратно в основной массив
        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                array[k] = leftArray[i];
                i++;
            } else {
                array[k] = rightArray[j];
                j++;
            }
            k++;
        }

        // Копируем оставшиеся элементы левой части, если они есть
        while (i < n1) {
            array[k] = leftArray[i];
            i++;
            k++;
        }

        // Копируем оставшиеся элементы правой части, если они есть
        while (j < n2) {
            array[k] = rightArray[j];
            j++;
            k++;
        }
    }

    // Основной метод программы
    public static void main(String[] args) {
        // Запуск тестов для сортировки слиянием
        runSorts("Merge Sort", (array) -> mergeSort(array, 0, array.length - 1));
    }

    // Метод для выполнения сортировок и замеров времени
    public static void runSorts(String sortName, SortAlgorithm algorithm) {
        // Печатаем заголовок таблицы
        System.out.printf("%-20s %-20s %-20s %-20s %-20s%n", "Size", "Sorted", "Nearly Sorted", "Reverse Sorted", "Random");

        // Выполняем тесты для различных размеров массива от 10,000 до 150,000 с шагом 10,000
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
