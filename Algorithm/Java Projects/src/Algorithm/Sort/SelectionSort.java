package Algorithm.Sort;

public class SelectionSort extends Sort {
    public void sort() {
        long startTime = System.nanoTime();
        int sizeOfNumbers = numbers.length;

        for (int i = 0; i < sizeOfNumbers; i++) {
            int minNumber = numbers[i];
            int minNumberIndex = i;
            for (int j = i; j < sizeOfNumbers; j++) {
                if (numbers[j] < minNumber) {
                    minNumber = numbers[j];
                    minNumberIndex = j;
                }
            }
            numbers[minNumberIndex] = numbers[i];
            numbers[i] = minNumber;
        }
        long endTime = System.nanoTime();
        long elapsedTime = endTime - startTime;
        System.out.println(elapsedTime);
    }
}
