# You are given an array of integers stones where stones[i] represents the weight of ith stone.
# We want to run a simulation on the stones as follows:
# At each step we choose two heaviest stones with weight x and y and smash them togethers
# if x == y both stones are destroyed
# if x < y the stone of weight x is destroyed and the stone of weight y has new weight y - x
# Continue until there is no more than one stone left. Return the weight of the last remaining stone or return 0 if none remain

import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)
    
    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        
        if second > first:
            heapq.heappush(stones, first - second)
    
    stones.append(0)
    return abs(stones[0])

# Test cases
stones1 = [2,3,6,2,4]
stones2 = [1,2]

print(lastStoneWeight(stones1))  # Expected output: 1
print(lastStoneWeight(stones2))  # Expected output: 1

# Time complexity: O(n log n), where n is the number of stones
# Space complexity: O(n), for the heap
