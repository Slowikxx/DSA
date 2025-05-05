# Design a stack class that supports the puch, pop, top and getMin operations
# - MinStack() initializes the stack object
# - void push(int val) pushes the element val onto the stack 
# - void pop() removes the element on the top of the stack
# - int top() gets the top element of the stack
# - int getMin() - retrieves the minimum element in the stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]

# Time complexity: O(1) for all operations
# Space complexity: O(n)