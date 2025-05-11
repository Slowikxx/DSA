# A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker system
# Implement the PrefixTree class:
# - PrefixTree() initializes the prefix tree object
# - void insert(String word) inserts the string word into the prefix tree
# - boolean search(String word) returns true if the string word is in the prefix tree (i.e was inserted before) and false otherwise
# - boolean startsWith(String prefix) returns true if there is a previously inserted string word that has the prefix and false otherwise

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True
    
    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True

# Time complexity: O(n), where n is the length of the string
# Space complexity: O(t), where t is the total number of nodes in the trie