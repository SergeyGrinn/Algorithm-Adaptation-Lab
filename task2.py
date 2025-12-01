arr = [5, 1, 4, 2, 8]
def bubble_sort_count(arr):
    n = len(arr)
    swaps = 0
    for j in range(n-1):
        for i in range(n-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
    return swaps
print(bubble_sort_count(arr))