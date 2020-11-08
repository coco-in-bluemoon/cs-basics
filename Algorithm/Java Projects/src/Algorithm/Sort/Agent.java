package Algorithm.Sort;

import java.util.Arrays;


public class Agent {

    public static void sortByAlgorithm(int[] numbers, Sort sortAlgorithm) {
        long startTime = System.nanoTime();

        sortAlgorithm.setNumbers(numbers);
        sortAlgorithm.sort();

        long endTime = System.nanoTime();
        long elapsedTime = endTime - startTime;
        String className = sortAlgorithm.getClass().getSimpleName();
        System.out.println("[Time for " + className + "] " + elapsedTime);

        sortAlgorithm.printNumbers();
    }

    public static void main(String[] args) {
        int[] numbers = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
        sortByAlgorithm(Arrays.copyOf(numbers, numbers.length), new SelectionSort());
        sortByAlgorithm(Arrays.copyOf(numbers, numbers.length), new BubbleSort());
        sortByAlgorithm(Arrays.copyOf(numbers, numbers.length), new InsertionSort());
        sortByAlgorithm(Arrays.copyOf(numbers, numbers.length), new QuickSort());
        sortByAlgorithm(Arrays.copyOf(numbers, numbers.length), new MergeSort());
    }
}
