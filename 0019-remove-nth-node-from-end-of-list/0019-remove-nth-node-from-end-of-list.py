# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head 
        dummy = ListNode(None, head)
        
        for i in range(1, n):
            fast = fast.next 
        
        pre_slow = dummy 

        while fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next
            
        pre_slow.next = pre_slow.next.next if pre_slow.next.next else None
        return dummy.next