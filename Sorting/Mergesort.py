def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


# Example usage
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", array)
    sorted_array = merge_sort(array)
    print("Sorted array:", sorted_array)
