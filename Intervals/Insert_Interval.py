# You are given an array of non-overlapping intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. Intervals is initially sorted in ascending order by start_i.
# You are given another interval newInterval = [start, end]
# Insert newInterval into intervals such that intervals is stll sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed
# Return intervals after adding newInterval

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
    res.append(newInterval)
    return res
    
# Test cases:
intervals1 = [[1,3],[4,6]]
newInterval1 = [2,5]
intervals2 = [[1,2],[3,5],[9,10]]
newInterval2 = [6,7]

print(insert(intervals1, newInterval1)) # Expected output: [[1,6]]
print(insert(intervals2, newInterval2)) # Expected output: [[1,2],[3,5],[6,7], [9,10]]

# Time complexity: O(n), where n is the length of intervals
# Space complexity: O(1) extra space and O(n) space for the output list