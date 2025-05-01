# You are given an array of integers nums of size n. The ith element represents a balloon with an intger value of nums[i]
# You must burst all of the balloons
# If you burst the ith balloon you will receive nums[i-1] * nums[i] * nums[i+1] coins.
# If i - 1 or i + 1 goes out of bounds of the array then assume the out of bounds value is 1
# Return the maximum number of coins you can receive by bursting all of the balloons


from typing import List

def maxCoins(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    dp = {}
    
    def dfs(l, r):
        if l > r:
            return 0
        if (l,r) in dp:
            return dp[(l,r)]
        
        dp[(l,r)] = 0
        for i in range(l, r+1):
            coins = nums[l-1] * nums[i] * nums[r+1]
            coins += dfs(l, i-1) + dfs(i+1,r)
            dp[(l,r)] = max(dp[(l,r)], coins)
        
        return dp[(l,r)]
        
    return dfs(1, len(nums) - 2)

# Test case
nums = [4,2,3,7]

print(maxCoins(nums)) # Expected output: 143

# Time complexity: O(n^3)
# Space complexity: O(n^2)