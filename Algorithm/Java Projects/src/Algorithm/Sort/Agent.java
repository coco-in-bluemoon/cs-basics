package Algorithm.Sort;

public class Agent {

    public static void sortByAlgorithm(int[] numbers, Sort sortAlgorithm) {
        long startTime = System.nanoTime();

        sortAlgorithm.setNumbers(numbers);
        sortAlgorithm.sort();

        long endTime = System.nanoTime();
        long elapsedTime = endTime - startTime;
        System.out.println("[Time] " + elapsedTime);

        sortAlgorithm.printNumbers();
    }

    public static void main(String[] args) {
        int[] numbers = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
//        sortByAlgorithm(numbers, new SelectionSort());
//        sortByAlgorithm(numbers, new BubbleSort());
//        sortByAlgorithm(numbers, new InsertionSort());
        sortByAlgorithm(numbers, new QuickSort());
    }
}
