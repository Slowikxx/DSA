# You are given an m x n 2D integer array matrix and an integer target
# - each row in matrix is sorted in non-decreasing order
# - the first integer of every row is grater than the last integer of the previous row
# Return true if target exists within the matrix or false otherwise

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    
    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
        
    if not (top <= bot):
        return False
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    
    return False

# Test cases:
matrix1 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target1 = 10
matrix2 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target2 = 15

print(searchMatrix(matrix1, target1)) # Expected output: True
print(searchMatrix(matrix2, target2)) # Expected output: False

# Time complexity: O(logn + logm) = O(log(n * m)), where n is the number of rows and m is the number of columns in the matrix
# Space complexity: O(1)