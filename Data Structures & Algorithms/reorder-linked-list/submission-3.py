class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #cover the edge case
        if not head or not head.next or not head.next.next:
            return

        prev = head

        while prev and prev.next and prev.next.next:
            cur = prev
            while cur.next.next:
                cur = cur.next
            
            # will be pointing to last but one node
            last = cur.next
            cur.next = None
            
            tmp = prev.next
            prev.next = last
            last.next = tmp
            
            prev = tmp
        return