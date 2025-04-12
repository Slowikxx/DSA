# Given an integer n, count the number of 1s in the binary representation of every number in the range [0,n]
# Return an array output where output[i] is the number of 1s in the binary representation of i

from typing import List


def countBits(n: int) -> List[int]:
    output = [0] * (n + 1)
    offset = 1
    
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        output[i] = 1 + output[i - offset]
    
    return output

# Test cases
n1 = 4
n2 = 6

print(countBits(n1))  # Expected output: [0, 1, 1, 2, 1]
print(countBits(n2))  # Expected output: [0, 1, 1, 2, 1, 2, 2]

# Time complexity: O(n)
# Space complexity: O(n)