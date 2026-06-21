# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        slow = dummy
        slow.next = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False
        