# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            slow.next  = prev
            prev = slow
            slow = next
        max_sum = 0
        while slow:
            max_sum = max(max_sum , slow.val + prev.val)
            prev = prev.next
            slow = slow.next
        return max_sum
            
            