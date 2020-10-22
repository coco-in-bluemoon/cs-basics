import random
import time


def insertion_sort(arr):
    n = len(arr)
    for idx in range(n):
        for jdx in range(idx, 0, -1):
            if arr[jdx] < arr[jdx-1]:
                arr[jdx-1], arr[jdx] = arr[jdx], arr[jdx-1]
            else:
                break


if __name__ == "__main__":
    size = random.randint(5, 10)
    arr = [0] * size
    for idx in range(size):
        arr[idx] = random.randint(1, size * 10)
    print(arr)
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    print(arr)

    elapsed_time = end_time - start_time
    print(f'{elapsed_time} Elapsed')
