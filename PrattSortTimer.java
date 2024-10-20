import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class PrattSortTimer {

    // Метод для сортировки с использованием последовательности Пратта
    public static void prattSort(int[] array) {
        int n = array.length;
        List<Integer> prattSequence = generatePrattSequence(n); // Генерируем последовательность Пратта

        // Проходим по всем промежуткам в последовательности Пратта
        for (int gap : prattSequence) {
            // Выполняем сортировку вставками для элементов, находящихся на расстоянии gap
            for (int i = gap; i < n; i++) {
                int temp = array[i]; // Сохраняем текущий элемент
                int j = i;
                // Сортировка вставками для элементов, находящихся на расстоянии gap
                while (j >= gap && array[j - gap] > temp) {
                    array[j] = array[j - gap]; // Сдвигаем элемент
                    j -= gap;
                }
                array[j] = temp; // Вставляем элемент на правильное место
            }
        }
    }

    // Метод для генерации последовательности Пратта
    public static List<Integer> generatePrattSequence(int max) {
        List<Integer> prattSequence = new ArrayList<>();
        int p = 1, q = 1;
        while (p <= max) {
            q = p;
            while (q <= max) {
                prattSequence.add(q); // Добавляем элемент в последовательность
                q *= 3; // Генерируем числа как произведение степеней 2 и 3
            }
            p *= 2;
        }
        prattSequence.sort((a, b) -> b - a); // Сортируем последовательность в обратном порядке
        return prattSequence;
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
            prattSort(sortedArray); // Сортируем
            long endTime = System.nanoTime(); // Конец отсчета времени
            double sortedTime = (endTime - startTime) / 1_000_000_000.0; // Время в секундах

            // 2. Почти отсортированный массив
            int[] nearlySortedArray = generateNearlySortedArray(size);
            startTime = System.nanoTime();
            prattSort(nearlySortedArray);
            endTime = System.nanoTime();
            double nearlySortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 3. Массив, отсортированный в обратном порядке
            int[] reverseSortedArray = generateReverseSortedArray(size);
            startTime = System.nanoTime();
            prattSort(reverseSortedArray);
            endTime = System.nanoTime();
            double reverseSortedTime = (endTime - startTime) / 1_000_000_000.0;

            // 4. Случайный массив
            int[] randomArray = generateRandomArray(size);
            startTime = System.nanoTime();
            prattSort(randomArray);
            endTime = System.nanoTime();
            double randomTime = (endTime - startTime) / 1_000_000_000.0;

            // Вывод результатов
            System.out.printf("%-20d %-20f %-20f %-20f %-20f%n", size, sortedTime, nearlySortedTime, reverseSortedTime, randomTime);
        }
    }
}
