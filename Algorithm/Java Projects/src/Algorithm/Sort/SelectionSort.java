package Algorithm.Sort;

public class SelectionSort extends Sort {
    @Override
    public void sort() {
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
    }
}
