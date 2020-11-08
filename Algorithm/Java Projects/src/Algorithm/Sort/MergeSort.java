package Algorithm.Sort;

public class MergeSort extends Sort{
    private int[] buffer;

    private void mergeSort(int startIndex, int endIndex) {
        int size = endIndex - startIndex;
        if (size == 1) {
            return;
        }

        int middleIndex = (startIndex + endIndex) / 2;

        mergeSort(0, middleIndex);
        mergeSort(middleIndex, endIndex);

        int indexLeft = startIndex;
        int indexRight = middleIndex;
        int indexMerged = 0;

        while (indexLeft < middleIndex && indexRight < endIndex) {
            int numberLeft = this.numbers[indexLeft];
            int numberRight = this.numbers[indexRight];

            if (numberLeft < numberRight) {
                buffer[indexMerged] = numberLeft;
                indexLeft += 1;
            } else {
                buffer[indexMerged] = numberRight;
                indexRight += 1;
            }
            indexMerged += 1;
        }

        while (indexLeft < middleIndex) {
            buffer[indexMerged] = this.numbers[indexLeft];
            indexMerged += 1;
            indexLeft += 1;
        }

        while (indexRight < endIndex) {
            buffer[indexMerged] = this.numbers[indexRight];
            indexMerged += 1;
            indexRight += 1;
        }

        for (int i = 0; i < size; i++) {
            this.numbers[startIndex + i] = buffer[i];
        }
    }

    @Override
    public void sort() {
        buffer = new int[this.numbers.length];
        mergeSort(0, this.numbers.length);
    }
}
