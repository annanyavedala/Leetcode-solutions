# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        head1=head
        head2=head1
        count=0
        while head is not None:
            prev=head
            count+=1
            head= head.next
        i=0
        while i<count//2:
            prev1=head1
            head1=head1.next
            i+=1
        prev1.next=None
        if head1.next is None:
            ll2=head1
        elif head1.next.next is None:
            x=head1.next
            x.next=head1
            head1.next=None
            ll2=x
        else:
            prev=head1
            curr=head1.next
            nextt=curr.next
            prev.next=None
            while(nextt!=None):
                curr.next=prev
                prev=curr
                curr=nextt
                nextt=nextt.next
            curr.next=prev
            ll2=curr
        
        maxx=0
        while(head2 is not None and ll2 is not None):
            maxx=max(maxx, head2.val+ll2.val)
            head2=head2.next
            ll2=ll2.next
            
        return maxx
            
        
            
        
        