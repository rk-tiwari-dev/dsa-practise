"""Partitioning an array means to split an array along an element, 
such that it divides the array into two parts with some specific property.
The element that partitions the array is called the partitioning element.
Given an array, find the element, partitioning along which, the sum of elements to its left, 
equals the sum of elements to its right. The partition element itself is to be excluded from both sums.
Return the index of the partitioning element. If no such element exists, return -1.
Input format
There are N+1 lines of input.

First line will contain a single integer N.

Second line will contain n space separated integer representing array elements.

Output format
Output the index of the partitioning element.

Constraints
2 <= N <= 10^6

1 <= Arr[i] <= 10^9

Sample Input 1
4

1 4 2 5

Sample Output 1
2

Explanation 1
Since 1 + 4 = 5 where 2 is such an element."""

# https://www.geeksforgeeks.org/find-element-array-sum-left-array-equal-sum-right-array/


# Python 3 Program to find an element
# such that sum of right side element
# is equal to sum of left side


# Function for Finds an element in
# an array such that left and right
# side sums are equal
def findElement(arr, n):

    # Forming prefix sum array from 0
    prefixSum = [0] * n
    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

    # Forming suffix sum array from n-1
    suffixSum = [0] * n
    suffixSum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffixSum[i] = suffixSum[i + 1] + arr[i]

    # Find the point where prefix
    # and suffix sums are same.
    for i in range(1, n - 1, 1):
        if prefixSum[i] == suffixSum[i]:
            return arr[i]

    return -1


# Driver Code
if __name__ == "__main__":

    arr = [1, 4, 2, 5]
    n = len(arr)
    print(findElement(arr, n))

# This code is contributed by ANKITRAI1

# Time complexity: O(n)
# Space complexity: O(n)
# n is the length of the array
# This algorithm is similar to the
# ArrayPrefixSum/FindEqualPartionsArray.py


"""
2nd approch 

def findElement(arr, n):
    for i in range(1, n):
        leftSum = sum(arr[0:i])
        rightSum = sum(arr[i+1:])
        if(leftSum == rightSum):
            return arr[i]
    return -1
    
    """
"""
3rd approch
# Python 3 Program to find an element 
# such that sum of right side element 
# is equal to sum of left side

# Function to compute partition
def findElement(arr, size) :

	right_sum, left_sum = 0, 0

	# Computing right_sum
	for i in range(1, size) :
		right_sum += arr[i]

	i, j = 0, 1

	# Checking the point of partition 
	# i.e. left_Sum == right_sum 
	while j < size :
		right_sum -= arr[j]
		left_sum += arr[i]

		if left_sum == right_sum :
			return arr[i + 1]

		j += 1
		i += 1

	return -1

# Driver Code
if __name__ == "__main__" :
	
	arr = [ 2, 3, 4, 1, 4, 5]
	n = len(arr)
	print(findElement(arr, n))

"""

# Single pass solution
"""
def findElement(arr, n):
    # Initialize sums of left and right
    left_sum = 0
    total_sum = sum(arr)
    
    for i in range(n):
        # Update right_sum by subtracting the current element
        total_sum -= arr[i]
        
        # If left_sum is equal to right_sum, we found the element
        if left_sum == total_sum:
            return arr[i]
        
        # Update left_sum for next iteration
        left_sum += arr[i]
        
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [1, 4, 2, 5]
    n = len(arr)
    print(findElement(arr, n))

"""
