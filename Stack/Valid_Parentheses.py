# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string is valid only if:
# 1. Every open bracket is closed by the same type of close bracket
# 2. Open brackets are closed in the correct order
# 3. Every close bracket has a corresponding open bracket of the same type
# Return true if s is a valid string and false otherwise

def isValid(s: str) -> bool:
    stack = []
    
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0 or (c == ')' and stack[-1] != '(') or (c == '}' and stack[-1] != '{') or (c == ']' and stack[-1] != '['):
                return False
            
            stack.pop()
    
    return len(stack) == 0

# Test cases
s1 = "[]"
s2 = "([{}])"

print(isValid(s1))  # Expected output: True
print(isValid(s2))  # Expected output: True

# Time complexity: O(n), where n is the length of the string s
# Space complexity: O(n), for the stack in the worst case when all characters are open brackets