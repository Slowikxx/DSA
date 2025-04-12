# Given an array nums containing n integers in the range [0,n] withouth any duplicates return the single number in the range that is missing from nums

from typing import List


def missingNumber(nums: List[int]) -> int:
    res = len(nums)
    
    for i in range(len(nums)):
        res += i - nums[i]
        
    return res

# Test cases
nums1 = [1,2,3]
nums2 = [0,2]

print(missingNumber(nums1)) # Expected output: 0
print(missingNumber(nums2)) # Expected output: 1

# Time complexity: O(n), where n is the length of the input array
# Space complexity: O(1)

# Solution using bitwise XOR
def missingNumberXOR(nums: List[int]) -> int:
    res = len(nums)
    xorr = res
    
    for i in range(res):
        xorr ^= i ^ nums[i]
    
    return xorr

# Test cases
print(missingNumberXOR(nums1)) # Expected output: 0
print(missingNumberXOR(nums2)) # Expected output: 1

# Time complexity: O(n), where n is the length of the input array
# Space complexity: O(1)

    