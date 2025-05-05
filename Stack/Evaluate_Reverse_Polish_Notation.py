# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation
# Return the integer that represents the evaluation of the expression
# - the operands may be integers or the results of other operations
# - the operators include '+', '-'., '*', '/'
# - assume that division between integers always truncates toward zero

from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []
    
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    
    return stack[0]

# Test case
tokens = ["1","2","+","3","*","4","-"]

print(evalRPN(tokens)) # Expected output: 5

# Time complexity: O(n), where n is the length of tokens
# Space complexity: O(n), for the stack