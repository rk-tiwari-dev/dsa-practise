def findmissingnumber(arr):
    n = len(arr)
    total = (n + 1) * (n + 2) / 2
    sum_of_arr = sum(arr)
    return total - sum_of_arr


print(findmissingnumber([1, 2, 3, 4, 5, 6, 7, 8, 10]))  # 9
print(findmissingnumber([1, 2, 3, 4, 5, 6, 8, 9, 10]))  # 7
print(findmissingnumber([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 10
