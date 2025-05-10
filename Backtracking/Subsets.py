# Given an array nums of unique integers return all possible subsets of nums
# The solution set must not contain duplicate subsets

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        dfs(i+1)
        
        subset.pop()
        dfs(i+1)
    
    dfs(0)
    return res

# Test cases
nums1 = [1,2,3]
nums2 = [7]

print(subsets(nums1)) # Expected output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsets(nums2)) # Expected output: [[].[7]]

# Time complexity: O(n * 2^n)
# Space complexity: O(n) exxtra space, O(2^n) for the output list