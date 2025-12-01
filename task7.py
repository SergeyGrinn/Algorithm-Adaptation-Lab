arr = [("Latvia", 300), ("Lithuania", 100), ("Latvia", 200)]
def bubble_sort_tuples_secondary(arr):
    n = len(arr)
    for j in range(n):
        for i in range(n - 1):
            country1, price1 = arr[i]
            country2, price2 = arr[i + 1]
            
            if country1 > country2 or (country1 == country2 and price1 > price2):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

print(bubble_sort_tuples_secondary(arr))