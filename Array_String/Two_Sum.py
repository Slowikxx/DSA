# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    j = 0
    
    while j < len(nums):
        for i in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return sorted([i, j])
        j += 1
    
    return []

# Test cases
nums1 = [3,4,5,6]
target1 = 7

nums2 = [4,5,6]
target2 = 10

print(two_sum(nums1, target1)) # Expected output: [0,1]
print(two_sum(nums2, target2)) # Expected output: [0,2]

# Time complexity: O(n^2), we are going through an array of size n and worst case we have to go through it n times (each against each)
# Space complexity: O(1), no extra space used

# More efficient solution

def two_sum_ef(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    
    for i in range(len(nums)):
        difference = target - nums[i]
        
        if difference in hashmap:
            return [hashmap[difference], i]
        
        hashmap[nums[i]] = i
    
    return []

print(two_sum_ef(nums1, target1)) # Expected output: [0,1]
print(two_sum_ef(nums2, target2)) # Expected output: [0,2]

# Time complexity: O(n), going through the array of size n once
# Space complexity: O(n), using a hashmap to store values and their indices, hashmap will store at worst n values