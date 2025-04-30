# There is a foreign language which uses the latin alphabet but the order among letters is not "a", "b", "c" ... "z" as in English
# You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new langugage
# Derive the order of letters in this language. If the order is invalid return empty string. If there are multiple valid order of letters return any of the,.
# A string a is lexicographically smaller than a string b if either of the following is true:
# - the first letter where they differ is smaller in a than in b
# - there is no index i such that a[i] != b[i] and a.length < b.length

from typing import List


def foreignDictionary(words: List[str]) -> str:
    adj = {c: set() for w in words for c in w}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    
    visit = {}
    res = []
    
    def dfs(c):
        if c in visit:
            return visit[c]
        visit[c] = True
        
        for nei in adj[c]:
            if dfs(nei):
                return True
        visit[c] = False
        res.append(c)
    
    for c in adj:
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)

# Test cases:
words1 = ["z", "o"]
words2 = ["hrn", "hrf", "er", "enn", "rfnn"]

print(foreignDictionary(words1)) # Expected output: "zo"
print(foreignDictionary(words2)) # Expected output: "hernf"

# Time complexity: O(n + v + e), where n is the sum of lengths of all the strings, v is the number of unique characters and e is the number of edges
# Space complexity: O(v + e)