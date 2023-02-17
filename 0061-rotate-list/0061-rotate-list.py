# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        leng, tail = 1, head
        
        if not head:
            return head
        while tail.next:
            tail = tail.next
            leng+=1
        k = k%leng
        cur = head
        if k == 0:
            return head
        
        while leng -k -1:
            cur = cur.next
            leng -=1 
        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead
        