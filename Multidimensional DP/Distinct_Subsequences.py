# You are given twoo strings s and t both consisting of english letters
# Return the number of distinct subsequences of s which are equal to t

def numDistinct(s: str, t: str) -> int:
    cache = {}
    
    def dfs(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        
        if s[i] == t[j]:
            cache[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
        else:
            cache[(i, j)] = dfs(i + 1, j)
        
        return cache[(i, j)]
    
    return dfs(0,0)

# Test cases

s1 = "caaat"
t1 = "cat"
s2 = "xxyxy"
t2 = "xy"

print(numDistinct(s1, t1)) # Expected output: 3
print(numDistinct(s2,t2)) # Expected output: 5

# Time complexity: O(n * m), where n is the length of the string s and m is the length of the string t
# Space complexity: O(n * m)
