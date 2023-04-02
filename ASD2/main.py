import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_split = merge(left, right)
    return merged, (inv_left + inv_right + inv_split)

def merge(left, right):
    i = j = 0
    inv = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += (len(left) - i)
    merged += left[i:]
    merged += right[j:]
    return merged, inv

def sort_and_apply_order(arr1, arr2):
    sorted_indices = sorted(range(len(arr1)), key=lambda k: arr1[k])
    arr1_sorted = [arr1[i] for i in sorted_indices]
    arr2_sorted = [arr2[sorted_indices[i]] for i in range(len(arr2))]
    return arr1_sorted, arr2_sorted

input_file = sys.argv[1]
output_file = sys.argv[2]
x = int(sys.argv[3])

with open(input_file, 'r') as f:
    u, m = map(int, f.readline().split())
    D = [[] for _ in range(u)]
    for line in f:
        row = list(map(int, line.split()))
        D[row[0] - 1] = row[1:]
B = [[] for _ in range(u)]
similarity = {}

B = [[D[i][D[x-1].index(j+1)] for j in range(m)] for i in range(u)]

for i in range(u):
    if i != x - 1:
        _, similarity[i+1] = merge_sort(B[i])

with open(output_file, 'w') as f:
    f.write(str(x) + '\n')
    for i, c in sorted(similarity.items(), key=lambda x: x[1]):
        if i != x:
            f.write(str(i) + ' ' + str(c) + '\n')

