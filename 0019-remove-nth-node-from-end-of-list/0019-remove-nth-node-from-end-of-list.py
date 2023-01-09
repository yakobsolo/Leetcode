# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr , count = head, head
        node = 0
        
        while count:
            node +=1 
            count = count.next
        if node-n  == 0:
            return head.next
        
        while ptr and node - n -1:
            ptr = ptr.next
            node -=1
        
        ptr.next = ptr.next.next
        
        return head
            
            