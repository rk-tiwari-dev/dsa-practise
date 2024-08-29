class Stack:
    def __init__(self):
        self.items = []
        self.size = 0  # Keep track of the stack size

    def push(self, item):
        """Push an item onto the stack."""
        self.items[self.size : self.size] = [item]  # Insert item at the end
        self.size += 1

    def pop(self):
        """Remove and return the top item from the stack. Raises an exception if the stack is empty."""
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        top_item = self.items[self.size - 1]  # Get the last item
        self.items = self.items[: self.size - 1]  # Remove the last item
        self.size -= 1
        return top_item

    def top(self):
        """Return the top item of the stack without removing it. Raises an exception if the stack is empty."""
        if self.isEmpty():
            raise IndexError("top from empty stack")
        return self.items[self.size - 1]

    def isEmpty(self):
        """Check if the stack is empty."""
        return self.size == 0


stack = Stack()

# Push an item onto the stack
stack.push(1)

# Print the contents of the stack
print(stack.items)  # Output: [1]


# time complexity: O(1)
# space complexity: O(n)
# where n is the number of items in the stack
