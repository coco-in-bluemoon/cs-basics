package Algorithm.Sort;

public class QuickSort extends Sort {
    private void quickSort(int startIndex, int endIndex) {
        if (startIndex >= endIndex) {
            return;
        }

        int pivot = this.numbers[startIndex];

        int findBiggerIndex = startIndex + 1;
        int findSmallerIndex = endIndex;

        while (findBiggerIndex <= findSmallerIndex) {
            while (findBiggerIndex <= endIndex && this.numbers[findBiggerIndex] <= pivot) {
                findBiggerIndex += 1;
            }

            while (findSmallerIndex > startIndex && this.numbers[findSmallerIndex] >= pivot) {
                findSmallerIndex -= 1;
            }

            if (findBiggerIndex > findSmallerIndex) {
                this.numbers[startIndex] = this.numbers[findSmallerIndex];
                this.numbers[findSmallerIndex] = pivot;
            } else {
                int temp = this.numbers[findSmallerIndex];
                this.numbers[findSmallerIndex] = this.numbers[findBiggerIndex];
                this.numbers[findBiggerIndex] = temp;
            }
        }

        quickSort(startIndex, findSmallerIndex - 1);
        quickSort(findSmallerIndex + 1, endIndex);
    }

    @Override
    public void sort() {
        quickSort(0, this.numbers.length-1);
    }
}
