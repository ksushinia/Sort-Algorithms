import java.util.Random;

public class HibbardSortTimer {

    // Метод для сортировки Шелла с последовательностью Хиббарда
    public static void HibbardSortTimer(int[] array) {
        int n = array.length;
        int k = 1;

        // Находим максимальный шаг в последовательности Хиббарда
        while ((1 << k) - 1 < n) {
            k++;
        }

        // Сортировка с использованием шагов Хиббарда
        for (int gap = (1 << (k - 1)) - 1; gap > 0; gap = (1 << (--k)) - 1) {
            for (int i = gap; i < n; i++) {
                int temp = array[i];
                int j;
                for (j = i; j >= gap && array[j - gap] > temp; j -= gap) {
                    array[j] = array[j - gap];
                }
                array[j] = temp;
            }
        }
    }

    // Метод для генерации случайного массива
    public static int[] generateRandomArray(int size) {
        Random random = new Random();
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = random.nextInt(100000);
        }
        return array;
    }

    // Метод для создания почти отсортированного массива
    public static int[] generateNearlySortedArray(int size) {
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = i;
        }
        // Перемешиваем 10% элементов
        for (int i = 0; i < size / 10; i++) {
            int index1 = new Random().nextInt(size);
            int index2 = new Random().nextInt(size);
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
            array[i] = size - i;
        }
        return array;
    }

    // Метод для запуска тестов
    public static void main(String[] args) {
        int startSize = 1000;
        int endSize = 15000;
        int step = 1000;

        System.out.printf("%-20s %-20s %-20s %-20s %-20s%n", "Size", "Sorted", "Nearly Sorted", "Reverse Sorted", "Random");

        for (int size = startSize; size <= endSize; size += step) {

            // 1. Отсортированный массив
            int[] sortedArray = new int[size];
            for (int i = 0; i < size; i++) {
                sortedArray[i] = i;
            }
            long startTime = System.nanoTime();
            HibbardSortTimer(sortedArray);
            long endTime = System.nanoTime();
            double sortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 2. Почти отсортированный массив
            int[] nearlySortedArray = generateNearlySortedArray(size);
            startTime = System.nanoTime();
            HibbardSortTimer(nearlySortedArray);
            endTime = System.nanoTime();
            double nearlySortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 3. Массив, отсортированный в обратном порядке
            int[] reverseSortedArray = generateReverseSortedArray(size);
            startTime = System.nanoTime();
            HibbardSortTimer(reverseSortedArray);
            endTime = System.nanoTime();
            double reverseSortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 4. Случайный массив
            int[] randomArray = generateRandomArray(size);
            startTime = System.nanoTime();
            HibbardSortTimer(randomArray);
            endTime = System.nanoTime();
            double randomTime = (endTime - startTime) / 1_000_000_000.0;

            // Вывод результатов
            System.out.printf("%-20d %-20f %-20f %-20f %-20f%n", size, sortedTime, nearlySortedTime, reverseSortedTime, randomTime);
        }
    }
}
