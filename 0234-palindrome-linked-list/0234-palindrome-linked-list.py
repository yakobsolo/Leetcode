# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        r = 0
        while head:
            stack.append(head.val)
            head = head.next
        for i in range(len(stack)//2):
            if stack[i] == stack[-1]:
                stack.pop()
               
            else:
                return False
        return True
        