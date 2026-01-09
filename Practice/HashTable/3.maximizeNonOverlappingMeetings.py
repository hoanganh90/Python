def maximizeNonOverlappingMeetings(meetings):
    # Write your code here
    meetings.sort(key=lambda x: (x[1], -x[0]))
    count = 1
    for i in range(len(meetings)-1):
        if meetings[i+1][0] >= meetings[i][1]:
            count += 1
    return count
print(maximizeNonOverlappingMeetings([[0, 5], [0, 1], [1, 2], [2, 3], [3, 5], [4, 6]]))