import time

def sumaArreglo(arr1):
    d= 0
    for i in range(arr1):
        d+=arr1[i]
    return d
def arrayFill(num):
    A = []
    for i in range(num):
        A.append(num-i)
    return A

for i in range (1000,10000,1000):
    arr = []
    arr = arrayFill(i)
    start = time.time()
    sumaArreglo(arr)
    print (time.time()-start)
