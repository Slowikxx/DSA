# You are given an array of k linked lists lists where each list is sorted in ascending order.
# Return the sorted linked list that is the result of mething all of the individual linked lists.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        mergedLists = []
        
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeTwoLists(l1, l2))
        
        lists = mergedLists
        
    return lists[0]

def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    
    return dummy.next

# Time complexity: O(n * k), where n is the total number of nodes across k lists and k is the total number of lists
# Space complexity: O(1)