# Given an unsorted array of integers nums and an integer k return the kth largest element in the array
# By kth largest element we mean the kth largest element in the sorted order, not the kth distinct element

from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    k = len(nums) - k
    
    def quickSelect(l, r):
        pivot, p = nums[r], l
        
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        
        if p > k:
            return quickSelect(l, p - 1)
        elif k > p:
            return quickSelect(p + 1, r)
        else:
            return nums[p]
    return quickSelect(0, len(nums) - 1)

# Test cases
nums1 = [2,3,1,5,4]
k1 = 2
nums2 = [2,3,1,1,5,5,4]
k2 = 3

print(findKthLargest(nums1, k1))  # Expected output: 4
print(findKthLargest(nums2, k2)) # Expected output: 4

# Time complexity: O(n), worst case O(n^2), where n is the length of nums
# Space complexity: O(n)