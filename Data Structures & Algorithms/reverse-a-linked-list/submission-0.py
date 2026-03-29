# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #3 need values
        prev = None
        curr = head
       
        #Iterate through linked list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #return reversed content
        return prev