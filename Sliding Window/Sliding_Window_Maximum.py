# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array.
# The window slides one position to the right until it reaches the right edge of the array
# Return a list that contains the maximum element in the window at each step

from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output = []
    q = deque()
    l = r = 0
    
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        
        if l > q[0]:
            q.popleft()
        
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    
    return output

# Test case
nums = [1,2,1,0,4,2,6]
k = 3

print(maxSlidingWindow(nums, k)) # Expected output: [2,2,4,4,6]

# Time complexity: O(n), where n is the length of numss
# Space complexity: O(n)
