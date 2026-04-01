# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        cur1 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        cur , prev= head2, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        cur2 = prev
        res = cur1
        while cur1 and cur2:
            tmp = cur1.next
            cur1.next = cur2
            tmp2 = cur2.next
            cur2.next = tmp

            cur1 = tmp
            cur2 = tmp2
        
        #first find the mid and detach the remainder of the list
        #reverse the second list
        #now interweave the nodes
        #return the list