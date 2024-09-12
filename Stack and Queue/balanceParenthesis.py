def areBracketsBalanced(s: str) -> str:
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in bracket_map.values():
            # If it's an opening bracket, push onto the stack
            stack.append(char)
        elif char in bracket_map:
            # If it's a closing bracket, check if it matches the top of the stack
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return "false"

    # If stack is empty, all opening brackets were properly closed
    return "true" if not stack else "false"
