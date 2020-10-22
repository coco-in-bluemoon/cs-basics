import random
import time


def heap_sort(arr):
    # construct max heap
    n = len(arr)
    for idx in range(1, n):
        index_child = idx
        while index_child:
            index_parent = (index_child - 1) // 2
            if arr[index_parent] < arr[index_child]:
                arr[index_child], arr[index_parent] =\
                    arr[index_parent], arr[index_child]
                index_child = index_parent
            else:
                break

    for idx in range(n-1, 0, -1):
        arr[idx], arr[0] = arr[0], arr[idx]
        for jdx in range(1, idx):
            index_child = jdx
            while index_child:
                index_parent = (index_child - 1) // 2
                if arr[index_parent] < arr[index_child]:
                    arr[index_child], arr[index_parent] =\
                        arr[index_parent], arr[index_child]
                    index_child = index_parent
                else:
                    break


if __name__ == "__main__":
    size = random.randint(5, 10)
    arr = [0] * size
    for idx in range(size):
        arr[idx] = random.randint(1, size * 10)
    print(arr)
    start_time = time.time()
    heap_sort(arr)
    end_time = time.time()
    print(arr)

    elapsed_time = end_time - start_time
    print(f'{elapsed_time} Elapsed')
