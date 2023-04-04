import sys
import matplotlib.pyplot as plt
import numpy as np
import svit as sv
import random
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

"""
def insertion_sort(array, low, high, counts):
    for i in range(low+1, high+1):
        key = array[i]
        j = i-1
        while j >= low and key < array[j]:
            array[j+1] = array[j]
            j -= 1
            counts += 1
        array[j+1] = key
    return counts

def algorithm2(array):
    def partition(array, low, high, counts):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            counts[0] += 1
            if array[j] <= pivot:
                counts[1] += 1
                i += 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quick_sort_median(array, low, high, counts):
        if high - low > 2:
            n = high - low + 1
            pivot_idx = median_of_three(array, low, low + n // 2, high)
            array[pivot_idx], array[high] = array[high], array[pivot_idx]
            q = partition(array, low, high, counts)
            quick_sort_median(array, low, q - 1, counts)
            quick_sort_median(array, q + 1, high, counts)
        else:
            insertion_sort(array, low, high, counts)

    def median_of_three(array, a, b, c):
        if array[a] < array[b]:
            if array[b] < array[c]:
                return b
            elif array[a] < array[c]:
                return c
            else:
                return a
        else:
            if array[a] < array[c]:
                return a
            elif array[b] < array[c]:
                return c
            else:
                return b
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

def quicksort_3way(array, p, r):
    comparisons = 0
    if r - p <= 2:
        if r - p == 2:
            if array[p] > array[r - 1]:
                array[p], array[r - 1] = array[r - 1], array[p]
                comparisons += 1
        comparisons += 1
        return comparisons

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


#def algorithm3(array):
 #   comparisons = quicksort(array, 0, len(array) - 1)
  #  sorted_array = array
   # return sorted_array, comparisons

input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r') as f:
    n = int(f.readline().strip())
    array = [int(f.readline().strip()) for _ in range(n)]
# Run the three sorting algorithms on the input array and get comparison counts
comparisons1 = 0
sorted_array1, comparisons1, swaps1 = algorithm1(array)

comparisons2 = 0
sorted_array2, comparisons2, swaps2 = algorithm21(array)

comparisons3 = quicksort_3way(array, 0, len(array))

print (sorted_array1)
print (sorted_array2)
#print (sorted_array3)
#comparisons3 = 0
#sorted_array3, comparisons3 = algorithm3(array)

# Write output to file
with open(output_file, 'w') as f:
    f.write(f'{comparisons1} {comparisons2} {comparisons3}')
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