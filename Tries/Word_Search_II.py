# Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.
# For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells.
# The same cell may not be used more than once in a word.

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    
    for w in words:
        root.addWord(w)
    
    ROWS, COLS = len(board), len(board[0])
    res, visit = set(), set()
    
    def dfs(r, c, node, word):
        if (r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children):
            return
        visit.add((r,c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.isWord:
            res.add(word)
        
        dfs(r-1, c, node, word)
        dfs(r + 1, c, node, word)
        dfs(r, c - 1, node, word)
        dfs(r, c + 1, node, word)
        visit.remove((r, c))
        
    for r in range(ROWS):
        for c in range(COLS):
            dfs(r,c,root, "")
    
    return list(res)

# Test cases
board1 = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words1 = ["bat","cat","back","backend","stack"]

board2 = [
  ["x","o"],
  ["x","o"]
]
words2 = ["xoxo"]

print(findWords(board1, words1)) # Expected output: ["cat","back","backend"]
print(findWords(board2, words2)) # Expected output: []

# Time complexity: O(m * n * 4 * 3^(t-1) + s), where m is number of rows, c is number of columns, t is the maximum length of any word in the array words and s is the sum of the lengths of all words
# Space complexity: O(s)