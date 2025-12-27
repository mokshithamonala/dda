import random
import time

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [random.randint(1, 50) for _ in range(10)]

start_time = time.time()
selectionSort(arr)
end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")
print("Sorted arr:", arr)
