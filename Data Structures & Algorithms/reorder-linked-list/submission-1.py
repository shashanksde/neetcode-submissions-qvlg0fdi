# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        #find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #have the middle, points to head of next node
        cur = slow.next 
        slow.next = None

        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        
        cur1 = head
        cur2 = prev #mistake here prev will be at head when loop ends
        while cur2:
            temp = cur1.next
            cur1.next = cur2
            cur1 = temp

            temp2 = cur2.next
            cur2.next = cur1
            cur2 = temp2
        # rem = cur1 if cur1 else cur2
        # tail = head
        # while tail.next:
        #     tail = tail.next
        # tail.next = rem
        
