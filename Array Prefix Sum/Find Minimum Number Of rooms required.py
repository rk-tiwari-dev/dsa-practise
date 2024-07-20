"""Problem Description
Given a list of meeting time intervals, you have to find the minimum number of rooms required to organize all the meetings.
Input format
First line contains an integer N, indicating the number of meetings.
Next N lines contain two space separated integers S and E, indicating the Starting and Ending time of a meeting, respectively.
Output format
Print the minimum number of rooms required.
Constraints
N <= 100000
0 <= S,E <= 1000000000 (10^9)
Si < Ei
Sample Input 1

0 20
5 10
10 15
Sample Output 1
2"""

from typing import List


arr = [[0, 20], [5, 10], [10, 15]]


def meetingRooms(lectures: List[List[int]]) -> int:

    Time = []
    for i in range(len(lectures)):
        Time.append((lectures[i][0], 1))  # 1 for start time here it is 0
        Time.append((lectures[i][1], -1))  # -1 for end time here it is 21
        print("Time is ", Time)
    Time.sort(key=lambda x: x[0])
    print("sorted array of time ", Time)
    answer = 0
    sum = 0

    for i in range(len(Time)):
        sum += Time[i][1]
        answer = max(answer, sum)

    return answer


print(meetingRooms(arr))
# Time complexity: O(nlogn)
# Space complexity: O(1)
