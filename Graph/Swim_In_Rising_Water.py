# You are given a square 2-D matrix of  distinct integers grid where each integer grid[i][j] represents the elevatiion at position (i,j)
# Rain starts to fall at time = 0 which causes the water level to rise. At time t whe water level across the entire grid is t.
# You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t
# Starting from the top left square (0,0) return the minimum amount of time it will take until it is possible to reach the bottom right square (n-1, n-1)

import heapq
from typing import List


def swimInWater(grid: List[List[int]]) -> int:
    N = len(grid)
    visit = set()
    minHeap = [[grid[0][0],0,0]]
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    
    visit.add((0,0,))
    
    while minHeap:
        t, r, c = heapq.heappop(minHeap)
        
        if r == N - 1 and c == N - 1:
            return t
        for dr, dc in directions:
            neiR, neiC = r + dr, c + dc
            if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                continue
            
            visit.add((neiR, neiC))
            heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])

# Test cases:
grid1 = [[0,1], [2,3]]
grid2 = [[0,1,2,10],[9,14,4,13], [12,3,8,15], [11,5,7,6]]

print(swimInWater(grid1)) # Expected output: 3
print(swimInWater(grid2)) # Expected output: 8

# Time complexity: O(n^2logn)
# Space complexity: O(n^2)