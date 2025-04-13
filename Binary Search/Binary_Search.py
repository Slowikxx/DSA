# You are given an array of distinct integers nums, sorted in ascending order, and an integer target
# Implement a function to search for target within nums. If it exists, then return its index, otherwise return -1.

from typing import List

def search(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    
    return -1


# Test cases
nums = [-1,0,2,4,6,8]
target1 = 4
target2 = 3

print(search(nums, target1)) # Expected output: 3
print(search(nums, target2)) # Expected output: -1

# Time complexity: O(n), worst case we have to iterate through the entire list
# Space complexity: O(1)

# better solution implementing binary search
def binarySearch(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        mid = l + ((r - l) // 2)
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    
    return -1

print(binarySearch(nums, target1)) # Expected output: 3
print(binarySearch(nums, target2)) # Expected output: -1

# Time complexity: O(log n), we only take half of the list each time
# Space complexity: O(1)