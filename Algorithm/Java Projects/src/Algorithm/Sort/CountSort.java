package Algorithm.Sort;

public class CountSort extends Sort {
    private int[] buffer = new int[100];
    @Override
    public void sort() {
        for (int i = 0; i < this.numbers.length; i++) {
            int number = this.numbers[i];
            buffer[number] += 1;
        }

        int index = 0;
        for (int i = 0; i < buffer.length; i++) {
            if (buffer[i] == 0) {
                continue;
            }

            int number = i;
            int counter = buffer[i];
            for (int j = 0; j < counter; j++) {
                this.numbers[index] = number;
                index += 1;
            }
        }
    }
}
