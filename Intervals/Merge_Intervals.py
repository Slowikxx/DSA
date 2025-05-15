# Given an array of intervals where intervals[i] = [start_i, end_i] merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Intervals are non-overlapping if they have no common point

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    max_val = max(interval[0] for interval in intervals)
    
    mp = [0] * (max_val + 1)
    for start, end in intervals:
        mp[start] = max(end + 1, mp[start])
    
    res = []
    have = -1
    interval_start = -1
    for i in range(len(mp)):
        if mp[i] != 0:
            if interval_start == -1:
                interval_start = i
            have = max(mp[i] - 1, have)
        if have == i:
            res.append([interval_start, have])
            have = -1
            interval_start = -1
    
    if interval_start != -1:
        res.append([interval_start, have])
    
    return res

# Test cases
intervals1 = [[1,3], [1,5], [6,7]]
intervals2 = [[1,2], [2,3]]

print(merge(intervals1)) # Expected output: [[1,5],[6,7]]
print(merge(intervals2)) # Expected output: [[1,3]]

# Time complexity: O(n + m), where n is the length of the array and m is the maximm start value among all the intervals
# Space complexity: O(n)