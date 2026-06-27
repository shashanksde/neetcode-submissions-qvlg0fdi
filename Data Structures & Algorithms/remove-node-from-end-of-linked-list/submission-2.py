# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head
        #calculate length
        cur = head
        k=0
        while cur:
            k+=1
            cur=cur.next
        
        #now start from dummy move till k-nth node
        prev, cur = dummy, dummy.next
        if (k-n)<0: return []
        for i in range(k-n):
            prev, cur = prev.next, cur.next
        
        prev.next = cur.next
        return dummy.next