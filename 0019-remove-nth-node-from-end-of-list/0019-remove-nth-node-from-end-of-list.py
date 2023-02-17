# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        
        ptr1 = ptr2 = head
        while ptr1:
            count +=1
            ptr1  = ptr1.next
        if count == n:
            return head.next
        count =count -n-1
        while count and ptr2:
            ptr2 = ptr2.next
            count -=1
        
        ptr2.next = ptr2.next.next
        
        return head