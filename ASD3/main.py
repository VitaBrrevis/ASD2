import sys
# import matplotlib.pyplot as plt
# import numpy as np
# import svit as sv
# import random
def algorithm1(array):
    # Quicksort algorithm
    comparisons = 0
    swaps = 0

    def partition(arr, low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]  # choose last element as pivot
        i = low - 1  # index of smaller element
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    sorted_array = list(array)  # make a copy of the original array
    quicksort(sorted_array, 0, len(array) - 1)
    return sorted_array, comparisons, swaps


def algorithm2(array):
    comparisons = 0
    swaps = 0
    def swap(arr,x, y):
        nonlocal swaps
        arr[x], arr[y] = arr[y], arr[x]
        swaps +=1

    def partition(arr, low, high):
        nonlocal comparisons
        pivot = arr[high]  # choose last element as pivot
        i = low - 1  # index of smaller element
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                #arr[i], arr[j] = arr[j], arr[i]
                swap(arr,i,j)
        #arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swap(arr,i + 1,high)
        return i + 1

    def quicksort(array, low, high):
        nonlocal comparisons
        if high - low + 1 <= 3:  # sort subarrays of size 3 or less without partitionin
            size = high - low + 1
            if size == 3:
                comparisons += 1
                if array[low] <= array[low+1]:
                    comparisons += 1
                    if array[low+1] <= array[high]:
                        pass
                    else:
                        #array[low + 1],array[high] = array[high],array[low+1]
                        swap(array,low + 1,high)
                        comparisons += 1
                        if array[low] <= array[low+1]:
                            pass
                        else:
                            #array[low], array[low+1] = array[low+1], array[low]
                            swap(array, low, low + 1)
                else:
                    #array[low], array[low + 1] = array[low + 1], array[low]
                    swap(array, low, low + 1)
                    comparisons += 1
                    if array[low+1] <= array[high]:
                        pass
                    else:
                        #array[low + 1], array[high] = array[high], array[low + 1]
                        swap(array, low + 1, high)
                        comparisons += 1
                        if array[low] <= array[low + 1]:
                            pass
                        else:
                            # array[low], array[low + 1] = array[low + 1], array[low]
                            swap(array, low, low + 1)
            if size == 2:
                comparisons += 1
                if array[low] > array[high]:
                    swap(array, low, high)
                    # array[low], array[high] = array[high], array[low]

            sorted_array = array[low:high+1]
            return sorted_array
        else:
            median_index = (low + high) // 2

            median = sorted([array[low], array[median_index], array[high]])[1]
            median_index = array.index(median)
            # array[high], array[median_index] = array[median_index], array[high]
            swap(array, high, median_index)

            pivot_index = partition(array, low, high)
            left = quicksort(array, low, pivot_index - 1)
            right = quicksort(array, pivot_index + 1, high)
            sorted_array =  ( left if left is not None else [] ) + [array[pivot_index]]+ ( right if right is not None else [] )
            return sorted_array

    # sorted_array = list(array)
    sorted_array = quicksort(array, 0, len(array) - 1)
    return sorted_array, comparisons, swaps

def algorithm3(array):
    comparisons = 0
    swaps = 0
    def swap(arr,x, y):
        nonlocal swaps
        arr[x], arr[y] = arr[y], arr[x]
        swaps += 1

    def partition(A, left, right):
        nonlocal comparisons
        a = left + 2; b = left + 2
        c = right - 1; d = right - 1
        p = A[left]; q = A[left + 1];  r = A[right]
        while b <= c:

            while A[b] < q and b <= c:
                comparisons += 2
                if A[b] < p:
                    swap(A, a, b)
                    a = a + 1
                b = b + 1

            while A[c] > q and b <= c:
                comparisons += 2
                if A[c] > r:
                    swap(A, c, d)
                    d = d - 1
                c = c - 1
            if b <= c:
                comparisons += 1
                if A[b] > r:
                    comparisons += 1
                    if A[c] < p:
                        swap(A,b,a); swap(A,a,c)
                        a = a + 1
                    else:
                        swap(A,b,c)
                    swap(A,c,d)
                    b = b + 1; c = c - 1; d = d - 1
                else:
                    comparisons += 1
                    if A[c] < p:
                        swap(A,b,a); swap(A,a,c)
                        a = a + 1
                    else:
                        swap(A,b,c)
                    b = b + 1; c = c - 1
        a = a - 1; b = b - 1; c = c + 1; d = d + 1
        swap(A,left + 1,a); swap(A,a,b)
        a = a - 1
        swap(A,left,a); swap(A,right,d)
        iq=b
        ip=a
        ir=d
        return ip,iq,ir

    def quicksort(array, low, high):
            nonlocal comparisons
            if high - low + 1 <= 3:  # sort subarrays of size 3 or less without partitioning
                size = high - low + 1
                if size == 3:
                    comparisons += 1
                    if array[low] <= array[low + 1]:
                        comparisons += 1
                        if array[low + 1] <= array[high]:
                            pass
                        else:
                            # array[low + 1],array[high] = array[high],array[low+1]
                            swap(array, low + 1, high)
                            comparisons += 1
                            if array[low] <= array[low + 1]:
                                pass
                            else:
                                # array[low], array[low+1] = array[low+1], array[low]
                                swap(array, low, low + 1)
                    else:
                        # array[low], array[low + 1] = array[low + 1], array[low]
                        swap(array, low, low + 1)
                        comparisons += 1
                        if array[low + 1] <= array[high]:
                            pass
                        else:
                            # array[low + 1], array[high] = array[high], array[low + 1]
                            swap(array, low + 1, high)
                            comparisons += 1
                            if array[low] <= array[low + 1]:
                                pass
                            else:
                                # array[low], array[low + 1] = array[low + 1], array[low]
                                swap(array, low, low + 1)
                if size == 2:
                    comparisons += 1
                    if array[low] > array[high]:
                        swap(array, low, high)
                        # array[low], array[high] = array[high], array[low]

            else:
                if array[low] > array[low+1]:
                    swap(array, low, low+1)
                if array[low+1] > array[high]:
                    swap(array, low + 1, high)
                if array[low] > array[low + 1]:
                    swap(array, low, low + 1)

                ip,iq,ir = partition(array, low, high)

                quicksort(array, low, ip )
                quicksort(array, ip + 1 , iq)
                quicksort(array, iq + 1 , high)

    quicksort(array, 0, len(array) - 1),
    return comparisons, swaps

sys.setrecursionlimit(200000)

input_file = "data.txt"

with open(input_file, 'r') as f:
    n = int(f.readline().strip())
    array = [int(f.readline().strip()) for _ in range(n)]
# Run the three sorting algorithms on the input array and get comparison counts
array1 = array.copy()
array3 = array.copy()

comparisons1 = 0
sorted_array1, comparisons1, swaps1 = algorithm1(array)

comparisons2 = 0
sorted_array2, comparisons2, swaps2 = algorithm2(array)

# comparisons3 = quicksort_3way(array, 0, len(array))
comparisons3 = 0
comparisons3, swaps3 = algorithm3(array3)


print("comparisons1: ", comparisons1, "sorted_array1: ", sorted_array1)
print("comparisons2: ", comparisons2, "sorted_array2: ", sorted_array2)
print("comparisons3: ", comparisons3, "sorted_array3: ", array3)