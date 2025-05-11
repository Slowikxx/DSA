# You are given an array of distinct integers nums and a target integer target
# Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target
# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
# You may return the combinations in any order and the order of numbers in each combination can be in any order

from typing import List

def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    res = []
    
    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(nums) or total > target:
            return
        
        cur.append(nums[i])
        dfs(i, cur, total + nums[i])
        cur.pop()
        dfs(i + 1, cur, total)
    
    dfs(0, [], 0)
    return res

# Test cases
nums1 = [2,5,6,9]
target1 = 9
nums2 = [3,4,5]
target2 = 16
nums3 = [3]
target3 = 5

print(combinationSum(nums1, target1)) # Expected output: [[2,2,5],[9]]
print(combinationSum(nums2, target2)) # Expected output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
print(combinationSum(nums3, target3)) # Expected output: []

# Time complexity: O(2 * t/m), where t is the target and m is the minimum value in nums
# Space complexity: O(t/m)