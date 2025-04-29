# You are given a 2-D grid of integers matrix where each integer is greater than or equal to 0.
# Return the length of the longest strictly increasing path within matrix
# From each cell within the path, you can move either horizontally or vertically. You may not move diagonally

from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = {}
    
    def dfs(r, c, prevVal):
        if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal):
            return 0
        if (r, c) in dp:
            return dp[(r,c)]
        
        res = 1
        res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
        res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
        dp[(r, c)] = res
        return res
    
    for r in range(ROWS):
        for c in range(COLS):
            dfs(r,c,-1)
    
    return max(dp.values())

# Test cases:
matrix1 = [[5,5,3],[2,3,6],[1,1,1]]
matrix2 = [[1,2,3],[2,1,4],[7,6,5]]

print(longestIncreasingPath(matrix1)) # Expected output: 4
print(longestIncreasingPath(matrix2)) # Expected output: 7

# Time complexity: O(n * m), where n is the number of rows and m is the number of columns in the given matrix
# Space complexity: O(n * m)