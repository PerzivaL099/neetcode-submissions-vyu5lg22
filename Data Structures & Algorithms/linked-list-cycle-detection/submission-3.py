# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #initialize 2 pointers
        slow = head
        fast = head
        #iterate through linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            #if slow == fast return true
            if slow == fast:
                return true
        return False
     