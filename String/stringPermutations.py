"""Problem Description
You are given a string, you have to rearrange the characters of the string using a given permutation.

The permutation is in the form of an integer array with size same as that of string in which each integer specifies the new position of the character currently present at that particular place.

For eg. consider the string "abcd" and permutation [2,4,3,1], then the new string will be "dacb".

Input format
First line contains an integer n - The length of string.

Second line contains a string - The given string

Third line contains n space separated integers - The permutation.

Output format
Print the new string after applying the permutation.

Sample Input 1
4

abcd

2 4 3 1

Sample Output 1
dacb

Explanation
According to the permutation 'a' goes to position 2, 'b' to 4, 'c' to 3, 'd' to 1. So we get the new string as "dacb"."""
### https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/
def stringPermutation(n: int, s: str, per: List[int]) -> str:
    new_string = [""] * n

    # Rearrange the characters based on the permutation
    for i in range(n):
        new_position = per[i] - 1  # convert to 0-based index
        new_string[new_position] = s[i]

    # Convert the list back to a string
    result = "".join(new_string)
    return result
