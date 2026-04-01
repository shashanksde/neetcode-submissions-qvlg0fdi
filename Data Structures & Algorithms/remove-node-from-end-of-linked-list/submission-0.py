# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length+=1
            cur = cur.next
        pos = length - n
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while pos>0:
            cur = cur.next
            pos-=1
        #when it is at the position
        cur.next = cur.next.next
        return dummy.next