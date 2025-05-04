# You are given a string s consisting of only uppercase english characters and an integer k
# You can choose up to k characters of the string and replace them with any other uppercase English character
# After performing at most k replacements return the length of the longest substring which contains only one distinct character

def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    maxFreq = 0
    
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxFreq = max(maxFreq, count[s[r]])
        
        while (r - l + 1) - maxFreq > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, r-l + 1)
    
    return res


# Test cases:

s1 = "XYYX"
k1 = 2
s2 = "AAABABB"
k2 = 1

print(characterReplacement(s1, k1)) # Expected output: 4
print(characterReplacement(s2, k2)) # Expected output: 5

# Time complexity: O(n), where n is the length of s
# Space complexity: O(m), where m is the total number of unique characters in s