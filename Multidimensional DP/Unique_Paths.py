# There is an m x n grid where you are allowed to move either down or to the right at any point in time
# Given the two integers m and n return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m-1][n-1])

def uniquePaths(m: int, n: int) -> int:
    row = [1] * n
    
    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1, -1):
            newRow[j] = newRow[j+1] + row[j]
        row = newRow
    
    return row[0]

# Test cases
m1 = 3
n1 = 6
m2 = 3
n2 = 3

print(uniquePaths(m1, n1)) # Expected output: 21
print(uniquePaths(m2,n2)) # Expected output: 6

# Time complexity: O(m * n), where m is the number of rows and n is the number of columns
# Space complexity: O(n)