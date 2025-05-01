# You are given an input string s consisting of lowercase english letters and a pattern p consisting of lowercase english letters as well as '.'  and '*' characters
# Return true if the pattern matches the entire input string, otherwise return false:
# - '.' martches any single character
# - '*' matches zero or more of the preceding element

def isMatch(s: str, p: str) -> bool:
    cache = {}
    
    def dfs(i, j):
        if (i, j) in cache:
            return cache([i, j])
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        
        match = i < len(s) and (s[i] == p[j] or p[j] == ".")
        
        if (j + 1) < len(p) and p[j+1] == "*":
            cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i+1, j))
            return cache[(i, j)]
        
        if match:
            cache[(i, j)] = dfs(i+1, j+1)
            return cache[(i,j)]
        
        cache[(i, j)] = False
        return False
    
    return dfs(0,0)
        
# Test cases
s1 = "aa"
p1 = ".b"
s2 = "nnn"
p2 = "n*"
s3 = "xyz"
p3 = ".*z"

print(isMatch(s1, p1)) # Expected output: False
print(isMatch(s2, p2)) # Expected output: True
print(isMatch(s3, p3)) # Expected output: True

# Time complexity: O(n * m), where n is the length of string s and m is the length of string p
# Space complexity: O(n * m)