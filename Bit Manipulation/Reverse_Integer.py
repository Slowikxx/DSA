# You are given a signed 32-bit integer x
# Return x after reversing each of its digits. After reversing if x goes outside the range return 0

import math

def reverse(x: int)-> int:
    MIN = -2147483648
    MAX = 2147483647
    
    res = 0
    while x:
        digit = int(math.fmod(x,10))
        x = int(x / 10)
        
        if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
            return 0
        
        if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
            return 0
        
        res = (res * 10) + digit
    
    return res
                
# Test cases
x1 = 1234
x2 = -1234

print(reverse(x1)) # Expected output: 4321
print(reverse(x2)) # Expected output: -4321

# Time complexity: O(1)
# Space complexity: O(1)