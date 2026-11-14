# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        revHead = self.reverseList(slow.next)
        slow.next = None
        res = 0

        while head and revHead:
            su = head.val + revHead.val
            res = max(res, su)
            head = head.next
            revHead = revHead.next
        
        return res

    

    def reverseList(self, head: ListNode | None):
        prev = None
        curr = head

        while curr:
            ptr = curr.next
            curr.next = prev
            prev = curr
            curr = ptr
        
        return prev
        
