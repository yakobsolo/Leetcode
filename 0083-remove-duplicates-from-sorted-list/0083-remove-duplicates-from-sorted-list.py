# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummyNode.next = head
        cur  = head
        while head and head.next:
            while head.next and head.val == head.next.val:
                head = head.next
            
            if head.next:
                cur.next = head.next
                head = head.next
                cur = cur.next
            else:
                cur.next = None
            
        return dummyNode.next
        