# Given a string s find the length of the longest substring withouth duplicate characters
# A substring is a contiguous sequence of characters within a string

def lengthOfLongestSubstring(s : str) -> int:
    charSet = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r-l + 1)
    
    return res

# Test cases:
s1 = "zxyzxyz"
s2 = "xxxx"

print(lengthOfLongestSubstring(s1)) # ExpectedOutput: 3
print(lengthOfLongestSubstring(s2)) # ExpectedOutput: 1

# Time complexity: O(n), where n is the length of s
# Space complexity: O(n)