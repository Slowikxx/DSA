# Given the beginning of a linked list return true if there is a cycle in the linked list.
# A cycle - at least one node in the list can be visited again by following the next pointer.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# Floyd's Tortoise and Hare algorithm - two pointers where one is slow and the other one is fast

# Time complexity: O(n), where n is the length of the given list
# Space complexity: O(1)