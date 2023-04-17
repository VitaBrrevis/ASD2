import sys
# import matplotlib.pyplot as plt
# import numpy as np
import svit as sv
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
        nonlocal swaps
        pivot = arr[high]  # choose last element as pivot
        i = low - 1  # index of smaller element
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                swap(arr,i,j)

        swap(arr,i + 1,high)

        return i + 1

    def insertion_sort(array, left, right):
        nonlocal comparisons
        nonlocal swaps
        for i in range(left + 1, right + 1):
            key = array[i]
            j = i - 1
            while j >= left and array[j] > key:
                comparisons += 1
                array[j + 1] = array[j]
                swaps+=1
                j -= 1
            if j != left - 1:
                comparisons += 1
            array[j + 1] = key
            swaps+=1
    def quicksort(array, low, high):
        nonlocal comparisons
        nonlocal swaps
        if high - low + 1 <= 3:
            insertion_sort(array, low, high)

            sorted_array = array[low:high+1]
            return sorted_array

        else:
            median_index = (low + high) // 2

            median = sorted([array[low], array[median_index], array[high]])[1]
            median_index = array.index(median)
            swap(array, high, median_index)
            swaps += 1
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
            comparisons+=1
            while A[c] > q and b <= c:
                comparisons += 2
                if A[c] > r:
                    swap(A, c, d)
                    d = d - 1
                c = c - 1
            comparisons+=1
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

    def insertion_sort(array, left, right):
        nonlocal comparisons
        nonlocal swaps
        for i in range(left + 1, right + 1):
            key = array[i]
            j = i - 1
            while j >= left and array[j] > key:
                comparisons += 1
                array[j + 1] = array[j]
                swaps+=1
                j -= 1
            if j != left - 1:
                comparisons += 1
            array[j + 1] = key
            swaps+=1


    def quicksort(array, low, high):
            nonlocal swaps
            nonlocal comparisons
            if high - low + 1 <= 3:
                insertion_sort(array, low, high)

            else:
                if array[low] > array[low+1]:
                    swap(array, low, low+1)
                    swaps += 1
                if array[low+1] > array[high]:
                    swap(array, low + 1, high)
                    swaps += 1
                if array[low] > array[low + 1]:
                    swap(array, low, low + 1)
                    swaps += 1

                ip,iq,ir = partition(array, low, high)

                quicksort(array, low, ip - 1)
                quicksort(array, ip + 1 , iq - 1)
                quicksort(array, iq + 1, ir - 1)
                quicksort(array, ir + 1 , high)

    quicksort(array, 0, len(array) - 1),
    return array, comparisons, swaps


sys.setrecursionlimit(200000)

input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r') as f:
    n = int(f.readline().strip())
    array = [int(f.readline().strip()) for _ in range(n)]
# Run the three sorting algorithms on the input array and get comparison counts
print(array)
arr1 = array.copy()
arr2 = array.copy()
comparisons1 = 0
sorted_array1, comparisons1, swaps1 = algorithm1(array)

comparisons2 = 0
sorted_array2, comparisons2, swaps2 = algorithm2(arr1)

# comparisons3 = quicksort_3way(array, 0, len(array))
comparisons3 = 0
sorted_array3, comparisons3, swaps3 = algorithm3(arr2)
#algorithm3(arr2, 0, len(arr2) - 1)


print("comparisons1: ", comparisons1, "sorted_array1: ", sorted_array1)
print("comparisons2: ", comparisons2, "sorted_array2: ", sorted_array2)
print("comparisons3: ", comparisons3, "sorted_array3: ", arr2)

with open(output_file, 'w') as f:
     f.write(f'{comparisons1} {comparisons2} {comparisons3}')

size = 1000
arr_r = sv.create_random_array(size)

arr_r1 = arr_r.copy()
arr_r2 = arr_r.copy()
y_best1, y_worst1, y_random1 = sv.measuring_operations(size, algorithm1, arr_r)
y_best2, y_worst2, y_random2 = sv.measuring_operations(size, algorithm2, arr_r1)
y_best3, y_worst3, y_random3 = sv.measuring_operations(size, algorithm3, arr_r2)
line_labels = ["asc", "desc", "random"]
chart_labels = ["first", "second", "third"]
#sv.build_line_charts(3, "comps + swaps", 3, line_labels, chart_labels, y_best1, y_worst1, y_random1, y_best2, y_worst2, y_random2, y_best3, y_worst3, y_random3)
#sv.build_line_charts1(3, "comps + swaps", 3, line_labels, chart_labels, y_best1, y_worst1, y_random1, y_best2, y_worst2, y_random2, y_best3, y_worst3, y_random3)
