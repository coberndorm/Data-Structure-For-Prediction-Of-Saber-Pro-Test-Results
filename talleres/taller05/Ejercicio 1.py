import time
import random
import math

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def arrayFill(num):
    A = []
    for i in range(num):
        A.append(num-i)
    return A

for i in range (1000,10000,1000):
    arr = []
    arr = arrayFill(i)
    start = time.time()
    insertionSort(arr)
    print (time.time()-start)