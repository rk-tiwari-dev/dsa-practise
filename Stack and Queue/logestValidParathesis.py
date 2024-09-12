def longest_valid_parentheses(s):
    stack = [-1]  # Initialize stack with -1 to handle base case
    max_length = 0

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)  # Push the index of '('
        else:  # char == ')'
            if stack:
                stack.pop()  # Pop the last unmatched '(' index
                if stack:
                    # Current valid substring length
                    max_length = max(max_length, i - stack[-1])
                else:
                    # Stack empty after pop, push current index as base
                    stack.append(i)

    return max_length


print(longest_valid_parentheses("(()"))  # 2