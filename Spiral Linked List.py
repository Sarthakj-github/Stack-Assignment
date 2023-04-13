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
        S=[]
        temp=head
        while temp:
            S.append(temp)
            temp=temp.next
        cur=head
        next=cur.next
        while S[-1]!=cur and S[-1]!=next:
            p2=S.pop()
            cur.next=p2
            p2.next=next
            cur=next
            next=cur.next
        if S[-1]==cur:
            cur.next=None
        if S[-1]==next:
            next.next=None
