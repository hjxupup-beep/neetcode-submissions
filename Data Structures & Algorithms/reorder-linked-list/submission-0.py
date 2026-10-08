# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next = None

        # reverse the linked list
        pre=None
        while second:
            tmp=second.next
            second.next=pre
            pre=second
            second=tmp
        second=pre # pre是另一半的head
        first=head

        #开始merge
        while second: #第一半可能更长
            tmp1,tmp2=first.next, second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2


        