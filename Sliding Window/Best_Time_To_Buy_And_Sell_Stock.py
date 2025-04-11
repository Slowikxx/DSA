# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose not to make any transactions in which case the profit would be 0,

from typing import List


def maxProfit(prices: List[int]) -> int:
    l = 0
    r = 1
    max_profit = 0
    
    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(max_profit, prices[r] - prices[l])
        else:
            l = r
        r += 1
    
    return max_profit

# Test cases
prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

print(maxProfit(prices1))  # Expected output: 5 (Buy on day 2 and sell on day 5)
print(maxProfit(prices2))  # Expected output: 0 (No transactions are done, profit is 0)

# Time complexity: O
# Space complexity: O