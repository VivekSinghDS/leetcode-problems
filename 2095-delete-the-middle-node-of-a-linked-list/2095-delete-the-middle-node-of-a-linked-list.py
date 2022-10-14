# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head 
        
        dummy = ListNode(0, head)
        pre_slow = dummy
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
            
        pre_slow.next = pre_slow.next.next
        return dummy.next