# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None or head.next.next == None: return head
        
        odd = head
        even = head.next
        dummynode = ListNode()
        dummynode.next = even
        dummynode2  = ListNode()
        dummynode2.next = head
        while odd and odd.next:
            
            odd.next = odd.next.next
            if odd.next != None:
                odd = odd.next
            
            if even.next:
                even.next = even.next.next
            even = even.next
            
        print(dummynode.next, odd)   
        odd.next = dummynode.next
        
        return dummynode2.next
        
        