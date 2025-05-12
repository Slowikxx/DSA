# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land)
# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
# The area of an island is defined as the number of cells within the island
# Return the maximum area of an sland in grid. If no island exists, return 0

from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    
    def dfs(r, c):
        if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
            return 0
        
        visit.add((r,c))
        
        return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
    
    area = 0
    for r in range(ROWS):
        for c in range(COLS):
            area = max(area, dfs(r, c))
    
    return area

# Test case
grid = grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

print(maxAreaOfIsland(grid)) # Expected output: 6

# Time complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid
# Space complexity: O(m * n)