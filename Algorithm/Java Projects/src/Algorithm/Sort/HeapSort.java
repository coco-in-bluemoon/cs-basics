package Algorithm.Sort;

public class HeapSort extends Sort {
    private void constructMaxHeap(int endHeapIndex) {
        for (int i = endHeapIndex; i >= 0; i--) {
            int index = i;
            int number = this.numbers[index];
            int parentIndex = (index - 1) / 2;
            int parentNumber = this.numbers[parentIndex];

            while (index > 0 && number > parentNumber) {
                this.numbers[index] = parentNumber;
                this.numbers[parentIndex] = number;
                index = parentIndex;
                parentIndex = (index - 1) / 2;

                number = this.numbers[index];
                parentNumber = this.numbers[parentIndex];
            }
        }
    }
    @Override
    public void sort() {
        for (int i = this.numbers.length - 1; i >= 0; i--) {
            int endHeapIndex = i;
            constructMaxHeap(endHeapIndex);
            int maxNumber = this.numbers[0];
            this.numbers[0] = this.numbers[i];
            this.numbers[i] = maxNumber;
        }

    }
}
