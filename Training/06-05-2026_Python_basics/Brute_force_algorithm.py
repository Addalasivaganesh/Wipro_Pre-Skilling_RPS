
def find_max(arr):
    max_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num

    return max_num
print(find_max([2, 4, 7, 9, 12, 23, 34, 45, 56, 67, 78, 89,99]))