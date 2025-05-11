# Design a data structure that supports adding new words and searching for existing words
# Implement the WordDictionary class:
# - void addWord(word) adds word to the data structure
# - bool search(word) returns true if there is any string in the data structure that matches word or false otherwise. Word may contain dots '.' where dots can be matched with any letter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
    
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)
                
# Time complexity: O(n) for both functions
# Space complexity: O(t + n) where n is the length of the string and t is the total number of trie nodes