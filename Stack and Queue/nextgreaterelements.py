# to get next greater elements in an array

arr = [1, 3, 2, 4]

result = []
stack = []

for i in range(len(arr)):
    # Pop elements from the stack while the top of the stack is less than or equal to the current element
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    # If stack is not empty, the top of the stack is the next greater element
    if stack:
        result.append(stack[-1])
    else:
        result.append(-1)
    # Push the current element onto the stack
    stack.append(arr[i])

print(result)
# Output: [-1, 4, 4, -1]

# explanation:
# We iterate the array from right to left. We keep a stack that stores the elements we have seen so far.
# We pop elements from the stack until the top element is greater than the current element or the stack is empty.
# If the stack is not empty, the next greater element is the top element of the stack.
# Otherwise, there is no next greater element, so we append -1 to the result.
# Finally, we push the current element onto the stack.
# The result is the reverse of the list we built.
# The time complexity is O(n) because we iterate the array once.
# The space complexity is O(n) because the stack can contain at most n elements.
# where n is the number of elements in the array.
