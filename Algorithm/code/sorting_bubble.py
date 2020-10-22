import random
import time


def bubble_sort(arr):
    n = len(arr)
    for idx in range(n):
        for jdx in range(n-idx-1):
            if arr[jdx] > arr[jdx+1]:
                arr[jdx], arr[jdx+1] = arr[jdx+1], arr[jdx]


if __name__ == "__main__":
    size = random.randint(5, 10)
    arr = [0] * size
    for idx in range(size):
        arr[idx] = random.randint(1, size * 10)
    print(arr)
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    print(arr)

    elapsed_time = end_time - start_time
    print(f'{elapsed_time} Elapsed')
