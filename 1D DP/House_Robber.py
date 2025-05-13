# You are given an integer array nums where nums[i] represents the amount of money the ith house has
# The houses are arranged in a straight line i.e. the ith house is the neighbor of the (i-1)th house and (i+1)th house
# You are planning to rob money from the houses but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into
# Return the maximum amount of money you can rob withouth alerting the police

from typing import List

def rob(nums: List[int]) -> int:
    rob1, rob2 = 0, 0
    
    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
        
    return rob2

# Test cases
nums1 = [1,1,3,3]
nums2 = [2,9,8,3,6]

print(rob(nums1)) # Expected output: 4
print(rob(nums2)) # Expected output: 16

# Time complexity: O(n), where n is the length of the input array
# Space complexity: O(1)