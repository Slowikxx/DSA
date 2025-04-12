# You are given an unsigned integer n. Return the number of 1 bits in its binary representation

def hammingWeight(n: int) -> int:
    res = 0
    
    while n:
        res += n % 2
        n = n >> 1
    
    return res

# Test cases
n1 = int(b'00000000000000000000000000001011',2)
n2 = int(b'01111111111111111111111111111101',2)

print(hammingWeight(n1))  # Expected output: 3
print(hammingWeight(n2))  # Expected output: 30


# Time complexity: O(1), while loop will run at most 32 times for a 32-bit integer, time complexity is constant
# Space complexity: O(1)

# downside of this approach is that it has to look at every bit which is wasting time

def hammingWeight2(n: int) -> int:
    res = 0
    
    while n:
        n &= (n-1)
        res += 1
    
    return res

print(hammingWeight2(n1))  # Expected output: 3
print(hammingWeight2(n2))  # Expected output: 30

# Time complexity: O(1) but we don't run extra iterations of the loop when we have 0s
# Space complexity: O(1)