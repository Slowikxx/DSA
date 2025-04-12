# Given a 32-bit unsigned integer n reverse the bits of the binary representation of n and return the result

def reverseBits(n: int) -> int:
    res = 0
    
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))
    
    return res

# Test cases
n = int(b'00000000000000000000000000010101',2)

print(reverseBits(n)) # Expected output: 2818572288

# Time complexity: O(1), the loop runs a fixed number of times (32)
# Space complexity: O(1)