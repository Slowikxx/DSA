# You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase
# After paying the cost you can step either to the (i+1)th floor or the (i+2)th floor
# Return the minimum cost to reach the top of the staircase

from typing import List


def minCostCimbingStairs(cost: List[int]) -> int:
    cost.append(0)
    
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
        
    return min(cost[0], cost[1])

# Test cases
cost1 = [1,2,3]
cost2 = [1,2,1,2,1,1,1]

print(minCostCimbingStairs(cost1))  # Expected output: 2
print(minCostCimbingStairs(cost2))  # Expected output: 4

# Time complexity: O(n), where n is the length of the cost array
# Space complexity: O(1)