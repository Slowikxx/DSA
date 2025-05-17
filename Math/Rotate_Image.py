# Given a square n x n matrix of integers rotate it by 90 degrees clockwise
# You must rotate the matrix in-place. DO not allocate another 2D matrix and do the rotation

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    l, r = 0, len(matrix) - 1
    
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topLeft = matrix[top][l+i]
            
            matrix[top][l+i] = matrix[bottom-i][l]
            matrix[bottom-i][l] = matrix[bottom][r-i]
            matrix[bottom][r-i] = matrix[top+i][r]
            matrix[top+i][r] = topLeft
    
        r -= 1
        l += 1

# Test cases
matrix1 = [
    [1,2],
    [3,4]
]
matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotate(matrix1)
rotate(matrix2)
print(matrix1) # Expected output: [[3,1], [4,2]]
print(matrix2) # Expected output: [[7,4,1], [8,5,2], [9,6,3]]

# Time complexity: O(n^2), where n is the number of rows in the matrix
# Space complexity: O(1)