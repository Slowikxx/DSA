# A happy number is defined by this algorithm:
# - given a positive integer replace it with sum of the squares pf its figits
# - repeat the above step unitl the number equals 1 or loops infinitely in a cycle that does not include 1
# - if it stops at 1 then the number is happy
# return true if given integer is happy, otherwise false

def isHappy(n: int) -> bool:
    visited = set()
    
    while n not in visited:
        visited.add(n)
        n = calculateSumSquares(n)
        
        if n == 1:
            return True
        
    return False

def calculateSumSquares(n: int) -> int:
    output = 0

    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 10
    
    return output
# Test cases
n1 = 100
n2 = 101

print(isHappy(n1))  # Expected output: True
print(isHappy(n2))  # Expected output: False

# Time complexity: O(log n), where n is the input number (we are dividing the number by 10 in each iteration)
# Space complexity: O(log n) for the visited set, in the worst case all numbers will be stored in the set

