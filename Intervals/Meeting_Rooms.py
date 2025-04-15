# Given an array of meeting time interval objects consisting of start and end times determine if a person could add all meetings to their schedule withouth any conflicts

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def canAttendMeetings(intervals: List[Interval]) -> bool:
    intervals.sort(key= lambda i : i.start)
    
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i-1].end:
            return False
    
    return True

# Test cases

intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
intervals2 = [Interval(5,8), Interval(9,15)]
intervals3 = [Interval(0, 8), Interval(8,10)]

print(canAttendMeetings(intervals1))  # Expected output: False
print(canAttendMeetings(intervals2))  # Expected output: True
print(canAttendMeetings(intervals3))  # Expected output: True

# Time complexity: O(n log n), n is the number of intervals, we are sorting
# Space complexity: O(1)