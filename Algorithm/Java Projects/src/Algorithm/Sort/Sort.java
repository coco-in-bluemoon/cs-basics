package Algorithm.Sort;

public abstract class Sort {
    protected int[] numbers;

    public void sort() {};

    public void printNumbers() {
        int sizeOfNumbers = numbers.length;
        for (int i = 0; i < sizeOfNumbers; i++) {
            System.out.print(numbers[i]);
            System.out.print(" ");
        }
        System.out.println();
    }

    public int[] getNumbers() {
        return numbers;
    }

    public void setNumbers(int[] numbers) {
        this.numbers = numbers;
    }
}
