import random
import time


def _merge_sort(start, end, arr):
    if end - start == 1:
        return (start, end)

    middle = (start + end) // 2
    ldx, ldx_end = _merge_sort(start, middle, arr)
    rdx, rdx_end = _merge_sort(middle, end, arr)

    temp = [0] * (end - start)
    index = 0
    while ldx < ldx_end and rdx < rdx_end:
        if arr[ldx] > arr[rdx]:
            temp[index] = arr[rdx]
            rdx += 1
        else:
            temp[index] = arr[ldx]
            ldx += 1
        index += 1

    while ldx < ldx_end:
        temp[index] = arr[ldx]
        ldx += 1
        index += 1
    while rdx < rdx_end:
        temp[index] = arr[rdx]
        rdx += 1
        index += 1

    for idx in range(end-start):
        arr[idx+start] = temp[idx]

    return (start, end)


def merge_sort(arr):
    n = len(arr)
    _merge_sort(0, n, arr)


if __name__ == "__main__":
    size = random.randint(5, 10)
    arr = [0] * size
    for idx in range(size):
        arr[idx] = random.randint(1, size * 10)
    print(arr)
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    print(arr)

    elapsed_time = end_time - start_time
    print(f'{elapsed_time} Elapsed')
