package Algorithm.Sort;

public class BubbleSort extends Sort{
    public void sort() {
        long startTime = System.nanoTime();

        int sizeOfNumbers = numbers.length;

        for (int i = 0; i < sizeOfNumbers; i++) {
            int endIndex = sizeOfNumbers - i - 1;
            for (int j = 0; j < endIndex; j++) {
                if (numbers[j] > numbers[j+1]) {
                    int temp = numbers[j];
                    numbers[j] = numbers[j + 1];
                    numbers[j + 1] = temp;
                }
            }
        }

        long endTime = System.nanoTime();
        long elapsedTime = endTime - startTime;
        System.out.println(elapsedTime);

    }
}
