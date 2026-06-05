import matplotlib.pyplot as plt
import random
import time

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


sizes=[10,20,30,40,50]
times=[]

for size in sizes:
    arr=[random.randint(1,100) for _ in range(size)]
    start=time.time()
    bubble_sort(arr)
    end=time.time()
    times.append(end-start)


plt.plot(sizes,times,marker='o')
plt.title("bubble sort")
plt.xlabel("input size")
plt.ylabel("time taken")
plt.grid()
plt.show()
