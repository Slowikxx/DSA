# Given an integer array nums and an integer k return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique
# You may return the output in any order

from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    
    for i in range(len(freq) - 1, 0 , -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

# Test cases
nums1 = [1,2,2,3,3,3]
k1 = 2
nums2 = [7,7]
k2 = 1

print(topKFrequent(nums1, k1)) # Expected output: [2,3]
print(topKFrequent(nums2, k2)) # Expected output: [7]

# Time complexity: O(n)
# Space complexity: O(n)