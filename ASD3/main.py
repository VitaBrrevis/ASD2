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
"""""
def algorithm21(array):
    comparisons = 0
    swaps = 0

    def quicksort(array, low, high, comparisons, swaps):
        if low < high:
            if high - low + 1 <= 3:
                sorted_array = sorted(array[low:high+1])
                size = high - low + 1
                match size:
                    case 3:
                        comparisons += 3
                    case 2:
                        comparisons += 1
                return sorted_array, comparisons, swaps
            else:
                middle = (low + high) // 2
                if array[low] <= array[middle] <= array[high] or array[high] <= array[middle] <= array[low]:
                    median_index = middle
                elif array[middle] <= array[low] <= array[high] or array[high] <= array[low] <= array[middle]:
                    median_index = low
                else:
                    median_index = high
                median = array[median_index]
                array[median_index], array[high] = array[high], array[median_index]
                i = low - 1
                for j in range(low, high):
                    comparisons += 1
                    if array[j] <= median:
                        i += 1
                        array[i], array[j] = array[j], array[i]
                        swaps += 1
                i += 1
                array[i], array[high] = array[high], array[i]
                swaps += 1
                q = i
                left, comparisons, swaps = quicksort(array, low, q - 1, comparisons, swaps)
                right, comparisons, swaps = quicksort(array, q + 1, high, comparisons, swaps)
                sorted_array = left + [array[q]] + right
                return sorted_array, comparisons, swaps
        else:
            return [], comparisons, swaps


    sorted_array, comparisons, swaps = quicksort(array, 0, len(array) - 1, comparisons, swaps)
    return sorted_array, comparisons, swaps
"""""
import random

def quicksort_3way(array, p, r):
    comparisons = 0
    if r - p <= 2:
        if r - p == 2:
            if array[p] > array[r - 1]:
                array[p], array[r - 1] = array[r - 1], array[p]
                comparisons += 1
        comparisons += 1
        return comparisons

    random.seed(42)
    q1, q2, q3 = random.sample(range(p, r), 3)
    if array[q1] > array[q2]:
        array[q1], array[q2] = array[q2], array[q1]
    if array[q2] > array[q3]:
        array[q2], array[q3] = array[q3], array[q2]
    if array[q1] > array[q2]:
        array[q1], array[q2] = array[q2], array[q1]
    q2_value = array[q2]

    i = p
    j = p
    k = r - 1
    while j <= k:
        if array[j] < q2_value:
            array[i], array[j] = array[j], array[i]
            comparisons += 1
            i += 1
            j += 1
        elif array[j] > q2_value:
            array[j], array[k] = array[k], array[j]
            comparisons += 1
            k -= 1
        else:
            j += 1

    left_comparisons = quicksort_3way(array, p, i - 1)
    middle_comparisons = quicksort_3way(array, i, j - 1)
    right_comparisons = quicksort_3way(array, k + 1, r)

    return comparisons + left_comparisons + middle_comparisons + right_comparisons

def algorithm3(array):
    comparisons = 0
    swaps = 0
    def swap(arr,x, y):
        nonlocal swaps
        arr[x], arr[y] = arr[y], arr[x]
        swaps +=1

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
            comparisons += 1
            while A[c] > q and b <= c:
                comparisons += 2
                if A[c] > r:
                    swap(A, c, d)
                    d = d - 1
                c = c - 1
            comparisons += 1
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
        return A.index(p),A.index(q),A.index(r)

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

                sorted_array = array[low:high + 1]
                return sorted_array
            else:
                if array[low] > array[low+1]:
                    swap(array, low, low+1)
                if array[low+1] > array[high]:
                    swap(array, low + 1, high)

                ip,iq,ir = partition(array, low, high)

                left = quicksort(array, low, ip )
                middle = quicksort(array, ip + 1 , iq)
                right = quicksort(array, iq + 1 , high)
                sorted_array = (left if left is not None else [])\
                               + (middle if middle is not None else []) + \
                               ( right if right is not None else [])
                return sorted_array

    # sorted_array = list(array)
    sorted_array = quicksort(array, 0, len(array) - 1),
    return sorted_array,comparisons, swaps


#def algorithm3(array):
 #   comparisons = quicksort(array, 0, len(array) - 1)
  #  sorted_array = array
   # return sorted_array, comparisons

sys.setrecursionlimit(200000)

input_file = "data.txt"
#output_file = sys.argv[2]
with open(input_file, 'r') as f:
    n = int(f.readline().strip())
    array = [int(f.readline().strip()) for _ in range(n)]
# Run the three sorting algorithms on the input array and get comparison counts

comparisons1 = 0
sorted_array1, comparisons1, swaps1 = algorithm1(array)

comparisons2 = 0
sorted_array2, comparisons2, swaps2 = algorithm2(array)

# comparisons3 = quicksort_3way(array, 0, len(array))
comparisons3 = 0
sorted_array3, comparisons3, swaps3 = algorithm2(array)


print("comparisons1: ", comparisons1, "sorted_array1: ", sorted_array1)
print("comparisons2: ", comparisons2, "sorted_array2: ", sorted_array2)
print("comparisons3: ", comparisons3, "sorted_array3: ", sorted_array3)
#comparisons3 = 0
#sorted_array3, comparisons3 = algorithm3(array)

#Write output to file
# with open(output_file, 'w') as f:
#      f.write(f'{comparisons1} {comparisons2} {comparisons3}')
"""""
size = 500
arr_r = sv.create_random_array(size)

arr_r1 = arr_r.copy()
y_best1, y_worst1, y_random1 = sv.measuring_operations(size, algorithm1, arr_r);
y_best2, y_worst2, y_random2 = sv.measuring_operations(size, algorithm21, arr_r1);
line_labels = ["best", "worst", "random"]
chart_labels = ["first", "second"]
sv.build_line_charts(2, "comps", 3, line_labels, chart_labels, y_best1, y_worst1, y_random1, y_best2, y_worst2, y_random2)
"""