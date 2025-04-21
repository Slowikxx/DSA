# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the heught of a bar which has a width of 1
# Return the maximum area of water that can be trapped between the bars

from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    maxLeft, maxRight = height[left], height[right]
    water_trapped = 0
    
    while left < right:
        if maxLeft < maxRight:
            left += 1
            maxLeft = max(maxLeft, height[left])
            water_trapped += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            water_trapped += maxRight - height[right]
    
    return water_trapped

# Test case
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

print(trap(height)) # Expected output: 9

# Time complexityL O(n), where n is the length of the height array
# Space complexity: O(1)