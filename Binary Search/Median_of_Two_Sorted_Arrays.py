# You are given two integer arrays nums1 and nums2 of size n and m where each is sorted in ascending order.
# Return the median value among all the elements of the two arrays.

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    total = len(nums1) + len(nums2)
    half = total // 2
    
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1
    
    l, r = 0, len(nums1) - 1
    
    while True:
        i = (l + r) // 2
        j = half - i - 2
        
        N1left = nums1[i] if i >= 0 else float('-infinity')
        N1right = nums1[i+1] if (i+1) < len(nums1) else float('infinity')
        N2left = nums2[j] if j >= 0 else float('-infinity')
        N2right = nums2[j+1] if (j+1) < len(nums2) else float('infinity')
        
        if N1left <= N2right and N2left <= N1right:
            if total % 2:
                return min(N1right, N2right)
            return (max(N1left, N2left) + min(N1right, N2right)) / 2
        elif N1left > N2right:
            r = i - 1
        else:
            l = i + 1

# Test cases:
nums1_1 = [1,2]
nums2_1 = [3]
nums1_2 = [1,3]
nums2_2 = [2,4]

print(findMedianSortedArrays(nums1_1, nums2_1)) # Expected output: 2.0
print(findMedianSortedArrays(nums1_2, nums2_2)) # Expected output: 2.5

# Time complexity: O(log(m+n)), where n is the length of nums1 and m ist the length of nums2
# Space complexity: O(log(m+n)), for the recursion stack