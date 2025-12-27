import random
import time

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = [random.randint(1, 50) for _ in range(20)]

start_time = time.time()
bubbleSort(arr)
end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")
print("Sorted arr is:",arr)