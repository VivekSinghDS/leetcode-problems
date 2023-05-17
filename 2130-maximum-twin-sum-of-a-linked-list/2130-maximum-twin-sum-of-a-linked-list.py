# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        current = slow 
        previous = None
        while current:
            next_ = current.next
            current.next = previous
            previous = current
            current = next_
        
        start = head 
        # print(previous.val)
        res = float('-inf')
        while previous:
            res = max(res, start.val + previous.val)
            start = start.next
            previous = previous.next
        return res
            
            
        