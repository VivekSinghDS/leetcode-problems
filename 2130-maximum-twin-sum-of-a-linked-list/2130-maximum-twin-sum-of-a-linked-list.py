# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        last = None 
        cur = head
        previous = None 
        while cur.next:
            
            cur.prev = previous
            previous = cur
            cur = cur.next
        
        cur.prev = previous
        # print(cur)
        last = cur
        # print(last)
        cur = head
        res = float('-inf')
        while cur != last:
            cur_val = cur.val
            last_val = last.val
            res = max(res, cur_val + last_val)
            cur = cur.next
            last = last.prev
        return res