# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            head1=head.next
            head.next=None
            head1.next=head
            return head1
        prev=head
        curr=prev.next
        nextt=curr.next
        prev.next=None
        while nextt is not None:
            curr.next=prev
            prev=curr
            curr=nextt
            nextt=nextt.next
        curr.next=prev
        return curr
            
            
            
        