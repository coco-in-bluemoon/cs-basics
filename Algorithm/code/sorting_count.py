import random
import time


def count_sort(arr, size):
    counter = [0] * (size+1)
    n = len(arr)
    for idx in range(n):
        counter[arr[idx]] += 1

    index = 0
    while index < n:
        for jdx in range(size+1):
            if not counter[jdx]:
                continue
            for _ in range(counter[jdx]):
                arr[index] = jdx
                index += 1


if __name__ == "__main__":
    size = random.randint(5, 10)
    arr = [0] * size
    for idx in range(size):
        arr[idx] = random.randint(1, size * 10)
    print(arr)
    start_time = time.time()
    count_sort(arr, size*10)
    end_time = time.time()
    print(arr)

    elapsed_time = end_time - start_time
    print(f'{elapsed_time} Elapsed')
