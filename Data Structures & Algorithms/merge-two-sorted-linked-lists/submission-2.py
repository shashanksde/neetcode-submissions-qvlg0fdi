class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        head = None
        

        cur1, cur2 = list1, list2
        if cur1 and cur2:
            if cur1.val<=cur2.val:
                head = cur1
            else:
                head = cur2
        elif cur1 and not cur2:
            head = cur1
        else:
            head = cur2

        while cur1 and cur2:
            if cur1.val<=cur2.val:
                while cur1.next and cur1.next.val <= cur2.val:
                    cur1 = cur1.next
                tmp = cur1.next
                cur1.next = cur2
                cur1 = tmp
            else:
                while cur2.next and cur2.next.val < cur1.val:
                    cur2 = cur2.next
                tmp = cur2.next
                cur2.next = cur1
                cur2 = tmp
        
        return head