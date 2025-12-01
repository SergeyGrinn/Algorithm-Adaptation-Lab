arr = [5, -2, 8, -5, 10, 0, -10]
def separate_neg_pos(arr):
    left = []
    right = []
    for num in arr:
        if num < 0:
            left.append(num)
        else:
            right.append(num)
    return left + right

print(separate_neg_pos(arr))