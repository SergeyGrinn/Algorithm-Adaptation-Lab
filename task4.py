arr = ["Melon", "Apple", "Zebra", "Grape"]
def insertion_sort_desc_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j].lower() < key.lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(insertion_sort_desc_strings(arr))

 