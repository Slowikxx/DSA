# Given an array of strings strs group all anagrams together into sublists. You may return the output in any order
# An anagram is a string that contains the exact same characters as another string but the order of the characters can be different

from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26 
        
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        res[tuple(count)].append(s)
    
    return res.values()

# Test cases
input1 = ["act","pots","tops","cat","stop","hat"]
input2 = ["x"]
input3 = [""]

print(groupAnagrams(input1)) # Expected output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(groupAnagrams(input2)) # Expected output: [["x"]]
print(groupAnagrams(input3)) # Expected output: [[""]]

# Time complexity: O(m * n), where m is the number of strings and n is the length of the longest string
# Space complexity: O(m) for extra space, O(m * n) for output list