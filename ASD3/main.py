import sys
def algorithm1(array):
    # Quicksort algorithm
    comparisons = 0

    def partition(arr, low, high):
        nonlocal comparisons
        pivot = arr[high]  # choose last element as pivot
        i = low - 1  # index of smaller element
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quicksort(arr, low, pivot_index - 1)
            quicksort(arr, pivot_index + 1, high)

    sorted_array = list(array)  # make a copy of the original array
    quicksort(sorted_array, 0, len(array) - 1)
    return sorted_array, comparisons


def algorithm2(array):
    comparisons = 0

    def quicksort(array, p, r):
        nonlocal comparisons
        if p < r:
            if r - p + 1 <= 3:  # sort subarrays of size 3 or less without partitioning
                comparisons += 3
                sorted_array = sorted(array[p:r+1])
                return sorted_array
            else:
                comparisons += 3
                median_index = (p + r) // 2
                median = sorted([array[p], array[median_index], array[r]])[1]
                i = p - 1
                for j in range(p, r):
                    comparisons += 1
                    if array[j] <= median:
                        i += 1
                        array[i], array[j] = array[j], array[i]
                array[i+1], array[r] = array[r], array[i+1]
                q = i + 1
                left = quicksort(array, p, q - 1)
                right = quicksort(array, q + 1, r)
                sorted_array = left + [array[q]] + right
                return sorted_array

    sorted_array = quicksort(array, 0, len(array) - 1)
    return sorted_array, comparisons


def partition(array, p, r):
    # Choose three pivot elements
    q1 = p
    q2 = (p + r) // 2
    q3 = r

    # Sort pivot elements
    if array[q1] > array[q2]:
        array[q1], array[q2] = array[q2], array[q1]
    if array[q2] > array[q3]:
        array[q2], array[q3] = array[q3], array[q2]
    if array[q1] > array[q2]:
        array[q1], array[q2] = array[q2], array[q1]

    # Partition array
    i = j = p
    k = r
    comparisons = 0
    while j <= k:
        if array[j] < array[q1]:
            array[i], array[j] = array[j], array[i]
            i += 1
            j += 1
            comparisons += 1
        elif array[j] >= array[q1] and array[j] < array[q2]:
            j += 1
            comparisons += 1
        elif array[j] >= array[q2] and array[j] < array[q3]:
            array[j], array[k] = array[k], array[j]
            k -= 1
            comparisons += 1
        else:
            array[k], array[j] = array[j], array[k]
            k -= 1
            j -= 1
            comparisons += 1

    return i, j, comparisons


def quicksort(array, p, r):
    comparisons = 0
    if p < r:
        i, j, comparisons = partition(array, p, r)
        comparisons += quicksort(array, p, i - 1)
        comparisons += quicksort(array, j, r)
    return comparisons


def algorithm3(array):
    comparisons = quicksort(array, 0, len(array) - 1)
    sorted_array = array
    return sorted_array, comparisons

input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r') as f:
    n = int(f.readline().strip())
    array = [int(f.readline().strip()) for _ in range(n)]

# Run the three sorting algorithms on the input array and get comparison counts
comparisons1 = 0
sorted_array1, comparisons1 = algorithm1(array)

comparisons2 = 0
sorted_array2, comparisons2 = algorithm2(array)

#comparisons3 = 0
#sorted_array3, comparisons3 = algorithm3(array)

# Write output to file
with open(output_file, 'w') as f:
    f.write(f'{comparisons1} {comparisons2} ')
