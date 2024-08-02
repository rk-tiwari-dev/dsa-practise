def zigzagConversion(n, s, rows):
    if rows == 1 or rows >= n:
        return s

    # Create a list for each row
    zigzag = ["" for _ in range(rows)]
    current_row = 0
    going_down = False

    for char in s:
        zigzag[current_row] += char
        if current_row == 0 or current_row == rows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    # Join all rows to form the final result
    result = "".join(zigzag)
    return result
