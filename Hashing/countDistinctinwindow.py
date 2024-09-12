def countDistinct(arr, n, k):
    d = {}
    counter = 0
    res = []

    for i in range(n):
        # Add the new element to the window
        if arr[i] not in d:
            d[arr[i]] = 1
            counter += 1
        else:
            d[arr[i]] += 1

        # Remove the old element from the window if the window size exceeds k
        if i >= k:
            element_to_remove = arr[i - k]
            d[element_to_remove] -= 1
            if d[element_to_remove] == 0:
                del d[element_to_remove]
                counter -= 1

        # Add the result to the list if the window size is at least k
        if i >= k - 1:
            res.append(counter)

    return res


# Test cases
print(countDistinct([1, 2, 1, 3, 4, 2, 3], 7, 4))
print(countDistinct([1, 2, 4, 4], 4, 2))
print(countDistinct([1, 2, 1, 3, 4, 2, 3], 7, 3))
