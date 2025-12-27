import random, time

def insertionSort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i-1
        while j>=0 and arr[j]>key:
            arr[j+1], j = arr[j], j-1
        arr[j+1] = key

def bucketSort(arr):
    if not arr: return arr
    b = [[] for _ in range(5)]
    mn, mx = min(arr), max(arr)
    for x in arr:
        b[int((x-mn)/(mx-mn+1)*5)].append(x)
    sorted_arr = []
    for bucket in b:
        insertionSort(bucket)
        sorted_arr.extend(bucket)
    return sorted_arr

arr = [random.randint(1,50) for _ in range(10)]
start = time.time()
arr = bucketSort(arr)
end = time.time()

print("Time taken:", end-start, "seconds")
print("Sorted arr:", arr)
