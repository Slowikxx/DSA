# Given an integer array nums return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0 and the indices i, j and k are all distinct
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

# Test cases:
nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]

print(threeSum(nums1)) # Expected output: [[-1,-1,2],[-1,0,1]]
print(threeSum(nums2)) # Expected output: []
print(threeSum(nums3)) # Expected output: [[0,0,0]]

# Time complexity: O(n^2)
# Space complexity: O(1) or O(n) extra space on the sorting algorithm and O(m) space for output list, where m is the number of triplets and n is the length of nums
