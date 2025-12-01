arr = [(101, 85), (102, 70), (103, 95)]
def bubble_sort_tuples_primary(arr):
    n = len(arr)
    for j in range(n):
        for i in range(n - 1):
            if arr[i][1] < arr[i + 1][1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

print(bubble_sort_tuples_primary(arr))