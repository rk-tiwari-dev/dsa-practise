arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]

def mergeTwoSortedArray(arr1, arr2):
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i < len(arr1):
        res.append(arr1[i])
        i += 1
    while j < len(arr2):
        res.append(arr2[j])
        j += 1
    return res

print(mergeTwoSortedArray(arr1, arr2))

# Time complexity: O(n+m)
# Space complexity: O(n+m)
# n is the length of arr1 and m is the length of arr2
    