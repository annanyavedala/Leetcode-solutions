# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        hh=head
        hho=head.next
        he=head
        ho=head.next
        while ho!=None and ho.next is not None:
            he.next=ho.next
            ho.next=he.next.next
            he=he.next
            ho=ho.next
        he.next=hho
        return hh
        
            
            
            
        
        
        
        