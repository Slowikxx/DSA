# Given a string s return true if it is a palindrome, otherwise return false

def isPalindrome(s: str) -> bool:
    new_s = ""
    
    for char in s:
        if char.isalnum():
            new_s += char.lower()
        
    return new_s == new_s[::-1]

# Test cases
s1 = "Was it a car or a cat I saw?"
s2 = "tab a cat"

print(isPalindrome(s1)) # Expected output: True
print(isPalindrome(s2)) # Expected output: False

# Time complexity: O(n), where n is the length of the string s
# Space complexity: O(n), we use extra space for new_s

# Two pointers solution with a helper isAlphanumeric function
def isAlphanumeric(c: str) -> bool:
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

def isPalindromeTwoPointer(s: str) -> bool:
    l = 0
    r = len(s) - 1
    
    while l < r:
        while l < r and not isAlphanumeric(s[l]):
            l += 1
        while r > l and not isAlphanumeric(s[r]):
            r -= 1
        
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    
    return True
    

print(isPalindromeTwoPointer(s1)) # Expected output: True
print(isPalindromeTwoPointer(s2)) # Expected output: False

# Time complexity: O(n), where n is the length of the string s
# Space complexity: O(1), we are not using any extra space