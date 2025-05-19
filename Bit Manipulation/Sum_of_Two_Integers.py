# Given two integers a and b, retirn the sum of them withouth using - or +

def getSum(a: int, b:int) -> int:
    mask = 0xFFFFFFFF
    max_int = 0x7FFFFFFF
    
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
    
    return a if a <= max_int else ~(a ^ mask)        

# Test cases
a1 = 1
b1 = 1
a2 = 4
b2 = 7

print(getSum(a1, b1)) # Expected output: 2
print(getSum(a2,b2)) # Expected outpyt: 11

# Time complexity: O(1)
# Space complexity: O(1)