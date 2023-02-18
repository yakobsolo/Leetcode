# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummynode = ListNode(0, head)
        
        leftnode, cur = dummynode , head
        l = left
        while left-1:
            leftnode = cur
            cur = cur.next
            left -=1
        
        prev = None
        for i in range(right - l +1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        leftnode.next.next = cur
        leftnode.next = prev
        
        return dummynode.next