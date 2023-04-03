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

    def quicksort(array, low, high):
        nonlocal comparisons
        if high - low + 1 <= 3:  # sort subarrays of size 3 or less without partitioning
            sorted_array = sorted(array[low:high+1])
            size = high - low + 1
            match size:
                case 3:
                    comparisons += 3
                case 2:
                    comparisons += 1
            return sorted_array
        else:
            median_index = (low + high) // 2
            median = sorted([array[low], array[median_index], array[high]])[1]
            median_index = array.index(median)
            """

            array[high], array[median_index] = array[median_index], array[high]
            array, comparisons = algorithm1(array)
            """
            i = low - 1
            for j in range(low, high + 1):
                if array[j] != array[median_index]:
                    comparisons += 1
                if array[j] <= median:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            median_index = array.index(median)
            array[i], array[median_index] = array[median_index], array[i]
            q = i
            left = quicksort(array, low, q - 1 )
            right = quicksort(array, q + 1, high)
            sorted_array = ( left if left is not None else [] ) + [array[q]]+ ( right if right is not None else [] )
            return sorted_array


    sorted_array = quicksort(array, 0, len(array) - 1)
    return sorted_array, comparisons

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
sorted_array1, comparisons1 = algorithm1(array)

comparisons2 = 0
sorted_array2, comparisons2 = algorithm21(array)

#comparisons3 = 0
#sorted_array3, comparisons3 = algorithm3(array)

# Write output to file
with open(output_file, 'w') as f:
    f.write(f'{comparisons1} {comparisons2} ')
