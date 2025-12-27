import random, time

def heapify(arr,n,i):
    l,r,largest=2*i+1,2*i+2,i
    if l<n and arr[l]>arr[largest]: largest=l
    if r<n and arr[r]>arr[largest]: largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heapSort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1): heapify(arr,n,i)
    for i in range(n-1,0,-1): arr[0],arr[i]=arr[i],arr[0]; heapify(arr,i,0)

arr=[random.randint(1,50) for _ in range(10)]
start=time.time()
heapSort(arr)
end=time.time()

print("Time taken:",end-start,"seconds")
print("Sorted arr:",arr)
