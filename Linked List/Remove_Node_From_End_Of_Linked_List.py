# You are given the beginning of a linked list head and an integer n
# Remove the nth node from the end of the list and return the beginning of the list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head
    
    while n > 0 and right:
        right = right.next
        n -= 1
    
    while right:
        left = left.next
        right = right.next
    
    left.next = left.next.next
    return dummy.next

# Time complexity: O(n), where n is the size of the list
# Space complexity: O(1)