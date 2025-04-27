# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.
# A queen in a chessboard can attack horizontally, vertically and diagonally
# Given an integer n return all distinct solutions to the n-queens puzzle
# Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space
# You may return the answer in any order

from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    col = set()
    posDiag = set()
    negDiag = set()
    
    res = []
    board = [["."] * n for i in range(n)]
    
    def backtrack(row):
        if row == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (row + c) in posDiag or (row - c) in negDiag:
                continue
            
            col.add(c)
            posDiag.add(row + c)
            negDiag.add(row - c)
            board[row][c] = "Q"
            
            backtrack(row + 1)
            
            col.remove(c)
            posDiag.remove(row + c)
            negDiag.remove(row - c)
            board[row][c] = "."
    backtrack(0)
    return res

# Test cases
n1 = 4
n2 = 1

print(solveNQueens(n1)) # Expected output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solveNQueens(n2)) # Expected output: [["Q"]]

# Time complexity: O(n!)
# Space complexity: O(n^2)