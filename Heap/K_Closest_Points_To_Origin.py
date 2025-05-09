# You are given a 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are given an integer k.
# Return the k closest points to the origin (0,0).
# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2))

import heapq
from typing import List

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    minHeap = []
    for x, y in points:
        dist = (x**2) + (y**2)
        minHeap.append([dist,x,y])
    
    heapq.heapify(minHeap)
    res = []
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x,y])
        k -= 1
    
    return res

# Test cases
points1 = [[0,2],[2,2]]
k1 = 1
points2 = [[0,2],[2,0],[2,2]]
k2 = 2

print(kClosest(points1, k1)) # Expected output: [[0,2]]
print(kClosest(points2, k2)) # Expected output: [[0,2], [2,0]]

# Time complexity: O(k * logn), where n is the length of the array points
# Space complexity: O(n)