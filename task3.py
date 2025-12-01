
arr = ["Melon", "Apple", "Zebra", "Grape"]
def selection_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j].lower() < arr[min_index].lower():
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort_strings(arr))