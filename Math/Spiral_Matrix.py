# Given an m x n matrix of integers return a list of all elements within the matrix in spiral order

from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1
        
        if not (left < right and top < bottom):
            break
        
        for i in range(right - 1, left -1 , -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1
    
    return res

# Test cases
matrix1 = [[1,2], [3,4]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
matrix3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(spiralOrder(matrix1)) # Expected output: [1,2,4,3]
print(spiralOrder(matrix2)) # Expected output: [1,2,3,6,9,8,7,4,5]
print(spiralOrder(matrix3)) # Expected output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Time complexity: O(m * n), where m is the number of rows and n is the number of columns
# Space complexity: O(1) extra space, O(m*n) space for the output