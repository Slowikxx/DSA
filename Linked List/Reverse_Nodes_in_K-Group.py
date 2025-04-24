# You are given the head of a singly linked list and a positive integer k
# You must reverse the first k nodes in the linked list and then reverse the next k nodes and so on.
# If there are fewer than k nodes left, leave the nodes as they are
# Return the modified list after reversing the nodes in each group of k
# You are only allowed to modify the nodes' next pointers not the values of the nodes

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    groupPrev = dummy
    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
        
        prev, curr = kth.next, groupPrev.next
        
        while curr != groupNext:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    
    return dummy.next
    
def getKth(curr : Optional[ListNode], k: int) -> Optional[ListNode]:
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

# Time complexity: O(n)
# Space complexity: O(1)