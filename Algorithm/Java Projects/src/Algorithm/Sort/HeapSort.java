package Algorithm.Sort;

public class HeapSort extends Sort {
    @Override
    public void sort() {
        for (int i = this.numbers.length - 1; i >= 0; i--) {
            int index = i;
            int number = this.numbers[index];
            int parentIndex = (index - 1) / 2;
            int parentNumber = this.numbers[parentIndex];

            while (parentIndex >= 0 && number > parentNumber) {
                this.numbers[index] = parentNumber;
                this.numbers[parentIndex] = number;
                index = parentIndex;
                parentIndex = (index - 1) / 2;
            }
        }
    }
}
