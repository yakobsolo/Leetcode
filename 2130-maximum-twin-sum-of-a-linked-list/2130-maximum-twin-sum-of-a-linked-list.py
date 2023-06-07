# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr= []
        while head:
            arr.append(head.val)
            head = head.next
        l, r = 0 , len(arr)-1
        max_sum = 0
        while l<r:
            max_sum = max(arr[l] + arr[r], max_sum)
            l+=1
            r-=1
        return max_sum