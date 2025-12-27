import random
import time

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [random.randint(1, 50) for _ in range(10)]

start_time = time.time()
insertionSort(arr)
end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")
print("Sorted arr:", arr)
