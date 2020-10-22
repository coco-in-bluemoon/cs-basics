import random
import time


def selection_sort(arr):
    n = len(arr)
    for idx in range(n):
        min_index = idx
        for jdx in range(idx, n):
            if arr[min_index] > arr[jdx]:
                min_index = jdx
        arr[idx], arr[min_index] = arr[min_index], arr[idx]


if __name__ == "__main__":
    size = random.randint(5, 10)
    arr = [0] * size
    for idx in range(size):
        arr[idx] = random.randint(1, size * 10)
    print(arr)
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    print(arr)

    elapsed_time = end_time - start_time
    print(f'{elapsed_time} Elapsed')
