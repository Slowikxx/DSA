# Given two strings s and t return true if the two strings are anagrams of each other, otherwise return false

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_hash = {}
    t_hash = {}
    
    for i in range(len(s)):
        s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
        t_hash[t[i]] = 1 + t_hash.get(t[i], 0)
    
    for char in s_hash:
        if s_hash[char] != t_hash.get(char, 0):
            return False
    
    return True
        

# Test cases
s1 = "racecar"
t1 = "carrace"

s2 = "jar"
t2 = "jam"

print(isAnagram(s1, t1))  # Expected output: True
print(isAnagram(s2, t2))  # Expected output: False

# Time complexity: O(s + t) / O(n), where s is the length of string s and t is the length of string t
# Space complexity: O(n), where n is the number of unique characters


# Alternative solution using sorting
def isAnagramSort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Test cases
print(isAnagramSort(s1, t1))  # Expected output: True
print(isAnagramSort(s2, t2))  # Expected output: False

# Time complexity: O(nlogn + mlogm), where n is the length of string s and m is the length of string t
# Space complexity: O(1) or O(n + m) depending on the sorting algorithm used