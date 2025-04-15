# You are given an integer n representing the number of steps to reach the top of the staircase. You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase

def climbStairs(n: int) -> int:
    one = 1
    two = 1
    
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
        
    return one

# Test cases
n1 = 2
n2 = 3

print(climbStairs(n1)) # Expected output: 2
print(climbStairs(n2)) # Expected output: 3

# Time complexity: O(n), where n is the number of steps
# Space complexity: O(1)