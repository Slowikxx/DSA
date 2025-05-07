# You are given the head of a singly linked list
# The positions of a linked list of length = 7 for xample can initially be represented as: [0,1,2,3,4,5,6]
# Reorder the nodes of the linked list to be in the following order: [0,6,1,5,2,4,3]
# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order: [0, n-1, 1, n-2, 2, n-3, 3, ...]
# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reorderList(head: Optional[ListNode]) -> None:
    slow, fast = head, head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    
    first, second = head, prev
    
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

# Time complexity: O(n), where n is the size of the linked list
# Space complexity: O(1)