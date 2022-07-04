# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return
        
        x = head
        y = x.next
        x.next = None
        
        while(y):
            z = y.next
            y.next = x
            x = y
            y = z
        
        
        
        return x