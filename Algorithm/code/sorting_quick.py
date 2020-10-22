import random
import time


def _quick_sort(start, end, arr):
    if start >= end:
        return

    pivot = start
    ldx = start + 1
    rdx = end - 1

    while ldx <= rdx:
        while ldx < end and arr[ldx] <= arr[pivot]:
            ldx += 1
        while rdx > start and arr[rdx] >= arr[pivot]:
            rdx -= 1

        if ldx < rdx:
            arr[ldx], arr[rdx] = arr[rdx], arr[ldx]
        else:
            arr[pivot], arr[rdx] = arr[rdx], arr[pivot]

    _quick_sort(start, rdx, arr)
    _quick_sort(rdx+1, end, arr)


def quick_sort(arr):
    n = len(arr)
    _quick_sort(0, n, arr)


if __name__ == "__main__":
    size = random.randint(5, 10)
    arr = [0] * size
    for idx in range(size):
        arr[idx] = random.randint(1, size * 10)
    print(arr)
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    print(arr)

    elapsed_time = end_time - start_time
    print(f'{elapsed_time} Elapsed')
