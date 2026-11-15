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

        copy = Node(0)
        hashMap = {}

        curr = head
        ptr = copy

        while curr:
            ptr.next = Node(curr.val)
            hashMap[curr] = ptr.next
            ptr = ptr.next
            curr = curr.next
        
        curr = head
        ptr = copy.next

        while curr:

            if curr.random:
                ptr.random = hashMap[curr.random]
            else:
                ptr.random = None
            ptr = ptr.next
            curr = curr.next
        
        return copy.next


                