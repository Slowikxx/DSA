# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list and return the head of it
# New list should be made up of nodes from list1 and list2

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next

# Time complexity: O(n + m) where n and m are the lengths of two lists
# Space complexity: O(1)