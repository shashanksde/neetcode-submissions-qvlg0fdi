"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldTocopy = {None:None}
        #create a key of every node in the hashmap first
        cur = head
        while cur:
            copy = Node(cur.val)
            oldTocopy[cur] = copy #key will be old node and value will be copy nodes
            cur = cur.next
        
        #now use the map to update the pointers of the copy nodes
        cur = head
        while cur:
            copy = oldTocopy[cur]
            copy.next = oldTocopy[cur.next] #wherever the cur.next is it can be obtained from the map
            copy.random = oldTocopy[cur.random]
            cur = cur.next
        
        return oldTocopy[head] #from the map if we return the value of the head node, it will have links to all the links