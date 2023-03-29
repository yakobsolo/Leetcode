# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_linked = 0
        start = node = head
        
        while start:
            len_linked += 1
            start = start.next
        
        middle = len_linked // 2
        counter = 0
        while node:
            
            if counter == middle:
                return node
            else:
                counter += 1
                node = node.next