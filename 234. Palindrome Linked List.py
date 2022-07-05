# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stor = list()
        ptr = head
        
        while ptr:
            stor.append(ptr.val)
            ptr = ptr.next
        
        return stor == stor[::-1]
        