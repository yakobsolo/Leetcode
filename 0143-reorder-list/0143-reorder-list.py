# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = []
        
        ptr1, ptr2 = head, head
        
        while ptr1:
            lst.append(ptr1.val)
            ptr1 = ptr1.next
        
        l, r = 0, len(lst) -1
        while l<r :
            ptr2.val = lst[l]
            ptr2 = ptr2.next
            ptr2.val = lst[r]
            ptr2 = ptr2.next
            
            l+=1
            r-=1
        if len(lst)%2 == 1:
            ptr2.val= lst[l]
        
        
        