# Design a class to find the kth largest integer in a stream of values including duplicates.
# Following methods should be implemented:
# constructor(int k, int[] nums) - initializes the object given an integer k and the stream of integers nums
# int add(int val) = adds the integer val to the stream and returns the kth largest integer in the stream

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
            
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Time complexity: O(m * log k), where m is the number of elements in the stream and k is the size of the heap
# Space complexity: O(k), for the heap