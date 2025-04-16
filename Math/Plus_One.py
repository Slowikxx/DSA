# You are given an integer array digits where each digits[i] is the ith digit of a large integer.
# It is ordered from most significant to least significant digit and will not conrain any leading zero
# Return the digit of the given integer after incrementing it by one

from typing import List


def plusOne(digits: List[int]) -> List[int]:
    digits = digits[::-1]
    carry = 1
    i = 0
    
    while carry:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
        else:
            digits.append(1)
            carry = 0
        i += 1
    
    return digits[::-1]

# Test cases
digits1 = [1,2,3,4]
digits2 = [9,9,9]

print(plusOne(digits1))  # Expected output: [1,2,3,5]
print(plusOne(digits2)) # Expected output: [1,0,0,0]

# Time complexity: O(n), where n is the length of the digits array
# Space complexity: O(1)