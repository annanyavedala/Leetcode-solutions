# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        head1=head
        head2=head
        if(head is None or head.next is None):
            return None
        if head.next.next is None:
            head.next=None
            return head
            
        while(head!=None):
            c+=1
            head=head.next
        for i in range((c//2)-1):
            head1=head1.next
        
        head1.next=head1.next.next
        return head2
            
        
        