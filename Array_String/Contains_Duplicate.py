# Given an integer array nums return true if any value appears more than once in the array, otherwise return false.

from typing import List


def hasDuplicate(nums: List[int]) -> bool:
    hashset = set()
    
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    
    return False

# Test cases

test_case_1 = [1,2,3,3]
test_case_2 = [1,2,3,4]

print(hasDuplicate(test_case_1)) # Expected output: True
print(hasDuplicate(test_case_2)) # Expected output: False

# Time complexity: O(n), where n is the number of elements in the array
# Space complexity: O(n), for the hash set to store unique elements

