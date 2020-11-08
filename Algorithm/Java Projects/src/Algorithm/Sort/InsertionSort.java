package Algorithm.Sort;

public class InsertionSort extends Sort {
    public void sort() {
        int sizeOfNumbers = numbers.length;

        for (int i = 0; i < sizeOfNumbers; i++) {
            for (int j = i; j > 0; j--) {
                if (numbers[j] < numbers[j-1]) {
                    int temp = numbers[j];
                    numbers[j] = numbers[j-1];
                    numbers[j-1] = temp;
                }
                else {
                    break;
                }
            }
        }
    }
}
