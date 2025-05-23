# You are given an array of integers numbbers that is sorted in non-decreasing order
# Return the indices (1-indexed) of two numbers [index1, index2] such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal therefore you may not use the same element twice
# There will always be exactly one valid solution
# Your solution must use O(1) additional space

from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    l,r = 0, len(numbers) - 1
    
    while l < r:
        curSum = numbers[l] + numbers[r]
        
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return []

# Test case
numbers = [1,2,3,4]
target = 3

print(twoSum(numbers, target)) # Expected output: [1,2]

# Time complexity: O(n), where n is the length of numbers
# Space complexity: O(1)