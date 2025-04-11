# You are given a non-empty array of integers nums. Every integer appears twice except for one.
# Return the integer that appears onlu once.
# Solution must be implemented with O(n) runtiime complexity and use only O(1) extra space

from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0
    
    for num in nums:
        res = res ^ num
    
    return res

# Test cases
nums1 = [3,2,3]
nums2 = [7,6,6,7,8]

print(singleNumber(nums1))  # Expected output: 2
print(singleNumber(nums2))  # Expected output: 8

# Time complexity: O (n), where n is the number of elements in the input list
# Space complexity: O(1), no extra space is used