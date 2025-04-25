# You are given a 2D integer array intervals where intervals[i] = [left_i, right_i] represents the ith interval starting at left_i and ending at right_i (inclusive)
# You are also given an integer array of query points queries. The result of query[j] is the length of the shortest interval i such that left_i <= queries[j] <= riight_i.
# If no such interval exists the result of this query is -1

# Return an array output where iutput[j] is the result of query[j]
# The length of an interval is calculated as right_i - left_i + 1

import heapq
from typing import List


def minInterval(intervals: List[int], queries: List[int]) -> List[int]:
    intervals.sort()
    minHeap = []
    res, i = {}, 0
    
    for q in sorted(queries):
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(minHeap, (r - l + 1, r))
            i += 1
            
        while minHeap and minHeap[0][1] < q:
            heapq.heappop(minHeap)
        res[q] = minHeap[0][0] if minHeap else -1
        
    return [ res[q] for q in queries ]    
# Test case
intervals = [[1,3],[2,3],[3,7],[6,6]]
queries = [2,3,1,7,6,8]

print(minInterval(intervals, queries)) # Expected output [2,2,3,5,1,-1]

# Time complexity: O(nlogn + mlogm), where n is the length of intervals and m is the length of queries
# Space complexity: O(n + m)