# Given a 2D grif grid where '1' represents land and '0' represets water count and return the number of islands.
# An island is formed by connecting adjacent leads horizontally or vertically and is surrounded by water.
# You may assume water is surrounding the grid (i.e. all the edges are water)

from typing import List

def numIslands(grid: List[List[str]]) -> int:
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    ROWS, COLS = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r,c):
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0'):
            return
        
        grid[r][c] = "0"
        for dr, dc in directions:
            dfs(r + dr, c + dc)
        
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                dfs(r, c)
                islands += 1
    
    return islands

# Test cases
grid1 =[
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

grid2 = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(numIslands(grid1)) # Expected output: 1
print(numIslands(grid2)) # Expected output: 4

# Time complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid
# Space complexity: O(m * n)