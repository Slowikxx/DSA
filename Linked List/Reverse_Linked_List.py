# Given the beginning of a singly linked list, reverse the list and return the new beginning of the list

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseListIterative(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
        
    return prev

# Time complexity: O(n), where n is the number of nodes in the linked list
# Space complexity: O(1)

def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    
    new_head = head
    if head.next:
        new_head = reverseListRecursive(head.next)
        head.next.next = head
    
    head.next = None
    
    return new_head

# Time complexity: O(n), where n is the number of nodes in the linked list
# Space complexity: O(n), due to the recursion stack