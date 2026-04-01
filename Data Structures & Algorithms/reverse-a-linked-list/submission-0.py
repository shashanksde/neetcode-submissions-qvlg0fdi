# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        prev = None
        while cur.next:
            temp = cur.next #temp=3, cur=2
            cur.next = prev #none<-0<-1<-2
            prev = cur #prev = 2
            cur = temp #cur =3
        
        cur.next = prev
        return cur
        '''
        head->1->2->3->none
              ^  ^
              temp = cur.next
              cur.next = prev
              prev = cur
              cur = temp
        i need cur.next to point to its prev node
        before i reverse cur.next i need a temp to point to cur.next so that i dont lose

        '''